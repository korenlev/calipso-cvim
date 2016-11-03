import unittest

from unittest.mock import MagicMock
from discover.find_links_for_pnics import FindLinksForPnics
from discover.fetcher import Fetcher
from test.test_links.test_data import mock_data
from test.test_links.find_parent import TestFindLinks
from discover.inventory_mgr import InventoryMgr

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestFindLinksForPnics(TestFindLinks):

    """
        Unittest for FindLinksForPnics

    """
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestFindLinksForPnics, self).setUp()
        self.inv = InventoryMgr()
        self.inv.set_inventory_collection()  #inorder to avoid attribute error, this method is invoked
        self.pnics = FindLinksForPnics()
        Fetcher.env = mock_data.oteps_env


    def test_add_links(self):
        """
            Testing the add links
        """
        logger.info("Testing the add links")
        try:
            self.pnics.add_pnic_network_links = MagicMock()  #mock the add_pnic_network_links()
            self.inv.find_items = MagicMock(return_value = mock_data.pnics_find_items) #mock the find items value
            self.pnics.add_links() #calling the add_links()
        except:
            self.is_test_failed()
          
     
    def test_add_pnic_network_links(self):
        """
            Testcase: add pnic network links - normal case
        """
        logger.info("Testing add pnic network links - normal case")
        self.inv.find_items=MagicMock(return_value=mock_data.pnics_ports) #mocked the value
        self.inv.get_by_id= MagicMock(return_value=mock_data.pnics_network) #mocked the value
        try:
            for pnic in mock_data.pnics_find_items:
                self.db.links.remove() #cleanup the links table
                self.pnics.add_pnic_network_links(pnic)
                links_count = self.db.links.find().count() #cross verify the database
                if not links_count:
                    self.is_test_failed()
        except:
            self.is_test_failed()
            
 
    def test_add_pnic_network_links_for_empty_ports(self):
        """
            Testcase: add pnic network links - empty ports
        """
        logger.info("Testing add pnic network links - empty ports")
        self.inv.find_items=MagicMock(return_value=[])
        try:
            for pnic in mock_data.pnics_find_items:
                self.db.links.remove() #cleanup the links table
                self.pnics.add_pnic_network_links(pnic)
                links_count = self.db.links.find().count() #cross verify the database
                if links_count:
                    self.is_test_failed() #for this case,no record is not created
        except:
            self.is_test_failed()
            

    def test_add_pnic_network_links_for_empty_network(self):
        """
            Testcase: add pnic network links - empty network
        """
        logger.info("Testing add pnic network links - empty network")
        self.inv.get_by_id=MagicMock(return_value=[])
        try:
            for pnic in mock_data.pnics_find_items:
                self.db.links.remove() #cleanup the links table
                self.pnics.add_pnic_network_links(pnic)
                links_count = self.db.links.find().count() #cross verify the database
                if links_count:
                    self.is_test_failed() #for this case,no record is not created
        except:
            pass #except be called for this testcase           
 

if __name__ == '__main__':
    unittest.main()
