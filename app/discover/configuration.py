from mongo_access import MongoAccess
from singleton import Singleton

class Configuration(MongoAccess, metaclass=Singleton):
  
  def __init__(self):
    self.db_client = MongoAccess()
    self.db = MongoAccess.db
    self.collection = self.db["environments"]
  
  def use_env(self, env_name):
    self.env = env_name
    envs = self.collection.find({"name": env_name})
    count = 0
    for e in envs:
      count += 1
      self.config = e["configuration"]
      if count > 1:
        raise ValueError("set_env: found multiple matching environments")
    if count == 0:
      raise ValueError("set_env: could not find matching environment")
  
  def get_env(self):
    return self.env
  
  def get(self, component):
    if not self.config:
      raise ValueError("Configuration: environment not set")
    matches = [c for c in self.config if c["name"] == component]
    if (len(matches) == 0):
      raise IndexError("No matches for configuration component: " + component)
    if len(matches) > 1:
      raise IndexError("Found multiple matches for configuration component: " + component)
    return matches[0]
