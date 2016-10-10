#!/usr/bin/env python3

# handle monitoring events

import argparse
import json
import sys
from time import gmtime, strftime

from discover.inventory_mgr import InventoryMgr
from discover.logger import Logger

ENV = 'Mirantis-Liberty'
INVENTORY_COLLECTION = 'Mirantis-Liberty'
STATUS_LABEL = ['OK', 'Warning', 'Critical']
TIME_FORMAT = '%Y-%m-%d %H:%M:%S %Z'

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', nargs='?', type=str,
        default='',
        help="read input from the specifed file \n(default: from stdin)")
    args = parser.parse_args()
    return args

input = None
args = get_args()
if args.inputfile:
    try:
        with open(args.inputfile, 'r') as input_file:
            input = input_file.read()
    except Exception as e:
        raise FileNotFoundError("failed to open input file: " + args.inputfile)
        exit(1)
else:
    input = sys.stdin.read()
    if not input:
        raise InputError("No input provided on stdin")
        exit(1)

check_result = json.loads(input)
check_result = check_result['check']
name = check_result['name']
status = check_result['status']
object_type = name[:name.index('_')]
object_id = name[name.index('_')+1:]
port_id = object_id[object_id.index('_')+1:]
object_id = object_id[:object_id.index('_')]
logger = Logger()
logger.set_loglevel('WARN')
inv = InventoryMgr()
inv.set_inventory_collection(INVENTORY_COLLECTION)
doc = inv.get_by_id(ENV, object_id)
if not doc:
    logger.log.warn('No matching object found with ID: ' + object_id)
ports = doc['ports']
port = ports[port_id]
if not port:
    logger.log.error('Port not found: ' + port_id)
port['status'] = STATUS_LABEL[status] # if status in range(0, 2) else 'Unknown'
port['status_value'] = status
port['status_text'] = check_result['output']

# set object status based on overall state of ports
status_list = [p['status'] for p in ports.values() if 'status' in p]
doc['status'] = \
    'Critical' if 'OK' not in status_list \
    else 'Warning' if 'Critical' in status_list or 'Warning' in status_list \
    else 'OK'

# set timestamp
check_time = gmtime(check_result['executed'])
port['status_timestamp'] = strftime(TIME_FORMAT, check_time)
inv.set(doc)
