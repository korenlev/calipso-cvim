import json

from discover.fetcher import Fetcher
from utils.inventory_mgr import InventoryMgr


class KubeFetchOteps(Fetcher):

    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    FLANNEL_PREFIX = 'flannel.alpha.coreos.com/'
    PUBLIC_IP_KEY = FLANNEL_PREFIX + 'public-ip'
    BACKEND_TYPE = FLANNEL_PREFIX + 'backend-type'
    BACKEND_DATA = FLANNEL_PREFIX + 'backend-data'
    OTEP_MAC_ATTR = 'VtepMAC'
    OTEP_UDP_PORT = 8285

    def get(self, vedge_id) -> list:
        host_id = vedge_id.replace('-vedge', '')
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not host:
            self.log.error('failed to find host by ID: {}'.format(host_id))
            return []
        annotations = host.get('annotations', {})
        ip_address = annotations.get(self.PUBLIC_IP_KEY, '')
        overlay_type = annotations.get(self.BACKEND_TYPE, '')
        backend_data = json.loads(annotations.get(self.BACKEND_DATA, {}))
        otep_mac = backend_data.get(self.OTEP_MAC_ATTR, '')
        doc = {
            'id': '{}-otep'.format(host_id),
            'name': '{}-otep'.format(host['name']),
            'host': host['name'],
            'parent_type': 'vedge',
            'parent_id': '{}-vedge'.format(host_id),
            'ip_address': ip_address,
            'overlay_type': overlay_type,
            'overlay_mac_address': otep_mac,
            'ports': {},
            'udp_port': self.OTEP_UDP_PORT
        }
        return [doc]
