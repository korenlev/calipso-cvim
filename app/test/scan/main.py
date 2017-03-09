import unittest

from test.scan.test_scan_aggregate import TestScanAggregate
from test.scan.test_scan_aggregates_root import TestScanAggregatesRoot
from test.scan.test_scan_environment import TestScanEnvironment
from test.scan.test_scan_host import TestScanHost
from test.scan.test_scan_host_network_agents_root import TestScanHostNetworkAgentsRoot
from test.scan.test_scan_instance import TestScanInstance
from test.scan.test_scan_instances_root import TestScanInstanceRoot
from test.scan.test_scan_network import TestScanNetwork
from test.scan.test_scan_networks_root import TestScanInstancesRoot
from test.scan.test_scan_oteps import TestScanOteps
from test.scan.test_scan_pnics_root import TestScanPnicsRoot
from test.scan.test_scan_project import TestScanProject
from test.scan.test_scan_projects_root import TestScanProjectsRoot
from test.scan.test_scan_region import TestScanRegion
from test.scan.test_scan_regions_root import TestScanRegionsRoot
from test.scan.test_scan_vconnectors_root import TestScanVconnectorsRoot
from test.scan.test_scan_vedge_pnics_root import TestScanVedgePnicsRoot
from test.scan.test_scan_vedges_root import TestScanVedgesRoot
from test.scan.test_scan_vnics_root import TestScanVnicsRoot
from test.scan.test_scan_vpp_pnics_root import TestScanVppPnicsRoot

from test.scan.test_scanner import TestScanner
from test.scan.test_scan_controller import TestScanController

if __name__=='__main__':
    unittest.main()
