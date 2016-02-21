#!/usr/bin/env python3

# Scan an object and insert/update in the inventory

# phase 1: start by scanning one environment, the one currently defined in the configuration

from configuration import Configuration
from inventory_mgr import InventoryMgr
from scan_environment import ScanEnvironment

env_name = "WebEX-Mirantis@Cisco"
conf = Configuration()
conf.use_env(env_name)

scanner = ScanEnvironment()
scanner.set_env(env_name)
scanner.scan({"type": "environment", "id": env_name}, "id")
