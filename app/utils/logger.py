import datetime
import logging

from messages.message import Message
from utils.inventory_mgr import InventoryMgr

SOURCE_SYSTEM = 'CALIPSO'


class MongoLoggingHandler(logging.Handler):
    """
    Logging handler for MongoDB
    """

    def __init__(self, _env, _level):
        super().__init__(_level)
        self.level = _level
        self.env = _env
        self.inv = InventoryMgr()

    def emit(self, record):
        # make sure we do not try to log to DB when DB is not ready
        if not self.inv.is_db_ready():
            return
        # make ID from current timestamp
        d = datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)
        timestamp_id = '{}.{}.{}'.format(d.days, d.seconds, d.microseconds)
        source = SOURCE_SYSTEM
        object_id = ''
        display_context = ''
        message = Message(timestamp_id, self.env, source,
                          object_id, display_context,
                          msg=Logger.formatter.format(record),
                          level=self.level)
        self.inv.collections['messages'].insert_one(message.get())


class Logger(object):
    formatter = None

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger("OS-DNA")
        self.env = None

    def set_env(self, _env):
        self.env = _env

    def set_loglevel(self, loglevel):
        # assuming loglevel is bound to the string value obtained from the
        # command line argument. Convert to upper case to allow the user to
        # specify --log=DEBUG or --log=debug
        numeric_level = getattr(logging, loglevel.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % loglevel)
        logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                            level=numeric_level)
        logger = logging.getLogger("OS-DNA")
        Logger.formatter = \
            logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
        ch = logging.StreamHandler()
        ch.setLevel(numeric_level)
        ch.setFormatter(Logger.formatter)
        # assuming level was set previously if there already is a handler
        logger.propagate = False
        if not logger.hasHandlers():
            logger.addHandler(ch)
            # logger.addHandler(MongoLoggingHandler(numeric_level, self.env))
        logger.setLevel(numeric_level)
        self.log = logger
