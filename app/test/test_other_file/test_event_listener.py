import unittest
from unittest.mock import MagicMock

from test.test_other_file.test_data import mock_data
from discover.event_listener import Worker
from discover.event_listener import get_args
from test.test_other_file.other_parent import TestParent
from discover.inventory_mgr import InventoryMgr

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestWorker(TestParent):
    """
        Unittet for EventHandler
    """
    
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestWorker, self).setUp()
        self.listener = Worker(None)

 
    def test_get_args(self):
        """
            Testcase: get args
        """
        logger.info("Testing get args")
        try:
            res = get_args()
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
    
    
    def test_set_env(self):
        """
            Testcase: set environment
        """
        logger.info("Testing environment")
        try:        
            self.inv = InventoryMgr()
            self.inv.set_collection = MagicMock(return_value=mock_data.NONE) #mock 
            self.listener.set_env(mock_data.env,mock_data.event_listener_coll)
            res = self.listener.notification_responses
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
        
    
    def test_get_consumers(self):
        """
            NOTE : this method not used any where .. 
                def get_consumers(self, Consumer, channel) ... where 'Consumer' it seems like Class..where not declared any where in 
                source code..
        """
        pass

    def test_process_task(self):
        """
            It used by get_consumers()
        """
        pass
    
    def test_handle_event(self):
        """
            It used by process_task()
        """
        pass
    
        
if __name__ == '__main__':
    unittest.main()
