from discover.fetcher import Fetcher
from discover.inventory_mgr import InventoryMgr
from discover.scan_host import ScanHost
from discover.scan_instances_root import ScanInstancesRoot


class EventInstanceAdd(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def handle(self, env, values):
        # find the host, to serve as parent
        instance_id = values['instance_id']
        host_id = values['host']
        instances_root_id = host_id + '-instances'
        instances_root = self.inv.get_by_id(env, instances_root_id)
        if not instances_root:
            self.log.info('instances root not found, aborting instance add')
            return None

        # scan instance
        instances_scanner = ScanInstancesRoot()
        instances_scanner.set_env(env)
        instances_scanner.scan(instances_root,
                               limit_to_child_id=instance_id, limit_to_child_type='instance')
        instances_scanner.scan_from_queue()

        # scan host
        host = self.inv.get_by_id(env, host_id)
        host_scanner = ScanHost()
        host_scanner.scan(host,
                          limit_to_child_type=['vconnectors_folder', 'vedges_folder'])
        host_scanner.scan_from_queue()
        host_scanner.scan_links()
        host_scanner.scan_cliques()
