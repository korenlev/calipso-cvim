import re
from fetcher import Fetcher
from inventory_mgr import InventoryMgr
from events.event_instance_delete import EventInstanceDelete
from events.event_instance_add import EventInstanceAdd

class EventHandler(Fetcher):

  def __init__(self, env, inventory_collection):
    super().__init__()
    self.inv = InventoryMgr()
    self.inv.set_inventory_collection(inventory_collection)
    self.env = env

  def instance_add(self, vals):
    print("instance_add")
    handler = EventInstanceAdd()
    handler.handle(self.env, vals)

  def instance_delete(self, vals):
    print("instance_delete")
    handler = EventInstanceDelete()
    handler.handle(self.env, vals)

  def instance_update(self, notification):
    vals = notification['payload']
    id = vals['instance_id']
    state = vals['state']
    old_state = vals['old_state']
    if state == 'building':
      return

    if state == 'active' and old_state == 'building':
      self.instance_add(vals)
      return

    if state == 'deleted' and old_state == 'active':
      self.instance_delete(vals)
      return

    name = vals['display_name']
    instance = self.inv.get_by_id(self.env, id)
    if not instance:
      return
    instance['name'] = name
    instance['object_name'] = name
    name_path = instance['name_path']
    instance['name_path'] = name_path[:name_path.rindex('/') + 1] + name
    # TBD: fix name_path for descendants
    if (name_path != instance['name_path']):
      self.inv.values_replace({
        "environment": self.env,
        "name_path": {"$regex": r"^" + re.escape(name_path + '/')}},
        {"name_path": {"from": name_path, "to": instance['name_path']}})
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
