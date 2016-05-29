from pymongo import MongoClient

import re
import logging

class MongoAccess:
  
  client = None
  db = None
  
  def __init__(self):
    self.mongo_connect()
    self.log = logging.getLogger("OS-DNA")
  
  def mongo_connect(self):
    if (MongoAccess.client != None):
      return
    MongoAccess.client = MongoClient('localhost', 27017)
    MongoAccess.db = MongoAccess.client.osdna

  def encode_dots(self, s):
    return s.replace(".", "[dot]")

  def decode_dots(self, s):
    return s.replace("[dot]", ".")

  # Mongo will not accpet dot (".") in keys, or $ in start of keys
  # $ in beginning of key does not happen in OpenStack,
  # so need to translate only "." --> "[dot]"
  def encode_mongo_keys(self, item):
    return self.change_dict_naming_convention(item, self.encode_dots)

  def decode_mongo_keys(self, item):
    return self.change_dict_naming_convention(item, self.decode_dots)

  # Convert a nested dictionary from one convention to another.
  # Args:
  #     d (dict): dictionary (nested or not) to be converted.
  #     convert_function (func): function that takes the string in one convention and returns it in the other one.
  # Returns:
  #     Dictionary with the new keys.
  def change_dict_naming_convention(self, d, convert_function):
    new = {}
    if not d:
      return d
    if isinstance(d, str):
      return d
    for k, v in d.items():
      new_v = v
      if isinstance(v, dict):
        new_v = self.change_dict_naming_convention(v, convert_function)
      elif isinstance(v, list):
        new_v = list()
        for x in v:
          new_v.append(self.change_dict_naming_convention(x, convert_function))
      new[convert_function(k)] = new_v
    return new
