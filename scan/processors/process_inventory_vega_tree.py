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


class ProcessInventoryVegaTree(GraphProcessor):
    PREREQUISITES = []
    GRAPH_NAME = "Inventory vega tree"
    GRAPH_TYPE = GraphType.INVENTORY_VEGA.value

    def run(self):
        super().run()
        data_list, graph_doc = self.get_data_list_and_graph_doc()
        graph_doc["graph"] = {"tree": data_list}
        self.inv.set(collection="graphs", item=graph_doc, allow_new_docs=True)
