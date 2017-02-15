from discover.folder_fetcher import FolderFetcher
from discover.scanner import Scanner
from utils.singleton import Singleton


class ScanVedgePnicsRoot(Scanner, metaclass=Singleton):
    def __init__(self):
        super().__init__([
            {
                "type": "pnics_folder",
                "fetcher": FolderFetcher("pnics", "vedge", "pNICs"),
                "environment_condition": {"mechanism_drivers": "VPP"},
                "children_scanner": "ScanVppPnicsRoot"
            }
        ])
