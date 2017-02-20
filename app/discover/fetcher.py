import json

from utils.binary_converter import BinaryConverter
from discover.configuration import Configuration
from discover.logger import Logger


class Fetcher(Logger):
    env = None
    configuration = None

    def __init__(self):
        super().__init__()

    @staticmethod
    def escape(string):
        return string

    @staticmethod
    def set_env(env):
        Fetcher.env = env
        Fetcher.configuration = Configuration()

    @staticmethod
    def get_env():
        return Fetcher.env

    @staticmethod
    def jsonify(obj, prettify=False):
        if prettify:
            return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            return json.dumps(obj)

    def set_logger(self, loglevel):
        self.log.set_level(loglevel)
