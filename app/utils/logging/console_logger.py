import logging

from utils.logging.logger import Logger


class ConsoleLogger(Logger):

    def __init__(self):
        super().__init__()
        ch = logging.StreamHandler()
        ch.setLevel(self.default_level)
        ch.setFormatter(self.formatter)
        self.log.addHandler(ch)
