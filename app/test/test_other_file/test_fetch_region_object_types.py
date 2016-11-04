import unittest

from discover.fetch_region_object_types import FetchRegionObjectTypes
from test.test_other_file.other_parent import TestParent
from test.test_other_file.test_data import mock_data

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestFetchRegionObjectTypes(TestParent):
    """
        Unittest for FetchRegionObjectTypes
    """
    
    def test_get(self):
        """
            Testcase: the get() for FetchRegionOjectTypes
        """
        logger.info("Testing the get() for FetchRegionOjectTypes")
        try:
            res = FetchRegionObjectTypes().get(mock_data.dummy_value)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()


    def test_get_empty_value(self):
        """
            Testcase: the get() for FetchRegionOjectTypes -empty value
        """
        logger.info("Testing the get() for FetchRegionOjectTypes")
        try:
            res = FetchRegionObjectTypes().get(mock_data.NONE)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
   

if __name__ == '__main__':
    unittest.main()
