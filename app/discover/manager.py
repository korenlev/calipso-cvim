#!/usr/bin/env python3
from abc import ABC, abstractmethod

from utils.logging.logger import Logger


class Manager(Logger, ABC):

    MIN_INTERVAL = 0.1  # To prevent needlessly frequent scans

    def __init__(self):
        super().__init__()
        self.conf = None
        self.collection = None
        self._update_document = None
        self.interval = self.MIN_INTERVAL

    @abstractmethod
    def configure(self):
        pass

    @abstractmethod
    def do_action(self):
        pass

    def run(self):
        self.configure()
        self.do_action()
