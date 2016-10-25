from discover.cli_fetch_host_pnics_ovs import CliFetchHostPnicsOvs
from test.fetch.cli_fetch.test_data.cli_fetch_host_pnics_ovs import *
from test.fetch.test_fetch import TestFetch
from unittest.mock import MagicMock


class TestCliFetchHostPnicsOvs(TestFetch):

    def setUp(self):
        self.configure_environment()
        self.fetcher = CliFetchHostPnicsOvs()
        self.fetcher.set_env(self.env)

    def test_get(self):
        # store original methods
        original_get_by_id = self.fetcher.inv.get_by_id
        original_run_fetch_lines = self.fetcher.run_fetch_lines
        original_find_interface_details = self.fetcher.find_interface_details

        # mock the methods
        self.fetcher.inv.get_by_id = MagicMock(return_value=NETWORK_NODE)
        self.fetcher.run_fetch_lines = MagicMock(return_value=INTERFACES_NAMES)
        self.fetcher.find_interface_details = MagicMock(return_value=INTERFACE)

        result = self.fetcher.get(PNICS_FOLDER["id"])

        # reset the methods
        self.fetcher.inv.get_by_id = original_get_by_id
        self.fetcher.run_fetch_lines = original_run_fetch_lines
        self.fetcher.find_interface_details = original_find_interface_details

        self.assertNotEqual(result, [], "Can't get pnics info")

    def test_get_with_wrong_host_type_node(self):
        # store original methods
        original_get_by_id = self.fetcher.inv.get_by_id

        # mock the methods
        self.fetcher.inv.get_by_id = MagicMock(return_value=WRONG_NODE)

        result = self.fetcher.get(PNICS_FOLDER["id"])

        # reset the methods
        self.fetcher.inv.get_by_id = original_get_by_id

        self.assertEqual(result, [], "Can't get empty array when the host_type contains neither Compute and Network")

    def test_find_interface_details(self):
        # store original methods
        original_run_fetch_lines = self.fetcher.run_fetch_lines
        original_handle_line = self.fetcher.handle_line
        original_set_interface_data = self.fetcher.set_interface_data

        # mock the methods
        self.fetcher.run_fetch_lines = MagicMock(return_value=IFCONFIG_CM_RESULT)
        self.fetcher.handle_line = MagicMock()
        self.fetcher.set_interface_data = MagicMock()

        result = self.fetcher.find_interface_details(NETWORK_NODE['id'], INTERFACES_NAMES[0])

        # reset the methods
        self.fetcher.run_fetch_lines = original_run_fetch_lines
        self.fetcher.handle_line = original_handle_line
        self.fetcher.set_interface_data = original_set_interface_data

        self.assertNotEqual(result, None, "Can't get interface")

    def test_handle_mac_address_line(self):
        self.fetcher.handle_line(RAW_INTERFACE, MAC_ADDRESS_LINE)
        self.assertEqual(RAW_INTERFACE['mac_address'], MAC_ADDRESS, "Can't get the correct mac address")

    # Test failed, defect, result: addr: expected result: 00:50:56:ac:e8:97
    # def test_handle_ipv6_address_line(self):
    #     self.fetcher.handle_line(RAW_INTERFACE, IPV6_ADDRESS_LINE)
    #     self.assertEqual(RAW_INTERFACE['IPv6 Address'], IPV6_ADDRESS, "Can' get the correct ipv6 address")

    # Test failed, defect, result: addr:172.16.13.2 expected result: 172.16.13.2
    # def test_handle_ipv4_address_line(self):
    #     self.fetcher.handle_line(RAW_INTERFACE, IPV4_ADDRESS_LINE)
    #     self.assertEqual(RAW_INTERFACE['IP Address'], IPV4_ADDRESS, "Can't get the correct ipv4 address")

    def test_set_interface_data(self):
        # store the original methods
        original_run_fetch_lines = self.fetcher.run_fetch_lines
        # mock the method
        self.fetcher.run_fetch_lines = MagicMock(return_value=ETHTOOL_RESULT)

        self.fetcher.set_interface_data(INTERFACE_FOR_SET)

        # reset run_fetch_lines method
        self.fetcher.run_fetch_lines = original_run_fetch_lines

        self.assertEqual(INTERFACE_FOR_SET[TEST_ATTRIBUTE1], EXPECTED_VALUE1)
        self.assertEqual(INTERFACE_FOR_SET[TEST_ATTRIBUTE2], EXPECTED_VALUE2)

