# scan a region for availability zones and aggregates
from discover.folder_fetcher import FolderFetcher
from discover.scanner import Scanner
from utils.singleton import Singleton


class ScanRegion(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanRegion, self).__init__([
            {
                "type": "aggregates_folder",
                "fetcher": FolderFetcher("aggregates", "region"),
                "children_scanner": "ScanAggregatesRoot"
            },
            {
                "type": "network",
                "fetcher": "ApiFetchNetworks",
                "children_scanner": "ScanNetwork"
            },
            {
                "type": "port",
                "fetcher": "ApiFetchPorts"
            }
        ])
