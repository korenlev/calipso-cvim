#!/usr/bin/env python3

import argparse
import json

import time
from collections import defaultdict

from kombu import Queue, Exchange
from kombu.mixins import ConsumerMixin

from discover.configuration import Configuration
from discover.event_handler import EventHandler
from discover.events.event_base import EventResult
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
        "environments_collection": "environments_config",
        "retry_limit": 10,
        "consume_all": False
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

    def __init__(self, connection, retry_limit, consume_all):
        self.connection = connection
        self.retry_limit = retry_limit
        self.consume_all = consume_all
        self.handler = None
        self.notification_responses = {}
        self.failing_messages = defaultdict(int)
        self.inv = InventoryMgr()

    def set_env(self, env, inventory_collection):
        self.inv.set_collections(inventory_collection)
        self.handler = EventHandler(env, inventory_collection)
        self.notification_responses = {
            "compute.instance.create.end": self.handler.instance_add,
            "compute.instance.rebuild.end": self.handler.instance_update,
            "compute.instance.update": self.handler.instance_update,
            "compute.instance.delete.end": self.handler.instance_delete,

            "servergroup.create": self.handler.region_add,
            "servergroup.update": self.handler.region_update,
            "servergroup.addmember": self.handler.region_update,
            "servergroup.delete": self.handler.region_delete,

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
        # If env listener can't process the message
        # or it's not intended for env listener to handle,
        # leave the message in the queue
        if processable and event_data["event_type"] in self.notification_responses:
            with open("/tmp/listener.log", "a") as f:
                f.write(body['oslo.message'] + "\n")
            event_result = self.handle_event(event_data["event_type"], event_data)

            # Check whether the event was fully handled
            # and, if not, whether it should be retried later
            if event_result.result:
                message.ack()
            elif event_result.retry:
                if 'message_id' not in event_data:
                    message.reject()
                else:
                    # Track message retry count
                    message_id = event_data['message_id']
                    self.failing_messages[message_id] += 1

                    # Retry handling the message
                    if self.failing_messages[message_id] <= self.retry_limit:
                        self.inv.log.info("Retrying handling message with id '{}'"
                                          .format(message_id))
                        message.requeue()
                    # Discard the message if it's not accepted
                    # after specified number of trials
                    else:
                        self.inv.log.warn("Discarding message with id '{}' as it's exceeded the retry limit"
                                          .format(message_id))
                        message.reject()
                        del self.failing_messages[message_id]
            else:
                message.reject()
        elif self.consume_all:
            message.reject()

    # This method passes the event to its handler.
    # Returns a (result, retry) tuple:
    # 'Result' flag is True if handler has finished successfully, False otherwise
    # 'Retry' flag specifies if the error is recoverable or not
    # 'Retry' flag is checked only is 'result' is False
    def handle_event(self, event_type, notification) -> EventResult:
        print("Got notification.\nEvent_type: {}\nNotification:\n{}".format(event_type, notification))
        try:
            return self.notification_responses[event_type](notification)
        except Exception as e:
            self.inv.log.exception(e)
            # TODO: an exception-causing handler should rather be fixed than retried (it's ok for now)
            return EventResult(result=False, retry=True)


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
    parser.add_argument("-r", "--retry_limit", nargs="?", type=int,
                        default=EnvironmentListener.DEFAULTS["retry_limit"],
                        help="Maximum number of times the OpenStack message "
                             "should be requeued before being discarded \n(default: {})"
                        .format(EnvironmentListener.DEFAULTS["retry_limit"]))
    parser.add_argument("--consume_all", action="store_true",
                        help="If this flag is set, environment listener will try to consume"
                             "all messages from OpenStack event queue "
                             "and reject incompatible messages."
                             "Otherwise they'll just be ignored.",
                        default=EnvironmentListener.DEFAULTS["consume_all"])
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
            worker = EnvironmentListener(connection=conn,
                                         retry_limit=args["retry_limit"],
                                         consume_all=args["consume_all"])
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
