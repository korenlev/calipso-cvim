from discover.scanner import Scanner
from discover.singleton import Singleton


class ScanOteps(Scanner, metaclass=Singleton):
    def __init__(self):
        super().__init__([
            {
                "type": "otep",
                "fetcher": "DbFetchOteps"
            }
        ])
