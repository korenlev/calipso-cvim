from fetcher import Fetcher

class FetchEnvironmentObjectTypes(Fetcher):
  def __init(self):
    pass
  
  
  def get(self, parent):
    ret = {
      "type": "region_object_type",
      "id": "",
      "parent": parent,
      "rows": [
        {"id": "regions_root", "text": "Regions", "descendants": 1},
        {"id": "projects_root", "text": "Projects", "descendants": 1}
      ]
    }
    return ret
