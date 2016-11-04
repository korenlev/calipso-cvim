import unittest

from test.test_other_file.test_data import mock_data
from discover.fetcher import Fetcher
from test.test_other_file.other_parent import TestParent

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestFetcher(TestParent):
    """
        Unittest for Fetcher
    """
    
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestFetcher, self).setUp()
        self.fetcher = Fetcher()


    def test_escape(self):
        """
            Testcase: escape()
        """
        logger.info("Testing escape()")
        res = self.fetcher.escape(mock_data.dummy_value)
        if not res:
            self.is_test_failed()
        
        
    def test_pretty(self):
        """
            Testcase: pretty
        """
        logger.info("Testing pretty")
        self.fetcher.set_prettify(mock_data.dummy_value)
        expected = self.fetcher.get_prettify()
        if not expected:
            self.is_test_failed()
        

    def test_env(self):
        """
            Testcase: env
        """
        logger.info("Testing the environment")
        self.fetcher.set_env(mock_data.env)
        expected = self.fetcher.get_env()
        if not expected:
            self.is_test_failed()
    
        
    def test_jsonify(self):
        """
            Testcase: jsonify
        """
        logger.info("Testing jsonify")
        try:
            res = self.fetcher.jsonify(mock_data.util_jsonify)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
        
        
    def test_set_logger(self):
        """
            Testcase: set logger
        """
        logger.info("Testing the set logger")
        try:
            self.fetcher.set_logger(mock_data.logger_level)  #AttributeError: 'Logger' object has no attribute 'set_level'
            res = self.fetcher.log
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
        


if __name__ == '__main__':
    unittest.main()