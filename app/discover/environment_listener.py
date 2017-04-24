#!/usr/bin/env python3

import argparse
import datetime
import json
import time
from collections import defaultdict

from kombu import Queue, Exchange
from kombu.mixins import ConsumerMixin

from discover.configuration import Configuration
from discover.event_handler import EventHandler
from discover.events.event_base import EventResult
from messages.message import Message
from monitoring.setup.monitoring_setup_manager import MonitoringSetupManager
from utils.constants import OperationalStatus
from utils.inventory_mgr import InventoryMgr
from utils.logger import Logger
from utils.string_utils import stringify_datetime
from utils.util import SignalHandler, setup_args


class EnvironmentListener(ConsumerMixin):

    SOURCE_SYSTEM = "OpenStack"

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

    def __init__(self, connection,
                 env_name: str = DEFAULTS["env"],
                 inventory_collection: str = DEFAULTS["inventory"],
                 mongo_config: str = DEFAULTS["mongo_config"],
                 retry_limit: int = DEFAULTS["retry_limit"],
                 consume_all: bool = DEFAULTS["consume_all"]):

        self.connection = connection
        self.retry_limit = retry_limit
        self.env_name = env_name
        self.consume_all = consume_all
        self.handler = None
        self.notification_responses = {}
        self.failing_messages = defaultdict(int)
        self.inv = InventoryMgr()

        self._set_collections(inventory_collection)
        self._set_default_handler(inventory_collection)
        self._set_monitoring(mongo_config)

    def _set_collections(self, inventory_collection: str):
        self.inv.set_collections(inventory_collection)

    def _set_default_handler(self, inventory_collection: str):
        self.handler = EventHandler(self.env_name, inventory_collection)
        self.notification_responses = {
            "compute.instance.create.end": self.handler.instance_add,
            "compute.instance.rebuild.end": self.handler.instance_update,
            "compute.instance.update": self.handler.instance_update,
            "compute.instance.delete.end": self.handler.instance_delete,

            # TODO: implement these handlers
            "servergroup.create": self.handler.not_implemented,  # self.handler.region_add,
            "servergroup.update": self.handler.not_implemented,  # self.handler.region_update,
            "servergroup.addmember": self.handler.not_implemented,  # self.handler.region_update,
            "servergroup.delete": self.handler.not_implemented,  # self.handler.region_delete,

            # TODO: implement these handlers
            "compute.instance.shutdown.start": self.handler.not_implemented,  # self.handler.instance_down,
            "compute.instance.power_off.start": self.handler.not_implemented,  # self.handler.instance_down,
            "compute.instance.power_on.end": self.handler.not_implemented,  # self.handler.instance_up,
            "compute.instance.suspend.start": self.handler.not_implemented,  # self.handler.instance_down,
            "compute.instance.suspend.end": self.handler.not_implemented,  # self.handler.instance_up,

            "network.create": self.handler.network_create,
            "network.create.start": self.handler.network_create,
            "network.create.end": self.handler.network_create,
            "network.update": self.handler.network_update,
            "network.update.start": self.handler.network_update,
            "network.update.end": self.handler.network_update,
            "network.delete": self.handler.network_delete,
            "network.delete.start": self.handler.network_delete,
            "network.delete.end": self.handler.network_delete,

            "subnet.create": self.handler.subnet_create,
            "subnet.create.start": self.handler.subnet_create,
            "subnet.create.end": self.handler.subnet_create,
            "subnet.update": self.handler.subnet_update,
            "subnet.update.start": self.handler.subnet_update,
            "subnet.update.end": self.handler.subnet_update,
            "subnet.delete": self.handler.subnet_delete,
            "subnet.delete.start": self.handler.subnet_delete,
            "subnet.delete.end": self.handler.subnet_delete,

            "port.create.end": self.handler.port_create,
            "port.update.end": self.handler.port_update,
            "port.delete.end": self.handler.port_delete,

            "router.create": self.handler.router_create,
            "router.create.start": self.handler.router_create,
            "router.create.end": self.handler.router_create,
            "router.update": self.handler.router_update,
            "router.update.start": self.handler.router_update,
            "router.update.end": self.handler.router_update,
            "router.delete": self.handler.router_delete,
            "router.delete.start": self.handler.router_delete,
            "router.delete.end": self.handler.router_delete,

            "router.interface.create": self.handler.router_interface_create,
            "router.interface.delete": self.handler.router_interface_delete,
        }

    def _set_monitoring(self, mongo_config: str):
        self.inv.monitoring_setup_manager = MonitoringSetupManager(mongo_config, self.env_name)
        self.inv.monitoring_setup_manager.server_setup()

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
        elif "event_type" in body.get("oslo.message", ""):
            return True, json.loads(body["oslo.message"])
        else:
            return False, None

    def process_task(self, body, message):
        received_timestamp = stringify_datetime(datetime.datetime.now())
        processable, event_data = self._extract_event_data(body)
        # If env listener can't process the message
        # or it's not intended for env listener to handle,
        # leave the message in the queue unless "consume_all" flag is set
        if processable and event_data["event_type"] in self.notification_responses:
            with open("/tmp/listener.log", "a") as f:
                f.write("{}\n".format(event_data))
            event_result = self.handle_event(event_data["event_type"], event_data)
            finished_timestamp = stringify_datetime(datetime.datetime.now())
            self.save_message(message_body=event_data,
                              result=event_result,
                              started=received_timestamp,
                              finished=finished_timestamp)

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
    def handle_event(self, event_type: str, notification: dict) -> EventResult:
        print("Got notification.\nEvent_type: {}\nNotification:\n{}".format(event_type, notification))
        try:
            result = self.notification_responses[event_type](notification)
            return result if result else EventResult(result=False, retry=False)
        except Exception as e:
            self.inv.log.exception(e)
            return EventResult(result=False, retry=False)

    def save_message(self, message_body: dict, result: EventResult, started: str, finished: str):
        try:
            message = Message(
                msg_id=message_body.get('message_id'),
                env=self.env_name,
                source=self.SOURCE_SYSTEM,
                object_id=result.object_id,
                object_type=result.object_type,
                display_context=result.document_id,
                level=message_body.get('priority'),
                msg=message_body,
                ts=message_body.get('timestamp'),
                received_ts=started,
                finished_ts=finished
            )
            self.inv.collections['messages'].insert_one(message.get())
            return True
        except Exception as e:
            self.inv.log.error("Failed to save message")
            self.inv.log.exception(e)
            return False


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
                                         consume_all=args["consume_all"],
                                         mongo_config=args["mongo_config"],
                                         inventory_collection=args["inventory"],
                                         env_name=env_name)
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
