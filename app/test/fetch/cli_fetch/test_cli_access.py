import time

from discover.cli_access import CliAccess
from test.fetch.test_fetch import TestFetch
from test.fetch.cli_fetch.test_data.cli_access import *
from unittest.mock import MagicMock,patch


class TestCliAccess(TestFetch):

    def setUp(self):
        self.configure_environment()
        self.cli_access = CliAccess()

    @patch("discover.ssh_conn.SshConn.exec")
    def test_run(self, ssh_conn_exec):
        # mock the command result
        ssh_conn_exec = MagicMock(return_value=RUN_RESULT)

        result = self.cli_access.run(COMMAND, COMPUTE_HOST['id'])

        # clear the cached command
        self.cli_access.cached_commands = {}
        self.assertNotEqual(result, "", "Can't get ip configuration from command line")

    @patch("discover.ssh_conn.SshConn.exec")
    def test_run_with_valid_cached_result(self, ssh_conn_exec):
        # add command and command result to cached commands
        curr_time = time.time()
        self.cli_access.cached_commands[COMMAND] = {
            "timestamp": curr_time,
            "result": RUN_RESULT
        }
        # mock the run command result
        ssh_conn_exec = MagicMock(return_value="")

        result = self.cli_access.run(COMMAND, COMPUTE_HOST['id'])
        # clear the cached command
        self.cli_access.cached_commands = {}
        self.assertNotEqual(result, "", "Can't get cached command result")

    def test_run_with_overtime_cached_result(self):
        # add overtime command and command result to cached commands
        curr_time = time.time()
        self.cli_access.cached_commands[COMMAND] = {
            "timestamp": curr_time - self.cli_access.cache_lifetime,
            "result": RUN_RESULT
        }
        # mock the run command result
        ssh_conn_exec = MagicMock(return_value="")

        result = self.cli_access.run(COMMAND, COMPUTE_HOST['id'])
        # clear the cached command
        self.cli_access.cached_commands = {}
        self.assertEqual(result, "", "Get the overtime cached data")

    def test_run_fetch_lines(self):
        cli_access = CliAccess()

        host = self.get_test_data({'type': 'host'})
        if not host:
            self.fail("No testing host in the database")

        result = cli_access.run_fetch_lines("ifconfig", host['id'])

        self.assertNotEqual(result, [], "Can't get ip configuration from command line")