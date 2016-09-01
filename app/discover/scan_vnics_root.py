from scanner import Scanner
from singleton import Singleton


class ScanVnicsRoot(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanVnicsRoot, self).__init__([
            {
                "type": "vnic",
                "environment_condition": {"network_plugins": "OVS"},
                "fetcher": "CliFetchInstanceVnicsOvs"
            },
            {
                "type": "vnic",
                "environment_condition": {"network_plugins": "VPP"},
                "fetcher": "CliFetchInstanceVnicsVpp"
            }
        ])
