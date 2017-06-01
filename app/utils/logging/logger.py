import logging
from abc import ABC


class Logger(ABC):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

    log_format = '%(asctime)s %(levelname)s: %(message)s'
    formatter = logging.Formatter(log_format)
    default_level = INFO

    PROJECT_NAME = 'CALIPSO'

    def __init__(self, logger_name=PROJECT_NAME):
        super().__init__()
        self.log = logging.getLogger(logger_name)
        logging.basicConfig(format=self.log_format,
                            level=self.default_level)
        self.log.propagate = False
        self.set_loglevel(self.default_level)
        self.env = None
        self.level = self.default_level

    def set_env(self, env):
        self.env = env

    @staticmethod
    def get_numeric_level(loglevel):
        numeric_level = getattr(logging, loglevel.upper(), Logger.default_level)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % loglevel)
        return numeric_level

    def set_loglevel(self, loglevel):
        # assuming loglevel is bound to the string value obtained from the
        # command line argument. Convert to upper case to allow the user to
        # specify --log=DEBUG or --log=debug
        numeric_level = self.get_numeric_level(loglevel)

        for handler in self.log.handlers:
            handler.setLevel(numeric_level)
        self.log.setLevel(numeric_level)
        self.level = loglevel

    def _log(self, level, message, *args, exc_info=False, **kwargs):
        self.log.log(level, message, *args, exc_info=exc_info, **kwargs)

    def debug(self, message, *args, **kwargs):
        self._log(logging.DEBUG, message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        self._log(logging.INFO, message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self._log(logging.WARNING, message, *args, **kwargs)

    def warn(self, message, *args, **kwargs):
        self.warning(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        self._log(logging.ERROR, message, *args, **kwargs)

    def exception(self, message, *args, **kwargs):
        self._log(logging.ERROR, message, exc_info=True, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        self._log(logging.CRITICAL, message, *args, **kwargs)

    def add_handler(self, handler):
        handler_defined = handler.__class__ in map(lambda h: h.__class__, self.log.handlers)

        if not handler_defined:
            handler.setLevel(self.default_level)
            handler.setFormatter(self.formatter)
            self.log.addHandler(handler)
