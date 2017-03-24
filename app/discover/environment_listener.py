#!/usr/bin/env python3

import argparse
import json

import time
from kombu import Queue, Exchange
from kombu.mixins import ConsumerMixin

from discover.configuration import Configuration
from discover.event_handler import EventHandler
from monitoring.setup.monitoring_setup_manager import MonitoringSetupManager
from utils.constants import OperationalStatus
from utils.inventory_mgr import InventoryMgr
from utils.logger import Logger
from utils.util import SignalHandler, setup_args


class EnvironmentListener(ConsumerMixin):

    DEFAULTS = {
        "env": "Mirantis-Liberty",
        "mongo_config": "",
        "inventory": "inventory",
        "loglevel": "INFO",
        "environments_collection": "environments_config"
    }

    event_queues = [
        Queue('notifications.nova',
              Exchange('nova', 'topic', durable=False),
              durable=False, routing_key='#'),
        Queue('notifications.neutron',
              Exchange('neutron', 'topic', durable=False),
              durable=False, routing_key='#'),
        Queue('notifications.neutron',
              Exchange('dhcp_agent', 'topic', durable=False),
              durable=False, routing_key='#'),
        Queue('notifications.info',
              Exchange('info', 'topic', durable=False),
              durable=False, routing_key='#')
    ]

    def __init__(self, connection):
        self.connection = connection
        self.handler = None
        self.notification_responses = {}
        self.inv = InventoryMgr()

    def set_env(self, env, inventory_collection):
        self.inv.set_collections(inventory_collection)
        self.handler = EventHandler(env, inventory_collection)
        self.notification_responses = {
            "compute.instance.create.end": self.handler.instance_add,
            "compute.instance.delete.end": self.handler.instance_delete,
            "compute.instance.rebuild.end": self.handler.instance_update,
            "compute.instance.update": self.handler.instance_update,

            "servergroup.create": self.handler.region_add,
            "servergroup.delete": self.handler.region_delete,
            "servergroup.update": self.handler.region_update,
            "servergroup.addmember": self.handler.region_update,

            "compute.instance.shutdown.start": self.handler.instance_down,
            "compute.instance.power_off.start": self.handler.instance_down,
            "compute.instance.power_on.end": self.handler.instance_up,
            "compute.instance.suspend.start": self.handler.instance_down,
            "compute.instance.suspend.end": self.handler.instance_up,

            "network.create.end": self.handler.network_create,
            "network.update.end": self.handler.network_update,
            "network.delete.end": self.handler.network_delete,

            "subnet.create.end": self.handler.subnet_create,
            "subnet.update.end": self.handler.subnet_update,
            "subnet.delete.end": self.handler.subnet_delete,

            "port.create.end": self.handler.port_create,
            "port.update.end": self.handler.port_update,
            "port.delete.end": self.handler.port_delete,

            "router.create.end": self.handler.router_create,
            "router.update.end": self.handler.router_update,
            "router.delete.end": self.handler.router_delete,

            "router.interface.create": self.handler.router_interface_create,
            "router.interface.delete": self.handler.router_interface_delete,
        }

    def get_consumers(self, consumer, channel):
        return [consumer(queues=self.event_queues,
                         accept=['json'],
                         callbacks=[self.process_task])]

    # Determines if message should be processed by a handler
    # and extracts message body if yes.
    @staticmethod
    def _extract_event_data(body):
        if "event_type" in body:
            return True, body
        elif "event_type" in body["oslo.message"]:
            return True, json.loads(body["oslo.message"])
        else:
            return False, None

    def process_task(self, body, message):
        processable, event_data = self._extract_event_data(body)
        if processable:
            with open("/tmp/listener.log", "a") as f:
                f.write(body['oslo.message'] + "\n")
            self.handle_event(event_data["event_type"], event_data)
            message.ack()

    def handle_event(self, type, notification):
        print("got notification, event_type: " + type + '\n' + str(notification))
        if type not in self.notification_responses.keys():
            return ""
        return self.notification_responses[type](notification)


def get_args():
    # Read listener config from command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                        default=EnvironmentListener.DEFAULTS["mongo_config"],
                        help="Name of config file with MongoDB server access details")
    parser.add_argument("-c", "--environments_collection", nargs="?", type=str,
                        default=EnvironmentListener.DEFAULTS["environments_collection"],
                        help="Name of collection where selected environment is taken from \n(default: {})"
                        .format(EnvironmentListener.DEFAULTS["environments_collection"]))
    parser.add_argument("-e", "--env", nargs="?", type=str,
                        default=EnvironmentListener.DEFAULTS["env"],
                        help="Name of target listener environment \n(default: {})"
                        .format(EnvironmentListener.DEFAULTS["env"]))
    parser.add_argument("-y", "--inventory", nargs="?", type=str,
                        default=EnvironmentListener.DEFAULTS["inventory"],
                        help="Name of inventory collection \n(default: 'inventory')")
    parser.add_argument("-l", "--loglevel", nargs="?", type=str,
                        default=EnvironmentListener.DEFAULTS["loglevel"],
                        help="Logging level \n(default: 'INFO')")
    args = parser.parse_args()
    return args


def listen(args: dict = None):
    from kombu import Connection
    logger = Logger()

    args = setup_args(args, EnvironmentListener.DEFAULTS, get_args)
    if 'process_vars' not in args:
        args['process_vars'] = {}

    logger.set_loglevel(args["loglevel"])

    conf = Configuration(args["mongo_config"], args["environments_collection"])

    env_name = args["env"]
    conf.use_env(env_name)

    amqp_config = conf.get("AMQP")
    host = amqp_config["host"]
    port = amqp_config["port"]
    user = amqp_config["user"]
    pwd = amqp_config["password"]
    connect_url = 'amqp://' + user + ':' + pwd + '@' + host + ':' + port + '//'
    with Connection(connect_url) as conn:
        try:
            print(conn)
            conn.connect()
            args['process_vars']['operational'] = OperationalStatus.RUNNING
            terminator = SignalHandler()
            worker = EnvironmentListener(conn)
            worker.set_env(env_name, args["inventory"])
            worker.inv.monitoring_setup_manager = MonitoringSetupManager(args["mongo_config"], env_name)
            worker.inv.monitoring_setup_manager.server_setup()
            worker.run()
            if terminator.terminated:
                args.get('process_vars', {})['operational'] = OperationalStatus.STOPPED
        except KeyboardInterrupt:
            print('Stopped')
            args['process_vars']['operational'] = OperationalStatus.STOPPED
        except Exception as e:
            logger.log.exception(e)
            args['process_vars']['operational'] = OperationalStatus.ERROR
        finally:
            # This should enable safe saving of shared variables
            time.sleep(0.1)


if __name__ == '__main__':
    listen()
