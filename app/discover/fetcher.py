import json

from discover.configuration import Configuration
from utils.logger import Logger


class Fetcher(Logger):

    def __init__(self):
        super().__init__()
        self.env = None
        self.configuration = None

    # TODO: is this method supposed to do nothing?
    @staticmethod
    def escape(string):
        return string

    def set_env(self, env):
        self.env = env
        self.configuration = Configuration()

    def get_env(self):
        return self.env
