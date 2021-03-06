###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from base.utils.constants import GraphType
from scan.processors.graph_processor import GraphProcessor


class ProcessInventoryForceTree(GraphProcessor):
    PREREQUISITES = []
    GRAPH_NAME = "Inventory force tree"
    GRAPH_TYPE = GraphType.INVENTORY_FORCE.value

    def run(self):
        super().run()
        data_list, graph_doc = self.get_data_list_and_graph_doc()

        links = [self.find_tree_link(data_list, item) for item in data_list]

        graph_doc["graph"] = {
            "nodes": data_list,
            "links": links
        }
        self.inv.set(collection="graphs", item=graph_doc, allow_new_docs=True)

    @staticmethod
    def find_tree_link(data_list, item):
        if not item.get('parent'):
            # meaning it is the root node
            item['parent'] = item['id']
        return next(({"source": d['id'], "target": item['id']} for d in data_list if d['id'] == item['parent']), None)
