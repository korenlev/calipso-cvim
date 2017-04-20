import re

PORT = "port number"
IP = "ipv4/ipv6 address"
HOSTNAME = "host name"
PATH = "path"

_PORT_REGEX = r'^0*(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|' \
           r'6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9])$'

_HOSTNAME_REGEX = r'^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])' \
               r'(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$'

_PATH_REGEX = r'^(\/){1}([^\/\0]+(\/)?)+$'

_IPV4_REGEX = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$'
_IPV6_REGEX = r'^(((?=.*(::))(?!.*\3.+\3))\3?|[\dA-F]{1,4}:)([\dA-F]{1,4}(\3|:\b)|\2){5}' \
             r'(([\dA-F]{1,4}(\3|:\b|$)|\2){2}|(((2[0-4]|1\d|[1-9])?\d|25[0-5])\.?\b){4})$'

_REGEX_MAP = {
    PORT: _PORT_REGEX,
    HOSTNAME: _HOSTNAME_REGEX,
    PATH: _PATH_REGEX,
    IP: [_IPV4_REGEX, _IPV6_REGEX]
}


def validate(key, value, regex_names, error_message=None):
    if not isinstance(regex_names, list):
        regex_names = [regex_names]

    for regex_name in regex_names:
        regexes = _REGEX_MAP[regex_name]

        if not isinstance(regexes, list):
            regexes = [regexes]

        try:
            value = str(value)
            match_regexes = [regex for regex in regexes
                             if re.match(regex, value)]
            if match_regexes:
                return None
        except:
            pass

    return error_message if error_message else \
        '{0} must be a valid {1}'.format(key, " or ".join(regex_names))
