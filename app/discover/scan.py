#!/usr/bin/env python3

# Scan an object and insert/update in the inventory

# phase 2: either scan default environment, or scan specific object

import argparse
import cgi

import os
import sys
import time

from discover.configuration import Configuration
from discover.fetcher import Fetcher
from monitoring.setup.monitoring_setup_manager import MonitoringSetupManager
from utils.inventory_mgr import InventoryMgr
from utils.util import Util


class ScanPlan:

    def __init__(self, args):
        self.obj = None
        self.scanner_class = None
        if "REQUEST_METHOD" in os.environ:
            self._init_from_cgi()
        elif isinstance(args, dict):
            self._init_from_dict(args)
        else:
            self._init_from_args(args)

    def _init_from_dict(self, args: dict):
        self.cgi = False
        self.loglevel = args.get("loglevel", ScanController.DEFAULTS["loglevel"])
        self.inventory_only = args.get("inventory_only", ScanController.DEFAULTS["inventory_only"])
        self.links_only = args.get("links_only", ScanController.DEFAULTS["links_only"])
        self.cliques_only = args.get("cliques_only", ScanController.DEFAULTS["cliques_only"])
        self.clear = args.get("clear", ScanController.DEFAULTS["clear"])
        self.clear_all = args.get("clear_all", ScanController.DEFAULTS["clear_all"])
        self.object_type = args.get("type", ScanController.DEFAULTS["type"])
        self.env = args.get("env", ScanController.DEFAULTS["env"])
        self.object_id = args.get("id", ScanController.DEFAULTS["env"])
        self.parent_id = args.get("parent_id", ScanController.DEFAULTS["parent_id"])
        self.type_to_scan = args.get("parent_type", ScanController.DEFAULTS["parent_type"])
        self.id_field = args.get("id_field", ScanController.DEFAULTS["id_field"])
        self.scan_self = args.get("scan_self", ScanController.DEFAULTS["scan_self"])
        self.child_type = args.get("type", ScanController.DEFAULTS["type"])
        self.child_id = None

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
        self.loglevel = form.getvalue("loglevel", ScanController.DEFAULTS["loglevel"])
        self.inventory_only = form.getvalue("inventory_only", ScanController.DEFAULTS["inventory_only"])
        self.links_only = form.getvalue("links_only", ScanController.DEFAULTS["links_only"])
        self.cliques_only = form.getvalue("cliques_only", ScanController.DEFAULTS["cliques_only"])
        self.clear = form.getvalue("clear", ScanController.DEFAULTS["clear"])
        self.clear_all = form.getvalue("clear_all", ScanController.DEFAULTS["clear_all"])
        self.object_type = form.getvalue("type", ScanController.DEFAULTS["type"])
        self.env = form.getvalue("env", ScanController.DEFAULTS["env"])
        self.object_id = form.getvalue("id", ScanController.DEFAULTS["env"])
        self.parent_id = form.getvalue("parent_id", ScanController.DEFAULTS["parent_id"])
        self.type_to_scan = form.getvalue("parent_type", ScanController.DEFAULTS["parent_type"])
        self.id_field = form.getvalue("id_field", ScanController.DEFAULTS["id_field"])
        self.scan_self = form.getvalue("scan_self", ScanController.DEFAULTS["scan_self"])
        self.child_type = None
        self.child_id = None


class ScanController(Fetcher):

    DEFAULTS = {
        "env": "WebEX-Mirantis@Cisco",
        "cgi": False,
        "mongo_config": "",
        "type": "environment",
        "inventory": "inventory",
        "scan_self": False,
        "parent_id": "",
        "parent_type": "",
        "id_field": "id",
        "loglevel": "INFO",
        "inventory_only": False,
        "links_only": False,
        "cliques_only": False,
        "clear": False,
        "clear_all": False
    }

    def __init__(self):
        super().__init__()
        self.conf = None
        self.inv = None

    def get_args(self):
        # try to read scan plan from command line parameters
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--cgi", nargs="?", type=bool, default=self.DEFAULTS["cgi"],
                            help="read argument from CGI (true/false) \n" +
                            "(default: false)")
        parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                            default=self.DEFAULTS["mongo_config"],
                            help="name of config file " +
                            "with MongoDB server access details")
        parser.add_argument("-e", "--env", nargs="?", type=str,
                            default=self.DEFAULTS["env"],
                            help="name of environment to scan \n" +
                            "(default: " + self.DEFAULTS["env"] + ")")
        parser.add_argument("-t", "--type", nargs="?", type=str,
                            default=self.DEFAULTS["type"],
                            help="type of object to scan \n" +
                            "(default: environment)")
        parser.add_argument("-y", "--inventory", nargs="?", type=str,
                            default=self.DEFAULTS["inventory"],
                            help="name of inventory collection \n" +
                            "(default: 'inventory')")
        parser.add_argument("-s", "--scan_self", action="store_true",
                            help="scan changes to a specific object \n" +
                            "(default: False)")
        parser.add_argument("-i", "--id", nargs="?", type=str,
                            default=self.DEFAULTS["env"],
                            help="ID of object to scan (when scan_self=true)")
        parser.add_argument("-p", "--parent_id", nargs="?", type=str,
                            default=self.DEFAULTS["parent_id"],
                            help="ID of parent object (when scan_self=true)")
        parser.add_argument("-a", "--parent_type", nargs="?", type=str,
                            default=self.DEFAULTS["parent_type"],
                            help="type of parent object (when scan_self=true)")
        parser.add_argument("-f", "--id_field", nargs="?", type=str,
                            default=self.DEFAULTS["id_field"],
                            help="name of ID field (when scan_self=true) \n" +
                            "(default: 'id', use 'name' for projects)")
        parser.add_argument("-l", "--loglevel", nargs="?", type=str,
                            default=self.DEFAULTS["loglevel"],
                            help="logging level \n(default: 'INFO')")
        parser.add_argument("--inventory_only", action="store_true",
                            help="do only scan to inventory\n(default: False)")
        parser.add_argument("--links_only", action="store_true",
                            help="do only links creation \n(default: False)")
        parser.add_argument("--cliques_only", action="store_true",
                            help="do only cliques creation \n(default: False)")
        parser.add_argument("--clear", action="store_true",
                            help="clear all data related to " +
                            "the specified environment prior to scanning\n" +
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

    # Get arguments from cli or another source and convert them to dict to enforce uniformity.
    # Throws a TypeError if arguments can't be converted to dict.
    def _setup_args(self, args: dict):
        if args is None:
            args = vars(self.get_args())
        if not isinstance(args, dict):
            try:
                args = dict(args)
            except TypeError:
                try:
                    args = vars(args)
                except TypeError:
                    raise TypeError("Wrong scan arguments format")
        return dict(self.DEFAULTS, **args)

    def run(self, args: dict = None):
        args = self._setup_args(args)
        # After this setup we assume args dictionary has all keys defined in self.DEFAULTS

        try:
            self.conf = Configuration(args['mongo_config'])
            self.inv = InventoryMgr()
            self.inv.set_inventory_collection(args['inventory'])
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
        scanner = Util().get_instance_of_class(class_name)
        scanner.set_env(env_name)

        # decide what scanning operations to do
        inventory_only = scan_plan.inventory_only
        links_only = scan_plan.links_only
        cliques_only = scan_plan.cliques_only
        results = []
        run_all = False if inventory_only or links_only or cliques_only \
            else True

        # setup monitoring server
        self.inv.monitoring_setup_manager = MonitoringSetupManager(args['mongo_config'], env_name)
        self.inv.monitoring_setup_manager.server_setup()

        # do the actual scanning
        if inventory_only or run_all:
            results = scanner.run_scan(
                scan_plan.obj,
                scan_plan.id_field,
                scan_plan.child_id,
                scan_plan.child_type)
            if args['type'] == 'environment':
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
