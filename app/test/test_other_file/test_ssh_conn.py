import unittest
from unittest.mock import MagicMock


from discover.configuration import Configuration
from test.test_other_file.test_data import mock_data
from discover.ssh_conn import SshConn
from test.test_other_file.other_parent import TestParent

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestSshConn(TestParent):
    """
        Unittest for SshConn
    """
    
    def setUp(self):
        """
            The setUp() methods allow you to define instructions that will be executed before each test method.
        """
        super(TestSshConn, self).setUp()
        self.conf = Configuration()
        self.conf.get = MagicMock(return_value=mock_data.ssh_conn)
        self.ssh = SshConn(mock_data.ssh_host_name)


    def test_connect(self):
        """
            Testcase: ssh connection
        """
        logger.info("Testing the ssh connection")
        try:
            self.ssh.connect()
            if not self.ssh:
                self.is_test_failed()
        except:
            self.is_test_failed()



    def test_exec(self):
        """
            Testcase: ssh exec 
        """
        logger.info("Testing the exec method for ssh")
        try:
            res = self.ssh.exec(mock_data.ssh_cmd)
            if not res:
                self.is_test_failed()
        except:
            self.is_test_failed()
 
 
    def test_exec_false_case(self):
        """
            Testcase: ssh exec -false case
        """
        logger.info("Testing the exec method for ssh")
        try:
            res = self.ssh.exec(mock_data.ssh_cmd_false)
            self.assertEqual(res,'')
        except:
            self.is_test_failed()        
 
        
    def test_get_host(self):
        """
            Testcase: get_host()
        """
        logger.info("Testing the get_host")
        res = self.ssh.get_host()
        if not res:
            self.is_test_failed()
        
 
    def test_disconnect_all(self):
        """
            Testcase: disconnect()
        """
        logger.info("Testing the disconnect")
        self.ssh.disconnect_all()
        
        try:
            res = self.ssh.exec(mock_data.ssh_cmd)
            if res:
                self.is_test_failed()
        except:
            pass
     


if __name__ == '__main__':
    unittest.main()
