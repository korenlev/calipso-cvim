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
        {"id": "projects root", "text": "projects", "descendants": 1},
        {"id": "aggregates root", "text": "aggregates", "descendants": 1},
        {"id": "availability zones root", "text": "availability zones", "descendants": 1}
      ]
    }
    return ret
