from discover.scanner import Scanner
from discover.singleton import Singleton


class ScanHostNetworkAgentsRoot(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanHostNetworkAgentsRoot, self).__init__([
            {
                "type": "network_agent",
                "fetcher": "DbFetchHostNetworkAgents"
            }
        ])
