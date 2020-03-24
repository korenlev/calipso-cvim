from datetime import datetime

from scan.processors.processor import Processor


class ProcessInventoryTree(Processor):
    PREREQUISITES = []
    COLLECTION = "trees"

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

        tree_doc = self.inv.find_one({"environment": self.env}, collection=self.COLLECTION)
        if not tree_doc:
            tree_doc = {
                "environment": self.env
            }

        tree_doc.update({
            "tree": data_list,
            "last_scanned": datetime.now()
        })

        self.inv.set(collection="trees", item=tree_doc, allow_new_docs=True)
