import logging


class Logger:
    def __init__(self):
        self.log = logging.getLogger("OS-DNA")

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
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
        ch = logging.StreamHandler()
        ch.setLevel(numeric_level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logger.propagate = False
        logger.setLevel(numeric_level)
        self.log = logger
