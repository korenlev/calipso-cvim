from pymongo import MongoClient

from utils.config_file import ConfigFile
from utils.dict_naming_converter import DictNamingConverter
from utils.logging.file_logger import FileLogger


# Provides access to MongoDB using PyMongo library
#
# Notes on authentication:
# default config file is /etc/osdna/mongo.conf
# you can also specify name of file from CLI with --mongo_config


class MongoAccess(DictNamingConverter):
    client = None
    db = None
    default_conf_file = '/local_dir/osdna_mongo_access.conf'
    config_file = None

    LOG_FILE = '/var/log/osdna/mongo_access.log'

    def __init__(self):
        self.log = FileLogger(self.LOG_FILE)
        self.ready = False
        self.connect_params = {}
        if not MongoAccess.config_file:
            raise ValueError('MongoAccess config file was not set')
        self.mongo_connect(MongoAccess.config_file)

    def is_db_ready(self) -> bool:
        return self.ready

    @staticmethod
    def set_config_file(_conf_file):
        MongoAccess.config_file = _conf_file

    def mongo_connect(self, config_file_path=""):
        if MongoAccess.client:
            return

        self.connect_params = {
            "server": "localhost",
            "port": 27017
        }

        if not config_file_path:
            config_file_path = self.default_conf_file

        try:
            config_file = ConfigFile(config_file_path)
            # read connection parameters from config file
            config_params = config_file.read_config()
            self.connect_params.update(config_params)
        except Exception as e:
            self.log.exception(e)
            raise

        self.prepare_connect_uri()
        MongoAccess.client = MongoClient(
            self.connect_params["server"],
            self.connect_params["port"]
        )
        MongoAccess.db = MongoAccess.client.osdna
        self.log.info('Connected to MongoDB')
        self.ready = True

    def prepare_connect_uri(self):
        params = self.connect_params
        self.log.debug('connecting to MongoDb server: {}'
                       .format(params['server']))
        uri = 'mongodb://'
        if 'password' in params:
            uri = uri + params['user'] + ':' + params['password'] + '@'
        uri = uri + params['server']
        if 'auth_db' in params:
            uri = uri + '/' + params['auth_db']
        self.connect_params['server'] = uri

    @staticmethod
    def update_document(collection, document, upsert=False):
        if isinstance(collection, str):
            collection = MongoAccess.db[collection]
        collection.update_one({'_id': document['_id']},
                              {'$set': document}, upsert=upsert)

    @staticmethod
    def encode_dots(s):
        return s.replace(".", "[dot]")

    @staticmethod
    def decode_dots(s):
        return s.replace("[dot]", ".")

    # Mongo will not accept dot (".") in keys, or $ in start of keys
    # $ in beginning of key does not happen in OpenStack,
    # so need to translate only "." --> "[dot]"
    @staticmethod
    def encode_mongo_keys(item):
        return MongoAccess.change_dict_naming_convention(item, MongoAccess.encode_dots)

    @staticmethod
    def decode_mongo_keys(item):
        return MongoAccess.change_dict_naming_convention(item, MongoAccess.decode_dots)

    @staticmethod
    def decode_object_id(item: dict):
        return dict(item, **{"_id": str(item["_id"])}) if item and "_id" in item else item
