import logging


class Logger:

    def __init__(self):
        super().__init__()
        self.set_log_level("DEBUG")
        self.log = logging.getLogger("OS-DNA-API")

    def set_log_level(self, log_level):
        numeric_level = getattr(logging, log_level.upper(), None)

        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % log_level)

        logging.basicConfig(format='%(name)s %(asctime)s %(levelname)s: %(message)s',
                            level=numeric_level)