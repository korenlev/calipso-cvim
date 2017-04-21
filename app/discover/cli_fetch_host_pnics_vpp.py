import re

from discover.fetcher import Fetcher
from utils.inventory_mgr import InventoryMgr

NAME_RE = '^[a-zA-Z]*GigabitEthernet'

class CliFetchHostPnicsVpp(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()
        self.name_re = re.compile(NAME_RE)

    def get(self, id):
        host_id = id[:id.rindex("-")]
        host_id = id[:host_id.rindex("-")]
        vedges = self.inv.find_items({
            "environment": self.get_env(),
            "type": "vedge",
            "host": host_id
        })
        ret = []
        for vedge in vedges:
            pnic_ports = vedge['ports']
            for pnic_name in pnic_ports:
                if not self.name_re.search(pnic_name):
                    continue
                pnic = pnic_ports[pnic_name]
                pnic['host'] = host_id
                pnic['id'] = host_id + "-pnic-" + pnic_name
                pnic['type'] = 'pnic'
                pnic['object_name'] = pnic_name
                pnic['Link detected'] = 'yes' if pnic['state'] == 'up' else 'no'
                ret.append(pnic)
        return ret
