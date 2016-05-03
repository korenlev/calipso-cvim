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
        {"id": "aggregates_root", "text": "Aggregates"},
        {"id": "availability_zones_root", "text": "Availability Zones"},
        {"id": "network_agents_root", "text": "network Agents"}
      ]
    }
    return ret
