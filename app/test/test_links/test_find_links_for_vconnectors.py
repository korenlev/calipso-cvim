import unittest
from discover.inventory_mgr import InventoryMgr
from unittest.mock import MagicMock
from discover.find_links_for_vconnectors import FindLinksForVconnectors
from test.test_links.test_data import mock_data
from test.test_links.find_parent import TestFindLinks

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestFindLinksForVconnectors(TestFindLinks):

    """
        Unittest for FindLinksForVconnectors

    """
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestFindLinksForVconnectors, self).setUp()
        self.vconnector = FindLinksForVconnectors()
        self.inv = InventoryMgr()
        self.inv.set_inventory_collection() #inorder to avoid attribute error



    def test_add_links(self):
        """
            Testcase: Testing add links
        """
        logger.info("Testing the add links")        
        try:
            self.vconnector.add_vnic_vconnector_link = MagicMock()  
            self.vconnector.add_vconnector_pnic_link = MagicMock()
            self.inv.find_items = MagicMock(return_value = mock_data.vconnector_link_vconnectors) #mock the find items value
            self.vconnector.add_links() #calling the add_links()
        except:
            self.is_test_failed()  
            
            
    def test_add_vnic_vconnector_link(self):
        """
            Testcase : add vnic vconnector link- normal case
        """
        logger.info("Testing add vnic vconnector link- normal case")
        self.inv.get_by_id = MagicMock(return_value=mock_data.vconnector_vnic)
        self.inv.set = MagicMock()
        try:
            self.db.links.remove() #cleanup the links table
            self.vconnector.add_vnic_vconnector_link(mock_data.vconnector_link_vconnectors[0],mock_data.vconnector_interface)
            links_count = self.db.links.find().count() #cross verify the database
            if not links_count:
                self.is_test_failed()
        except:
            self.is_test_failed()
            
            
    def test_add_vnic_vconnector_link_vnic_empty(self):
        """
            Testcase : add vnic vconnector link for empty vnic
        """
        logger.info("Testing add vnic vconnector link for empty vnic")
        self.inv.get_by_id = MagicMock(return_value=[])
        try:
            self.db.links.remove() #cleanup the links table
            res = self.vconnector.add_vnic_vconnector_link(mock_data.vconnector_link_vconnectors[0],mock_data.vconnector_interface)
            self.assertEqual(res, None)
        except:
            self.is_test_failed()       


    def test_add_vnic_vconnector_link_interface(self):
        """
            Testcase : add vnic vconnector link - interface based testcase
        """
        logger.info("Testing add vnic vconnector link - interface based testcase")
        self.inv.get_by_field = MagicMock(return_value=mock_data.vconnector_vnic)
        try:
            self.db.links.remove() #cleanup the links table
            self.vconnector.add_vnic_vconnector_link(mock_data.vconnector_link_vconnectors[0],mock_data.vconnector_interface_dict)
            links_count = self.db.links.find().count() #cross verify the database
            if not links_count:
                self.is_test_failed()
        except:
            self.is_test_failed()
            

    def test_add_vnic_vconnector_link_interface_notcontain_macaddress(self):
        """
            Testcase : add vnic vconnector link interface -negative scenario
        """
        logger.info("Testing add vnic vconnector link interface -negative scenario")
        self.inv.get_by_field = MagicMock(return_value=mock_data.vconnector_vnic)
        try:
            self.db.links.remove() #cleanup the links table
            res = self.vconnector.add_vnic_vconnector_link(mock_data.vconnector_link_vconnectors[0],mock_data.vconnector_interface_dummy)
            self.assertEqual(res, None)
        except:
            self.is_test_failed()       
            
            
    def test_add_vconnector_pnic_link(self):
        """
            Testcase : add vconnector pnic link -normal case
        """
        logger.info("Testing add vconnector pnic link -normal case")
        self.inv.find_items=MagicMock(return_value=mock_data.pnics_find_items[0])
        try:
  
            self.db.links.remove() #cleanup the links table
            self.vconnector.add_vconnector_pnic_link(mock_data.vconnector_link_vconnectors[0],mock_data.vconnector_interface)
            links_count = self.db.links.find().count() #cross verify the database
            if not links_count:
                self.is_test_failed()
        except:
            self.is_test_failed()
     
          
  
    def test_add_vconnector_pnic_link_negative_ifname(self):
        """
            Testcase : add vconnector pnic link - negative ifname cases
        """
        logger.info("Testing add vconnector pnic link - negative ifname cases")
        try:
            self.db.links.remove() #cleanup the links table
            res = self.vconnector.add_vconnector_pnic_link(mock_data.vconnector_link_vconnectors[0],mock_data.vconnector_interface_ifname)
            self.assertEqual(res,None)
        except:
            self.is_test_failed()
              
              
    def test_add_vconnector_pnic_link_empty_pnic(self):
        """
            Testcase : add vconnector pnic link - empty pnic
        """
        logger.info("Testing add vconnector pnic link - empty pnic")
        self.inv.find_items=MagicMock(return_value=[])
        try:
            self.db.links.remove() #cleanup the links table
            res = self.vconnector.add_vconnector_pnic_link(mock_data.vconnector_link_vconnectors[0],mock_data.vconnector_interface)
            self.assertEqual(res,None)
        except:
            self.is_test_failed()


if __name__ == '__main__':
    unittest.main()
