import argparse
import datetime

import time

import pymongo
from functools import partial

from discover.manager import Manager
from utils.constants import ScanStatus, EnvironmentFeatures
from utils.exceptions import ScanArgumentsError
from utils.inventory_mgr import InventoryMgr
from utils.logging.file_logger import FileLogger
from utils.mongo_access import MongoAccess
from discover.scan import ScanController


class ScanManager(Manager):

    DEFAULTS = {
        "mongo_config": "",
        "collection": "scans",
        "environments_collection": "environments_config",
        "interval": 1,
        "loglevel": "INFO"
    }

    def __init__(self):
        self.args = self.get_args()
        super().__init__(log_directory=self.args.log_directory,
                         mongo_config_file=self.args.mongo_config)
        self.db_client = None
        self.environments_collection = None

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                            default=ScanManager.DEFAULTS["mongo_config"],
                            help="Name of config file " +
                                 "with MongoDB server access details")
        parser.add_argument("-c", "--collection", nargs="?", type=str,
                            default=ScanManager.DEFAULTS["collection"],
                            help="Scans collection to read from")
        parser.add_argument("-e", "--environments_collection", nargs="?", type=str,
                            default=ScanManager.DEFAULTS["environments_collection"],
                            help="Environments collection to update after scans")
        parser.add_argument("-i", "--interval", nargs="?", type=float,
                            default=ScanManager.DEFAULTS["interval"],
                            help="Interval between collection polls"
                                 "(must be more than {} seconds)"
                                 .format(ScanManager.MIN_INTERVAL))
        parser.add_argument("-l", "--loglevel", nargs="?", type=str,
                            default=ScanManager.DEFAULTS["loglevel"],
                            help="Logging level \n(default: '{}')"
                                 .format(ScanManager.DEFAULTS["loglevel"]))
        parser.add_argument("-d", "--log_directory", nargs="?", type=str,
                            default=FileLogger.LOG_DIRECTORY,
                            help="File logger directory \n(default: '{}')"
                                 .format(FileLogger.LOG_DIRECTORY))
        args = parser.parse_args()
        return args

    def configure(self):
        self.db_client = MongoAccess()
        self.inv = InventoryMgr()
        self.inv.set_collections()
        self.collection = self.db_client.db[self.args.collection]
        self.environments_collection = self.db_client.db[self.args.environments_collection]
        self._update_document = partial(MongoAccess.update_document, self.collection)
        self.interval = max(self.MIN_INTERVAL, self.args.interval)
        self.log.set_loglevel(self.args.loglevel)

        self.log.info("Started ScanManager with following configuration:\n"
                      "Mongo config file path: {0.args.mongo_config}\n"
                      "Scans collection: {0.collection.name}\n"
                      "Environments collection: {0.environments_collection.name}\n"
                      "Polling interval: {0.interval} second(s)"
                      .format(self))

    def _build_scan_args(self, scan_request: dict):
        args = {
            'mongo_config': self.args.mongo_config
        }

        def set_arg(name_from: str, name_to: str = None):
            if name_to is None:
                name_to = name_from
            val = scan_request.get(name_from)
            if val:
                args[name_to] = val

        set_arg("object_id", "id")
        set_arg("log_level", "loglevel")
        set_arg("environment", "env")
        set_arg("scan_only_inventory", "inventory_only")
        set_arg("scan_only_links", "links_only")
        set_arg("scan_only_cliques", "cliques_only")
        set_arg("inventory")
        set_arg("clear")
        set_arg("clear_all")

        return args

    def _finalize_scan(self, scan_request: dict, status: ScanStatus, scanned: bool):
        scan_request['status'] = status.value
        self._update_document(scan_request)
        # If no object id is present, it's a full env scan.
        # We need to update environments collection
        # to reflect the scan results.
        if not scan_request.get('id'):
            self.environments_collection\
                .update_one(filter={'name': scan_request.get('environment')},
                            update={'$set': {'scanned': scanned}})

    def _fail_scan(self, scan_request: dict):
        self._finalize_scan(scan_request, ScanStatus.FAILED, False)

    def _complete_scan(self, scan_request: dict):
        self._finalize_scan(scan_request, ScanStatus.COMPLETED, True)

    # PyCharm type checker can't reliably check types of document
    # noinspection PyTypeChecker
    def _clean_up(self):
        # Find and fail all running scans
        running_scans = list(self
                             .collection
                             .find(filter={'status': ScanStatus.RUNNING.value}))
        self.collection\
            .update_many(filter={'_id': {'$in': [scan['_id']
                                                 for scan
                                                 in running_scans]}},
                         update={'$set': {'status': ScanStatus.FAILED.value}})

        # Find all environments connected to failed full env scans
        env_scans = [scan['environment']
                     for scan in running_scans
                     if not scan.get('object_id')
                     and scan.get('environment')]

        # Set 'scanned' flag in those envs to false
        if env_scans:
            self.environments_collection\
                .update_many(filter={'name': {'$in': env_scans}},
                             update={'$set': {'scanned': False}})

    def do_action(self):
        self._clean_up()
        try:
            while True:
                # Find a pending request that is waiting the longest time
                results = self.collection.find({'status': ScanStatus.PENDING.value,
                                                'submit_timestamp': {'$ne': None}})\
                                         .sort("submit_timestamp", pymongo.ASCENDING)\
                                         .limit(1)

                # If no scans are pending, sleep for some time
                if results.count() == 0:
                    time.sleep(self.interval)
                else:
                    scan_request = results[0]
                    if not self.inv.is_feature_supported(scan_request.get('environment'),
                                                         EnvironmentFeatures.SCANNING):
                        self.log.error("Scanning is not supported for env '{}'"
                                       .format(scan_request.get('environment')))
                        self._fail_scan(scan_request)
                        continue

                    scan_request['start_timestamp'] = datetime.datetime.utcnow()
                    scan_request['status'] = ScanStatus.RUNNING.value
                    self._update_document(scan_request)

                    # Prepare scan arguments and run the scan with them
                    try:
                        scan_args = self._build_scan_args(scan_request)

                        self.log.info("Starting scan for '{}' environment"
                                      .format(scan_args.get('env')))
                        self.log.debug("Scan arguments: {}".format(scan_args))
                        result, message = ScanController().run(scan_args)
                    except ScanArgumentsError as e:
                        self.log.error("Scan request '{id}' has invalid arguments. Errors:\n{errors}"
                                       .format(id=scan_request['_id'],
                                               errors=e))
                        self._fail_scan(scan_request)
                    except Exception as e:
                        self.log.exception(e)
                        self.log.error("Scan request '{}' has failed.".format(scan_request['_id']))
                        self._fail_scan(scan_request)
                    else:
                        # Check is scan returned success
                        if not result:
                            self.log.error(message)
                            self.log.error("Scan request '{}' has failed.".format(scan_request['_id']))
                            self._fail_scan(scan_request)
                            continue

                        # update the status and timestamps.
                        self.log.info("Request '{}' has been scanned.".format(scan_request['_id']))
                        end_time = datetime.datetime.utcnow()
                        scan_request['end_timestamp'] = end_time
                        self._complete_scan(scan_request)
        finally:
            self._clean_up()


if __name__ == "__main__":
    ScanManager().run()
