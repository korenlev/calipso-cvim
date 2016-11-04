import unittest

from discover.inventory_mgr import InventoryMgr
from discover.singleton import Singleton
from test.test_other_file.other_parent import TestParent

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestSingleton(TestParent):
    """
        Unittest for Singleton
    """
    
    def test_call(self):
        """
            Testcase:  call()
            
        """
        try:
            logger.info("Testing singleton")
            res = Singleton.__call__(InventoryMgr)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
        
        


if __name__ == '__main__':
    unittest.main()
