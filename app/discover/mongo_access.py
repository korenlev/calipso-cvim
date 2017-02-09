import os
import sys

from bson.objectid import ObjectId
from pymongo import MongoClient
from discover.logger import Logger


# Provides access to MongoDB using PyMongo library
#
# Notes on authentication:
# default config file is /etc/osdna/mongo.conf
# you can also specify name of file from CLI with --mongo_config


class MongoAccess(Logger):
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
            # try to look in the current work directory
            # as defined by PYTHONPATH
            python_path = os.environ['PYTHONPATH']
            if os.pathsep in python_path:
                python_path = python_path.split(os.pathsep)[0]
            config_file = python_path + '/config/' + self.default_conf_file
            if not os.path.isfile(config_file):
                msg = "failed to open config file: " + config_file
                self.log.error(msg)
                sys.exit(1)
        if config_file:
            # read connection parameters from file
            try:
                with open(config_file) as f:
                    for line in f:
                        l = line.strip()
                        if " " not in l:
                            continue
                        pos = l.index(" ")
                        attr = l[:pos]
                        if attr.startswith("#"):
                            continue  # skip comments
                        val = l[pos + 1:].strip()
                        if val:
                            self.connect_params[attr] = val
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

    # Convert a nested dictionary from one convention to another.
    # Args:
    #     d (dict): dictionary (nested or not) to be converted.
    #     cf (func): convert function - takes the string in one convention,
    #                returns it in the other one.
    # Returns:
    #     Dictionary with the new keys.
    def change_dict_naming_convention(self, d, cf):
        new = {}
        if not d:
            return d
        if isinstance(d, str):
            return d
        if isinstance(d, ObjectId):
            return d
        for k, v in d.items():
            new_v = v
            if isinstance(v, dict):
                new_v = self.change_dict_naming_convention(v, cf)
            elif isinstance(v, list):
                new_v = list()
                for x in v:
                    new_v.append(self.change_dict_naming_convention(x, cf))
            new[cf(k)] = new_v
        return new
