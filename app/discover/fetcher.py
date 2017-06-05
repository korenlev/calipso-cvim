from discover.configuration import Configuration
from utils.logging.full_logger import FullLogger


class Fetcher:

    def __init__(self):
        super().__init__()
        self.env = None
        self.log = FullLogger()
        self.configuration = None

    @staticmethod
    def escape(string):
        return string

    def set_env(self, env):
        self.env = env
        self.log.set_env(env)
        self.configuration = Configuration()

    def get_env(self):
        return self.env
