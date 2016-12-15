# scan a project for endpoints and regions
from discover.scanner import Scanner
from discover.singleton import Singleton


class ScanProject(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanProject, self).__init__([
            {
                "type": "availability_zone",
                "fetcher": "ApiFetchAvailabilityZones"
            },
            {
                "type": "host",
                "fetcher": "ApiFetchProjectHosts",
                "children_scanner": "ScanHost"
            }
        ])
