from fetcher import Fetcher


class FetchRegionObjectTypes(Fetcher):
    def __init(self):
        pass

    def get(self, parent):
        ret = {
            "id": "",
            "parent": parent,
            "rows": [
                {
                    "id": "aggregates_root",
                    "type": "aggregates_folder",
                    "text": "Aggregates"
                },
                {
                    "id": "availability_zones_root",
                    "type": "availability_zones_folder",
                    "text": "Availability Zones"
                },
                {
                    "id": "network_agents_root",
                    "type": "network_agents_folder",
                    "text": "network Agents"
                }
            ]
        }
        return ret
