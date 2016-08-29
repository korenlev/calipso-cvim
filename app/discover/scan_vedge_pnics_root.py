from folder_fetcher import FolderFetcher
from scanner import Scanner
from singleton import Singleton


class ScanVedgePnicsRoot(Scanner, metaclass=Singleton):
    def __init__(self):
        super().__init__([
            {
                "type": "pnics_folder",
                "fetcher": FolderFetcher("pnics", "vedge", "pNICs"),
                "environment_condition": {"network_plugins": "VPP"},
                "children_scanner": "ScanVppPnicsRoot"
            }
        ])
