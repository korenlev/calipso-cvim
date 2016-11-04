import unittest

from test.test_other_file.test_data import mock_data
from discover.mongo_access import MongoAccess
from test.test_other_file.other_parent import TestParent

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestMongoAccess(TestParent):
    """
        Unittest for MongoAccess
    """
    
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestMongoAccess, self).setUp()
        self.mongo = MongoAccess()
    

    def test_mongo_connect(self):
        """
            Testcase : mongo connection
        """
        logger.info("Testing mongo connection")
        try:
            MongoAccess.db[mock_data.mongo_table].find_one({})  #checking the db connection by accessing inventory table
        except:
            self.is_test_failed()
            
            
    def test_mongo_connect_wrong_table(self):
        """
            Testcase: mongo connection  -false case
        """
        logger.info("Testing mongo connection for false case")
        try:
            MongoAccess.db[mock_data.mongo_table_false].find_one({})
        except:
            self.is_test_failed()

        
    def test_encode_mongo_keys(self):
        """
            Testcase: encode mongo keys
        """
        logger.info("Testing encode mongo keys")
        try:
            res = self.mongo.encode_mongo_keys(mock_data.mongo_access_key_encode)
            if '.' in res:
                self.is_test_failed()
            
        except:
            self.is_test_failed()
            
    
    def test_decode_mongo_keys(self):
        """
            Testcase: decode mongo keys
        """
        logger.info("Testing decode mongo keys")
        try:
            res = self.mongo.decode_mongo_keys(mock_data.env)
            if "[dot]" in res:
                self.is_test_failed()
        except:
            self.is_test_failed()
            
      
    def test_encode_dots(self):
        """
            Testcase: encode dots
        """
        logger.info("Testing encode dots")
        res = self.mongo.encode_dots(mock_data.mongo_access_encode)
        if '.' in res:
            self.is_test_failed()
         
         
    def test_decode_dots(self):
        """
            Testcase: decode dots
        """
        logger.info("Testing decode dots")
        res = self.mongo.decode_dots(mock_data.mongo_access_decode)
        if "[dot]" in res:
            self.is_test_failed()
            
            
    def test_change_dict_naming_convention(self):
        """
            Testcase: change dict naming convention
        """
        logger.info("Testing change dict naming convention")
        try:
            res = self.mongo.change_dict_naming_convention(mock_data.mongo_access_key_decode, self.mongo.encode_dots)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
        


if __name__ == '__main__':
    unittest.main()
