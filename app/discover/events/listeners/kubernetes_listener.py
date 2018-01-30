import argparse
import datetime
import socket
from typing import Callable, List

import os

from kubernetes.client import Configuration as KubeConf, CoreV1Api
from kubernetes.watch import Watch

from discover.configuration import Configuration
from discover.event_handler import EventHandler
from discover.events.event_base import EventResult
from discover.events.kube.kube_metadata_parser import parse_metadata_file, \
    KubeMetadataParser
from discover.events.listeners.listener_base import ListenerBase
from messages.message import Message
from monitoring.setup.monitoring_setup_manager import MonitoringSetupManager
from utils.constants import EnvironmentFeatures
from utils.inventory_mgr import InventoryMgr
from utils.logging.full_logger import FullLogger
from utils.logging.logger import Logger
from utils.mongo_access import MongoAccess
from utils.util import setup_args


class KubernetesListener(ListenerBase):

    SOURCE_SYSTEM = "Kubernetes"
    COMMON_METADATA_FILE = "kube_events.json"

    LOG_FILENAME = "kubernetes_listener.log"
    LOG_LEVEL = Logger.INFO

    DEFAULTS = {
        "env": "Kubernetes",
        "mongo_config": "",
        "metadata_file": "",
        "inventory": "inventory",
        "loglevel": "INFO",
        "environments_collection": "environments_config",
    }

    def __init__(self, config, event_handler,
                 environment: str = DEFAULTS["env"],
                 inventory_collection: str = DEFAULTS["inventory"]):
        super().__init__()
        self.environment = environment
        self.handler = event_handler

        self.inv = InventoryMgr()
        self.inv.set_collections(inventory_collection)
        if self.inv.is_feature_supported(self.environment,
                                         EnvironmentFeatures.MONITORING):
            self.inv.monitoring_setup_manager = \
                MonitoringSetupManager(self.environment)

        self.base_url = 'https://{}:{}'.format(config['host'], config['port'])
        self.bearer_token = config.get('token', '')
        conf = KubeConf()
        conf.host = self.base_url
        conf.user = config['user']
        conf.api_key_prefix['authorization'] = 'Bearer'
        conf.api_key['authorization'] = self.bearer_token
        conf.verify_ssl = False
        self.api = CoreV1Api()

    def process_event(self, event):
        received_timestamp = datetime.datetime.now()

        event_type = ".".join(
            (event['object'].kind, event['type'])
        ).lower()
        result = self.handle_event(event_type=event_type, notification=event)

        finished_timestamp = datetime.datetime.now()
        self.save_message(message_body=event,
                          result=result,
                          started=received_timestamp,
                          finished=finished_timestamp)

        if result.result is True:
            self.log.info("Event '{event_type}' for object '{object_id}' "
                          "was handled successfully."
                          .format(event_type=event_type,
                                  object_id=result.related_object))
        else:
            self.log.error("Event handling '{event_type}' "
                           "for object '{object_id}' failed.\n"
                           "Message: {message}"
                           .format(event_type=event_type,
                                   object_id=result.related_object,
                                   message=result.message))

    def handle_event(self, event_type: str, notification: dict) -> EventResult:
        try:
            result = self.handler.handle(event_name=event_type,
                                         notification=notification)
            return result if result else EventResult(result=False, retry=False)
        except Exception as e:
            self.log.exception(e)
            return EventResult(result=False, retry=False)

    def save_message(self, message_body: dict, result: EventResult,
                     started: datetime, finished: datetime):
        try:
            message = Message(
                msg_id=None,  # TODO: generate?
                env=self.environment,
                source=self.SOURCE_SYSTEM,
                object_id=result.related_object,
                display_context=result.display_context,
                level="info" if result.result is True else "error",
                msg={},  # TODO: filter and dump select fields
                received_ts=started,
                finished_ts=finished
            )
            self.inv.collections['messages'].insert_one(message.get())
            return True
        except Exception as e:
            self.inv.log.error("Failed to save message")
            self.inv.log.exception(e)
            return False

    @staticmethod
    def listen(args: dict = None):
        args = setup_args(args, KubernetesListener.DEFAULTS, get_args)
        if 'process_vars' not in args:
            args['process_vars'] = {}

        logger = FullLogger()
        logger.set_loglevel(args["loglevel"])
        logger.setup(env=args["env"])

        env_name = args['env']
        inventory_collection = args["inventory"]

        MongoAccess.set_config_file(args["mongo_config"])
        inv = InventoryMgr()
        inv.set_collections(inventory_collection)
        conf = Configuration(args["environments_collection"])
        conf.use_env(env_name)

        event_handler = EventHandler(env_name, inventory_collection)

        env_config = conf.get_env_config()
        common_metadata_file = os.path.join(
            env_config.get('app_path', '/etc/calipso'),
            'config',
            KubernetesListener.COMMON_METADATA_FILE
        )

        # import common metadata
        metadata_parser = import_metadata(event_handler=event_handler,
                                          metadata_file_path=common_metadata_file)

        # import custom metadata if supplied
        if args["metadata_file"]:
            import_metadata(event_handler, args["metadata_file"])

        kube_config = conf.get('Kubernetes')
        listener = KubernetesListener(config=kube_config,
                                      event_handler=event_handler)

        metadata_parser.load_endpoints(api=listener.api)

        watch = Watch()
        streams = [
            watch.stream(endpoint)
            for endpoint
            in metadata_parser.endpoints
        ]
        while not watch._stop:
            try:
                for stream in streams:
                    event = next(stream, None)
                    if event:
                        listener.process_event(event)

            except Exception as e:
                logger.exception(e)
                watch.stop()
        logger.info("Watch stopped")


def get_args():
    # Read listener config from command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                        default=KubernetesListener.DEFAULTS["mongo_config"],
                        help="Name of config file with MongoDB access details")
    parser.add_argument("--metadata_file", nargs="?", type=str,
                        default=KubernetesListener.DEFAULTS["metadata_file"],
                        help="Name of custom configuration metadata file")
    def_env_collection = KubernetesListener.DEFAULTS["environments_collection"]
    parser.add_argument("-c", "--environments_collection", nargs="?", type=str,
                        default=def_env_collection,
                        help="Name of collection where selected environment " +
                             "is taken from \n(default: {})"
                        .format(def_env_collection))
    parser.add_argument("-e", "--env", nargs="?", type=str,
                        default=KubernetesListener.DEFAULTS["env"],
                        help="Name of target listener environment \n" +
                             "(default: {})"
                        .format(KubernetesListener.DEFAULTS["env"]))
    parser.add_argument("-y", "--inventory", nargs="?", type=str,
                        default=KubernetesListener.DEFAULTS["inventory"],
                        help="Name of inventory collection \n"" +"
                             "(default: '{}')"
                        .format(KubernetesListener.DEFAULTS["inventory"]))
    parser.add_argument("-l", "--loglevel", nargs="?", type=str,
                        default=KubernetesListener.DEFAULTS["loglevel"],
                        help="Logging level \n(default: '{}')"
                        .format(KubernetesListener.DEFAULTS["loglevel"]))
    args = parser.parse_args()
    return args


# Imports metadata from file,
# updates event handler with new handlers
def import_metadata(event_handler: EventHandler,
                    metadata_file_path: str) -> KubeMetadataParser:
    metadata_parser = parse_metadata_file(metadata_file_path)
    event_handler.discover_handlers(metadata_parser.handlers_package,
                                    metadata_parser.event_handlers)
    return metadata_parser

if __name__ == '__main__':
    KubernetesListener.listen()
