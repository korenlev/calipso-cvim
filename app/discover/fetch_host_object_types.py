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
        {"id": "instances_root", "text": "Instances"},
        {"id": "networks_root", "text": "Networks"},
        {"id": "pnics_root", "text": "pNICs"},
        {"id": "vservices_root", "text": "vServices"}
      ]
    }
    return ret
