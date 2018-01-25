import argparse
import socket

import os

from kubernetes.client import Configuration as KubeConf, CoreV1Api
from kubernetes.watch import Watch

from discover.configuration import Configuration
from discover.event_handler import EventHandler
from discover.events.event_base import EventResult
from discover.events.kube.kube_metadata_parser import parse_metadata_file
from discover.events.listeners.listener_base import ListenerBase
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
        "retry_limit": 10,
        "consume_all": False
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

    def handle_event(self, event_type: str, notification: dict) -> EventResult:
        # self.log.info("Got notification.\n"
        #               "Event_type: {}\n"
        #               "Notification:\n{}".format(event_type, notification))
        try:
            result = self.handler.handle(event_name=event_type,
                                         notification=notification)
            return result if result else EventResult(result=False, retry=False)
        except Exception as e:
            self.log.exception(e)
            return EventResult(result=False, retry=False)

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
        import_metadata(event_handler, common_metadata_file)

        # import custom metadata if supplied
        if args["metadata_file"]:
            import_metadata(event_handler, args["metadata_file"])

        kube_config = conf.get('Kubernetes')
        listener = KubernetesListener(config=kube_config,
                                      event_handler=event_handler)

        watch = Watch()
        while True:
            try:
                for event in watch.stream(listener.api.list_pod_for_all_namespaces):
                    event_type = ".".join(
                        (event['object'].kind, event['type'])
                    ).lower()

                    listener.handle_event(event_type=event_type,
                                          notification=event)
            except socket.timeout:
                logger.info("Reconnecting to Kubernetes")
            except Exception as e:
                logger.exception(e)
                watch.stop()
                break
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
                    metadata_file_path: str) -> None:
    handlers_package, event_handlers = parse_metadata_file(metadata_file_path)
    event_handler.discover_handlers(handlers_package, event_handlers)


if __name__ == '__main__':
    KubernetesListener.listen()
