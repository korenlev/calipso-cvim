#!/usr/bin/env python3
"""
Check OVS vEdge health

Run command: 
ps -aux | grep "\(ovs-vswitchd\|ovsdb-server\)"

OK if for both ovs-vswitchd AND ovsdb-server processes we see '(healthy)'
otherwise CRITICAL

return full text output of the command
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
cmd = 'ps aux | grep "\(ovs-vswitchd\|ovsdb-server\): monitoring" | grep -v grep'

try:
    out = subprocess.check_output([cmd], stderr=subprocess.STDOUT, shell=True)
    out = binary2str(out)
    lines = out.splitlines()
    matching_lines = [l for l in lines if '(healthy)']
    rc = 0 if len(matching_lines) == 2 else 2
    print(out)
except subprocess.CalledProcessError as e:
    print("Error finding expected output: " + binary2str(e.output))
    rc = 2

exit(rc)
