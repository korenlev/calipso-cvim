from discover.db_fetch_vedges_ovs import DbFetchVedgesOvs
from test.fetch.test_fetch import TestFetch
from test.fetch.db_fetch.test_data.db_fetch_vedges_ovs import *
from unittest.mock import MagicMock


class TestDbFetchVedgesOvs(TestFetch):

    def setUp(self):
        self.configure_environment()
        self.fetcher = DbFetchVedgesOvs()
        self.fetcher.set_env(self.env)

    def test_get(self):
        # store original methods
        original_get_objects_list_by_id = self.fetcher.get_objects_list_for_id
        original_get_by_id = self.fetcher.inv.get_by_id
        original_run_fetch_lines = self.fetcher.run_fetch_lines
        # mock methods
        self.fetcher.get_objects_list_for_id = MagicMock(return_value=AGENT)
        self.fetcher.inv.get_by_id = MagicMock(return_value=HOST)
        self.fetcher.run_fetch_lines = MagicMock(return_value=VSCTL_LINES)

        result = self.fetcher.get(VEDGES_FOLDER['id'])
        # reset methods
        self.fetcher.get_objects_list_for_id = original_get_objects_list_by_id
        self.fetcher.inv.get_by_id = original_get_by_id
        self.fetcher.run_fetch_lines = original_run_fetch_lines

        self.assertNotEqual(result, [], "Can't get vedges")

    def test_get_without_host(self):
        # store original methods
        original_get_objects_list_by_id = self.fetcher.get_objects_list_for_id
        original_get_by_id = self.fetcher.inv.get_by_id
        # mock methods
        self.fetcher.get_objects_list_for_id = MagicMock(return_value=AGENT)
        self.fetcher.inv.get_by_id = MagicMock(return_value=[])

        result = self.fetcher.get(VEDGES_FOLDER['id'])
        # reset methods
        self.fetcher.get_objects_list_for_id = original_get_objects_list_by_id
        self.fetcher.inv.get_by_id = original_get_by_id

        self.assertEqual(result, [], "Can't get empty array when the host is empty")

    def test_get_without_host_type(self):
        # store original methods
        original_get_objects_list_by_id = self.fetcher.get_objects_list_for_id
        original_get_by_id = self.fetcher.inv.get_by_id
        # mock methods
        self.fetcher.get_objects_list_for_id = MagicMock(return_value=AGENT)
        self.fetcher.inv.get_by_id = MagicMock(return_value=WRONG_HOST)

        result = self.fetcher.get(VEDGES_FOLDER['id'])
        # reset methods
        self.fetcher.get_objects_list_for_id = original_get_objects_list_by_id
        self.fetcher.inv.get_by_id = original_get_by_id

        self.assertEqual(result, [], "Can't get empty array when the host has no host type")

    def test_fetch_ports_from_dpctl(self):
        # store original methods
        original_run_fetch_lines = self.fetcher.run_fetch_lines
        # mock method
        self.fetcher.run_fetch_lines = MagicMock(return_value=DPCTL_LINES)

        results = self.fetcher.fetch_ports_from_dpctl(HOST['id'])
        # reset methods
        self.fetcher.run_fetch_lines = original_run_fetch_lines
        # check the result
        for port in results.values():
            self.assertIn("id", port, "Can't get id")
            self.assertIn("internal", port, "Can't get internal")
            self.assertIn("name", port, "Can't get name")

    def test_fetch_port_tags_from_vsctl(self):
        ports = self.fetcher.fetch_port_tags_from_vsctl(VSCTL_LINES, PORTS_BEFORE_TAGS)
        for name in VERIFY_TAGS:
            self.assertEqual(ports[name]['tag'], VERIFY_TAGS[name], "Tag is not correct")

    def test_fetch_ports(self):
        # store original method
        original_fetch_ports_from_dpctl = self.fetcher.fetch_ports_from_dpctl
        # mock methods
        self.fetcher.fetch_ports_from_dpctl = MagicMock(return_value=PORTS_BEFORE_TAGS)
        ports = self.fetcher.fetch_ports(HOST, VSCTL_LINES)

        # reset method
        self.fetcher.fetch_ports_from_dpctl = original_fetch_ports_from_dpctl
        self.assertNotEqual(ports, [], "Can't get ports")

    def test_get_overlay_tunnels(self):
        results = self.fetcher.get_overlay_tunnels(DOC_TO_GET_OVERLAY, VSCTL_LINES)
        self.assertEqual(results, tunnel_ports)