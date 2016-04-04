import json
import re
from inventory_mgr import InventoryMgr

class Fetcher:
  
  inventory = None
  
  def __init__(self):
    self.prettify = False
    self.environment = ""
    if not Fetcher.inventory:
      Fetcher.inventory = InventoryMgr()
  
  def escape(self, string):
    return string
  
  def set_prettify(self, prettify):
    self.prettify = prettify
    
  def get_prettify(self):
    return self.prettify
  
  def set_env(self, env):
    self.environment = env

  def get_env(self):
    return self.environment

  def jsonify(self, obj):
    if self.prettify:
      return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    else:
      return json.dumps(obj)
  
  def binary2str(self, txt):
    s = str(txt)
    s = re.sub(r"^b.", "", s)
    s = re.sub(r"'$", "", s)
    return s
    
