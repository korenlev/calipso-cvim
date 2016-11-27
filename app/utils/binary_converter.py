from discover.logger import Logger


class BinaryConverter(Logger):

    def binary2str(self, txt):
        if not isinstance(txt, bytes):
            return str(txt)
        try:
            s = txt.decode("ascii")
        except TypeError:
            s = str(txt)
        return s

