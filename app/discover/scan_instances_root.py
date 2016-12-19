from discover.scanner import Scanner
from discover.singleton import Singleton


class ScanInstancesRoot(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanInstancesRoot, self).__init__([
            {
                "type": "instance",
                "fetcher": "ApiFetchHostInstances",
                "children_scanner": "ScanInstance"
            }
        ])
