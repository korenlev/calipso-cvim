from discover.scanner import Scanner
from discover.singleton import Singleton


class ScanVedgesRoot(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanVedgesRoot, self).__init__([
            {
                "type": "vedge",
                "fetcher": "DbFetchVedgesOvs",
                "environment_condition": {"mechanism_drivers": "OVS"},
                "children_scanner": "ScanOteps"
            },
            {
                "type": "vedge",
                "fetcher": "DbFetchVedgesVpp",
                "environment_condition": {"mechanism_drivers": "VPP"},
                "children_scanner": "ScanVedgePnicsRoot"
            }
        ])
