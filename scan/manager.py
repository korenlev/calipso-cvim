#!/usr/bin/env python3
###############################################################################
# Copyright (c) 2017-2019 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import datetime

from abc import ABC, abstractmethod

from base.utils.logging.file_logger import FileLogger
from base.utils.logging.full_logger import FullLogger
from base.utils.mongo_access import MongoAccess


class Manager(ABC):

    def __init__(self, log_directory: str = None,
                 mongo_config_file: str = None,
                 log_level: str = None):
        super().__init__()
        if log_directory:
            FileLogger.LOG_DIRECTORY = log_directory
        MongoAccess.config_file = mongo_config_file
        self.log = FullLogger(level=log_level)
        self.conf = None
        self.inv = None
        self.collection = None
        self._update_document = None

    @abstractmethod
    def configure(self):
        pass

    @abstractmethod
    def do_action(self):
        pass

    def run(self):
        self.configure()
        self.do_action()
