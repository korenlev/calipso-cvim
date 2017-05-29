from utils.logging.console_logger import ConsoleLogger
from utils.logging.mongo_logging_handler import MongoLoggingHandler


class FullLogger(ConsoleLogger):

    def __init__(self):
        super().__init__()

    def _log(self, level, message, exc_info=False, *args, **kwargs):
        handler_defined = MongoLoggingHandler.__class__ \
                          in map(lambda handler: handler.__class__, self.log.handlers)
        if 'env' in kwargs and not handler_defined:
            try:
                self.log.addHandler(MongoLoggingHandler(kwargs.get('env'),
                                                        self.level))
            except:
                pass

        super()._log(level=level, message=message, exc_info=exc_info,
                     *args, **kwargs)
