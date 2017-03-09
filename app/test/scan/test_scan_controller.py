import sys
import os

from unittest.mock import MagicMock, patch
from test.scan.test_scan import TestScan
from test.scan.test_data.scan import *
from discover.scan import ScanController
from test.scan import mock_module
from test.scan.mock_module import ScanEnvironment


class TestScanController(TestScan):

    def setUp(self):
        self.configure_environment()
        self.scan_controller = ScanController()
        sys.modules[MODULE_NAME_FOR_IMPORT] = mock_module

    def check_args_values(self, args, arguments):
        self.assertEqual(args.cgi, arguments['CGI'], "The value of cgi is wrong")
        self.assertEqual(args.mongo_config, arguments['MONGO_CONFIG'],
                         "The value of mongo_config is wrong")
        self.assertEqual(args.env, arguments['ENV'], "The value of environment is wrong")
        self.assertEqual(args.type, arguments['TYPE'], "The value of type is wrong")
        self.assertEqual(args.inventory, arguments['INVENTORY'], "The value of inventory si wrong")
        self.assertEqual(args.scan_self, arguments['SCAN_SELF'], "The value of scan_self is wrong")
        self.assertEqual(args.id, arguments['ID'], "The value of id is wrong")
        self.assertEqual(args.parent_id, arguments['PARENT_ID'], 'The value of parent_id  is wrong')
        self.assertEqual(args.parent_type, arguments['PARENT_TYPE'], "The value of parent_type is wrong")
        self.assertEqual(args.id_field, arguments['ID_FIELD'], "The value of id_field is wrong")
        self.assertEqual(args.loglevel, arguments['LOGLEVEL'], "The value of loglevel is wrong")
        self.assertEqual(args.inventory_only, arguments['INVENTORY_ONLY'],"The value of inventory_only is wrong")
        self.assertEqual(args.links_only, arguments['LINKS_ONLY'], "The value of links_only is wrong")
        self.assertEqual(args.cliques_only, arguments['CLIQUES_ONLY'], "The value of cliques_only is wrong")
        self.assertEqual(args.clear, arguments['CLEAR'], "The value of clear is wrong")

    def test_get_args_with_default_arguments(self):
        sys.argv = DEFAULT_COMMAND_ARGS
        args = self.scan_controller.get_args()
        # check the default value of each argument
        self.check_args_values(args, DEFAULT_ARGUMENTS)

    def test_get_args_with_short_command_args(self):
        sys.argv = SHORT_COMMAND_ARGS
        args = self.scan_controller.get_args()
        # check the value parsed by short arguments
        self.check_args_values(args, ARGUMENTS)

    def test_get_args_with_full_command_args(self):
        sys.argv = LONG_COMMAND_ARGS
        args = self.scan_controller.get_args()
        # check the value parsed by long arguments
        self.check_args_values(args, ARGUMENTS)

    def side_effect(self, key, default):
        if key in FORM.keys():
            return FORM[key]
        else:
            return default

    # there may be a possible defect here after change in the source code, should change the test data
    @patch("cgi.FieldStorage.getvalue")
    def test_get_scan_object_from_cgi(self, get_value):
        original_prepare_scan_plan = self.scan_controller.prepare_scan_plan

        get_value.side_effect = self.side_effect
        self.scan_controller.prepare_scan_plan = MagicMock()

        self.scan_controller.get_scan_object_from_cgi()
        self.scan_controller.prepare_scan_plan.assert_called_once_with(CGI_PLAN)

        self.scan_controller.prepare_scan_plan = original_prepare_scan_plan

    @patch.dict(os.environ, {"REQUEST_METHOD": "POST"})
    def test_get_scan_plan_with_request_method(self):
        original_get_scan_object_from_cgi = self.scan_controller.get_scan_object_from_cgi
        original_prepare_scan_plan = self.scan_controller.prepare_scan_plan

        self.scan_controller.get_scan_object_from_cgi = MagicMock()
        self.scan_controller.prepare_scan_plan = MagicMock()

        sys.argv = LONG_COMMAND_ARGS
        args = self.scan_controller.get_args()
        self.scan_controller.get_scan_plan(args)

        self.scan_controller.get_scan_object_from_cgi.assert_any_call()
        self.scan_controller.prepare_scan_plan.assert_not_called()

        self.scan_controller.get_scan_object_from_cgi = original_get_scan_object_from_cgi
        self.scan_controller.prepare_scan_plan = original_prepare_scan_plan

    def test_get_scan_plan_without_request_method(self):
        original_get_scan_object_from_cgi = self.scan_controller.get_scan_object_from_cgi
        original_prepare_scan_plan = self.scan_controller.prepare_scan_plan

        self.scan_controller.get_scan_object_from_cgi = MagicMock()
        self.scan_controller.prepare_scan_plan = MagicMock()

        sys.argv = LONG_COMMAND_ARGS
        args = self.scan_controller.get_args()
        self.scan_controller.get_scan_plan(args)

        self.scan_controller.get_scan_object_from_cgi.assert_not_called()
        self.assertEqual(self.scan_controller.prepare_scan_plan.call_count, 1)

        self.scan_controller.get_scan_object_from_cgi = original_get_scan_object_from_cgi
        self.scan_controller.prepare_scan_plan = original_prepare_scan_plan

    def check_plan_values(self, plan, scanner_class, module_file, obj_id,
                          child_type, child_id):
        self.assertEqual(plan['scanner_class'], scanner_class, "The scanner class is wrong")
        self.assertEqual(plan['module_file'], module_file, "The module file is wrong")
        self.assertEqual(plan['child_type'], child_type, "The child type is wrong")
        self.assertEqual(plan['child_id'], child_id, "The child id is wrong")
        self.assertEqual(plan['object_id'], obj_id, "The object is wrong")

    def test_prepare_scan_plan(self):
        plan = self.scan_controller.prepare_scan_plan(SCAN_ENV_PLAN_TO_BE_PREPARED)
        self.check_plan_values(plan, SCANNER_CLASS_FOR_ENV, MODULE_FILE_FOR_ENV,
                               OBJ_ID_FOR_ENV, CHILD_TYPE_FOR_ENV,
                               CHILD_ID_FOR_ENV)

    def test_prepare_scan_region_plan(self):
        original_get_by_id = self.inv.get_by_id
        self.inv.get_by_id = MagicMock(return_value=REGIONS_FOLDER)

        self.scan_controller.inv = self.inv
        plan = self.scan_controller.prepare_scan_plan(SCAN_REGION_PLAN_TO_BE_PREPARED)

        self.check_plan_values(plan, SCANNER_CLASS_FOR_REGION, MODULE_FILE_FOR_REGION,
                               OBJ_ID_FOR_REGION, CHILD_TYPE_FOR_REGION,
                               CHILD_ID_FOR_REGION)
        self.inv.get_by_id = original_get_by_id

    def test_prepare_scan_region_folder_plan(self):
        plan = self.scan_controller.prepare_scan_plan(SCAN_PROJECT_FOLDER_PLAN_TO_BE_PREPARED)
        self.check_plan_values(plan, SCANNER_CLASS_FOR_REGION_FOLDER, MODULE_FILE_FOR_REGION_FOLDER,
                               OBJ_ID_FOR_REGION_FOLDER, CHILD_TYPE_FOR_REGION_FOLDER,
                               CHILD_ID_FOR_REGION_FOLDER)

    def check_scan_counts(self, run_scan_count, scan_cliques_count, scan_links_count):
        self.assertEqual(ScanEnvironment.run_scan_count, run_scan_count, "run_scan count is wrong")
        self.assertEqual(ScanEnvironment.scan_cliques_count, scan_cliques_count, "scan_cliques count is wrong")
        self.assertEqual(ScanEnvironment.scan_links_count, scan_links_count, "scan_links count is wrong")

    def test_scan(self):
        self.scan_controller.get_args = MagicMock()
        self.scan_controller.get_scan_plan = MagicMock(return_value=PREPARED_ENV_PLAN)

        self.scan_controller.run()
        self.check_scan_counts(1, 1, 1)
        ScanEnvironment.reset_counts()

    def test_scan_with_inventory_only(self):
        self.scan_controller.get_args = MagicMock()
        self.scan_controller.get_scan_plan = MagicMock(return_value=PREPARED_ENV_INVENTORY_ONLY_PLAN)

        self.scan_controller.run()
        self.check_scan_counts(1, 0, 0)
        ScanEnvironment.reset_counts()

    def test_scan_with_links_only(self):
        self.scan_controller.get_args = MagicMock()
        self.scan_controller.get_scan_plan = MagicMock(return_value=PREPARED_ENV_LINKS_ONLY_PLAN)

        self.scan_controller.run()
        self.check_scan_counts(0, 0, 1)
        ScanEnvironment.reset_counts()

    def test_scan_with_cliques_only(self):
        self.scan_controller.get_args = MagicMock()
        self.scan_controller.get_scan_plan = MagicMock(return_value=PREPARED_ENV_CLIQUES_ONLY_PLAN)

        self.scan_controller.run()
        self.check_scan_counts(0, 1, 0)
        ScanEnvironment.reset_counts()

    def tearDown(self):
        del sys.modules[MODULE_NAME_FOR_IMPORT]