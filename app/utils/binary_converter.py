from utils.logging.console_logger import ConsoleLogger


class BinaryConverter:

    def __init__(self):
        self.log = ConsoleLogger()

    def binary2str(self, txt):
        if not isinstance(txt, bytes):
            return str(txt)
        try:
            s = txt.decode("utf-8")
        except TypeError:
            s = str(txt)
        return s

