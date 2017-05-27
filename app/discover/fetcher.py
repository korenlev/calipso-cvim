from discover.configuration import Configuration
from utils.logging.logger import Logger


class Fetcher(Logger):

    def __init__(self):
        super().__init__()
        self.configuration = None

    @staticmethod
    def escape(string):
        return string

    def set_env(self, env):
        super().set_env(env)
        self.configuration = Configuration()

    def get_env(self):
        return self.env
