from discover.scanner import Scanner
from discover.singleton import Singleton


class ScanVconnectorsRoot(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanVconnectorsRoot, self).__init__([
            {
                "type": "vconnector",
                "environment_condition": {"network_plugins": "OVS"},
                "fetcher": "CliFetchVconnectorsOvs"
            },
            {
                "type": "vconnector",
                "environment_condition": {"network_plugins": "VPP"},
                "fetcher": "CliFetchVconnectorsVpp"
            }
        ])
