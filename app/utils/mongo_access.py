import os
import sys

from pymongo import MongoClient
from utils.dict_naming_converter import DictNamingConverter
from utils.logger import Logger
from utils.util import Util


# Provides access to MongoDB using PyMongo library
#
# Notes on authentication:
# default config file is /etc/osdna/mongo.conf
# you can also specify name of file from CLI with --mongo_config


class MongoAccess(Logger, Util, DictNamingConverter):
    client = None
    db = None
    default_conf_file = 'osdna_mongo_access.conf'

    def __init__(self, config_file=""):
        super().__init__()
        self.mongo_connect(config_file)

    def mongo_connect(self, config_file=""):
        if (MongoAccess.client is not None):
            return
        self.connect_params = {
            "server": "localhost",
            "port": 27017
        }
        if not config_file:
            config_file = self.get_config_file(self.default_conf_file)
            if not os.path.isfile(config_file):
                msg = "failed to open config file: " + config_file
                self.log.error(msg)
                sys.exit(1)
        if config_file:
            try:
                # read connection parameters from file
                config_params = self.read_config_from_config_file(config_file)
                self.connect_params.update(config_params)
            except Exception:
                self.log.error("failed to open config file: " + config_file)
                raise
        self.prepare_connect_uri()
        MongoAccess.client = MongoClient(
            self.connect_params["server"],
            self.connect_params["port"]
        )
        MongoAccess.db = MongoAccess.client.osdna

    def prepare_connect_uri(self):
        params = self.connect_params
        uri = 'mongodb://'
        if 'password' in params:
            uri = uri + params['user'] + ':' + params['password'] + '@'
        uri = uri + params['server']
        if 'auth_db' in params:
            uri = uri + '/' + params['auth_db']
        self.connect_params['server'] = uri

    def encode_dots(self, s):
        return s.replace(".", "[dot]")

    def decode_dots(self, s):
        return s.replace("[dot]", ".")

    # Mongo will not accpet dot (".") in keys, or $ in start of keys
    # $ in beginning of key does not happen in OpenStack,
    # so need to translate only "." --> "[dot]"
    def encode_mongo_keys(self, item):
        return self.change_dict_naming_convention(item, self.encode_dots)

    def decode_mongo_keys(self, item):
        return self.change_dict_naming_convention(item, self.decode_dots)
