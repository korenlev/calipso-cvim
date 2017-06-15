def binary2str(txt):
    if not isinstance(txt, bytes):
        return str(txt)
    try:
        s = txt.decode("utf-8")
    except TypeError:
        s = str(txt)
    return s
