import unittest
from unittest.mock import MagicMock

from test.test_other_file.test_data import mock_data
from discover.network_agents_list import NetworkAgentsList
from test.test_other_file.other_parent import TestParent

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestNetworkAgentsList(TestParent):
    """
        Unittest for NetworkAgentsList
    """

    def test_get_type(self):
        """
            Testcase: network_agent_types table
        """
        logger.info("Testing network agent type")
        nwt_agent = NetworkAgentsList()
        res = nwt_agent.get_type(mock_data.network_agent_list_type)
        if not res:
            self.is_test_failed()
            
            
    def test_get_type_false_type(self):
        """
            Testcase: network_agent_types table - false
        """
        logger.info("Testing network agent type table - false case")
        try:
            nwt_agent = NetworkAgentsList()
            res = nwt_agent.get_type(mock_data.network_agent_false_list_type)
            if res:
                self.is_test_failed()
        except:
            self.is_test_failed()

        

if __name__ == '__main__':
    unittest.main()
