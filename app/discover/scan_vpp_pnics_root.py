from scanner import Scanner
from singleton import Singleton


class ScanVppPnicsRoot(Scanner, metaclass=Singleton):
    def __init__(self):
        super().__init__([
            {
                "type": "pnic",
                "fetcher": "CliFetchHostPnicsVpp",
                "environment_condition": {"network_plugins": "VPP"},
                "children_scanner": "ScanOteps"
            }
        ])
