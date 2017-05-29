import logging

from utils.logging.logger import Logger
from utils.logging.mongo_logging_handler import MongoLoggingHandler


class MessageLogger(Logger):

    def __init__(self, env: str = None):
        super().__init__(logger_name="{}-Message".format(self.PROJECT_NAME))
        self.add_handler(MongoLoggingHandler(env, self.level))
