#!/usr/bin/env python3
###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import asyncio
from abc import ABC, abstractmethod
from typing import Optional

from base.utils.logging.file_logger import FileLogger
from base.utils.logging.full_logger import FullLogger
from base.utils.mongo_access import MongoAccess


class Manager(ABC):

    def __init__(self, log_directory: Optional[str] = None,
                 mongo_config_file: Optional[str] = None,
                 log_file: Optional[str] = None,
                 log_level: Optional[str] = None):
        super().__init__()
        if log_directory:
            FileLogger.LOG_DIRECTORY = log_directory
        MongoAccess.config_file = mongo_config_file
        self.log = FullLogger(name=self.__class__.__name__, log_file=log_file, level=log_level)
        self.conf = None
        self.inv = None
        self.collection = None
        self._update_document = None

    @abstractmethod
    def configure(self) -> None:
        pass

    @abstractmethod
    def do_action(self) -> None:
        pass

    def run(self):
        self.configure()
        self.do_action()


class AsyncManager(Manager, ABC):

    def __init__(self, log_directory: Optional[str] = None,
                 mongo_config_file: Optional[str] = None,
                 log_level: Optional[str] = None,
                 log_file: Optional[str] = None):
        super().__init__(log_directory=log_directory,
                         mongo_config_file=mongo_config_file,
                         log_level=log_level,
                         log_file=log_file)
        self.task: Optional[asyncio.Future] = None

    @abstractmethod
    async def configure(self) -> None:
        pass

    @abstractmethod
    async def do_action(self) -> None:
        pass

    def stop(self):
        """
            When overriding this method,
            subclasses should call this one as the last action
        """
        if self.task:
            self.task.cancel()

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.configure())
        self.task = asyncio.ensure_future(self.do_action())
