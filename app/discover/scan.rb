#!/usr/bin/env ruby

# Scan an object and insert/update in the inventory

# phase 1: start by scanning one environment, the one currently defined in the configuration

require_relative 'configuration'
require_relative 'inventory_mgr'
require_relative 'db_fetch_regions'
require_relative 'scan_environment'

debug = false

env_name = "WebEX-Mirantis@Cisco"
Configuration.instance.use_env(env_name)
inventory = InventoryMgr.instance
scanner = ScanEnvironment.instance
scanner.set_env(env_name)
scanner.scan({:type => "environment", :id => env_name}, "id")
