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
            'id': "{}:{}".format(self.env, self.env),
            'name': self.env,
        }]

        data_list.extend([{
            'id': "{}:{}".format(self.env, doc['id']),
            'name': doc['name'],
            'parent': "{}:{}".format(self.env, doc['parent_id']),
            'type': doc['type']
        } for doc in self.inv.find_items({"environment": self.env})])

        graph_doc = self.inv.find_one({"environment": self.env}, collection=self.COLLECTION)
        if not graph_doc:
            graph_doc = {
                "name": self.GRAPH_NAME,
                "type": GraphType.INVENTORY.value,
                "environment": self.env
            }

        graph_doc.update({
            "graph": {
                "tree": data_list
            },
            "last_scanned": datetime.now()
        })

        self.inv.set(collection="graphs", item=graph_doc, allow_new_docs=True)
