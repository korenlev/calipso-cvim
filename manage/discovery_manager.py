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
from typing import Optional

from base.manager import Manager
from base.utils.data_access_base import DataAccessBase
from base.utils.logging.file_logger import FileLogger
from base.utils.logging.logger import Logger
from manage import discovery_api
from manage.async_mongo_connector import AsyncMongoConnector
from manage.async_replication_client import AsyncReplicationClient
from manage.pod_data import PodData
from manage.pod_manager import PodManager
from manage.schedule_manager import ScheduleManager


class DiscoveryManager(Manager, DataAccessBase):
    REQUIRED_ENV_VARIABLES = {
        'central_mongo_host': 'CALIPSO_MONGO_SERVICE_HOST',
        'central_mongo_password': 'CALIPSO_MONGO_SERVICE_PWD',
    }
    OPTIONAL_ENV_VARIABLES = {
        'discovery_api_user': 'CALIPSO_MANAGE_SERVICE_USER',
        'discovery_api_password': 'CALIPSO_MANAGE_SERVICE_PWD',
        'central_mongo_port': 'CALIPSO_MONGO_SERVICE_PORT',
        'central_mongo_user': 'CALIPSO_MONGO_SERVICE_USER',
    }

    DEFAULTS = {
        "bind": "0.0.0.0",
        "port": "8757",
        "log_file": "discovery_manager.log",
        "log_level": Logger.INFO,
        "cert_file": "",
        "key_file": "",
        "project_prefix": "cvim"
    }

    def __init__(self):
        self.args: argparse.Namespace = self.get_args()
        super().__init__(log_directory=self.args.log_directory,
                         log_level=self.args.log_level, log_file=self.args.log_file)

        self.setup_data: Optional[dict] = None
        self.project_prefix: str = self.args.project_prefix
        self.verify_remotes_tls: bool = not self.args.skip_remotes_tls_verify

        calipso_connection_params = self.get_connection_parameters()
        self.central_mongo_host: str = calipso_connection_params['central_mongo_host']
        self.central_mongo_port: int = int(calipso_connection_params.get('central_mongo_port',
                                                                         AsyncMongoConnector.DEFAULT_PORT))
        self.central_mongo_user: str = calipso_connection_params.get('central_mongo_user',
                                                                     AsyncMongoConnector.DEFAULT_USER)
        self.central_mongo_password: str = calipso_connection_params['central_mongo_password']

        self.discovery_api_user: str = calipso_connection_params.get('discovery_api_user')
        self.discovery_api_password: str = calipso_connection_params.get('discovery_api_password')

        self.schedule_manager: Optional[ScheduleManager] = None
        self.discovery_api: Optional[discovery_api.DiscoveryAPI] = None

        self.tls: bool = False
        if self.args.key_file and self.args.cert_file:
            self.tls = True
        elif self.args.key_file or self.args.cert_file:
            raise ValueError("Either both key_file and cert_file should be specified or neither")

    @staticmethod
    def get_args() -> argparse.Namespace:
        parser = argparse.ArgumentParser()
        parser.add_argument("--cert_file", nargs="?", type=str,
                            default=DiscoveryManager.DEFAULTS["cert_file"],
                            help="Path to SSL certificate")
        parser.add_argument("--key_file", nargs="?", type=str,
                            default=DiscoveryManager.DEFAULTS["key_file"],
                            help="Path to SSL key")
        parser.add_argument("-b", "--bind", nargs="?", type=str,
                            default=DiscoveryManager.DEFAULTS["bind"],
                            help="Address or addresses to bind Discovery API to. "
                                 "Must be a hostname/IP or a list of comma-separated hostnames/IPs")
        parser.add_argument("-p", "--port", nargs="?", type=int,
                            default=DiscoveryManager.DEFAULTS["port"],
                            help="A port for Discovery API to bind to")
        parser.add_argument("-d", "--log_directory", nargs="?", type=str,
                            default=FileLogger.LOG_DIRECTORY,
                            help="Log file path \n(default: '{}')"
                            .format(FileLogger.LOG_DIRECTORY))
        parser.add_argument("-f", "--log_file", nargs="?", type=str,
                            default=DiscoveryManager.DEFAULTS["log_file"],
                            help="Scan manager log file name \n(default: '{}')"
                            .format(DiscoveryManager.DEFAULTS["log_file"])),
        parser.add_argument("-l", "--log_level", nargs="?", type=str,
                            default=DiscoveryManager.DEFAULTS["log_level"],
                            help="Logging level \n(default: '{}')"
                            .format(DiscoveryManager.DEFAULTS["log_level"]))
        parser.add_argument("--project_prefix", nargs="?", type=str,
                            default=DiscoveryManager.DEFAULTS["project_prefix"],
                            help="Project prefix to use in environment configurations")
        parser.add_argument("--skip_remotes_tls_verify", action="store_true",
                            help="Skip TLS verification on remotes")
        parser.add_argument("--skip_discovery", action="store_true", default=False,
                            help="Skip remotes discovery (simulate schedules only)"
                            .format(DiscoveryManager.DEFAULTS["log_level"]))
        parser.add_argument("--skip_replication", action="store_true", default=False,
                            help="Skip remotes replication (simulate schedules only)"
                            .format(DiscoveryManager.DEFAULTS["log_level"]))
        args = parser.parse_args()
        return args

    def configure_central_pod(self) -> None:
        PodData.set_project_prefix(self.project_prefix)
        PodData.VERIFY_TLS = self.verify_remotes_tls

        self.schedule_manager = ScheduleManager(mongo_host=self.central_mongo_host,
                                                mongo_port=self.central_mongo_port,
                                                mongo_pwd=self.central_mongo_password,
                                                mongo_user=self.central_mongo_user,
                                                log_directory=self.args.log_directory,
                                                log_file=self.args.log_file,
                                                log_level=self.args.log_level,
                                                skip_discovery=self.args.skip_discovery,
                                                skip_replication=self.args.skip_replication)

        self.schedule_manager.run(detach=True)

    def stop_schedule_manager(self):
        if self.schedule_manager:
            self.schedule_manager.stop()

    @staticmethod
    def setup_loggers(level: str = Logger.INFO, log_file: str = ""):
        if log_file:
            for cls in (AsyncReplicationClient, discovery_api.DiscoveryAPI, PodManager):
                cls.LOG_FILE = log_file
        for cls in (AsyncReplicationClient, discovery_api.DiscoveryAPI, PodManager):
            cls.LOG_LEVEL = level

    def configure(self) -> None:
        self.setup_loggers(level=self.args.log_level, log_file=self.args.log_file)
        self.configure_central_pod()

        self.discovery_api = discovery_api.DiscoveryAPI(discovery_mgr=self,
                                                        user=self.discovery_api_user,
                                                        password=self.discovery_api_password,
                                                        host=self.args.bind,
                                                        port=self.args.port,
                                                        tls=self.tls,
                                                        key_file=self.args.key_file,
                                                        cert_file=self.args.cert_file)
        discovery_api.discovery_manager = self

        self.log.info("Started DiscoveryManager with following configuration: "
                      "Bind address(es): {0.bind}, port: {0.port}. "
                      "Log path: {0.log_directory}{0.log_file}, log level: {0.log_level}. "
                      .format(self.args))

    def do_action(self) -> None:
        self.discovery_api.run()


if __name__ == "__main__":
    discovery_manager = DiscoveryManager()
    try:
        discovery_manager.run()
    finally:
        discovery_manager.stop_schedule_manager()
