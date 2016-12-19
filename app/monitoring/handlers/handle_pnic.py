# handle monitoring event for pNIC objects

from time import gmtime, strftime

from discover.inventory_mgr import InventoryMgr
from discover.logger import Logger

ENV = 'Mirantis-Liberty'
INVENTORY_COLLECTION = 'Mirantis-Liberty'
STATUS_LABEL = ['OK', 'Warning', 'Critical']
TIME_FORMAT = '%Y-%m-%d %H:%M:%S %Z'

class HandlePnic():

    def handle(self, id, check_result):
        object_id = id[:id.index('-')]
        mac = id[id.index('-')+1:]
        mac_address = '%s:%s:%s:%s:%s:%s' % \
            (mac[0:2], mac[2:4], mac[4:6], mac[6:8], mac[8:10], mac[10:12])
        object_id += '-' + mac_address
        logger = Logger()
        logger.set_loglevel('WARN')
        inv = InventoryMgr()
        inv.set_inventory_collection(INVENTORY_COLLECTION)
        doc = inv.get_by_id(ENV, object_id)
        if not doc:
            logger.log.warn('No matching object found with ID: ' + object_id)
        status = check_result['status']
        doc['status'] = STATUS_LABEL[status] 
        doc['status_value'] = status
        doc['status_text'] = check_result['output']
        

        # set timestamp
        check_time = gmtime(check_result['executed'])
        doc['status_timestamp'] = strftime(TIME_FORMAT, check_time)
        inv.set(doc)
        return status


