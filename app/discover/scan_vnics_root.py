from discover.scanner import Scanner
from discover.singleton import Singleton


class ScanVnicsRoot(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanVnicsRoot, self).__init__([
            {
                "type": "vnic",
                "environment_condition": {"mechanism_drivers": ["OVS", "LXB"]},
                "fetcher": "CliFetchInstanceVnics"
            },
            {
                "type": "vnic",
                "environment_condition": {"mechanism_drivers": "VPP"},
                "fetcher": "CliFetchInstanceVnicsVpp"
            }
        ])
