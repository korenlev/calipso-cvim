from fetcher import Fetcher

class FetchHostObjectTypes(Fetcher):
  def __init__(self):
    pass
  
  
  def get(self, parent):
    ret = {
      "type": "host object type",
      "id": "",
      "parent": parent,
      "rows": [
        {"id": "instances root", "text": "instances", "descendants": 1},
        {"id": "vservices root", "text": "vservices", "descendants": 1}
      ]
    }
    return ret
