#!/usr/bin/env python3
"""
sudo vppctl show hardware-interfaces:

take only the virtual interfaces, e.g. "VirtualEthernet0/0/0"
Status: "OK" if "up" is detected in the interface line, CRITICAL otherwise

return full text of "vppctl show hardware-interfaces"
"""

import re
import subprocess

NAME_RE = '^[a-zA-Z]*GigabitEthernet'

def binary2str(txt):
    if not isinstance(txt, bytes):
      return str(txt)
    try:
      s = txt.decode("ascii")
    except TypeError:
      s = str(txt)
    return s

rc = 0

try:
    out = subprocess.check_output(["sudo vppctl show hardware-interfaces"],
                                  stderr=subprocess.STDOUT,
                                  shell=True)
    out = binary2str(out)
    lines = out.splitlines()
    name_re = re.compile(NAME_RE)
    matching_lines = [l for l in lines if name_re.search(l)]
    matching_line = matching_lines[0] if matching_lines else None
    if matching_line:
        rc = 0 if "up" in matching_line.split() else 2
        print('output from "vppctl show hardware-interfaces": \n\n' + out)
    else:
        rc = 2
        print('Error: failed to find pNic in output of ' +
              '"vppctl show hardware-interfaces": ' + out)
except subprocess.CalledProcessError as e:
    print("Error running 'vppctl show hardware-interfaces': " + binary2str(e.output))
    rc = 2

exit(rc)
