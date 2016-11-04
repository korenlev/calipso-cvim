import unittest

from test.test_other_file.test_data import mock_data
from discover.util import Util
from test.test_other_file.other_parent import TestParent

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestUtil(TestParent):
    """
        Unittest for Util
    """
    
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestUtil, self).setUp()
        self.util = Util()


    def test_get_module_file_by_class_name(self):
        """
            Testcase: module class name
        """
        logger.info("Testing module file by class name")
        res = self.util.get_module_file_by_class_name(mock_data.util_class_name) #this method convert string to lowercase
        if not res.lower():
            self.is_test_failed()

        
        
    def test_get_instance_of_class(self):
        """
            Testcase: instance of class
        """
        logger.info("Testing the class instance")
        try:
            res = self.util.get_instance_of_class(mock_data.util_class_name)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
        
    
    def test_jsonify(self):
        """
            Testcase: jsonify
        """
        logger.info("Testing jsonify")
        res = self.util.jsonify(mock_data.util_jsonify )
        if not res:
            self.is_test_failed()


    def test_prettify(self):
        """
            Testcase: prettify
        """
        logger.info("Testing prettify")
        self.util.set_prettify(mock_data.dummy_value)
        res = self.util.get_prettify()
        if not res:
            self.is_test_failed()


if __name__ == '__main__':
    unittest.main()
