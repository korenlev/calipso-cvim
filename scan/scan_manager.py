###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import argparse
import datetime
import time

import pymongo
from dateutil.relativedelta import relativedelta
from functools import partial

import urllib3

from base.fetcher import Fetcher
from base.utils.constants import ScanStatus, EnvironmentFeatures, ScheduledScanInterval, ScheduledScanStatus
from base.utils.elastic_access import ElasticAccess
from base.utils.exceptions import ScanArgumentsError
from base.utils.inventory_mgr import InventoryMgr
from base.utils.logging.file_logger import FileLogger
from base.utils.logging.full_logger import FullLogger
from base.utils.logging.logger import Logger
from base.utils.mongo_access import MongoAccess
from base.utils.origins import ScanOrigins, ScanOrigin
from base.manager import Manager
from scan.scan import ScanController


class ScanManager(Manager):

    DEFAULTS = {
        "mongo_config": "",
        "es_config": "",
        "scans": "scans",
        "scheduled_scans": "scheduled_scans",
        "environments": "environments_config",
        "interval": 1,
        "loglevel": "INFO",
        "logfile": "scan_manager.log",
    }

    MIN_INTERVAL = 0.1  # To prevent needlessly frequent scans

    INTERVALS = {
        ScheduledScanInterval.ONCE: None,
        ScheduledScanInterval.HOURLY: relativedelta(hours=1),
        ScheduledScanInterval.DAILY: relativedelta(days=1),
        ScheduledScanInterval.WEEKLY: relativedelta(weeks=1),
        ScheduledScanInterval.MONTHLY: relativedelta(months=1),
        ScheduledScanInterval.YEARLY: relativedelta(years=1),
    }

    LOG_NAME = "Scanner"
    LOG_FILE = "scanner.log"

    def __init__(self):
        self.args = self.get_args()
        super().__init__(log_directory=self.args.log_directory,
                         log_level=self.args.loglevel,
                         log_file=self.args.logfile,
                         mongo_config_file=self.args.mongo_config)
        self.db_client = None
        self.environments_collection = None
        self.scans_collection = None
        self.scheduled_scans_collection = None
        self.es_client = None
        self.interval = None

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                            default=ScanManager.DEFAULTS["mongo_config"],
                            help="Path to config file " +
                                 "with MongoDB server access details")
        parser.add_argument("--es_config", nargs="?", type=str,
                            default=ScanManager.DEFAULTS["es_config"],
                            help="Path to config file " +
                                 "with ElasticSearch server access details")
        parser.add_argument("-c", "--scans_collection", nargs="?", type=str,
                            default=ScanManager.DEFAULTS["scans"],
                            help="Scans collection to read from")
        parser.add_argument("-s", "--scheduled_scans_collection", nargs="?",
                            type=str,
                            default=ScanManager.DEFAULTS["scheduled_scans"],
                            help="Scans collection to read from")
        parser.add_argument("-e", "--environments_collection", nargs="?",
                            type=str,
                            default=ScanManager.DEFAULTS["environments"],
                            help="Environments collection to update "
                                 "after scans")
        parser.add_argument("-i", "--interval", nargs="?", type=float,
                            default=ScanManager.DEFAULTS["interval"],
                            help="Interval between collection polls"
                                 "(must be more than {} seconds)"
                                 .format(ScanManager.MIN_INTERVAL))
        parser.add_argument("-f", "--logfile", nargs="?", type=str,
                            default=ScanManager.DEFAULTS["logfile"],
                            help="Scan manager log file name \n(default: '{}')"
                                 .format(ScanManager.DEFAULTS["logfile"]))
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
        self.scans_collection = self.db_client.db[self.args.scans_collection]
        self.scheduled_scans_collection = self.db_client.db[self.args.scheduled_scans_collection]
        self.environments_collection = self.db_client.db[self.args.environments_collection]
        self._update_document = partial(MongoAccess.update_document, self.scans_collection)
        self.interval = max(self.MIN_INTERVAL, self.args.interval)

        # ElasticSearch post-scan indexing is disabled in this release, no ES connection
        self.es_client = ElasticAccess()
        #self._connect_es_client(self.args.es_config)

        self.log.info("Started ScanManager with following configuration: {1}. {2}. "
                      "Scans collection: {0.scans_collection.name}. "
                      "Environments collection: {0.environments_collection.name}. "
                      "Polling interval: {0.interval} second(s)"
                      .format(self,
                              MongoAccess.get_source_text(),
                              self.es_client.get_connection_text()))

    def _connect_es_client(self, es_config, retries=ElasticAccess.CONNECTION_RETRIES):
        if not self.es_client:
            return False

        ElasticAccess.config_file = es_config
        try:
            self.es_client.connect(retries)
        except (urllib3.exceptions.NewConnectionError, ConnectionError) as e:
            self.log.error("Failed to connect to ElasticSearch. Error: {}".format(e))
        return self.es_client.is_connected

    def _build_scan_args(self, scan_request: dict):
        args = {
            'mongo_config': self.args.mongo_config,
            'scheduled': True if scan_request.get('interval') else False
        }

        def set_arg(name_from: str, name_to: str = None):
            if name_to is None:
                name_to = name_from
            val = scan_request.get(name_from)
            if val:
                args[name_to] = val

        set_arg("_id")
        set_arg("object_id", "id")
        set_arg("log_level", "loglevel")
        set_arg("environment", "env")
        set_arg("scan_only_inventory", "inventory_only")
        set_arg("scan_only_links", "links_only")
        set_arg("scan_only_cliques", "cliques_only")
        set_arg("implicit_links")
        set_arg("inventory")
        set_arg("clear")
        set_arg("clear_all")

        return args

    def _finalize_scan(self, scan_request: dict, status: ScanStatus,
                       scanned: bool):
        scan_request['status'] = status.value
        self._update_document(scan_request)
        # If no object id is present, it's a full env scan.
        # We need to update environments collection
        # to reflect the scan results.
        if not scan_request.get('id'):
            env_update_data = {'scanned': scanned}
            if scanned:
                env_update_data['last_scanned'] = scan_request.get('end_timestamp')

            self.environments_collection\
                .update_one(filter={'name': scan_request.get('environment')},
                            update={'$set': MongoAccess.encode_mongo_keys(env_update_data)})

    def _fail_scan(self, scan_request: dict):
        self._finalize_scan(scan_request, ScanStatus.FAILED, False)

    def _complete_scan(self, scan_request: dict, result_message: str):
        status = ScanStatus.COMPLETED if result_message == 'ok' \
            else ScanStatus.COMPLETED_WITH_ERRORS
        self._finalize_scan(scan_request, status, True)

    # PyCharm type checker can't reliably check types of document
    # noinspection PyTypeChecker
    def _clean_up(self):
        # Find and fail all running scans
        running_scans = list(self
                             .scans_collection
                             .find(filter={'status': ScanStatus.RUNNING.value}))
        self.scans_collection \
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

    def _submit_scan_request_for_schedule(self, scheduled_scan, ts):
        scans = self.scans_collection
        new_scan = {
            'status': ScanStatus.PENDING.value,
            'log_level': scheduled_scan['log_level'],
            'clear': scheduled_scan['clear'],
            'scan_only_inventory': scheduled_scan['scan_only_inventory'],
            'scan_only_links': scheduled_scan['scan_only_links'],
            'scan_only_cliques': scheduled_scan['scan_only_cliques'],
            'implicit_links': scheduled_scan.get('implicit_links', False),
            'submit_timestamp': ts,
            'environment': scheduled_scan['environment'],
            'es_index': scheduled_scan.get('es_index', False)
        }
        scans.insert_one(new_scan)

    def _set_scheduled_requests_next_run(self, scheduled_scan, interval, ts):
        if self.INTERVALS[interval]:
            scheduled_scan['scheduled_timestamp'] = ts + self.INTERVALS[interval]
            status = scheduled_scan.get('status')
            if not status or status == ScheduledScanStatus.UPCOMING.value:
                scheduled_scan['status'] = ScheduledScanStatus.ONGOING.value
        else:
            scheduled_scan['status'] = ScheduledScanStatus.FINISHED.value
        doc_id = scheduled_scan.pop('_id')
        self.scheduled_scans_collection.update({'_id': doc_id}, scheduled_scan)

    def _prepare_scheduled_requests_for_interval(self, interval):
        now = datetime.datetime.utcnow()
        condition = {
            'imported': {'$ne': True},
            'send_to_remote': {'$ne': True},
            'recurrence': interval.value,
            'scheduled_timestamp': {'$lte': now},
            'status': {'$ne': ScheduledScanStatus.FINISHED.value}
        }
        matches = self.scheduled_scans_collection.find(condition).sort('scheduled_timestamp', pymongo.ASCENDING)
        for match in matches:
            # first, submit a scan request where the scheduled time has come
            self._submit_scan_request_for_schedule(match, now)
            # next, set the next run time for the scheduled scan
            self._set_scheduled_requests_next_run(match, interval, now)

    def _prepare_scheduled_requests(self):
        # see if any scheduled request is waiting to be submitted
        for interval in self.INTERVALS.keys():
            self._prepare_scheduled_requests_for_interval(interval)

    def handle_scans(self):
        self._prepare_scheduled_requests()

        # Find a pending request that is waiting the longest time
        results = (
            self.scans_collection.find({
                'status': ScanStatus.PENDING.value,
                'submit_timestamp': {'$ne': None},
                'imported': {'$ne': True},
                'send_to_remote': {'$ne': True}
            }).sort("submit_timestamp", pymongo.ASCENDING).limit(1)
        )

        # If no scans are pending, sleep for some time
        if results.count() == 0:
            time.sleep(self.interval)
        else:
            scan_request = results[0]
            env = scan_request.get('environment')
            scan_feature = EnvironmentFeatures.SCANNING
            origin = ScanOrigin(origin_id=scan_request["_id"],
                                origin_type=(ScanOrigins.SCHEDULED
                                             if scan_request.get("scheduled")
                                             else ScanOrigins.MANUAL))

            log_level = scan_request.get('log_level', Logger.default_level)
            try:
                Logger.check_level(log_level)
            except ValueError as e:
                self.log.error(e)
                self._fail_scan(scan_request)
                return

            logger = FullLogger(name=self.LOG_NAME,
                                log_file=self.LOG_FILE,
                                env=env, origin=origin,
                                level=log_level)
            if not self.inv.is_feature_supported(env, scan_feature):
                logger.error("Scanning is not supported for env '{}'".format(scan_request.get('environment')))
                self._fail_scan(scan_request)
                return

            scan_request['start_timestamp'] = datetime.datetime.utcnow()
            scan_request['status'] = ScanStatus.RUNNING.value
            self._update_document(scan_request)

            # Prepare scan arguments and run the scan with them
            try:
                scan_args = self._build_scan_args(scan_request)
                scan_args.update({
                    'origin': origin,
                    'logger': logger,
                    'logfile': self.LOG_FILE
                })

                logger.info("Starting scan for '{}' environment".format(scan_args.get('env')))
                logger.debug("Scan arguments: {}".format(scan_args))
                result, message = ScanController().run(scan_args)
            except ScanArgumentsError as e:
                logger.error("Scan request '{id}' "
                             "has invalid arguments. "
                             "Errors: {errors}"
                             .format(id=scan_request['_id'],
                                     errors=e))
                self._fail_scan(scan_request)
            except Exception as e:
                logger.exception(e)
                logger.error("Scan request '{}' has failed."
                             .format(scan_request['_id']))
                self._fail_scan(scan_request)
            else:
                # Check is scan returned success
                if not result:
                    logger.error(message)
                    logger.error("Scan request '{}' has failed."
                                 .format(scan_request['_id']))
                    self._fail_scan(scan_request)
                    return

                # update the status and timestamps.
                logger.info("Request '{}' has been scanned. ({})"
                            .format(scan_request['_id'], message))
                end_time = datetime.datetime.utcnow()
                scan_request['end_timestamp'] = end_time

                self._complete_scan(scan_request, message)
                if scan_request.get('es_index') is True:
                    self.log.error("ElasticSearch post-scan indexing is disabled in this release")
                    # below lines can enable post-scan indexing, kept for future demand
                    #if self.es_client.is_connected:
                    #    try:
                    #        self.es_client.dump_collections(env)
                    #        self.es_client.dump_tree(env)
                    #    except Exception as e:
                    #        self.log.error("Error occurred while trying "
                    #                       "to index documents to ElasticSearch: {}".format(e))
                    #elif not self._connect_es_client(self.args.es_config, retries=3):
                    #    self.log.error("ElasticSearch client is not connected, but post-scan indexing was requested")

    def do_action(self):
        self._clean_up()
        try:
            while True:
                self.handle_scans()
        finally:
            self._clean_up()


if __name__ == "__main__":
    ScanManager().run()
