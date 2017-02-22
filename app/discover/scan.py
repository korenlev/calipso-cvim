#!/usr/bin/env python3

# Scan an object and insert/update in the inventory

# phase 2: either scan default environment, or scan specific object

import argparse
import cgi
import importlib

import os
import sys
import time

from discover.configuration import Configuration
from discover.fetcher import Fetcher
from monitoring.setup.monitoring_setup_manager import MonitoringSetupManager
from utils.inventory_mgr import InventoryMgr
from utils.util import Util


class ScanPlan:

    def __init__(self, cmd_args):
        self.obj = None
        self.scanner_class = None
        if "REQUEST_METHOD" in os.environ:
            self._init_from_cgi()
        else:
            self._init_from_args(cmd_args)

    def _init_from_args(self, cmd_args):
        self.cgi = False
        self.loglevel = cmd_args.loglevel
        self.inventory_only = cmd_args.inventory_only
        self.links_only = cmd_args.links_only
        self.cliques_only = cmd_args.cliques_only
        self.clear = cmd_args.clear
        self.clear_all = cmd_args.clear_all
        self.object_type = cmd_args.type
        self.env = cmd_args.env
        self.object_id = cmd_args.id
        self.parent_id = cmd_args.parent_id
        self.type_to_scan = cmd_args.parent_type
        self.id_field = cmd_args.id_field
        self.scan_self = cmd_args.scan_self
        self.child_type = cmd_args.type
        self.child_id = None

    def _init_from_cgi(self):
        form = cgi.FieldStorage()
        self.cgi = True,
        self.loglevel = form.getvalue("loglevel", "INFO"),
        self.inventory_only = form.getvalue("inventory_only", ""),
        self.links_only = form.getvalue("links_only", ""),
        self.cliques_only = form.getvalue("cliques_only", ""),
        self.clear = form.getvalue("clear", ""),
        self.clear_all = form.getvalue("clear_all", ""),
        self.object_type = form.getvalue("type", "environment"),
        self.env = form.getvalue("env", ScanController.default_env),
        self.object_id = form.getvalue("id", ScanController.default_env),
        self.parent_id = form.getvalue("parent_id", ""),
        self.type_to_scan = form.getvalue("parent_type", ""),
        self.id_field = form.getvalue("id_field", "id"),
        self.scan_self = form.getvalue("scan_self", "")
        self.child_type = None
        self.child_id = None


class ScanController(Fetcher):
    default_env = "WebEX-Mirantis@Cisco"

    def __init__(self):
        super().__init__()
        self.conf = None
        self.inv = None

    def get_args(self):
        # try to read scan plan from command line parameters
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--cgi", nargs="?", type=bool, default=False,
                            help="read argument from CGI (true/false) \n" +
                            "(default: false)")
        parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                            default="",
                            help="name of config file " +
                            "with MongoDB servr access details")
        parser.add_argument("-e", "--env", nargs="?", type=str,
                            default=self.default_env,
                            help="name of environment to scan \n" +
                            "(default: " + self.default_env + ")")
        parser.add_argument("-t", "--type", nargs="?", type=str,
                            default="environment",
                            help="type of object to scan \n" +
                            "(default: environment)")
        parser.add_argument("-y", "--inventory", nargs="?", type=str,
                            default="inventory",
                            help="name of inventory collection \n" +
                            "(default: 'inventory')")
        parser.add_argument("-s", "--scan_self", action="store_true",
                            help="scan changes to a specific object \n" +
                            "(default: False)")
        parser.add_argument("-i", "--id", nargs="?", type=str,
                            default=ScanController.default_env,
                            help="ID of object to scan (when scan_self=true)")
        parser.add_argument("-p", "--parent_id", nargs="?", type=str,
                            default="",
                            help="ID of parent object (when scan_self=true)")
        parser.add_argument("-a", "--parent_type", nargs="?", type=str,
                            default="",
                            help="type of parent object (when scan_self=true)")
        parser.add_argument("-f", "--id_field", nargs="?", type=str,
                            default="id",
                            help="name of ID field (when scan_self=true) \n" +
                            "(default: 'id', use 'name' for projects)")
        parser.add_argument("-l", "--loglevel", nargs="?", type=str,
                            default="INFO",
                            help="logging level \n(default: 'INFO')")
        parser.add_argument("--inventory_only", action="store_true",
                            help="do only scan to inventory\n(default: False)")
        parser.add_argument("--links_only", action="store_true",
                            help="do only links creation \n(default: False)")
        parser.add_argument("--cliques_only", action="store_true",
                            help="do only cliques creation \n(default: False)")
        parser.add_argument("--clear", action="store_true",
                            help="clear all data related to " +
                            "the specified environemtn prior to scanning\n" +
                            "(default: False)")
        parser.add_argument("--clear_all", action="store_true",
                            help="clear all data prior to scanning\n" +
                            "(default: False)")
        args = parser.parse_args()
        return args

    def get_scan_plan(self, args):
        return self.prepare_scan_plan(ScanPlan(args))

    def prepare_scan_plan(self, plan):
        module = plan.object_type
        if not plan.scan_self:
            plan.scan_self = plan.object_type != "environment"

        plan.object_type = plan.object_type.title().replace("_", "")

        if not plan.scan_self:
            plan.child_type = None
        else:
            plan.child_id = plan.object_id
            plan.object_id = plan.parent_id
            if plan.type_to_scan.endswith("_folder"):
                module = plan.child_type + "s_root"
            else:
                module = plan.type_to_scan
            plan.object_type = module.title().replace("_", "")
            plan.object_id = plan.parent_id

        if module == "environment":
            plan.obj = {"id": plan.env}
        else:
            # fetch object from inventory
            obj = self.inv.get_by_id(plan.env, plan.object_id)
            if not obj:
                raise ValueError("No match for object ID: " + plan.object_id)
            plan.obj = obj

        plan.scanner_class = "Scan" + plan.object_type
        return plan

    def run(self):
        # get arguments and parsing arguments.
        args = self.get_args()
        try:
            self.conf = Configuration(args.mongo_config)
            self.inv = InventoryMgr()
            self.inv.set_inventory_collection(args.inventory)
        except FileNotFoundError:
            sys.exit(1)

        scan_plan = self.get_scan_plan(args)
        if scan_plan.clear or scan_plan.clear_all:
            self.inv.clear(scan_plan)
        self.conf.set_loglevel(scan_plan.loglevel)

        env_name = scan_plan.env
        self.conf.use_env(env_name)

        # generate ScanObject Class and instance.
        class_name = scan_plan.scanner_class
        scanner = Util.get_instance_of_class(class_name)
        scanner.set_env(env_name)

        # decide what scanning operations to do
        inventory_only = scan_plan.inventory_only
        links_only = scan_plan.links_only
        cliques_only = scan_plan.cliques_only
        results = []
        run_all = False if inventory_only or links_only or cliques_only \
            else True

        # setup monitoring server
        self.inv.monitoring_setup_manager = MonitoringSetupManager(args.mongo_config, env_name)
        self.inv.monitoring_setup_manager.server_setup()

        # do the actual scanning
        if inventory_only or run_all:
            results = scanner.run_scan(
                scan_plan.obj,
                scan_plan.id_field,
                scan_plan.child_id,
                scan_plan.child_type)
            if args.type == 'environment':
                now = time.gmtime()
                time_str = time.strftime("%Y-%m-%dT%H:%M:%SZ", now)
                self.conf.update_env({'last_scanned': time_str})
        if links_only or run_all:
            scanner.scan_links()
        if cliques_only or run_all:
            scanner.scan_cliques()
        scanner.deploy_monitoring_setup()
        if scan_plan.cgi:
            response = {"success": not isinstance(results, bool),
                        "results": [] if isinstance(results, bool) else results}

            print("Content-type: application/json\n\n")
            print(response)
            print("\n")


if __name__ == '__main__':
    scan_manager = ScanController()
    scan_manager.run()
