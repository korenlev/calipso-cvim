import unittest

from discover.configuration import Configuration
from discover.mongo_access import MongoAccess
from test.test_links.config.find_link_config import MONGODB_CONFIG, ENV_CONFIG
from discover.inventory_mgr import InventoryMgr



class TestFindLinks(unittest.TestCase):
    def setUp(self):
        MongoAccess()
        self.mongo_config = MONGODB_CONFIG
        self.env = ENV_CONFIG
        self.conf = Configuration(self.mongo_config)      
        self.db = MongoAccess.db
        self.inv = InventoryMgr()
        
        
    def is_test_passed(self):
        pass
    
    def is_test_failed(self):
        self.fail("Testcase Failed")
        
        
    def tearDown(self):
        """
            The tearDown() methods allow you to define instructions that will be executed after each test method.
         
        """
        self.db.logout() #logut the database