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


class ProcessInventoryChildrenTree(GraphProcessor):
    PREREQUISITES = []
    GRAPH_NAME = "Inventory children tree"
    GRAPH_TYPE = GraphType.INVENTORY_TREE.value

    def run(self):
        super().run()
        data_list, graph_doc = self.get_data_list_and_graph_doc()

        for i in data_list:
            if not i.get('parent'):
                # meaning it is the root node
                i['parent'] = 'root'
            i.update({'children': [d for d in data_list if d['parent'] == i['id']]})

        graph_doc["graph"] = data_list[0]

        self.inv.set(collection="graphs", item=graph_doc, allow_new_docs=True)
