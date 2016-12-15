from discover.folder_fetcher import FolderFetcher
from discover.scanner import Scanner
from discover.singleton import Singleton


class ScanHost(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanHost, self).__init__([
            # creating only top folder for vServices, lower levels are categories
            # like gateways, DHCPs, etc., and they will be created
            # while fetching vservices, by specifying master_parent_id.
            #
            # this is necessary to allow fetch of vServices to happen
            # before fetch of vService vNICs
            {
                "type": "vservices_folder",
                "fetcher": FolderFetcher("vservices", "host"),
                "children_scanner": "ScanInstancesRoot"
            },
            {
                "type": "vservice",
                "fetcher": "CliFetchHostVservices"
            },
            # fetching of vService vNICs is done from host for efficiency
            {
                "type": "vnic",
                "environment_condition": {"mechanism_drivers": "OVS"},
                "fetcher": "CliFetchVserviceVnicsOvs"
            },
            {
                "type": "vnic",
                "environment_condition": {"mechanism_drivers": "VPP"},
                "fetcher": "CliFetchVserviceVnicsVpp"
            },
            {
                "type": "instances_folder",
                "fetcher": FolderFetcher("instances", "host"),
                "children_scanner": "ScanInstancesRoot"
            },
            {
                "type": "pnics_folder",
                "fetcher": FolderFetcher("pnics", "host", "pNICs"),
                "environment_condition": {"mechanism_drivers": "OVS"},
                "children_scanner": "ScanPnicsRoot"
            },
            {
                "type": "vconnectors_folder",
                "fetcher": FolderFetcher("vconnectors", "host", "vConnectors"),
                "children_scanner": "ScanVconnectorsRoot"
            },
            {
                "type": "vedges_folder",
                "fetcher": FolderFetcher("vedges", "host", "vEdges"),
                "children_scanner": "ScanVedgesRoot"
            },
            {
                "type": "network_agents_folder",
                "fetcher": FolderFetcher("network_agents", "host",
                                         "Network agents"),
                "children_scanner": "ScanHostNetworkAgentsRoot"
            }
        ])
