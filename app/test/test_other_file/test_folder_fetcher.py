import unittest
from unittest.mock import MagicMock

from test.test_other_file.test_data import mock_data
from discover.folder_fetcher import FolderFetcher
from test.test_other_file.other_parent import TestParent

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestFolderFetcher(TestParent):
    """
        Unittest for FolderFetcher
    """
    
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestFolderFetcher, self).setUp()
        self.folder = FolderFetcher(mock_data.folder_fetcher_types_name,mock_data.folder_fetcher_parent_type)  #mock 

    
    def test_get(self):
        """
            Testcase: get()
        """
        logger.info("Testing get()")
        try:
            res = self.folder.get(mock_data.folder_fetcher_id)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            
            
    def test_get_empty_value(self):
        """
            Testcase: get()-empty value
        """
        logger.info("Testing get()-empty value")
        try:
            res = self.folder.get(mock_data.EMPTY)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()


if __name__ == '__main__':
    unittest.main()
