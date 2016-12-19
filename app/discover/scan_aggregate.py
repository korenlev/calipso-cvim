# scan a host aggregate for hosts
from discover.scanner import Scanner
from discover.singleton import Singleton


class ScanAggregate(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanAggregate, self).__init__([
            {
                "type": "host_ref",
                "fetcher": "DbFetchAggregateHosts"
            }
        ])
