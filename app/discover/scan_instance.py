# scan a host for instances
from discover.folder_fetcher import FolderFetcher
from discover.scanner import Scanner
from utils.singleton import Singleton


class ScanInstance(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanInstance, self).__init__([
            {
                "type": "vnics_folder",
                "fetcher": FolderFetcher("vnics", "instance", "vNICs"),
                "children_scanner": "ScanVnicsRoot"
            }
        ])
