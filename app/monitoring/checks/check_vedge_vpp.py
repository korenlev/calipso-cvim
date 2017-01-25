#!/usr/bin/env python3
"""
sudo vppctl show runtime:

test 1: was the return value not null?
test 2: is startup-config-process = done?
1 and 2 = vedge status ok
1 and not 2 = vedge status warning
not 1 = vedge status critical

return full text of "vppctl show runtime"
"""

import re
import sys
import subprocess

def binary2str(txt):
    if not isinstance(txt, bytes):
      return str(txt)
    try:
      s = txt.decode("ascii")
    except TypeError:
      s = str(txt)
    return s

rc = 0
search_pattern = re.compile("^startup-config-process ")

try:
    out = subprocess.check_output(["sudo vppctl show runtime"],
                                  stderr=subprocess.STDOUT,
                                  shell=True)
    out = binary2str(out)
    lines = out.splitlines()
    matching_lines = [l for l in lines if search_pattern.match(l)]
    matching_line = matching_lines[0] if matching_lines else None
    if matching_line and "done" in matching_line.split():
        print('output from "vppctl show runtime":\n' + out)
    else:
        rc = 1
        print('Error: failed to find status in output of "vppctl show runtime": ' + out)
except subprocess.CalledProcessError as e:
    print("Error finding 'vppctl show runtime': " + binary2str(e.output))
    rc = 2

exit(rc)
