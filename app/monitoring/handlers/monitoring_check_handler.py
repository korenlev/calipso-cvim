# handle monitoring event

from bson import ObjectId
from time import gmtime, strftime

from discover.inventory_mgr import InventoryMgr
from discover.logger import Logger

ENV = 'Mirantis-Mitaka'
INVENTORY_COLLECTION = 'Mirantis-Mitaka'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S %Z'

class MonitoringCheckHandler(Logger):

  STATUS_LABEL = ['OK', 'Warning', 'Critical']

  def __init__(self):
    self.set_loglevel('WARN')
    self.inv = InventoryMgr()
    self.inv.set_inventory_collection(INVENTORY_COLLECTION)

  def doc_by_id(self, object_id):
    doc = self.inv.get_by_id(ENV, object_id)
    if not doc:
      self.log.warn('No matching object found with ID: ' + object_id)
    return doc

  def doc_by_db_id(self, db_id, coll_name=None):
    coll = self.inv.coll[coll_name] if coll_name else None
    doc = self.inv.find_in_db({'_id': ObjectId(db_id)}, get_single=True, collection=coll)
    if not doc:
      self.log.warn('No matching object found with DB ID: ' + db_id)
    return doc

  def set_doc_status(self, doc, status, status_text, timestamp):
    doc['status'] = self.STATUS_LABEL[status] if isinstance(status, int) else status
    if status_text:
      doc['status_text'] = status_text
    doc['status_timestamp'] = strftime(TIME_FORMAT, timestamp)
    coll = self.inv.coll['links' if 'link_type' in doc else 'inventory']
    self.inv.set(doc, collection=coll)

  def check_ts(self, check_result):
    return gmtime(check_result['executed'])

  def keep_result(self, doc, check_result):
    status = check_result['status']
    self.set_doc_status(doc, status, check_result['output'], self.check_ts(check_result))

