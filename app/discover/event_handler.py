from logger import Logger
from inventory_mgr import InventoryMgr

class EventHandler(Logger):

  def __init__(self, env, inventory_collection):
    super().__init__()
    self.inv = InventoryMgr()
    self.inv.set_inventory_collection(inventory_collection)
    self.env = env

  def instance_add(self, notification):
    print("instance_add")

  def instance_delete(self, notification):
    print("instance_delete")

  def instance_update(self, notification):
    vals = notification['payload']
    id = vals['instance_id']
    instance = self.inv.get_by_id(self.env, id)
    if not instance:
      return
    name = vals['display_name']
    instance['name'] = name
    instance['object_name'] = name
    name_path = instance['name_path']
    instance['name_path'] = name_path[:name_path.rindex('/') + 1] + name
    # TBD: fix name_path for descendants
    self.inv.set(instance)

  def instance_down(self, notification):
    pass

  def instance_up(self, notification):
    pass

  def region_add(self, notification):
    pass

  def region_delete(self, notification):
    pass

  def region_update(self, notification):
    pass
