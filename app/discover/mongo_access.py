from pymongo import MongoClient

class MongoAccess:
  
  client = None
  db = None
  
  def __init__(self):
    self.connect()
  
  def connect(self):
    if (MongoAccess.client != None):
      return
    MongoAccess.client = MongoClient('localhost', 27017)
    MongoAccess.db = MongoAccess.client.osdna
