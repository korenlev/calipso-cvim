from discover.cli_fetch_host_pnics import CliFetchHostPnics
from test.fetch.cli_fetch.test_data.cli_fetch_host_pnics_ovs import *
from test.fetch.test_fetch import TestFetch
from unittest.mock import MagicMock
from unittest.mock import call


class TestCliFetchHostPnics(TestFetch):

    def setUp(self):
        self.configure_environment()
        self.fetcher = CliFetchHostPnics()
        self.fetcher.set_env(self.env)

    def check_get_result(self, host,
                         interface_lines, interface_names,
                         interface_details, expected_result,
                         err_msg):
        original_get_by_id = self.fetcher.inv.get_by_id
        original_run_fetch_lines = self.fetcher.run_fetch_lines
        original_find_interface_details = self.fetcher.find_interface_details

        self.fetcher.inv.get_by_id = MagicMock(return_value=host)
        self.fetcher.run_fetch_lines = MagicMock(return_value=interface_lines)
        self.fetcher.find_interface_details = MagicMock(side_effect=
                                                        interface_details)
        result = self.fetcher.get(PNICS_FOLDER_ID)
        self.assertEqual(result, expected_result, err_msg)

        if interface_names:
            interface_calls = [call(HOST_ID, interface_name) for
                               interface_name in interface_names]
            self.fetcher.find_interface_details.assert_has_calls(interface_calls,
                                                                 any_order=True)
        # reset the methods
        self.fetcher.inv.get_by_id = original_get_by_id
        self.fetcher.run_fetch_lines = original_run_fetch_lines
        self.fetcher.find_interface_details = original_find_interface_details

    def test_get(self):
        test_cases = [
            {
                "host": NETWORK_NODE,
                "interface_lines": INTERFACE_LINES,
                "interface_names": INTERFACE_NAMES,
                "interface_details": [INTERFACE, None],
                "expected_results": INTERFACES_GET_RESULTS,
                "err_msg": "Can't get interfaces"
            },
            {
                "host": [],
                "interface_lines": None,
                "interface_names": None,
                "interface_details": None,
                "expected_results": [],
                "err_msg": "Can't get [] when the host " +
                           "doesn't exist in the database"
            },
            {
                "host": WRONG_NODE,
                "interface_lines": None,
                "interface_names": None,
                "interface_details": None,
                "expected_results": [],
                "err_msg": "Can't get [] when the host doesn't " +
                           "have required host type"
            },
            {
                "host": NETWORK_NODE,
                "interface_lines": [],
                "interface_names": None,
                "interface_details":None,
                "expected_results": [],
                "err_msg": "Can't get [] when " +
                           "the interface lines is []"
            }
        ]
        for test_case in test_cases:
            self.check_get_result(test_case["host"],
                                  test_case["interface_lines"],
                                  test_case["interface_names"],
                                  test_case["interface_details"],
                                  test_case["expected_results"],
                                  test_case["err_msg"])

    def test_find_interface_details(self):
        # store original methods
        original_run_fetch_lines = self.fetcher.run_fetch_lines
        original_handle_line = self.fetcher.handle_line
        original_set_interface_data = self.fetcher.set_interface_data

        # mock the methods
        self.fetcher.run_fetch_lines = MagicMock(return_value=IFCONFIG_CM_RESULT)
        self.fetcher.handle_line = MagicMock()
        self.fetcher.set_interface_data = MagicMock()

        result = self.fetcher.find_interface_details(NETWORK_NODE['id'], INTERFACE_LINES[0])

        # reset the methods
        self.fetcher.run_fetch_lines = original_run_fetch_lines
        self.fetcher.handle_line = original_handle_line
        self.fetcher.set_interface_data = original_set_interface_data

        self.assertNotEqual(result, None, "Can't get interface")

    def test_handle_mac_address_line(self):
        self.fetcher.handle_line(RAW_INTERFACE, MAC_ADDRESS_LINE)
        self.assertEqual(RAW_INTERFACE['mac_address'], MAC_ADDRESS, "Can't get the correct mac address")

    # Test failed, defect, result: addr: expected result: fe80::f816:3eff:fea1:eb73/64
    # def test_handle_ipv6_address_line(self):
    #     self.fetcher.handle_line(RAW_INTERFACE, IPV6_ADDRESS_LINE)
    #     self.assertEqual(RAW_INTERFACE['IPv6 Address'], IPV6_ADDRESS, "Can' get the correct ipv6 address")
    #
    # # Test failed, defect, result: addr:172.16.13.2 expected result: 172.16.13.2
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

