import unittest
from unittest.mock import MagicMock

from discover.find_links_for_vservice_vnics import FindLinksForVserviceVnics
from test.test_links.test_data import mock_data
from test.test_links.find_parent import TestFindLinks
from discover.inventory_mgr import InventoryMgr

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestFindLinksForVServiceVnics(TestFindLinks):

    """
        Unittest for FindLinksForVServiceVnics

    """
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestFindLinksForVServiceVnics, self).setUp()
        self.inv = InventoryMgr()
        self.inv.set_inventory_collection()  #inorder to avoid attribute error, this method is invoked
        self.link_vservice_vnics = FindLinksForVserviceVnics()


    def test_add_links(self):
        """
            Testing the add links
        """
        logger.info("Testing the add links")
        try:
            self.link_vservice_vnics.add_link_for_vnic = MagicMock()  #mock the add_link_for_vnic()
            self.inv.find_items = MagicMock(return_value = mock_data.vservice_find_items) #mock the find items value
            self.link_vservice_vnics.add_links() #calling the add_links()
        except:
            self.is_test_failed()
            
            
    def side_effect(self,*args):
        if mock_data.vservice_find_items[0].get('host') in args:
            return mock_data.vservice_host
        elif mock_data.vservice_find_items[0].get('network') in args:
            return mock_data.vservice_network
        else:
            return mock_data.vservice_vservice  
          
    
    def test_add_link_for_vnic(self):
        """
            Testcase : add link for vnic
        """
        logger.info("Testing the add links for vnic -normal testcase")
        self.inv.get_by_id=MagicMock(side_effect=self.side_effect)
        try:
            for vnic in mock_data.vservice_find_items:
                self.db.links.remove() #cleanup the links table
                FindLinksForVserviceVnics().add_link_for_vnic(vnic)
                links_count = self.db.links.find().count() #cross verify the database
                if not links_count:
                    self.is_test_failed()
        except:
            self.is_test_failed() 
                    
         
    def test_add_link_for_vnic_for_empty_host(self):
        """
            Testcase : add link for vnic for empty host
        """
        logger.info("Testing add link for vnic for empty host")
        self.inv.get_by_id=MagicMock(return_value=[])
        try:
            for vnic in mock_data.vservice_find_items:
                self.db.links.remove() #cleanup the links table
                FindLinksForVserviceVnics().add_link_for_vnic(vnic)
                links_count = self.db.links.find().count() #cross verify the database
                if links_count:
                    self.is_test_failed() #if record created, the testcase is failed
        except:
            pass  #should expect trigger
        
        
    def side_effect_host(self,*args):
        if mock_data.vservice_find_items[0].get('host') in args:
            mock_data.vservice_host["host_type"]=[]
            return mock_data.vservice_host

        
    def test_add_link_for_vnic_host_not_contain_network(self):
        """
            Testcase : add link for vnic - host not contain network
        """
        logger.info("Testing add link for vnic - host not contain network")
        self.inv.get_by_id=MagicMock(side_effect=self.side_effect_host)
        try:
            for vnic in mock_data.vservice_find_items:
                self.db.links.remove() #cleanup the links table
                res = FindLinksForVserviceVnics().add_link_for_vnic(vnic)
                self.assertEqual(res,None) # the return is None
                links_count = self.db.links.find().count() #cross verify the database
                if links_count:
                    self.is_test_failed() #if record created, the case is fail
        except:
            self.is_test_failed()


    def side_effect_network(self,*args):
        if mock_data.vservice_find_items[0].get('host') in args:
            return mock_data.vservice_host
        elif mock_data.vservice_find_items[0].get('network') in args:
            return []
        else:
            return[]
       
        
    def test_add_link_for_vnic_for_empty_network(self):
        """
            Testcase : add link for vnic - empty network
        """
        logger.info("Testing add link for vnic - empty network")
        self.inv.get_by_id=MagicMock(side_effect=self.side_effect_network)
        try:
            for vnic in mock_data.vservice_find_items:
                self.db.links.remove() #cleanup the links table
                FindLinksForVserviceVnics().add_link_for_vnic(vnic)
                links_count = self.db.links.find().count() #cross verify the database
                if links_count:
                    self.is_test_failed() #if record created, the case is fail
        except:
            pass # expect part should trigger   
        

    def test_add_link_for_vnic_for_empty_vservice(self):
        """
            Testcase : add link for vnic for empty vservice
        """
        logger.info("Testing add link for vnic for empty vservice")
        self.inv.get_by_id=MagicMock(side_effect=self.side_effect_network)
        try:
            for vnic in mock_data.vservice_find_items:
                self.db.links.remove() #cleanup the links table
                FindLinksForVserviceVnics().add_link_for_vnic(vnic)
                links_count = self.db.links.find().count() #cross verify the database
                if links_count:
                    self.is_test_failed() #if record created, the case is fail
        except:
            pass # expect part should trigger      
       


if __name__ == '__main__':
    unittest.main()
