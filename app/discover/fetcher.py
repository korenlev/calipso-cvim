import json

from discover.configuration import Configuration
from utils.logger import Logger


class Fetcher(Logger):

    def __init__(self):
        super().__init__()
        self.env = None
        self.configuration = None

    @staticmethod
    def escape(string):
        return string

    def set_env(self, env):
        self.env = env
        self.configuration = Configuration()

    def get_env(self):
        return self.env

    @staticmethod
    def jsonify(obj, prettify=False):
        if prettify:
            return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            return json.dumps(obj)

    def set_logger(self, loglevel):
        self.log.set_level(loglevel)
