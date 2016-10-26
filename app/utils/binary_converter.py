class BinaryConverter():

    def binary2str(self, txt):
        if not isinstance(txt, bytes):
            return str(txt)
        try:
            s = txt.decode("ascii")
        except TypeError:
            s = str(txt)
        return s

