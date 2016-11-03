import unittest
from unittest.mock import MagicMock

from discover.find_links_for_oteps import FindLinksForOteps
from test.test_links.test_data import mock_data
from test.test_links.find_parent import TestFindLinks
from discover.inventory_mgr import InventoryMgr

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestFindLinksForOteps(TestFindLinks):

    """
        Unittest for FindLinksForOteps

    """
    
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestFindLinksForOteps, self).setUp()
        self.inv = InventoryMgr()
        self.inv.set_inventory_collection()  #inorder to avoid attribute error, this method is invoked
        self.oteps = FindLinksForOteps()


    def test_add_links(self):
        """
            Testcase : Testing the add links
        """
        logger.info("Testing add links")
        try:
            self.oteps.add_vedge_otep_link = MagicMock()  #mock the add_pnic_network_links()
            self.oteps.add_otep_vconnector_link = MagicMock()  #mock the add_pnic_network_links()
            self.oteps.add_otep_pnic_link = MagicMock()  #mock the add_pnic_network_links()            
            self.inv.find_items = MagicMock(return_value = mock_data.otep_find_items) #mock the find items value
            self.oteps.add_links() #calling the add_links()
        except:
            self.is_test_failed()
            
          
    def test_add_vedge_otep_link(self):
        """
            Testcase : add vedge otep link-normal case
        """
        logger.info("Testing add vedge otep link-normal case")
        self.inv.get_by_id=MagicMock(return_value=mock_data.otep_link_vedge)
        try:
            for otep in mock_data.otep_find_items:
                self.db.links.remove() #cleanup the links table
                self.oteps.add_vedge_otep_link(otep)
                links_count = self.db.links.find().count() #cross verify the database
                if not links_count:
                    self.is_test_failed()
        except:
            self.is_test_failed() 
             
 
    def test_add_vedge_otep_link_empty_vedge(self):
        """
            Testcase : add vedge otep link for empty vedge
        """
        logger.info("Testing add vedge otep link for empty vedge")
        self.inv.get_by_id=MagicMock(return_value=[])
        try:
            for otep in mock_data.otep_find_items:
                self.db.links.remove() #cleanup the links table
                self.oteps.add_vedge_otep_link(otep)
                links_count = self.db.links.find().count() #cross verify the database
                if links_count:
                    self.is_test_failed()
        except:
            pass 


    def test_add_otep_vconnector_link(self):
        """
            Testcase : add otep vconnector link -normal case
        """
        logger.info("Testing add otep vconnector link -normal case")
        self.inv.find_items=MagicMock(return_value=mock_data.vconnector_link_vconnector)
        try:
            for otep in mock_data.otep_find_items:
                self.db.links.remove() #cleanup the links table
                self.oteps.add_otep_vconnector_link(otep)
                links_count = self.db.links.find().count() #cross verify the database
                if not links_count:
                    self.is_test_failed()
        except:
            self.is_test_failed() 


    def test_add_otep_vconnector_link_vconnector_empty(self):
        """
            Testcase : add otep vconncetor link - empty vconnector
        """
        logger.info("Testing add otep vconncetor link - empty vconnector")
        self.inv.find_items=MagicMock(return_value=[])
        try:
            for otep in mock_data.otep_find_items:
                self.db.links.remove() #cleanup the links table
                res = self.oteps.add_otep_vconnector_link(otep)
                self.assertEqual(res, None)
        except:
            self.is_test_failed() 


    def test_add_otep_vconnector_link_not_vconnector_in_otep(self):
        """
            Testcase : add otep vconnector link - vconnector not in otep
        """
        logger.info("Testing add otep vconnector link - vconnector not in otep")
        try:
            for otep in mock_data.otep_find_items:
                self.db.links.remove() #cleanup the links table
                res = self.oteps.add_otep_vconnector_link(otep.pop('vconnector'))
                self.assertEqual(res, None)
        except:
            self.is_test_failed()
        
         
    def test_add_otep_pnic_link(self):
        """
            Testcase: add otep pnic link- normal case
        """
        logger.info("Testing add otep pnic link- normal case")
        self.inv.find_items=MagicMock(return_value=mock_data.vconnector_link_vconnector)
        try:
            for otep in mock_data.otep_find_items:
                self.db.links.remove() #cleanup the links table
                self.oteps.add_otep_pnic_link(otep)
                links_count = self.db.links.find().count() #cross verify the database
                if not links_count:
                    self.is_test_failed()
        except:
            self.is_test_failed()  
             
            
    def test_add_otep_pnic_link_not_pnic(self):
        """
            Testcase : add otep pnic link -empty pnic
        """
        logger.info("Testing add otep pnic link -empty pnic")
        self.inv.find_items=MagicMock(return_value=[])
        try:
            for otep in mock_data.otep_find_items:
                self.db.links.remove() #cleanup the links table
                res = self.oteps.add_otep_pnic_link(otep)
                self.assertEqual(res, None)
        except:
            self.is_test_failed()             
        

if __name__ == '__main__':
    unittest.main()
