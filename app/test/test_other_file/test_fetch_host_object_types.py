import unittest
from discover.fetch_host_object_types import FetchHostObjectTypes
from test.test_other_file.other_parent import TestParent
from test.test_other_file.test_data import mock_data
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestFetchHostObjectTypes(TestParent):
    """
        Unittest for FetchHostObjectTypes
    """

    def test_get(self):
        """
            Testcase: get() for FetchHostObjectType
        """
        logger.info("Testing get() for FetchHostObjectType")
        try:
            res = FetchHostObjectTypes().get(mock_data.dummy_value)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            

    def test_get_empty_value(self):
        """
            Testcase: get() for FetchHostObjectType - empty value
        """
        logger.info("Testing get() for FetchHostObjectType")
        try:
            res = FetchHostObjectTypes().get(mock_data.NONE)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()


if __name__ == '__main__':
    unittest.main()
