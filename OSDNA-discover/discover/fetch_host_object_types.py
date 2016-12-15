from discover.fetcher import Fetcher


class FetchHostObjectTypes(Fetcher):
    def __init__(self):
        pass

    def get(self, parent):
        ret = {
            "id": "",
            "parent": parent,
            "rows": [
                {
                    "id": "instances_root",
                    "type": "instances_folder",
                    "text": "Instances"
                },
                {
                    "id": "networks_root",
                    "type": "networks_folder",
                    "text": "Networks"
                },
                {
                    "id": "vservices_root",
                    "type": "vservices_folder",
                    "text": "vServices"
                }
            ]
        }
        return ret
