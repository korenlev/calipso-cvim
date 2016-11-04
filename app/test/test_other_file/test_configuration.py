import unittest

from test.test_other_file.test_data import mock_data
from discover.configuration import Configuration
from test.test_other_file.other_parent import TestParent
from unittest.mock import MagicMock

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestConfiguration(TestParent):
    """
        Unittest for Configuration

    """
    
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestConfiguration, self).setUp()
        self.conf = Configuration()


    def test_use_env(self):
        """
            Testcase:  use environment -normal case
        """
        logger.info("Testing the use environment-normal case")
        try:
            self.conf.collection.find= MagicMock(return_value=mock_data.conf_find_env)
            self.conf.use_env(mock_data.env)
        except:
            self.is_test_failed()
            
            
    def test_use_env_empty(self):
        """
            Testcase: use environment -empty env
        """
        logger.info("Testing the use environment - empty env")
        try:
            self.conf.collection.find= MagicMock(return_value=[])
            self.conf.use_env(mock_data.env)
        except:
            pass  #for no env, the expect part trigger
        
        
    def test_use_more_env(self):
        """
            Testcase: use environment -more env
        """
        logger.info("Testing the use environment- more env")
        try:
            self.conf.collection.find= MagicMock(return_value=mock_data.conf_find_more_env)
            self.conf.use_env(mock_data.env)
        except:
            pass  #for no env, the expect part trigger
        
        
    def test_get_env_config(self):
        """
            Testcase: get env config
        """
        logger.info("Testing the get env config")
        try:
            self.conf.collection.find= MagicMock(return_value=mock_data.conf_find_env)
            self.conf.use_env(mock_data.env)
            res = self.conf.get_env_config()   
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
 
 
    def test_get_config(self):
        """
            Testcase: get config
        """
        logger.info("Testing the get config")
        try:
            self.conf.collection.find= MagicMock(return_value=mock_data.conf_find_env)
            self.conf.use_env(mock_data.env)
            res = self.conf.get_config()
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            
                 
    def test_get_env(self):
        """
            Testcase: get env
        """
        logger.info("Testing the get env")
        try:
            self.conf.collection.find= MagicMock(return_value=mock_data.conf_find_env)
            self.conf.use_env(mock_data.env)
            res = self.conf.get_env()
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
    
    
    def test_get(self):
        """
            Testcase : get
        """
        logger.info("Testing the get")
        try:
            self.conf.collection.find= MagicMock(return_value=mock_data.conf_find_env)
            self.conf.use_env(mock_data.env)
            res = self.conf.get(mock_data.conf_component)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
         
         
    def test_has_network_plugin(self):
        """
            Testcase: has_network_plugin
        """
        logger.info("Testing the has_network_plugin")
        try:
            self.conf.collection.find= MagicMock(return_value=mock_data.conf_find_env)
            self.conf.use_env(mock_data.env)
            res = self.conf.has_network_plugin(mock_data.config_name)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()


if __name__ == '__main__':
    unittest.main()
