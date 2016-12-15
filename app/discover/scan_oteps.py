from discover.scanner import Scanner
from discover.singleton import Singleton


class ScanOteps(Scanner, metaclass=Singleton):
    def __init__(self):
        super().__init__([
            {
                "type": "otep",
                "environment_condition": {"mechanism_drivers": "OVS"},
                "fetcher": "DbFetchOteps"
            },
            {
                "type": "otep",
                "environment_condition": {"mechanism_drivers": "VPP"},
                "fetcher": "DbFetchOteps"
            },
            {
                "type": "otep",
                "environment_condition": {"mechanism_drivers": "LXB"},
                "fetcher": "CliFetchOtepsLxb"
            }
        ])
