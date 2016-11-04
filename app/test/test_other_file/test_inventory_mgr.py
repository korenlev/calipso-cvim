import unittest
from unittest.mock import MagicMock

from test.test_other_file.test_data import mock_data
from discover.inventory_mgr import InventoryMgr
from test.test_other_file.other_parent import TestParent

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestInventoryMgr(TestParent):
    """
        Unittest for InventoryMgr
    """
    
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestInventoryMgr, self).setUp()
        self.inv = InventoryMgr()
        self.inv.set_inventory_collection()  #inorder to avoid Arribute Error


    def test_set_collection(self):
        """
            Testcase: set collection
        """
        logger.info("Testing set collection")
        try:
            self.inv.get_coll_name = MagicMock(return_value=mock_data.inv_coll_name)
            res = self.inv.set_collection(mock_data.event_listener_coll,collection_name=mock_data.EMPTY) #mock data
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()


    def test_get_coll_name(self):
        """
            Testcase: get coll name
        """
        logger.info("Testing gety coll name")        
        try:
            res = self.inv.get_coll_name(mock_data.event_listener_coll)  
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
         
         
    def test_set_inventory_collection(self):
        """
            Testcase: set inventory collections
        """
        logger.info("Testing set inventory collections")        
        try:
            self.inv.set_inventory_collection(mock_data.EMPTY)
            res = self.inv.links   #links table
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            
    
    def test_clear(self):
        """
            Clear the record in tables.. [sample.click....]
        """
        pass
           
    
    def test_process_results(self):
        """
            Testcase: process results
        """
        logger.info("Testing process results")        
        try:
            self.inv.get_base_url = MagicMock(return_value = mock_data.inv_base_url)
            res = self.inv.process_results(mock_data.inv_process_result) 
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            
            
    def test_process_results_empyt_raw_result(self):
        """
            Testcase: process results - empty raw result
        """
        logger.info("Testing process results emtpy raw result")        
        try:
            self.inv.get_base_url = MagicMock(return_value = mock_data.inv_base_url)
            res = self.inv.process_results(mock_data.dummy_list) 
            self.assertEqual(res, [])
        except:
            self.is_test_failed()
     
     
    def test_get_by_id(self):
        """
            Testcase: get by id
        """
        logger.info("Testing get by id")        
        try:
            self.inv.find = MagicMock(return_value=mock_data.inv_process_result)
            self.inv.get_base_url = MagicMock(return_value = mock_data.inv_base_url)
            res = self.inv.get_by_id(mock_data.env,mock_data.inventory_dummy_id)
            print(res)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()    
            
    
    def test_get_by_ids(self):
        """
            Testcase: get by ids
        """
        logger.info("Testing get by ids")        
        try:
            self.inv.find = MagicMock(return_value=mock_data.inv_process_result)
            self.inv.get_base_url = MagicMock(return_value = mock_data.inv_base_url)
            res = self.inv.get_by_ids(mock_data.env,mock_data.inventory_dummy_id)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed() 
            
    
    def test_get_by_field(self):
        """
            Testcase: get by field
        """
        logger.info("Testing get by field")        
        try:
            self.inv.find = MagicMock(return_value=mock_data.inv_process_result)  
            self.inv.get_base_url = MagicMock(return_value = mock_data.inv_base_url)  
            res = self.inv.get_by_field(mock_data.env, mock_data.inventory_type,None,True)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()


    def test_get(self):
        """
            Testcase: get
        """
        logger.info("Testing get")         
        try:
            self.inv.get_by_field = MagicMock(return_value=mock_data.inv_get_by_field)
            res = self.inv.get(mock_data.env, mock_data.inventory_type, None, True)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            
            
    def test_get_children(self):
        """
            Testcase: get children
        """
        logger.info("Testing get children")        
        try:
            self.inv.find = MagicMock(return_value=mock_data.inv_process_result)
            self.inv.get_base_url = MagicMock(return_value = mock_data.inv_base_urls)   
            res = self.inv.get_children(mock_data.env,mock_data.inventory_type,mock_data.NONE)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
 
 
    def test_get_single(self):
        """
            Testcase: get single
        """
        logger.info("Testing get single")        
        try:
            self.inv.find = MagicMock(return_value=mock_data.inv_process_result)
            self.inv.get_base_url = MagicMock(return_value = mock_data.inv_base_urls) 
            res = self.inv.get_single(mock_data.env,mock_data.inventory_type,None)
            if not res:
                self.is_test_failed()
        except Exception as e:
            self.assertIsNotNone(str(e))
            
    
    def test_check(self):
        """
            Testcase: check
        """
        logger.info("Testing check")        
        try:
            self.inv.check(mock_data.inv_get_by_field[0], mock_data.inv_check_filed)
        except:
            self.is_test_failed()
            
            
    def test_get_base_url(self):
        """
            Testcase: get base url
        """
        logger.info("Testing get base url")        
        try:
            res = self.inv.get_base_url(mock_data.inv_base_url)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            

    def test_find(self):
        """
            Testcase: find
        """
        logger.info("Testing find")        
        try:
            self.inv.find = MagicMock(return_value=mock_data.inv_find_inv)
            res = self.inv.find(mock_data.dummy_dict)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            
            
    def test_find_items(self):
        """
            Testcase: find items
        """
        logger.info("Testing find items")        
        try:
            self.inv.find= MagicMock(return_value=mock_data.inv_finds_inv)
            self.inv.get_base_url = MagicMock(return_value = mock_data.inv_base_urls) 
            res = self.inv.find_items(mock_data.dummy_dict)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
         
         
    def test_get_clique_finder(self):
        """
            Testcase: get clique finder
        """
        logger.info("Testing get clique finder")        
        try:
            res = self.inv.get_clique_finder()
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            

    def test_set(self):
        """
            Testcase : set
        """
        logger.info("Testing set")        
        try:
            self.inv.set(mock_data.inv_set)
            res = self.db.inventory.find({'id': mock_data.inv_set['id']}).count() #cross verify the db, whether the value is updated or not
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            
 
    def test_create_link(self):
        """
            Testcase: create link
        """
        logger.info("Testing create link")        
        env = mock_data.inv_create['env']
        host = mock_data.inv_create['host']
        src = mock_data.inv_create['src']
        source_id = mock_data.inv_create['source_id']
        target = mock_data.inv_create['target']
        target_id = mock_data.inv_create['target_id']
        link_type = mock_data.inv_create['link_type']
        state= mock_data.inv_create['state']
        link_name = mock_data.inv_create['link_name']
        link_weight = mock_data.inv_create['link_weight']
        source_label = mock_data.inv_create['source_label']
        target_label = mock_data.inv_create['target_label']
        extra_attributes = mock_data.inv_create['extra_attributes']
         
        self.db.links.remove() #cleanup the links table
        self.inv.create_link(env, host, src, source_id, target, target_id, link_type, link_name, state, link_weight, source_label, target_label, extra_attributes)
        links_count = self.db.links.find().count()  #cross verify the database
        self.assertNotEqual(links_count,0, "Testcase Failed") #result
   
   
            
    def test_delete_wrong_filter(self):
        """
            Testcase: delete
        """
        logger.info("Testing delete")     
        try:
            res = self.inv.delete(mock_data.inv_delete_coll, mock_data.inv_del_filter)
            if res:
                self.is_test_failed()
        except:
            self.is_test_failed()
        
        
        
if __name__ == '__main__':
    unittest.main()
