#!/usr/bin/env python3

# Scan an object and insert/update in the inventory

# phase 2: either scan default environment, or scan specific object

import argparse
import cgi

import os
import time

from discover.configuration import Configuration
from discover.fetcher import Fetcher
from monitoring.setup.monitoring_setup_manager import MonitoringSetupManager
from utils.exceptions import ScanArgumentsError
from utils.inventory_mgr import InventoryMgr
from utils.util import Util


class ScanPlan:
    """
    @DynamicAttrs
    """

    COMMON_ATTRIBUTES = (("loglevel",),
                         ("inventory_only",),
                         ("links_only",),
                         ("cliques_only",),
                         ("clear",),
                         ("clear_all",),
                         ("object_type", "type", "type"),
                         ("env",),
                         ("object_id", "id", "env"),
                         ("parent_id",),
                         ("type_to_scan", "parent_type", "parent_type"),
                         ("id_field",),
                         ("scan_self",),
                         ("child_type", "type", "type"))

    def __init__(self, args=None):
        self.obj = None
        self.scanner_class = None
        self.args = args
        for attribute in self.COMMON_ATTRIBUTES:
            setattr(self, attribute[0], None)

        if "REQUEST_METHOD" in os.environ:
            self._init_from_cgi()
        elif isinstance(args, dict):
            self._init_from_dict()
        else:
            self._init_from_args()
        self._validate_args()

    def _validate_args(self):
        errors = []
        if (self.inventory_only and self.links_only) \
                or (self.inventory_only and self.cliques_only) \
                or (self.links_only and self.cliques_only):
            errors.append("Only one of the *_only flags can be True.")

        if errors:
            raise ScanArgumentsError("\n".join(errors))

    def _set_arg_from_dict(self, attribute_name, arg_name=None,
                           default_key=None):
        default_key = default_key if default_key else attribute_name
        setattr(self,
                attribute_name,
                self.args.get(arg_name if arg_name else attribute_name,
                              ScanController.DEFAULTS[default_key]))

    def _set_arg_from_cmd(self, attribute_name, arg_name=None):
        setattr(self,
                attribute_name,
                getattr(self.args, arg_name if arg_name else attribute_name))

    def _set_arg_from_form(self, attribute_name, arg_name=None,
                           default_key=None):
        default_key = default_key if default_key else attribute_name
        setattr(self,
                attribute_name,
                self.args.getvalue(arg_name if arg_name else attribute_name,
                                   ScanController.DEFAULTS[default_key]))

    def _init_from_dict(self):
        self.cgi = False
        for arg in self.COMMON_ATTRIBUTES:
            self._set_arg_from_dict(*arg)
        self.child_id = None

    def _init_from_args(self):
        self.cgi = False
        for arg in self.COMMON_ATTRIBUTES:
            self._set_arg_from_cmd(*arg[:2])
        self.child_id = None

    def _init_from_cgi(self):
        self.args = cgi.FieldStorage()
        self.cgi = True
        for arg in self.COMMON_ATTRIBUTES:
            self._set_arg_from_form(*arg)
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
        parser.add_argument("-c", "--cgi", nargs="?", type=bool,
                            default=self.DEFAULTS["cgi"],
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
        parser.add_argument("--clear", action="store_true",
                            help="clear all data related to the specified " +
                                 "environment prior to scanning\n" +
                                 "(default: False)")
        parser.add_argument("--clear_all", action="store_true",
                            help="clear all data prior to scanning\n" +
                                 "(default: False)")

        # At most one of these arguments may be present
        scan_only_group = parser.add_mutually_exclusive_group()
        scan_only_group.add_argument("--inventory_only", action="store_true",
                                     help="do only scan to inventory\n" +
                                          "(default: False)")
        scan_only_group.add_argument("--links_only", action="store_true",
                                     help="do only links creation \n" +
                                          "(default: False)")
        scan_only_group.add_argument("--cliques_only", action="store_true",
                                     help="do only cliques creation \n" +
                                          "(default: False)")

        return parser.parse_args()

    def get_scan_plan(self, args):
        # noinspection PyTypeChecker
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

    def run(self, args: dict = None):
        args = Util.setup_args(args, self.DEFAULTS, self.get_args)
        # After this setup we assume args dictionary has
        # all keys defined in self.DEFAULTS

        try:
            self.conf = Configuration(args['mongo_config'])
            self.inv = InventoryMgr()
            self.inv.set_collections(args['inventory'])
        except FileNotFoundError:
            return False, 'Mongo configuration file not found'

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
        self.inv.monitoring_setup_manager = \
            MonitoringSetupManager(args['mongo_config'], env_name)
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
        return True, 'ok'


if __name__ == '__main__':
    scan_manager = ScanController()
    scan_manager.run()
