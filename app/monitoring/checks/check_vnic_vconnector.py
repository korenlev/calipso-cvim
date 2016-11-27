#!/usr/bin/env python3

# find status of vnic-vconnector link
# vconnector object name defines name of bridge
# use "brctl showmacs <bridge>", then look for the MAC address

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

if len(sys.argv) < 3:
  print('usage: ' + sys.argv[0] + ' <bridge> <mac_address>')
  exit(2)
bridge_name = str(sys.argv[1])
mac_address = str(sys.argv[2])

rc = 0

try:
  out = subprocess.check_output(["brctl showmacs " + bridge_name],
    stderr=subprocess.STDOUT,
    shell=True)
  out = binary2str(out)
  lines = out.splitlines()
  line_number = 1
  line = ''
  found = False
  while line_number < len(lines):
    line = lines[line_number]
    if mac_address in line:
      found = True
      break
    line_number+=1
  state_match = re.match('^\W+([A-Z]+)', line)
  if not found:
    rc = 2
    print('Error: failed to find MAC ' +  mac_address + ":\n" + out + "\n")
  else:
    # grab "is local?" and "ageing timer" values
    line_parts = line.split() # port, mac address, is local?, ageing timer
    is_local = line_parts[2]
    ageing_timer = line_parts[3]
    header = \
      'vConnector bridge name: ' + bridge_name + '\n' + \
      'vNIC MAC address: ' + mac_address + '\n' + \
      'is local: ' + is_local + '\n' + \
      'ageing timer: ' + ageing_timer + '\n' + \
      'vNIC MAC address: ' + mac_address + '\n' + \
      'command: brctl showmacs' + bridge_name + '\n' + \
      'output:\n'
    print(header + out)
except subprocess.CalledProcessError as e:
  print("Error finding MAC " +  mac_address + ": " + binary2str(e.output) + "\n")
  rc = 2

exit(rc)
