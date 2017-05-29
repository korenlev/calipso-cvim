import logging

from utils.logging.logger import Logger


class ConsoleLogger(Logger):

    def __init__(self):
        super().__init__(logger_name="{}-Console".format(self.PROJECT_NAME))
        self.add_handler(logging.StreamHandler())

