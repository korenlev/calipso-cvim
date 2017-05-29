import logging

from utils.logging.logger import Logger


class ConsoleLogger(Logger):

    def __init__(self):
        super().__init__()
        self.add_handler(logging.StreamHandler())
