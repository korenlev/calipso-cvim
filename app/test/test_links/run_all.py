import unittest


from test.test_links import test_find_links_for_instance_vnics
from test.test_links import test_find_links_for_pnics
from test.test_links import test_find_links_for_vservice_vnic
from test.test_links import test_find_links_for_oteps
from test.test_links import test_find_links_for_vconnectors
from test.test_links import test_find_links_for_vedges

        
def suite():
        
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_find_links_for_instance_vnics.TestFindLinksForInstanceVnics))
    suite.addTest(unittest.makeSuite(test_find_links_for_pnics.TestFindLinksForPnics))
    suite.addTest(unittest.makeSuite(test_find_links_for_vservice_vnic.TestFindLinksForVServiceVnics))
    suite.addTest(unittest.makeSuite(test_find_links_for_oteps.TestFindLinksForOteps))
    suite.addTest(unittest.makeSuite(test_find_links_for_vconnectors.TestFindLinksForVconnectors))
    suite.addTest(unittest.makeSuite(test_find_links_for_vedges.TestFindLinksForVedges))    
    return suite


if '__main__' == __name__:
    Suite = suite()
    runner = unittest.TextTestRunner()
    runner.run(Suite) 