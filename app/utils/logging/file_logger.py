import logging.handlers

from utils.logging.logger import Logger


class FileLogger(Logger):

    def __init__(self, log_file: str, level: str = Logger.default_level):
        super().__init__(logger_name="{}-File".format(self.PROJECT_NAME),
                         level=level)
        self.add_handler(logging.handlers.WatchedFileHandler(log_file))

