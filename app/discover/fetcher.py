import json
import re

from logger import Logger

class Fetcher(Logger):

  env = None

  def __init__(self):
    super().__init__()
    self.prettify = False
    self.environment = ""

  def escape(self, string):
    return string
  
  def set_prettify(self, prettify):
    self.prettify = prettify
    
  def get_prettify(self):
    return self.prettify
  
  def set_env(self, env):
    Fetcher.env = env

  def get_env(self):
    return Fetcher.env

  def jsonify(self, obj):
    if self.prettify:
      return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    else:
      return json.dumps(obj)
  
  def binary2str(self, txt):
    if not isinstance(txt, bytes):
      return str(txt)
    try:
      s = txt.decode("ascii")
    except TypeError:
      s = str(txt)
    return s
    
  def set_logger(self, loglevel):
    self.log.set_level(loglevel)
