import argparse
import datetime

import time

from discover.manager import Manager
from utils.exceptions import ScanArgumentsError
from utils.mongo_access import MongoAccess
from discover.scan import ScanController


class ScanManager(Manager):

    DEFAULTS = {
        "mongo_config": "",
        "collection": "scans",
        "interval": 1
    }

    def __init__(self):
        super().__init__()
        self.args = None
        self.db_client = None
        self.db = None

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
        parser.add_argument("-i", "--interval", nargs="?", type=float,
                            default=ScanManager.DEFAULTS["interval"],
                            help="Interval between collection polls"
                                 "(must be more than {} seconds)"
                            .format(ScanManager.MIN_INTERVAL))
        args = parser.parse_args()
        return args

    def configure(self):
        self.args = self.get_args()
        self.db_client = MongoAccess(self.args.mongo_config)
        self.db = MongoAccess.db
        self.collection = self.db[self.args.collection]
        self.interval = max(self.MIN_INTERVAL, self.args.interval)

        self.log.info("Started ScanManager with following configuration:\n"
                      "Mongo config file path: {0}\n"
                      "Collection: {1}\n"
                      "Polling interval: {2} second(s)"
                      .format(self.args.mongo_config, self.collection.name, self.interval))

    def _build_scan_args(self, scan_request):
        args = {
            'mongo_config': self.args.mongo_config
        }

        def set_arg(name_from, name_to=None):
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

    def do_action(self):
        while True:
            scan_request = self.collection.find_one({'status': 'pending',
                                                     'submit_timestamp': {'$ne': None}})

            # if no scans are pending, sleep for some time
            if not scan_request:
                time.sleep(self.interval)
            else:
                scan_request['start_timestamp'] = datetime.datetime.utcnow()
                scan_request['status'] = 'running'
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
                    scan_request['status'] = 'failed'
                    self._update_document(scan_request)
                except Exception as e:
                    self.log.error(e)
                    self.log.info("Scan request '{}' has failed.".format(scan_request['_id']))
                    scan_request['status'] = 'failed'
                    self._update_document(scan_request)
                else:
                    # Check is scan returned success
                    if not result:
                        self.log.error(message)
                        self.log.info("Scan request '{}' has failed.".format(scan_request['_id']))
                        scan_request['status'] = 'failed'
                        self._update_document(scan_request)

                    # update the status and timestamps.
                    self.log.info("Request '{}' has been scanned.".format(scan_request['_id']))
                    end_time = datetime.datetime.utcnow()
                    scan_request['status'] = 'completed'
                    scan_request['end_timestamp'] = end_time
                    self._update_document(scan_request)


if __name__ == "__main__":
    ScanManager().run()
