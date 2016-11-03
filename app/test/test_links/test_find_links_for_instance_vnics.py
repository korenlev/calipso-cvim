import unittest
from unittest.mock import MagicMock

from discover.inventory_mgr import InventoryMgr
from discover.find_links_for_instance_vnics import FindLinksForInstanceVnics
from test.test_links.test_data import mock_data
from test.test_links.find_parent import TestFindLinks

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestFindLinksForInstanceVnics(TestFindLinks):

    """
        Unittest for FindLinksForInstanceVnics

    """
    
    
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestFindLinksForInstanceVnics, self).setUp()
        self.inv = InventoryMgr()
        self.inv.set_inventory_collection()  #inorder to avoid attribute error, this method is invoked
        self.link_instance_vnics = FindLinksForInstanceVnics()
        
        
    def test_add_links(self):
        """
            Testcase : Testing the add links
        """
        logger.info("Testing the add links")        
        try:
            self.link_instance_vnics.add_link_for_vnic = MagicMock()  #mock the add_link_for_vnic()
            self.inv.find_items = MagicMock(return_value = mock_data.vnics_find_items) #mock the find items value
            self.link_instance_vnics.add_links()
        except:
            self.is_test_failed()  
            

    def side_effect(self,*args):
        if mock_data.vnics_find_items[0].get('instance_id') in args:
            return mock_data.link_instance_vnics_get_by_id_instance
        else:
            return mock_data.link_instance_vnics_get_by_id_host
        

    def test_add_links_for_vnic(self):
        """
            Testcase : Testing the add links for vnic - normal case
        """
        logger.info("Testing add links for vnic - normal case")
        self.inv.get_by_id=MagicMock(side_effect=self.side_effect)
        self.inv.set= MagicMock()
        try:
            for vnic in mock_data.vnics_find_items:
                self.db.links.remove() #cleanup the links table
                FindLinksForInstanceVnics().add_link_for_vnic(vnic)
                links_count = self.db.links.find().count() #cross verify the database
                if not links_count:
                    self.is_test_failed()
        except:
            self.is_test_failed()
            
    
    def test_add_links_for_vnic_empty_instance(self):
        """
            Testcase : add link for vnic - empty instance
        """
        logger.info("Testing add link for vnic - empty instance")
        self.inv.get_by_id=MagicMock(return_value=[])
        try:
            for vnic in mock_data.vnics_find_items:
                self.db.links.remove() #cleanup the links table
                FindLinksForInstanceVnics().add_link_for_vnic(vnic)
                links_count = self.db.links.find().count() #cross verify the database
                if links_count:
                    self.is_test_failed()
        except:
            pass # expect should occur for this scenario
        
        
    def test_add_links_for_vnic_instance_not_contain_network_info(self):
        """
            Testcase : add links for vnic - instance not contain newtork info

        """
        logger.info("Testing add links for vnic - instance not contain newtork info")
        self.inv.get_by_id=MagicMock(return_value=[mock_data.link_instance_vnics_get_by_id_instance.pop('network_info')])
        try:
            for vnic in mock_data.vnics_find_items:
                self.db.links.remove() #cleanup the links table
                FindLinksForInstanceVnics().add_link_for_vnic(vnic)
                links_count = self.db.links.find().count() #cross verify the database
                if links_count:
                    self.is_test_failed()
        except:
            pass  #except should occurs for this scenario
        
        
    def side_effect_empty_host(self,*args):
        if mock_data.vnics_find_items[0].get('instance_id') in args:
            return mock_data.link_instance_vnics_get_by_id_instance
        else:
            return []        
        
        
    def test_add_links_for_vnic_empty_host(self):
        """
            Testcase : addd links for vnic - empty host
        """
        logger.info("Testing addd links for vnic - empty host")
        self.inv.get_by_id=MagicMock(side_effect=self.side_effect_empty_host)
        try:
            for vnic in mock_data.vnics_find_items:
                self.db.links.remove() #cleanup the links table
                FindLinksForInstanceVnics().add_link_for_vnic(vnic)
                links_count = self.db.links.find().count() #cross verify the database
                if links_count:
                    self.is_test_failed()
        except:
            pass  #for this case, except must trigger becuase -->host_types = host["host_type"]



    def side_effect_host(self,*args):
        if mock_data.vnics_find_items[0].get('instance_id') in args:
            return mock_data.link_instance_vnics_get_by_id_instance
        else:
            mock_data.link_instance_vnics_get_by_id_host['host_type']=[]
            return mock_data.link_instance_vnics_get_by_id_host

        

    def test_add_links_for_vnic_host_not_contain_network_and_compute(self):
        """
            Testcase : add links for vnic - host not contain network & compute
        """
        logger.info("Testing add links for vnic - host not contain network & compute")
        self.inv.get_by_id=MagicMock(side_effect=self.side_effect_host)  #mocking get_by_id based on argument
        try:
            for vnic in mock_data.vnics_find_items:
                self.db.links.remove() #cleanup the links table
                res = FindLinksForInstanceVnics().add_link_for_vnic(vnic)    #should return []
                self.assertEqual(res, [])
        except:
            self.is_test_failed()
            
            

if __name__ == '__main__':
    unittest.main()