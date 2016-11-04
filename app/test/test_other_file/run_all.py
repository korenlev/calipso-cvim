import unittest


from test.test_other_file import test_util
from test.test_other_file import test_singleton
from test.test_other_file import test_ssh_conn
from test.test_other_file import test_network_agents_list
from test.test_other_file import test_mongo_access
from test.test_other_file import test_logger
from test.test_other_file import test_inventory_mgr
from test.test_other_file import test_folder_fetcher
from test.test_other_file import test_fetcher
from test.test_other_file import test_fetch_region_object_types
from test.test_other_file import test_fetch_host_object_types
from test.test_other_file import test_event_listener
from test.test_other_file import test_configuration
from test.test_other_file import test_clique_finder
        
def suite():
        
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_util.TestUtil))
    suite.addTest(unittest.makeSuite(test_singleton.TestSingleton))   
    suite.addTest(unittest.makeSuite(test_ssh_conn.TestSshConn))
    suite.addTest(unittest.makeSuite(test_network_agents_list.TestNetworkAgentsList))
    suite.addTest(unittest.makeSuite(test_mongo_access.TestMongoAccess))
    suite.addTest(unittest.makeSuite(test_logger.TestLogger))
    suite.addTest(unittest.makeSuite(test_inventory_mgr.TestInventoryMgr))  
    suite.addTest(unittest.makeSuite(test_folder_fetcher.TestFolderFetcher))
    suite.addTest(unittest.makeSuite(test_fetcher.TestFetcher))
    suite.addTest(unittest.makeSuite(test_fetch_host_object_types.TestFetchHostObjectTypes))
    suite.addTest(unittest.makeSuite(test_fetch_region_object_types.TestFetchRegionObjectTypes))
    suite.addTest(unittest.makeSuite(test_event_listener.TestWorker))
    suite.addTest(unittest.makeSuite(test_configuration.TestConfiguration))
    suite.addTest(unittest.makeSuite(test_clique_finder.TestCliqueFinder))
    return suite
    
  
    

if '__main__' == __name__:
    Suite = suite()
    runner = unittest.TextTestRunner()
    runner.run(Suite) 