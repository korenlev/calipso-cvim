###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from datetime import datetime

from base.utils.constants import GraphType
from scan.processors.processor import Processor


class ProcessInventoryTree(Processor):
    PREREQUISITES = []
    COLLECTION = "graphs"
    GRAPH_NAME = "Inventory graph"

    def run(self):
        super().run()

        data_list = [{
            'id': self.env,
            'name': self.env,
        }]

        data_list.extend([{
            'id': doc['id'],
            'id_path': doc['id_path'],
            'name': doc['name'],
            'parent': doc['parent_id'],
            'type': doc['type'],
            'host': doc.get('host')
        } for doc in self.inv.find_items({"environment": self.env})])

        graph_doc = self.inv.find_one({"environment": self.env, "type": GraphType.INVENTORY.value}, collection=self.COLLECTION)
        if not graph_doc:
            graph_doc = {
                "name": self.GRAPH_NAME,
                "type": GraphType.INVENTORY.value,
                "environment": self.env
            }

        links = [self.find_tree_links(data_list, item) for item in data_list]

        graph_doc.update({
            "graph": {
                "nodes": data_list,
                "links": links
            },
            "last_scanned": datetime.now()
        })

        self.inv.set(collection="graphs", item=graph_doc, allow_new_docs=True)

    @staticmethod
    def find_tree_links(data_list, item):
        if not item.get('parent'):
            # meaning it is the root node
            item.update({'parent': item['id']})
        tree_links = [{"source": d['id'], "target": item['id']} for d in data_list if d['id'] == item['parent']][0]
        return tree_links
