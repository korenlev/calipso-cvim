# scan a host for instances

from folder_fetcher import FolderFetcher
from scanner import Scanner
from singleton import Singleton


class ScanInstance(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanInstance, self).__init__([
            {
                "type": "vnics_folder",
                "fetcher": FolderFetcher("vnics", "instance", "vNICs"),
                "children_scanner": "ScanVnicsRoot"
            }
        ])
