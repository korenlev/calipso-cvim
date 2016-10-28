from discover.scan_pnics_root import ScanPnicsRoot
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_pnics_root import obj, id_field, child_id, child_type


class TestSanPnicsRoot(TestScan):
    def test_scan_pnics_root(self):
        self.scan_pnic = ScanPnicsRoot()

        self.scan = Scanner(self.scan_pnic.types_to_fetch)
        results = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertEqual(results, obj)

        # check environment
        type_of_environment = self.scan.check_type_env(self.scan_pnic.types_to_fetch)

        self.assertEqual(type_of_environment, True)
