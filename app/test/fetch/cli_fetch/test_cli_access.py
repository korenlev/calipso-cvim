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
        ssh_conn_exec.return_value = RUN_RESULT

        result = self.cli_access.run(COMMAND, COMPUTE_HOST['id'])

        # clear the cached command
        self.cli_access.cached_commands = {}
        print(result)
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
        ssh_conn_exec.return_value = ""

        result = self.cli_access.run(COMMAND, COMPUTE_HOST['id'])
        # clear the cached command
        self.cli_access.cached_commands = {}
        self.assertNotEqual(result, "", "Can't get cached command result")

    @patch("discover.ssh_conn.SshConn.exec")
    def test_run_with_expired_cached_result(self, ssh_conn_exec):
        # add overtime command and command result to cached commands
        curr_time = time.time()
        self.cli_access.cached_commands[CACHED_COMMAND] = {
            "timestamp": curr_time - self.cli_access.cache_lifetime,
            "result": RUN_RESULT
        }
        # mock the run command result
        ssh_conn_exec.return_value = ""

        result = self.cli_access.run(COMMAND, COMPUTE_HOST['id'])
        # clear the cached command
        self.cli_access.cached_commands = {}
        self.assertEqual(result, "", "Get the overtime cached data")

    def test_run_fetch_lines(self):
        # store the original run method
        original_run = self.cli_access.run
        # mock the result from run method
        self.cli_access.run = MagicMock(return_value=RUN_RESULT)

        result = self.cli_access.run_fetch_lines(COMMAND, COMPUTE_HOST['id'])

        # reset run method
        self.cli_access.run = original_run

        self.assertNotEqual(len(result), 1, "Can't split the command result into lines")

    def test_run_fetch_lines_with_empty_command_result(self):
        # store the original run method
        original_run = self.cli_access.run
        # mock the empty result from run method
        self.cli_access.run = MagicMock(return_value="")

        result = self.cli_access.run_fetch_lines(COMMAND, COMPUTE_HOST['id'])

        # reset run method
        self.cli_access.run = original_run

        self.assertEqual(result, [], "Can't get empty array when the command result is empty")
