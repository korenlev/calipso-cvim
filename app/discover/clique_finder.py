from fetcher import Fetcher
from mongo_access import MongoAccess

from bson.objectid import ObjectId

class CliqueFinder(Fetcher, MongoAccess):
  
  def __init__(self, inventory, links, clique_types, cliques):
    super().__init__()
    self.inv = inventory
    self.links = links
    self.clique_types = clique_types
    self.cliques = cliques
  
  def find_cliques(self):
    self.log.info("scanning for cliques")
    clique_types = self.clique_types.find({"environment": self.get_env()})
    for clique_type in clique_types:
      self.find_cliques_for_type(clique_type)
    self.log.info("finished scanning for cliques")

  def find_cliques_for_type(self, clique_type):
    object_type = clique_type["focal_point_type"]
    objects_for_focal_point_type = self.inv.find({
      "environment": self.get_env(),
      "type": object_type
    })
    for o in objects_for_focal_point_type:
      self.construct_clique_for_focal_point(o, clique_type)
  
  def construct_clique_for_focal_point(self, o, clique_type):
    # keep a hash of nodes in clique that were visited for each type
    # start from the focal point
    nodes_of_type = {o["type"]: {str(o["_id"]): 1}}
    clique = {
      "environment": self.env,
      "focal_point": o["_id"],
      "focal_point_type": o["type"],
      "links": []
    }
    for link_type in clique_type["link_types"]:
      from_type = link_type[:link_type.index("-")]
      to_type = link_type[link_type.index("-")+1:]
      if from_type not in nodes_of_type.keys():
        continue
      for from_point in nodes_of_type[from_type].keys():
        matches = self.links.find({
          "environment": self.env,
          "link_type": link_type,
          "source": ObjectId(from_point)
        })
        for link in matches:
          id = link["_id"]
          if id in clique["links"]:
            continue
          clique["links"].append(id)
          to_point = str(link["target"])
          if to_type not in nodes_of_type:
            nodes_of_type[to_type] = {}
          nodes_of_type[to_type][to_point] = 1

    # after adding the links to the clique, create/update the clique
    if not clique["links"]:
      return
    self.cliques.update_one(
      {
        "environment": self.get_env(),
        "focal_point": clique["focal_point"]
      },
      {'$set': clique},
      upsert=True)
