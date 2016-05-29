import json
import re
import logging

from inventory_mgr import InventoryMgr

class Fetcher:
  
  inventory = None
  
  def __init__(self):
    super().__init__()
    self.prettify = False
    self.environment = ""
    if not Fetcher.inventory:
      Fetcher.inventory = InventoryMgr()
    self.log = logging.getLogger("OS-DNA")
  
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
    try:
      s = txt.decode("utf-8")
    except TypeError:
      s = str(txt)
    s = re.sub(r"^b.", "", s)
    s = re.sub(r"'$", "", s)
    return s
    
  def set_logger(self, loglevel):
    # assuming loglevel is bound to the string value obtained from the
    # command line argument. Convert to upper case to allow the user to
    # specify --log=DEBUG or --log=debug
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
      raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
      level=numeric_level)
    logger = logging.getLogger("OS-DNA")
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(numeric_level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.propagate = False
    logger.setLevel(numeric_level)
    self.log = logger
