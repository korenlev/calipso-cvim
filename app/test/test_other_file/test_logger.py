import unittest

from test.test_other_file.test_data import mock_data
from discover.logger import Logger
from test.test_other_file.other_parent import TestParent

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestLogger(TestParent):
    """
        Unittest for Logger
    """
    
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestLogger, self).setUp()
        self.logg = Logger()


    def test_set_loglevel(self):
        """
            Testcase: loglevel
        """
        logger.info("Testing the loglevel")
        try:
            self.logg.set_loglevel(mock_data.logger_level)
            res = self.logg.log
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()


    def test_set_loglevel_wrong_log(self):
        """
            Testcase: loglevel- wrong log
        """
        logger.info("Testing the loglevel-wrong loglevel")
        try:
            self.logg.set_loglevel(mock_data.dummy_value)
            res = self.logg.log
            if res:
                self.is_test_failed()
        except:
            pass



if __name__ == '__main__':
    unittest.main()
