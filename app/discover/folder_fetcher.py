#!/usr/bin/env python3

from fetcher import Fetcher

class FolderFetcher(Fetcher):

  def __init__(self, types_name, parent_type, text=""):
    super(FolderFetcher, self).__init__()
    self.types_name = types_name
    self.parent_type = parent_type
    self.text = text
    if not self.text:
      self.text = self.types_name.capitalize()
  
  def get(self, id):
    oid = id + "-" + self.types_name
    root_obj = {
      "id": oid,
      "name": oid,
      "text": self.text,
      "type": self.parent_type + "_object_type",
      "parent_id": id,
      "parent_type": self.parent_type
    }
    return self.jsonify([root_obj])
