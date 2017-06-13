#!/usr/bin/env python3
from abc import ABC, abstractmethod

from utils.logging.full_logger import FullLogger
from utils.mongo_access import MongoAccess


class Manager(ABC):

    MIN_INTERVAL = 0.1  # To prevent needlessly frequent scans

    def __init__(self, mongo_config_file: str = None):
        super().__init__()
        MongoAccess.config_file = mongo_config_file
        self.log = FullLogger()
        self.conf = None
        self.inv = None
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
