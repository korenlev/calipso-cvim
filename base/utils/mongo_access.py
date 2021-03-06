###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from urllib.parse import quote_plus

from pymongo import MongoClient
import ssl

from base.utils.data_access_base import DataAccessBase
from base.utils.dict_naming_converter import DictNamingConverter
# Provides access to MongoDB using PyMongo library
#
# Notes on authentication:
# default config file is calipso_mongo_access.conf
# you can also specify name of file from CLI with --mongo_config


class MongoAccess(DataAccessBase, DictNamingConverter):
    client = None
    db = None
    default_conf_file = '/local_dir/calipso_mongo_access.conf'
    config_file = None

    DB_NAME = 'calipso'
    LOG_FILENAME = 'mongo_access.log'

    REQUIRED_ENV_VARIABLES = {
        'server': 'CALIPSO_MONGO_SERVICE_HOST',
        'user': 'CALIPSO_MONGO_SERVICE_USER',
        'pwd': 'CALIPSO_MONGO_SERVICE_PWD'
    }
    OPTIONAL_ENV_VARIABLES = {
        'port': 'CALIPSO_MONGO_SERVICE_PORT',
        'auth_db': 'CALIPSO_MONGO_SERVICE_AUTH_DB',
        'rs': 'CALIPSO_MONGO_SERVICE_RS_NAME'
    }

    def __init__(self):
        super().__init__()

        self.connect_params = {}
        self.mongo_connect()

    @staticmethod
    def is_db_ready() -> bool:
        return MongoAccess.client is not None

    @staticmethod
    def escape_ipv6(host: str) -> str:
        return "[{}]".format(host) if len(host.split(":")) > 1 else host

    def mongo_connect(self):
        if MongoAccess.client:
            return

        self.connect_params = {
            "server": "localhost",
            "port": 27017
        }

        connection_params = self.get_connection_parameters()
        self.connect_params.update(connection_params)

        self.prepare_connect_uri()
        MongoAccess.client = MongoClient(
            self.connect_params["server"],
            int(self.connect_params["port"]),
            ssl=True, ssl_cert_reqs=ssl.CERT_NONE
        )
        MongoAccess.db = getattr(MongoAccess.client,
                                 self.connect_params.get('auth_db', self.DB_NAME))
        MongoAccess.db.authenticate(name=self.connect_params['user'],
                                    password=self.connect_params['pwd'])
        self.log.info('Connected to MongoDB')

    def prepare_connect_uri(self):
        params = self.connect_params
        self.log.debug('connecting to MongoDB server: {}'
                       .format(params['server']))
        uri = 'mongodb://'
        if 'user' in params and 'pwd' in params:
            uri += '{}:{}@'.format(quote_plus(params['user']), quote_plus(params['pwd']))
        else:
            self.log.info('MongoDB credentials missing')

        uri += "{}/".format(self.escape_ipv6(params['server']))

        if 'auth_db' in params:
            uri += '{}'.format(params['auth_db'])
        if 'rs' in params:
            uri += '?replicaSet={}'.format(params['rs'])

        self.connect_params['server'] = uri

    @staticmethod
    def update_document(collection, document, upsert=False):
        if isinstance(collection, str):
            collection = MongoAccess.db[collection]
        doc_id = document.pop('_id')
        collection.update_one(
            {'_id': doc_id},
            {'$set': MongoAccess.encode_mongo_keys(document)},
            upsert=upsert
        )
        document['_id'] = doc_id

    @staticmethod
    def encode_dots(s):
        return s.replace(".", "[dot]")

    @staticmethod
    def encode_starting_dollars(s):
        return s.replace("$", "[dollar]") if s.startswith("$") else s

    @classmethod
    def encode_all(cls, s):
        return cls.encode_starting_dollars(cls.encode_dots(s))

    @staticmethod
    def decode_dots(s):
        return s.replace("[dot]", ".")

    @staticmethod
    def decode_starting_dollars(s):
        return s.replace("[dollar]", "$") if s.startswith("[dollar]") else s

    @classmethod
    def decode_all(cls, s):
        return cls.decode_starting_dollars(cls.decode_dots(s))

    # Mongo will not accept dot (".") in keys, or $ in start of keys
    # $ in beginning of key does not happen in OpenStack,
    # so need to translate only "." --> "[dot]"
    @staticmethod
    def encode_mongo_keys(item):
        change_naming_func = MongoAccess.change_dict_naming_convention
        return change_naming_func(item, MongoAccess.encode_all)

    @staticmethod
    def decode_mongo_keys(item):
        change_naming_func = MongoAccess.change_dict_naming_convention
        return change_naming_func(item, MongoAccess.decode_all)

    @staticmethod
    def decode_object_id(item: dict):
        return dict(item, **{"_id": str(item["_id"])}) \
            if item and "_id" in item \
            else item
