import logging
import logging.handlers

from utils.logging.logger import Logger
from utils.logging.mongo_logging_handler import MongoLoggingHandler


class FullLogger(Logger):

    def __init__(self, env: str = None, log_file: str = None):
        super().__init__(logger_name="{}-Full".format(self.PROJECT_NAME))

        # Console handler
        self.add_handler(logging.StreamHandler())

        # Message handler
        if env:  # TODO: make env optional
            self.add_handler(MongoLoggingHandler(env, self.level))

        # File handler
        if log_file:
            self.add_handler(logging.handlers.WatchedFileHandler(log_file))

    # Make sure we update MessageHandler with new env
    def set_env(self, env):
        super().set_env(env)

        defined_handler = next(
            filter(
                lambda handler: handler.__class__ == MongoLoggingHandler.__class__,
                self.log.handlers
            ), None)

        if defined_handler:
            defined_handler.env = env
        else:
            self.add_handler(MongoLoggingHandler(env, self.level))
