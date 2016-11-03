import unittest
from discover.find_links_for_vedges import FindLinksForVedges
from discover.fetcher import Fetcher
from test.test_links.test_data import mock_data
from test.test_links.find_parent import TestFindLinks
from discover.inventory_mgr import InventoryMgr
from discover.configuration import Configuration
from unittest.mock import MagicMock

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestFindLinksForVedges(TestFindLinks):

    """
        Unittest for FindLinksForVedges

    """
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestFindLinksForVedges, self).setUp()
        Fetcher.configuration = Configuration()
        self.inv = InventoryMgr()
        self.inv.set_inventory_collection()  #inorder to avoid attribute error, this method is invoked
        self.vedge = FindLinksForVedges()


    def test_add_links(self):
        """
            Testcase: add links
        """
        logger.info("Testing add links")
        try:
            self.vedge.add_link_for_vedge = MagicMock()  #mock the add_link_for_vedge()
            self.inv.find_items = MagicMock(return_value = mock_data.vedges_find_items) #mock the find items value
            self.vedge.add_links() #calling the add_links()
        except:
            self.is_test_failed()
            

    def test_add_link_for_vedge(self):
        """
            Testcase : add link for vedge-normal case
        """
        logger.info("Testing add link for vedge-normal case")
        self.inv.get_by_id=MagicMock(return_value=mock_data.vedge_vedge)
        try:
            self.vedge.add_link_for_vedge(mock_data.vedge_vedge,mock_data.vedge_port)
            links_count = self.db.links.find().count() #cross verify the database
            if not links_count:
                self.is_test_failed()
        except:
            self.is_test_failed() 
            
            
    def test_add_link_for_vedge_empty_vnic(self):
        """
            Testcase : add link for vedge -empty vnic
        """
        logger.info("Testing add link for vedge- empty vnic")
        self.vedge.find_matching_vconnector = MagicMock()  #mock the find_matching_vconnector()
        self.vedge.find_matching_pnic = MagicMock()  #mock the find_matching_pnic()
        self.inv.get_by_id=MagicMock(return_value=[])
        try:
            res = self.vedge.add_link_for_vedge(mock_data.vedge_vedge,mock_data.vedge_port)
            self.assertEqual(res, None)
        except:
            self.is_test_failed()          
    

    def test_find_matching_vconnector(self):
        """
            Testcase : find matching vconnector
        """
        logger.info("Testing find matching vconnector")

        Fetcher.configuration.has_network_plugin = MagicMock(return_value = True) #mock
        self.inv.find_items=MagicMock(return_value=mock_data.vedge_vedge)
        try:
            self.vedge.find_matching_vconnector(mock_data.vedge_vedge,mock_data.vedge_port)
            links_count = self.db.links.find().count() #cross verify the database
            if not links_count:
                self.is_test_failed()
        except:
            self.is_test_failed() 
            

    def test_find_matching_vconnector_empty_vconnector(self):
        """
            Testcase : find matching vconnector -empty vconnector
        """
        logger.info("Testing find matching vconnector -empty vconnector")

        Fetcher.configuration.has_network_plugin = MagicMock(return_value = mock_data.true)
        self.inv.find_items=MagicMock(return_value=[])
        try:
            res = self.vedge.find_matching_vconnector(mock_data.vedge_vedge,mock_data.vedge_port)
            self.assertEqual(res,None)
        except:
            self.is_test_failed() 
            
            

    def test_find_matching_vconnector_pname_check(self):
        """
            Testcase : find matching vconnector -pname check
        """
        logger.info("Testing find matching vconnector -pname check")

        Fetcher.configuration.has_network_plugin = MagicMock(return_value =mock_data.false)
        try:
            res = self.vedge.find_matching_vconnector(mock_data.vedge_vedge,mock_data.vedge_port_pname_check)
            self.assertEqual(res,None)
        except:
            self.is_test_failed()
        



    def test_find_matching_pnic(self):
        """
            Testcase : find matching pnic - normal case
        """
        logger.info("Testing find matching pnic- normal case")
        self.inv.find_items=MagicMock(return_value=mock_data.vedge_vedge)
        try:
            self.vedge.find_matching_pnic(mock_data.vedge_vedge,mock_data.vedge_port)
            links_count = self.db.links.find().count() #cross verify the database
            if not links_count:
                self.is_test_failed()
        except:
            self.is_test_failed()  



    def test_find_matching_pnic_empty_pnic(self):
        """
            Testcase : find matching pnic -empty pnic 
        """
        logger.info("Testing find matching pnic-empty pnic")
        self.inv.find_items=MagicMock(return_value=[])
        try:
            res = self.vedge.find_matching_pnic(mock_data.vedge_vedge,mock_data.vedge_port)
            self.assertEqual(res,None)
        except:
            self.is_test_failed()  
            
            
    def test_find_matching_pnic_empty_pnic_pname(self):
        """
            Testcase : find matching pnic -empty pnic pname
        """
        logger.info("Testing find matching pnic -empty pnic pname")
        try:
            res = self.vedge.find_matching_pnic(mock_data.vedge_vedge_pname_negative_case,mock_data.vedge_port)
            self.assertEqual(res,None)
        except:
            self.is_test_failed()   
                      
            
    def test_find_matching_pnic_empty_pnic_pname_check(self):
        """
            Testcase : find matching pnic -empty pnic pname check
        """
        logger.info("Testing find matching pnic -empty pnic pname check")
        try:
            res = self.vedge.find_matching_pnic(mock_data.vedge_vedge,mock_data.vedge_port_negative_case)
            self.assertEqual(res,None)
        except:
            self.is_test_failed()    
        

if __name__ == '__main__':
    unittest.main()
