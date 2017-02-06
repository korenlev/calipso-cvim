import re


class SpecialCharConverter():

    translated_re = re.compile(r'---[.][.][0-9]+[.][.]---')

    def encode_special_characters(self, s):
        SPECIAL_CHARS = [':', '/']
        for c in SPECIAL_CHARS:
            if c in s:
                s = s.replace(c, '---..' + str(ord(c)) + '..---')
        return s

    def decode_special_characters(self, s):
        replaced = []
        for m in re.finditer(self.translated_re, s):
            match = m.group(0)
            char_code = match[5:len(match)-5]
            if char_code in replaced:
                next
            replaced.append(char_code)
            s = s.replace(match, chr(int(char_code)))
        return s
