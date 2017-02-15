from discover.scanner import Scanner
from utils.singleton import Singleton


class ScanVppPnicsRoot(Scanner, metaclass=Singleton):
    def __init__(self):
        super().__init__([
            {
                "type": "pnic",
                "fetcher": "CliFetchHostPnicsVpp",
                "environment_condition": {"mechanism_drivers": "VPP"},
                "children_scanner": "ScanOteps"
            }
        ])
