###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from base.utils.inventory_mgr import InventoryMgr
from base.utils.logging.console_logger import ConsoleLogger
from base.utils.mongo_access import MongoAccess
from base.utils.singleton import Singleton


class Configuration(metaclass=Singleton):
    def __init__(self, environments_collection="environments_config"):
        super().__init__()
        self.db_client = MongoAccess()
        self.db = MongoAccess.db
        self.inv = InventoryMgr()
        self.collection = self.inv.collections.get(environments_collection)
        self.env_name = None
        self.environment = None
        self.configuration = None
        self.log = ConsoleLogger()

    def use_env(self, env_name):
        self.log.debug("Configuration taken from environment: {}"
                       .format(env_name))
        self.env_name = env_name

        envs = self.collection.find({"name": env_name})
        if envs.count() == 0:
            raise ValueError("use_env: could not find matching environment")
        if envs.count() > 1:
            raise ValueError("use_env: found multiple matching environments")

        self.environment = envs[0]
        self.configuration = self.environment["configuration"]

    def get_env_config(self):
        return self.environment

    def get_configuration(self):
        return self.configuration

    def get_env_name(self):
        return self.env_name

    def get_env_type(self):
        return 'OpenStack' if 'environment_type' not in self.environment \
            else self.environment['environment_type']

    def update_env(self, values):
        self.collection.update_one({"name": self.env_name},
                                   {'$set': MongoAccess.encode_mongo_keys(values)})

    def get(self, component):
        try:
            matches = [c for c in self.configuration if c["name"] == component]
        except AttributeError:
            raise ValueError("Configuration: environment not set")
        if len(matches) == 0:
            raise IndexError("No matches for configuration component: " + component)
        if len(matches) > 1:
            raise IndexError("Found multiple matches for configuration component: " + component)
        return matches[0]

    def has_network_plugin(self, name):
        if 'mechanism_drivers' not in self.environment:
            self.log.error('Environment missing mechanism_drivers definition: ' +
                           self.environment['name'])
        mechanism_drivers = self.environment['mechanism_drivers']
        return name in mechanism_drivers
