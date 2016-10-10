# handle monitoring event for OTEP objects

from time import gmtime, strftime

from discover.inventory_mgr import InventoryMgr
from discover.logger import Logger

ENV = 'Mirantis-Liberty'
INVENTORY_COLLECTION = 'Mirantis-Liberty'
STATUS_LABEL = ['OK', 'Warning', 'Critical']
TIME_FORMAT = '%Y-%m-%d %H:%M:%S %Z'

class HandleOtep():

    def handle(self, id, check_result):
        object_id = id[:id.index('_')]
        port_id = id[id.index('_')+1:]
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
        status = check_result['status']
        port['status'] = STATUS_LABEL[status] 
        port['status_value'] = status
        port['status_text'] = check_result['output']
        
        # set object status based on overall state of ports
        status_list = [p['status'] for p in ports.values() if 'status' in p]
        doc['status'] = \
            'Critical' \
                 if 'OK' not in status_list \
            else 'Warning' \
                if 'Critical' in status_list or 'Warning' in status_list \
            else 'OK'

        # set timestamp
        check_time = gmtime(check_result['executed'])
        port['status_timestamp'] = strftime(TIME_FORMAT, check_time)
        inv.set(doc)
        return status


