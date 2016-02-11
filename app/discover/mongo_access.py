from pymongo import MongoClient

class MongoAccess:
  
  client = None
  db = None
  
  def __init__(self):
    connect()
  
  def connect(self):
    if (client != None):
      return
    client = MongoClient('localhost', 27017) #, :database => 'osdna')
    db = client.osdna
