import unittest
from unittest.mock import MagicMock

from test.test_other_file.test_data import mock_data
from discover.clique_finder import CliqueFinder
from test.test_other_file.other_parent import TestParent

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestCliqueFinder(TestParent):
    """
        Unittest for CliqueFinder
    """
    
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestCliqueFinder, self).setUp()
        self.clique = CliqueFinder(inventory=self.db[mock_data.inventory], links=self.db[mock_data.links], clique_types=self.db[mock_data.clique_clique_type], constraints=self.db[mock_data.constraints], cliques=None)
        
        
    def test_find_cliques_by_link(self):
        """
            Testcase : Testing clique by links
        """
        logger.info("Testing cliques by links") 
        try:
            self.clique.links.find = MagicMock(return_value=mock_data.clique_finder_find)
            res = self.clique.find_cliques_by_link(mock_data.dummy_list)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            
            
    def test_find_links_by_source(self):
        """
            Testcase : Testing find links by source
        """
        logger.info("Testing find links by source") 
        try:
            self.clique.links.find = MagicMock(return_value=mock_data.clique_finder_find)
            res = self.clique.find_links_by_source(mock_data.dummy_db_id)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            
            
    def test_find_links_by_target(self):
        """
            Testcase : Testing find links by target
        """
        logger.info("Testing find links by target") 
        try:
            self.clique.links.find = MagicMock(return_value=mock_data.clique_finder_find)
            res = self.clique.find_links_by_target(mock_data.dummy_db_id)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            
            
            
    def test_get_clique_types(self):
        """
            Testcase : Testing clique types
        """
        logger.info("Testing clique types") 
        try:
            self.clique.get_clique_types= MagicMock(return_value=mock_data.clique_types_find[0])
            self.clique.find_cliques_for_type = MagicMock()
            self.clique.find_cliques()
        except:
            self.is_test_failed()
            
    
    def test_find_cliques_for_type(self):
        """
            Testcase : Testing find cliques for type
        """
        logger.info("Testing find cliques for type") 
        try:
            self.clique.clique_constraints.find_one= MagicMock(mock_data.clique_constraints[0])
            self.inv.find = MagicMock(return_value=mock_data.inv_finds_inv)
            self.clique.construct_clique_for_focal_point = MagicMock()
            self.clique.find_cliques_for_type(mock_data.clique_constraints[0])
        except:
            self.is_test_failed()
        
            

    def test_rebuild_clique(self):
        """
            Testcase : Testing rebuild clique
        """
        logger.info("Testing rebuild clique") 
        try:
            self.clique.clique_constraints.find_one= MagicMock(mock_data.clique_constraints[0])
            self.clique.get_clique_types = MagicMock(return_value=mock_data.clique_clique_type)
            self.inv.find_one = MagicMock(return_value=mock_data.inv_finds_inv[0])
            self.clique.rebuild_clique(mock_data.clique_constraints[0])
        except:
            self.is_test_failed()

    def test_check_constraints(self):
        """
            Testcase : Testing check constraints
        """
        logger.info("Testing check constrainst-normal case") 
        try:
            res = self.clique.check_constraints(mock_data.clique_constraints[0], mock_data.clique_finder_link)
            self.assertEqual(res,True)
        except:
            self.is_test_failed()
            
            
    def test_check_constraints_attributes_not_in_links(self):
        """
            Testcase : Testing checm contraints -attributes not in links
        """
        logger.info("Testing checm contraints -attributes not in links") 
        try:
            res = self.clique.check_constraints(mock_data.clique_constraints[0], mock_data.clique_finder_link_not_attributes)
            self.assertEqual(res,True)
        except:
            self.is_test_failed()   


if __name__ == '__main__':
    unittest.main()
