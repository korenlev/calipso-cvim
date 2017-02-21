# handle monitoring event
import sys

from bson import ObjectId
from time import gmtime, strftime

from discover.configuration import Configuration
from utils.inventory_mgr import InventoryMgr
from utils.logger import Logger
from utils.special_char_converter import SpecialCharConverter

TIME_FORMAT = '%Y-%m-%d %H:%M:%S %Z'


class MonitoringCheckHandler(Logger, SpecialCharConverter):

  STATUS_LABEL = ['OK', 'Warning', 'Critical']

  def __init__(self, args):
    self.set_loglevel('WARN')
    self.env = args.env
    try:
      self.conf = Configuration(args.mongo_config)
      self.inv = InventoryMgr()
      self.inv.set_inventory_collection(args.inventory)
    except FileNotFoundError:
      sys.exit(1)

  def doc_by_id(self, object_id):
    doc = self.inv.get_by_id(self.env, object_id)
    if not doc:
      self.log.warn('No matching object found with ID: ' + object_id)
    return doc

  def doc_by_db_id(self, db_id, coll_name=None):
    coll = self.inv.coll[coll_name] if coll_name else None
    doc = self.inv.find({'_id': ObjectId(db_id)},
                        get_single=True, collection=coll)
    if not doc:
      self.log.warn('No matching object found with DB ID: ' + db_id)
    return doc

  def set_doc_status(self, doc, status, status_text, timestamp):
    doc['status'] = self.STATUS_LABEL[status] if isinstance(status, int) \
        else status
    if status_text:
      doc['status_text'] = status_text
    doc['status_timestamp'] = strftime(TIME_FORMAT, timestamp)
    if 'link_type' in doc:
        self.inv.write_link(doc)
    else:
        self.inv.set(doc)

  def check_ts(self, check_result):
    return gmtime(check_result['executed'])

  def keep_result(self, doc, check_result):
    status = check_result['status']
    self.set_doc_status(doc, status, check_result['output'],
                        self.check_ts(check_result))
