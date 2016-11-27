from fetcher import Fetcher

class FetchHostObjectTypes(Fetcher):
  def __init__(self):
    pass
  
  
  def get(self, parent):
    ret = {
      "type": "host_object_type",
      "id": "",
      "parent": parent,
      "rows": [
        {"id": "instances_root", "text": "Instances", "descendants": 1},
        {"id": "networks_root", "text": "Networks", "descendants": 1},
        {"id": "pnics_root", "text": "pNICs", "descendants": 1},
        {"id": "vservices_root", "text": "vServices", "descendants": 1}
      ]
    }
    return ret
