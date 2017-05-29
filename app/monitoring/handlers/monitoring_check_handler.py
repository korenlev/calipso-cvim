# handle monitoring event
import datetime
import sys
from time import gmtime, strftime

from bson import ObjectId

from discover.configuration import Configuration
from messages.message import Message
from utils.inventory_mgr import InventoryMgr
from utils.logging.console_logger import ConsoleLogger
from utils.special_char_converter import SpecialCharConverter
from utils.string_utils import stringify_datetime

TIME_FORMAT = '%Y-%m-%d %H:%M:%S %Z'
SOURCE_SYSTEM = 'Sensu'
ERROR_LEVEL = ['info', 'warn', 'error']


class MonitoringCheckHandler(ConsoleLogger, SpecialCharConverter):
    STATUS_LABEL = ['OK', 'Warning', 'Critical']

    def __init__(self, args):
        self.set_loglevel('WARN')
        self.env = args.env
        try:
            self.conf = Configuration(args.mongo_config)
            self.inv = InventoryMgr()
            self.inv.set_collections(args.inventory)
        except FileNotFoundError:
            sys.exit(1)

    def doc_by_id(self, object_id):
        doc = self.inv.get_by_id(self.env, object_id)
        if not doc:
            self.log.warn('No matching object found with ID: ' + object_id)
        return doc

    def doc_by_db_id(self, db_id, coll_name=None):
        coll = self.inv.collections[coll_name] if coll_name else None
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

    @staticmethod
    def check_ts(check_result):
        return gmtime(check_result['executed'])

    def keep_result(self, doc, check_result):
        status = check_result['status']
        ts = self.check_ts(check_result)
        self.set_doc_status(doc, status, check_result['output'], ts)
        self.keep_message(doc, check_result)

    def keep_message(self, doc, check_result, error_level=None):
        msg_id = check_result['id']
        obj_id = ObjectId(doc['_id'])
        display_context = doc['id']
        level = error_level if error_level else ERROR_LEVEL[check_result['status']]
        dt = datetime.datetime.utcfromtimestamp(check_result['executed'])
        ts = stringify_datetime(dt)
        message = Message(msg_id=msg_id, env=self.env, source=SOURCE_SYSTEM,
                          object_id=obj_id, object_type=doc['type'],
                          display_context=display_context, level=level,
                          msg=check_result, ts=ts)
        collection = self.inv.collections['messages']
        collection.insert_one(message.get())
