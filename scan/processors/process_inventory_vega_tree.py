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


class ProcessInventoryVegaTree(Processor):
    PREREQUISITES = []
    COLLECTION = "graphs"
    GRAPH_NAME = "Inventory vega tree"

    def run(self):
        super().run()

        data_list = [{
            'id': self.env,
            'name': self.env,
        }]

        for doc in self.inv.find_items({"environment": self.env}):
            d = {}
            if 'folder' in doc['type']:
                d = {'name': doc.get('text', doc['name'])}
            else:
                d = {'name': doc['name']}
            d.update(
                {
                    'id': doc['id'],
                    'id_path': doc['id_path'],
                    'parent': doc['parent_id'],
                    'type': doc['type'],
                    'host': doc.get('host')
                }
            )
            data_list.append(d)

        graph_doc = self.inv.find_one({"environment": self.env, "type": GraphType.INVENTORY_VEGA.value},
                                      collection=self.COLLECTION)
        if not graph_doc:
            graph_doc = {
                "name": self.GRAPH_NAME,
                "type": GraphType.INVENTORY_VEGA.value,
                "environment": self.env
            }

        graph_doc.update({
            "graph": {
                "tree": data_list
            },
            "last_scanned": datetime.now()
        })

        self.inv.set(collection="graphs", item=graph_doc, allow_new_docs=True)