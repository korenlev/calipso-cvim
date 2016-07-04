from singleton import Singleton
from scanner import Scanner

class ScanHostNetworkAgentsRoot(Scanner, metaclass=Singleton):

  def __init__(self):
    super(ScanHostNetworkAgentsRoot, self).__init__([
      {
        "type": "network_agent",
        "fetcher": "DbFetchHostNetworkAgents"
      }
    ])
