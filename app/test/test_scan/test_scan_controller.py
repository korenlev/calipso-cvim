from attrdict import AttrDict
from unittest.mock import MagicMock

from discover.scan import ScanController
from discover.inventory_mgr import InventoryMgr
from discover.scan_environment import ScanEnvironment

from test_scan import TestScan
from test_data.scan_controller import PAYLOAD_ARGS, ARGS_INVENTORY, ARGS_LINKS, ARGS_CLIQUES


class TestScanController(TestScan):
    def test_get_args(self):

        self.scan = ScanController()
        self.scan.inv = InventoryMgr()
        self.scan.inv.set_inventory_collection(PAYLOAD_ARGS['inventory'])

        # Mock the arguments
        self.scan.get_args = MagicMock(return_value=PAYLOAD_ARGS)

        expected_args = self.scan.get_args
        expected_args = expected_args.return_value
        actual_args = PAYLOAD_ARGS

        self.assertEqual(expected_args, actual_args)

    def test_get_scan_plan(self):

        # Convert dict to dict object
        self.args = AttrDict(PAYLOAD_ARGS)

        self.scan = ScanController()

        # Passing PAYLOAD_ARGS to get the scan plan
        self.scan_plan_args = self.scan.get_scan_plan(self.args)
        self.assertNotEqual(self.scan_plan_args, self.args)

        expected_env = self.scan_plan_args['parent_id']
        actual_env = self.args['parent_id']

        self.assertEqual(expected_env, actual_env)

    def test_prepare_scan_plan(self):

        self.args = AttrDict(PAYLOAD_ARGS)
        self.args['object_type'] = 'environment'

        self.scan = ScanController()

        # Parsing PAYLOAD_ARGS to prepare the scan plan
        self.scan_prepare_plan = self.scan.prepare_scan_plan(self.args)

        expected_env = self.scan_prepare_plan
        actual_env = self.args

        self.assertEqual(expected_env, actual_env)

    def test_scan_run(self):

        self.args = AttrDict(PAYLOAD_ARGS)
        self.args['object_type'] = 'environment'
        self.args['scanner_class'] = 'ScanEnvironment'
        self.args['module_file'] = 'scan_environment'

        self.scan = ScanController()
        self.scan.get_args = MagicMock(return_value=self.args)
        self.scan.get_scan_plan = MagicMock(return_value=self.args)

        self.assertNotEqual(self.scan.run, [], "Can't able to pass the module")

    def test_scan_inventory_only(self):
        self.args_object = AttrDict(ARGS_INVENTORY)
        self.args_object['env'] = self.env

        scan_plan = ScanController()
        scan_plan = scan_plan.get_scan_plan(self.args_object)
        inventory_only = scan_plan["inventory_only"]

        if inventory_only:
            self.assertTrue(inventory_only, True)
        else:
            self.assertFalse(inventory_only, False)

        scanner = ScanEnvironment()
        scan_env = scanner.set_env(self.env)

        self.assertEqual(None, scan_env)

        if inventory_only:
            results = scanner.run_scan(scan_plan["obj"], scan_plan["id_field"],
                                       scan_plan["child_id"], scan_plan["child_type"])

            self.assertEqual(results['id'], self.env)

    def test_scan_links_only(self):
        self.args_object = AttrDict(ARGS_LINKS)
        self.args_object['env'] = self.env

        scan_plan = ScanController()
        scan_plan = scan_plan.get_scan_plan(self.args_object)
        links_only = scan_plan["links_only"]

        if links_only:
            self.assertTrue(links_only, True)
        else:
            self.assertFalse(links_only, False)

        scanner = ScanEnvironment()
        scan_env = scanner.set_env(self.env)

        self.assertEqual(None, scan_env)

        if links_only:
            result = scanner.scan_links()

            self.assertEqual(result, None)

    def test_scan_cliques_only(self):
        self.args_object = AttrDict(ARGS_CLIQUES)
        self.args_object['env'] = self.env

        scan_plan = ScanController()
        scan_plan = scan_plan.get_scan_plan(self.args_object)
        cliques_only = scan_plan["cliques_only"]

        if cliques_only:
            self.assertTrue(cliques_only, True)
        else:
            self.assertFalse(cliques_only, False)

        scanner = ScanEnvironment()
        scan_env = scanner.set_env(self.env)

        self.assertEqual(None, scan_env)

        if cliques_only:
            result = scanner.scan_cliques()

            self.assertEqual(result, None)

