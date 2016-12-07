# base class for scanners

import json
import queue
import traceback

from discover.configuration import Configuration
from discover.fetcher import Fetcher
from discover.find_links_for_instance_vnics import FindLinksForInstanceVnics
from discover.find_links_for_oteps import FindLinksForOteps
from discover.find_links_for_pnics import FindLinksForPnics
from discover.find_links_for_vconnectors import FindLinksForVconnectors
from discover.find_links_for_vedges import FindLinksForVedges
from discover.find_links_for_vservice_vnics import FindLinksForVserviceVnics
from discover.inventory_mgr import InventoryMgr
from discover.ssh_conn import SshConn
from discover.util import Util


class Scanner(Util, Fetcher):
    inventory = None
    config = None
    environment = None
    env = None
    root_patern = None
    scan_queue = queue.Queue()
    scan_queue_track = {}
    monitoring_setup_manager = None

    def __init__(self, types_to_fetch):
        """
        Scanner is the base class for scanners.
        :param types_to_fetch:  types_to_fetch is a list,
        which contains many dictionaries.
        Each dictionary has some key:value pairs like:
        {
            "type": "project",
            "fetcher": "ApiFetchProjects",
            "object_id_to_use_in_child": "name",
            "children_scanner": "ScanProject"
        }
        The key:value pairs indicate that which data should be scanned.
        """
        super(Scanner, self).__init__()
        self.types_to_fetch = types_to_fetch
        if not Scanner.inventory:
            Scanner.inventory = InventoryMgr()
        self.config = Configuration()

    def scan(self, obj, id_field="id",
             limit_to_child_id=None, limit_to_child_type=None):
        types_children = []
        if not limit_to_child_type:
            limit_to_child_type = []
        elif isinstance(limit_to_child_type, str):
            limit_to_child_type = [limit_to_child_type]
        try:
            for t in self.types_to_fetch:
                if limit_to_child_type and t["type"] not in limit_to_child_type:
                    continue
                children = self.scan_type(t, obj, id_field)
                if limit_to_child_id:
                    children = [c for c in children
                        if c[id_field] == limit_to_child_id]
                    if not children:
                        continue
                types_children.append({
                    "type": t["type"],
                    "children": children})
        except ValueError:
            return False
        if limit_to_child_id and len(types_children) > 0:
            t = types_children[0]
            children = t["children"]
            return children[0]
        return obj

    def check_type_env(self, type_to_fetch):
        # check if type is to be run in this environment
        if "environment_condition" not in type_to_fetch:
            return True
        env_cond = type_to_fetch["environment_condition"]
        conf = self.config.get_env_config()

        for attr, required_val in env_cond.items():
            if attr == "mechanism_drivers":
                continue
            if attr not in conf or conf[attr] != required_val:
                return False

        # check network plugins
        if "mechanism_drivers" in env_cond:
            if "mechanism_drivers" not in conf:
                return False
            if env_cond["mechanism_drivers"] not in conf["mechanism_drivers"]:
                return False

        return True

    def scan_type(self, type_to_fetch, parent, id_field):
        # check if type is to be run in this environment
        if not self.check_type_env(type_to_fetch):
            return []

        if not parent:
            id = None
        else:
            id = str(parent[id_field])
            if not id or not id.rstrip():
                raise ValueError("Object missing " + id_field + " attribute")

        # get Fetcher instance
        fetcher = type_to_fetch["fetcher"]
        if isinstance(fetcher, str):
            fetcher_class = type_to_fetch["fetcher"]
            fetcher = self.get_instance_of_class(fetcher_class)
        fetcher.set_env(self.get_env())

        # get children_scanner instance
        try:
            children_scanner_class = type_to_fetch["children_scanner"]
            children_scanner = \
                self.get_instance_of_class(children_scanner_class)
            children_scanner.set_env(self.get_env())
            children_scanner.set_monitoring_setup_manager(
                self.monitoring_setup_manager)
        except KeyError:
            children_scanner = None

        escaped_id = fetcher.escape(str(id)) if id else id
        self.log.info(
            "scanning : type=%s, parent: (type=%s, name=%s, id=%s)",
            type_to_fetch["type"],
            "environment" if "type" not in parent else parent["type"],
            "" if "name" not in parent else parent["name"],
            escaped_id)

        # fetch data from environment by CLI, API or MySQL
        # It depends on the Fetcher's config.
        try:
            db_results = fetcher.get(escaped_id)
        except Exception as e:
            self.log.error(
                "Error while scanning : " +
                "fetcher=%s, " +
                "type=%s, " +
                "type=%s, " +
                "parent: (type=%s, name=%s, id=%s), error: %s",
                fetcher.__class__.__name__,
                type_to_fetch["type"],
                "environment" if "type" not in parent else parent["type"],
                "" if "name" not in parent else parent["name"],
                escaped_id,
                e)
            traceback.print_exc()
            return []

        # format results
        if isinstance(db_results, dict):
            results = db_results["rows"] if db_results["rows"] else [db_results]
        elif isinstance(db_results, str):
            results = json.loads(db_results)
        else:
            results = db_results

        # get child_id_field
        try:
            child_id_field = type_to_fetch["object_id_to_use_in_child"]
        except KeyError:
            child_id_field = "id"

        environment = self.get_env()
        children = []

        for o in results:
            o["id"] = str(o["id"])
            o["environment"] = environment
            o["type"] = type_to_fetch["type"] if type_to_fetch["type"] \
                else o["type"]
            try:
                o["show_in_tree"] = type_to_fetch["show_in_tree"]
            except KeyError:
                o["show_in_tree"] = True

            try:
                parent_id_path = parent["id_path"]
                parent_name_path = parent["name_path"]
            except KeyError:
                parent_id_path = "/" + environment
                parent_name_path = "/" + environment

            try:
                # case of dynamic folder added by need
                master_parent_type = o["master_parent_type"]
                master_parent_id = o["master_parent_id"]
                master_parent = self.inventory.get_by_id(
                    self.get_env(),
                    master_parent_id)
                if not master_parent:
                    self.log.error(
                        "failed to find master parent " +
                        master_parent_id)
                    continue
                folder = {
                    "environment": parent["environment"],
                    "parent_id": master_parent_id,
                    "parent_type": master_parent_type,
                    "id": o["parent_id"],
                    "id_path": master_parent["id_path"] + "/" +
                        o["parent_id"],
                    "show_in_tree": True,
                    "name_path": master_parent["name_path"] +
                        o["parent_text"],
                    "name": o["parent_id"],
                    "type": o["parent_type"],
                    "text": o["parent_text"]
                }
                # remove master_parent_type & master_parent_id after use,
                # as they're there just ro help create the dynamic folder
                o.pop("master_parent_type", True)
                o.pop("master_parent_id", True)
                Scanner.inventory.set(folder)
            except KeyError:
                pass

            if "text" in o and o["text"]:
                name = o["text"]
            elif "name" in o and o["name"]:
                name = o["name"]
            else:
                name = o["id"]
            o["name"] = name

            if "parent_id" not in o and parent:
                parent_id = parent["id"]
                o["parent_id"] = parent_id
                o["parent_type"] = parent["type"]
            elif "parent_id" in o and o["parent_id"] != parent["id"]:
                # using alternate parent - fetch parent path from inventory
                parent_obj = Scanner.inventory.get_by_id(environment,
                    o["parent_id"])
                if parent_obj:
                    parent_id_path = parent_obj["id_path"]
                    parent_name_path = parent_obj["name_path"]
            o["id_path"] = parent_id_path + "/" + o["id"].strip()
            o["name_path"] = parent_name_path + "/" + name

            # keep list of projects that an object is in
            associated_projects = []
            keys_to_remove = []
            for k in o:
                if k.startswith("in_project-"):
                    proj_name = k[k.index('-') + 1:]
                    associated_projects.append(proj_name)
                    keys_to_remove.append(k)
            for k in keys_to_remove:
                o.pop(k)
            if len(associated_projects) > 0:
                projects = o["projects"] if "projects" in o.keys() else []
                projects.extend(associated_projects)
                if projects:
                    o["projects"] = projects

            if "create_object" not in o or o["create_object"]:
                # add/update object in DB
                Scanner.inventory.set(o)
                # create the corresponding monitoring setup
                self.monitoring_setup_manager.create_setup(o)

            # add objects into children list.
            children.append(o)

            # put children scanner into queue
            if children_scanner:
                self.queue_for_scan(o, child_id_field, children_scanner)
        return children

    # scanning queued items, rather than going depth-first (DFS)
    # this is done to allow collecting all required data for objects
    # before continuing to next level
    # for example, get host ID from API os-hypervisors call, so later
    # we can use this ID in the "os-hypervisors/<ID>/servers" call
    def queue_for_scan(self, o, child_id_field, children_scanner):
        if o["id"] in Scanner.scan_queue_track:
            return
        Scanner.scan_queue_track[o["type"] + ";" + o["id"]] = 1
        Scanner.scan_queue.put({"object": o,
            "child_id_field": child_id_field, "scanner": children_scanner})

    def run_scan(self, obj, id_field, child_id, child_type):
        results = self.scan(obj, id_field, child_id, child_type)

        # run children scanner from queue.
        self.scan_from_queue()
        SshConn.disconnect_all()
        return results

    def scan_from_queue(self):
        while not Scanner.scan_queue.empty():
            item = Scanner.scan_queue.get()
            scanner = item["scanner"]
            if isinstance(scanner, str):
                # got name of scanner class - create an instance of it
                scanner = self.get_instance_of_class(scanner)

            # run scan recursively
            scanner.scan(item["object"], item["child_id_field"])
        self.log.info("Scan complete")

    def scan_links(self):
        self.log.info("scanning for links")
        fetchers_implementing_add_links = [
            FindLinksForPnics(),
            FindLinksForInstanceVnics(),
            FindLinksForVserviceVnics(),
            FindLinksForVconnectors(),
            FindLinksForVedges(),
            FindLinksForOteps()
        ]
        for fetcher in fetchers_implementing_add_links:
            fetcher.add_links()

    def scan_cliques(self):
        Scanner.inventory.scan_cliques(self.get_env())

    def set_monitoring_setup_manager(self, monitoring_setup_manager):
        self.monitoring_setup_manager = monitoring_setup_manager
