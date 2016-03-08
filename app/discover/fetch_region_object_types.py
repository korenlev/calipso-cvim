from fetcher import Fetcher

class FetchRegionObjectTypes(Fetcher):
  def __init(self):
    pass
  
  
  def get(self, parent):
    ret = {
      "type": "region_object_type",
      "id": "",
      "parent": parent,
      "rows": [
        {"id": "aggregates_root", "text": "Aggregates", "descendants": 1},
        {"id": "availability_zones_root", "text": "Availability Zones", "descendants": 1},
        {"id": "network_agents_root", "text": "network Agents", "descendants": 1}
      ]
    }
    return ret
