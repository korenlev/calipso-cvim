from discover.folder_fetcher import FolderFetcher
from discover.scanner import Scanner
from discover.singleton import Singleton


class ScanNetwork(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanNetwork, self).__init__([
            {
                "type": "ports_folder",
                "fetcher": FolderFetcher("ports", "network")
            },
            {
                "type": "network_services_folder",
                "fetcher": FolderFetcher("network_services", "network", "Network vServices")
            }
        ])
