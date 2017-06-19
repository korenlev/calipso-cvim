#!/usr/bin/env python3
"""
for vservice with type T and id X
run on the corresponding host:
ip netns pid X
response is pid(s), for example:
32075

For DHCP there are multiple pid, we will take the dnsmasq process

then run :
ps -uf -p 32075

get STAT - "S" and "R" = OK
"""

import subprocess
import sys

from binary_converter import binary2str


rc = 0

args = sys.argv
if len(args) < 3:
    print('usage: check_vservice.py <vService type> <vService ID>')
    exit(2)

vservice_type = args[1]
vservice_id = args[2]
netns_cmd = 'ip netns pid {}'.format(vservice_id)
pid = ''
ps_cmd = ''
try:
    out = subprocess.check_output([netns_cmd], stderr=subprocess.STDOUT,
                                  shell=True)
    out = binary2str(out)
    lines = out.splitlines()
    if not lines:
        print('no matching vservice: {}'.format(vservice_id))
        exit(2)
    pid = lines[0]
except subprocess.CalledProcessError as e:
    print("Error running '{}': {}"
          .format(netns_cmd, binary2str(e.output)))
    exit(2)
try:
    ps_cmd = 'ps -uf -p {}'.format(pid)
    out = subprocess.check_output([ps_cmd], stderr=subprocess.STDOUT,
                                  shell=True)
    ps_out = binary2str(out)
    lines = ps_out.splitlines()
    if not lines:
        print('no matching vservice: {}'.format(vservice_id))
        exit(2)
    line = lines[0]
    headers = lines[0].split()
    lines = lines[1:]
    if vservice_type == 'dhcp':
        lines = [line for line in lines if 'dnsmasq' in line]
    values = lines[0].split()
    stat_index = headers.index('STAT')
    status = values[stat_index]
    rc = 0 if status in ['S', 'R'] else 2
    print('{}\n{}\n{}'.format(netns_cmd, ps_cmd, ps_out))
except subprocess.CalledProcessError as e:
    print("Error running '{}': {}".format(ps_cmd, binary2str(e.output)))
    rc = 2

exit(rc)
