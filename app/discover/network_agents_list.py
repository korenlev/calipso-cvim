from mongo_access import MongoAccess

class NetworkAgentsList(MongoAccess):
  
  def __init__(self):
    super(NetworkAgentsList, self).__init__()
    self.list = MongoAccess.db["network_agent_types"]
  
  def get_type(self, description):
    matches = self.list.find({"description": description})
    for doc in matches:
      doc["_id"] = str(doc["_id"])
      return doc
    return {}
