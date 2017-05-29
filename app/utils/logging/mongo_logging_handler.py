import datetime
import logging

from messages.message import Message
from utils.inventory_mgr import InventoryMgr
from utils.logging.logger import Logger


class MongoLoggingHandler(logging.Handler):
    """
    Logging handler for MongoDB
    """
    SOURCE_SYSTEM = 'CALIPSO'

    def __init__(self, _env, _level):
        super().__init__(Logger.get_numeric_level(_level))
        self.str_level = _level
        self.env = _env
        self.inv = InventoryMgr()

    def emit(self, record):
        # make sure we do not try to log to DB when DB is not ready
        if not (self.inv and self.inv.is_db_ready() and 'messages' in self.inv.collections):
            return
        # make ID from current timestamp
        d = datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)
        timestamp_id = '{}.{}.{}'.format(d.days, d.seconds, d.microseconds)
        source = self.SOURCE_SYSTEM
        object_id = ''
        display_context = ''
        message = Message(timestamp_id, self.env, source,
                          object_id, display_context,
                          msg=Logger.formatter.format(record),
                          level=self.str_level)
        self.inv.collections['messages'].insert_one(message.get())