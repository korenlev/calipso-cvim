#!/usr/bin/env python3

# handle monitoring events

import json
import sys
from time import gmtime, strftime

from inventory_mgr import InventoryMgr
from logger import Logger

ENV = 'Mirantis-Liberty'
INVENTORY_COLLECTION = 'Mirantis-Liberty'
STATUS_LABEL = ['OK', 'Warning', 'Critical']
TIME_FORMAT = '%Y-%m-%d %H:%M:%S %Z'

check_result = json.loads(sys.stdin.read())
check_result = check_result['check']
name = check_result['name']
status = check_result['status']
object_id = name[:name.index('_')]
port_id = name[name.index('_')+1:]
logger = Logger()
logger.set_loglevel('WARN')
inv = InventoryMgr()
inv.set_inventory_collection(INVENTORY_COLLECTION)
doc = inv.get_by_id(ENV, object_id)
if not doc:
    loggger.log.warn('No matching object found with ID: ' + object_id)
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
