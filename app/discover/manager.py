#!/usr/bin/env python3
from abc import ABC, abstractmethod

from utils.logger import Logger


class Manager(Logger, ABC):

    MIN_INTERVAL = 0.1  # To prevent needlessly frequent scans

    def __init__(self):
        super().__init__()
        self.conf = None
        self.collection = None
        self.interval = self.MIN_INTERVAL

    @abstractmethod
    def configure(self):
        pass

    @abstractmethod
    def do_action(self):
        pass

    def _update_document(self, document, upsert=False):
        self.collection.update_one({'_id': document['_id']},
                                   {'$set': document}, upsert=upsert)

    def run(self):
        self.configure()
        self.do_action()
