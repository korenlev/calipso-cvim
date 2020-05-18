from datetime import datetime

from scan.processors.processor import Processor


class GraphProcessor(Processor):
    COLLECTION = "graphs"
    GRAPH_NAME = "unknown"
    GRAPH_TYPE = None

    def get_data_list_and_graph_doc(self) -> (list, dict):
        data_list = [{
            'id': self.env,
            'name': self.env,
        }]

        for doc in self.inv.find_items({"environment": self.env}):
            data_list.append({
                'id': doc['id'],
                'id_path': doc['id_path'],
                'parent': doc['parent_id'],
                'type': doc['type'],
                'host': doc.get('host'),
                'name': doc.get('text', doc['name']) if doc['type'].endswith('folder') else doc['name']
            })

        graph_doc = self.inv.find_one({"environment": self.env, "type": self.GRAPH_TYPE},
                                      collection=self.COLLECTION)

        if not graph_doc:
            graph_doc = {
                "name": self.GRAPH_NAME,
                "type": self.GRAPH_TYPE,
                "environment": self.env
            }

        graph_doc.update({
            "last_scanned": datetime.now()
        })

        return data_list, graph_doc
