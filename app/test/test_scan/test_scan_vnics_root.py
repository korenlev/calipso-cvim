from OSDNA.app.discover.scan_vnics_root import ScanVnicsRoot
from OSDNA.app.discover.scanner import Scanner

from OSDNA.app.test_scan.test_scan import TestScan
from OSDNA.app.test_scan.test_data.scan_vnics_root import obj, id_field, child_id, child_type


class TestScanVnicsRoot(TestScan):

    def test_scan_vnics_root(self):

        self.scan_vnic = ScanVnicsRoot()

        self.scan = Scanner(self.scan_vnic.types_to_fetch)
        results = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertEqual(results, obj)

        # check environment
        type_of_environment = self.scan.check_type_env(self.scan_vnic.types_to_fetch)

        self.assertEqual(type_of_environment, True)