###############################################################################
# Copyright (c) 2017-2019 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from typing import Optional

import bson
import pymongo
from bson.objectid import ObjectId
from datetime import datetime

from base.fetcher import Fetcher
from base.utils.constants import GraphType
from base.utils.inventory_mgr import InventoryMgr
from base.utils.origins import Origin


class CliqueFinder(Fetcher):
    DEFAULT_GRAPH_NODES_ATTRIBUTES = ["_id", "id", "type", "name", "host"]
    DEFAULT_GRAPH_LINKS_ATTRIBUTES = ["_id", "id", "link_type", "source", "target", "host"]

    reversed_link_types = {}

    def __init__(self):
        super().__init__()
        self.env_config: Optional[dict] = None
        self.inv: Optional[InventoryMgr] = None
        self.inventory: Optional[pymongo.collection.Collection] = None
        self.links: Optional[pymongo.collection.Collection] = None
        self.clique_types: Optional[pymongo.collection.Collection] = None
        self.clique_types_by_type: dict = {}
        self.clique_constraints_by_type: dict = {}
        self.clique_constraints: Optional[pymongo.collection.Collection] = None
        self.cliques: Optional[pymongo.collection.Collection] = None
        self.graphs: Optional[pymongo.collection.Collection] = None

    def setup(self, env: str, origin: Origin = None) -> None:
        super().setup(env, origin)
        self.inv = InventoryMgr()
        self.inventory = self.inv.inventory_collection
        self.links = self.inv.collections["links"]
        self.clique_types = self.inv.collections["clique_types"]
        self.clique_types_by_type = {}
        self.clique_constraints_by_type = {}
        self.clique_constraints = self.inv.collections["clique_constraints"]
        self.cliques = self.inv.collections["cliques"]
        self.graphs = self.inv.collections["graphs"]

    def set_env(self, env: str) -> None:
        super().set_env(env)
        self.env_config = self.configuration.environment

    def find_cliques_by_link(self, links_list: list) -> pymongo.cursor.Cursor:
        return self.links.find({'links': {'$in': links_list}})

    def find_links_by_source(self, db_id: bson.ObjectId) -> pymongo.cursor.Cursor:
        return self.links.find({'source': db_id})

    def find_links_by_target(self, db_id: bson.ObjectId) -> pymongo.cursor.Cursor:
        return self.links.find({'target': db_id})

    def find_cliques(self) -> None:
        """
            Entry point for external users.
            Finds and saves all cliques for active environment
        """
        self.log.info("Scanning for cliques")
        clique_types = self.get_clique_types().values()
        for focal_point_clique_types in clique_types:
            for clique_type in focal_point_clique_types:
                self.find_cliques_for_type(clique_type)
        self.log.info("Finished scanning for cliques")

    def get_priority_score(self, clique_type: dict) -> int:
        """
            Calculate priority score for clique type per environment and configuration
        """

        # environment-specific clique type takes precedence
        env = clique_type.get('environment')
        config = self.env_config
        # ECT - Clique Type with Environment name
        if env:
            if self.env == env:
                return 2**6
            if env == 'ANY':
                # environment=ANY serves as fallback option
                return 2**0
            return 0
        # NECT - Clique Type without Environment name
        else:
            env_type = clique_type.get('environment_type')
            if env_type and env_type != config.get('environment_type'):
                return 0

            score = 0

            distribution = clique_type.get('distribution')
            if distribution:
                if config['distribution'] != distribution:
                    return 0

                score += 2**5

                dv = clique_type.get('distribution_version')
                if dv:
                    if dv != config['distribution_version']:
                        return 0
                    score += 2**4

            mechanism_drivers = clique_type.get('mechanism_drivers')
            if mechanism_drivers:
                if not isinstance(mechanism_drivers, list):
                    mechanism_drivers = [mechanism_drivers]
                if all(m not in config['mechanism_drivers'] for m in mechanism_drivers):
                    return 0
                score += 2**3

            type_drivers = clique_type.get('type_drivers')
            if type_drivers:
                if type_drivers != config['type_drivers']:
                    return 0
                score += 2**2

            # If no configuration is specified, this clique type
            # is a fallback for its environment type
            return max(score, 2**1)

    def _find_matching_clique_types(self, candidates: list) -> list:
        """
            Get clique type with max priority for given focal point type
        """

        if not candidates:
            return []

        scored_clique_types = [
            {'score': self.get_priority_score(candidate), 'clique_type': candidate}
            for candidate in candidates
        ]
        max_score = max(scored_clique_types, key=lambda t: t['score'])
        if max_score['score'] == 0:
            self.log.warn('No matching clique types '
                          'for focal point type: {fp_type}'
                          .format(fp_type=candidates[0].get('focal_point_type')))
            return []

        return [sct['clique_type'] for sct in scored_clique_types if sct['score'] == max_score['score']]

    def get_clique_types(self) -> dict:
        """
            Finds and returns best matching clique types for each object type
        """
        if not self.clique_types_by_type:
            # Group all clique types by focal point type
            clique_types_candidates = {}
            for clique_type in self.clique_types.find({}):
                fp_type = clique_type.get('focal_point_type', '')
                if not clique_types_candidates.get(fp_type):
                    clique_types_candidates[fp_type] = []
                clique_types_candidates[fp_type].append(clique_type)

            # Select best matching clique types for each object type
            for object_type, candidates in clique_types_candidates.items():
                selected = self._find_matching_clique_types(candidates)
                if not selected:
                    continue
                self.clique_types_by_type[object_type] = selected
        return self.clique_types_by_type

    def _fetch_constraints_for_type(self, focal_point_type: str) -> list:
        if not self.clique_constraints_by_type:
            docs = self.inv.find_items({}, collection='clique_constraints')
            for doc in docs:
                fp_type = doc['focal_point_type']
                if fp_type not in self.clique_constraints_by_type:
                    self.clique_constraints_by_type[fp_type] = []
                self.clique_constraints_by_type[fp_type].append(doc)
        return self.clique_constraints_by_type.get(focal_point_type, [])

    def get_clique_constraints(self, focal_point_type: str) -> list:
        constraints_for_type = self._fetch_constraints_for_type(focal_point_type)
        constraints = {}
        for constraint_def in constraints_for_type:
            constraint_env = constraint_def.get('environment')
            if constraint_env == self.env:
                return constraint_def['constraints']

            # TODO: we always choose last if no env matches?
            if not constraint_env:
                constraints = constraint_def

        return constraints.get('constraints', [])

    def find_cliques_for_type(self, clique_type):
        """
            Find and save all cliques for the given focal point type
        """

        focal_point_type = clique_type["focal_point_type"]
        self.log.info("Scanning cliques for focal_point_type '{}', clique_type name: '{}'"
                      .format(focal_point_type, clique_type.get('name')))

        constraints = self.get_clique_constraints(focal_point_type)
        object_type = clique_type["focal_point_type"]
        objects_for_focal_point_type = self.inventory.find({
            "environment": self.get_env(),
            "type": object_type
        })

        for focal_point in objects_for_focal_point_type:
            self.construct_clique_for_focal_point(focal_point=focal_point,
                                                  clique_type=clique_type,
                                                  constraints=constraints)

    def rebuild_clique(self, clique: dict) -> None:
        """
            Rebuild the clique after a change in data
        """
        focal_point = self.inventory.find_one({'_id': clique['focal_point']})
        constraint = self.clique_constraints.find_one({"focal_point_type": focal_point['type']})
        constraints = constraint["constraints"] if constraint else []

        clique_types = self.get_clique_types()
        clique_type = clique_types.get(focal_point['type'])
        if not clique_type:
            self.cliques.delete({'_id': clique['_id']})
        else:
            new_clique = self.construct_clique_for_focal_point(focal_point=focal_point,
                                                               clique_type=clique_type,
                                                               constraints=constraints)
            if not new_clique:
                self.cliques.delete({'_id': clique['_id']})

    def construct_clique_for_focal_point(self, focal_point: dict,
                                         clique_type: dict, constraints: list) -> Optional[dict]:
        """
            Fully build and save the clique for a give focal point object.
            Returns the resulting document
        """

        # Keep a hash of nodes in clique that were visited.
        # For each type start from the focal point
        visited_nodes = {
            focal_point["type"]: {
                str(focal_point["_id"])
            }
        }

        clique = {
            "environment": self.env,
            "clique_type": clique_type["_id"],
            "focal_point": focal_point["_id"],
            "focal_point_object_id": focal_point["id"],
            "focal_point_type": focal_point["type"],
            "nodes": [],
            "links": [],
            "links_detailed": [],
            "constraints": {c: focal_point.get(c) for c in constraints},
            "last_scanned": datetime.now()
        }
        graph = {
            "environment": self.env,
            "name": "Graph for '{}' object: {}".format(focal_point["type"], focal_point["id"]),
            "type": GraphType.CLIQUE.value,
            "graph": {}
        }

        focal_point_obj = self.inv.find_one({"_id": clique["focal_point"]})
        # Discard cliques with invalid focal point
        if not focal_point_obj:
            self.log.warning(
                "Didn't find {} with _id {} for clique discovery".format(focal_point["type"], focal_point["id"])
            )
            return None

        allow_implicit = clique_type.get('use_implicit_links', False)
        for link_type in clique_type["link_types"]:
            if not self.add_links_by_type(clique=clique, link_type=link_type,
                                          visited_nodes=visited_nodes, allow_implicit=allow_implicit):
                self.log.debug('No matches for link type {}'.format(link_type))

        # Discard empty cliques
        if not clique["links"]:
            return None

        # After adding the links to the clique, create/update the clique
        for visited_node in visited_nodes.values():
            clique["nodes"].extend([ObjectId(node) for node in visited_node])

        focal_point_obj["clique"] = True
        focal_point_obj.pop("_id", None)
        self.cliques.update_one({
                "environment": self.env,
                "focal_point": clique["focal_point"]
            }, {
                '$set': clique
            },
            upsert=True
        )
        clique_document = self.inventory.update_one({
                "_id": clique["focal_point"]
            }, {
                '$set': focal_point_obj
            },
            upsert=True
        )

        # TODO: field names?
        graph_attributes = clique_type.get("graph_attributes", {})
        graph["graph"]["nodes"] = self.inv.find_items(
            search={"_id": {"$in": clique["nodes"]}},
            projection=graph_attributes.get("nodes", self.DEFAULT_GRAPH_NODES_ATTRIBUTES)
        )
        graph["graph"]["links"] = [
            {k: link.get(k) for k in graph_attributes.get("links", self.DEFAULT_GRAPH_LINKS_ATTRIBUTES)}
            for link in clique["links_detailed"]
        ]

        self.graphs.update_one({
                "environment": graph["environment"],
                "name": graph["name"],
            }, {
                "$set": graph
            },
            upsert=True
        )

        return clique_document

    @staticmethod
    def check_constraints(clique: dict, link: dict) -> bool:
        """
            Check whether the link passes all constraints in clique definition
        """

        if "attributes" not in link:
            return True

        attributes = link["attributes"]
        constraints = clique["constraints"]
        for c in constraints:
            if c not in attributes:
                continue  # constraint not applicable to this link

            constr_values = [constraints[c]] if not isinstance(constraints[c], list) else constraints[c]
            link_value = attributes[c]
            if link_value not in constr_values:
                return False

        return True

    @staticmethod
    def get_reversed_link_type(link_type: str) -> str:
        if link_type not in CliqueFinder.reversed_link_types:
            CliqueFinder.reversed_link_types[link_type] = '-'.join(link_type.split('-')[::-1])
        return CliqueFinder.reversed_link_types[link_type]

    def add_links_by_type(self, clique: dict, link_type: str, visited_nodes: dict,
                          allow_implicit: bool = False) -> bool:
        """
            Finds and adds links by type, then finds and adds target nodes.
            Returns the fact whether any nodes were added using this process
        """

        # Check if it's backwards
        reversed_link_type = self.get_reversed_link_type(link_type)
        # Handle case of links like T<->T
        self_linked = link_type == reversed_link_type

        use_reversed = False
        if not self_linked:
            link_search_condition = {
                "environment": self.env,
                "link_type": reversed_link_type
            }
            if not allow_implicit:
                link_search_condition['implicit'] = False
            matches = self.links.find_one(link_search_condition)
            use_reversed = True if matches else False

        nodes_found = False
        if self_linked or not use_reversed:
            nodes_found = self.add_nodes_by_link_type(clique=clique, link_type=link_type,
                                                      visited_nodes=visited_nodes,
                                                      allow_implicit=allow_implicit,
                                                      is_reversed=False)
        if (self_linked and not nodes_found) or use_reversed:
            nodes_found = self.add_nodes_by_link_type(clique=clique, link_type=link_type,
                                                      visited_nodes=visited_nodes,
                                                      allow_implicit=allow_implicit,
                                                      is_reversed=True)
        return nodes_found

    def add_nodes_by_link_type(self, clique: dict, link_type: str, visited_nodes: dict,
                               is_reversed: bool = False, allow_implicit: bool = False) -> bool:
        """
            Add matching nodes to clique based on link type.
            Returns the fact whether at least one new node was added
        """

        if is_reversed:
            link_type = self.get_reversed_link_type(link_type)

        # Assuming object types can't contain dashes ("-")
        from_type, to_type = link_type.split("-")
        side_to_match, other_side = ('target', 'source') if is_reversed else ('source', 'target')
        match_type, other_side_type = (to_type, from_type) if is_reversed else (from_type, to_type)
        if match_type not in visited_nodes.keys():
            return False

        new_nodes = set()
        for node in visited_nodes[match_type]:
            new_nodes_by_type = self.add_links_for_node(node=node, clique=clique, link_type=link_type,
                                                        side_to_match=side_to_match, other_side=other_side,
                                                        allow_implicit=allow_implicit)
            new_nodes |= new_nodes_by_type

        if other_side_type not in visited_nodes:
            visited_nodes[other_side_type] = set()
        visited_nodes[other_side_type] |= new_nodes

        return len(new_nodes) > 0

    def add_links_for_node(self, node: str, clique: dict,
                           link_type: str, side_to_match: str, other_side: str,
                           allow_implicit: bool = False) -> set:
        """
            Finds and adds matching links for given node.
            Returns a list of new nodes to apply the process for.
        """

        link_search_condition = {
            "environment": self.env,
            "link_type": link_type,
            side_to_match: ObjectId(node),
        }
        if not allow_implicit:
            link_search_condition['implicit'] = False

        matches = self.links.find(link_search_condition)

        nodes_to_add = set()
        for link in matches:
            link_id = link["_id"]
            if link_id in clique["links"] or not self.check_constraints(clique=clique, link=link):
                continue

            clique["links"].append(link_id)
            clique["links_detailed"].append(link)
            target_node = str(link[other_side])
            nodes_to_add.add(target_node)
        return nodes_to_add
