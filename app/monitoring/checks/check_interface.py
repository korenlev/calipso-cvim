#!/usr/bin/env python3

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

if len(sys.argv) < 2:
    print('name of interface must be specified')
    exit(2)
nic_name = str(sys.argv[1])

rc = 0

try:
    out = subprocess.check_output(["ifconfig " + nic_name],
        stderr=subprocess.STDOUT,
        shell=True)
    out = binary2str(out)
    lines = out.splitlines()
    line_number = 1
    while line_number < len(lines):
      line = lines[line_number]
      if ' BROADCAST ' in line:
        break
      line_number+=1
    state_match = re.match('^\W+([A-Z]+)', line)
    if not state_match:
        rc = 2
        print('Error: failed to find status in ifconfig output: ' + out)
    else:
        rc = 0 if state_match.group(1) == 'UP' else 2
        print(out)
except subprocess.CalledProcessError as e:
    print("Error finding NIC " +  nic_name + ": " + binary2str(e.output) + "\n")
    rc = 2

exit(rc)
