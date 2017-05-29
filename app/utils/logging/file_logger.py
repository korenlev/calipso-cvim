import logging.handlers

from utils.logging.logger import Logger


class FileLogger(Logger):

    def __init__(self, log_file: str):
        super().__init__()
        self.log = logging.getLogger("{}-File".format(self.PROJECT_NAME))
        self.add_handler(logging.handlers.WatchedFileHandler(log_file))
