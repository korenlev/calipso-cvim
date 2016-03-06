from fetcher import Fetcher

class FetchRegionObjectTypes(Fetcher):
  def __init(self):
    pass
  
  
  def get(self, parent):
    ret = {
      "type": "region object type",
      "id": "",
      "parent": parent,
      "rows": [
        {"id": "projects_root", "text": "projects", "descendants": 1},
        {"id": "aggregates_root", "text": "aggregates", "descendants": 1},
        {"id": "availability_zones_root", "text": "availability zones", "descendants": 1},
        {"id": "network_agents_root", "text": "network agents", "descendants": 1}
      ]
    }
    return ret
