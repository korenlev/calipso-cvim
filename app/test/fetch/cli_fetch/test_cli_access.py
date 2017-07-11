import time

from test.fetch.cli_fetch.test_data.cli_access import *
from test.fetch.test_fetch import TestFetch
from unittest.mock import MagicMock, patch
from utils.cli_access import CliAccess


class TestCliAccess(TestFetch):

    def setUp(self):
        self.configure_environment()
        self.cli_access = CliAccess()

    @patch("utils.ssh_conn.SshConn.exec")
    def test_run(self, ssh_conn_exec):
        # mock the command result
        ssh_conn_exec.return_value = RUN_RESULT

        result = self.cli_access.run(COMMAND, COMPUTE_HOST_ID)

        # clear the cached command
        self.cli_access.cached_commands = {}
        self.assertNotEqual(result, "", "Can't get ip configuration from command line")

    @patch("utils.ssh_conn.SshConn.exec")
    def test_run_with_valid_cached_result(self, ssh_conn_exec):
        # add command and command result to cached commands
        curr_time = time.time()
        self.cli_access.cached_commands[CACHED_COMMAND] = {
            "timestamp": curr_time,
            "result": RUN_RESULT
        }
        # mock the run command result
        ssh_conn_exec.return_value = ""

        result = self.cli_access.run(COMMAND, COMPUTE_HOST_ID)
        # clear the cached command
        self.cli_access.cached_commands = {}
        self.assertNotEqual(result, "", "Can't get cached command result")

    @patch("utils.ssh_conn.SshConn.exec")
    def test_run_with_expired_cached_result(self, ssh_conn_exec):
        # add overtime command and command result to cached commands
        curr_time = time.time()
        self.cli_access.cached_commands[CACHED_COMMAND] = {
            "timestamp": curr_time - self.cli_access.cache_lifetime,
            "result": RUN_RESULT
        }
        # mock the run command result
        ssh_conn_exec.return_value = ""

        result = self.cli_access.run(COMMAND, COMPUTE_HOST_ID)
        # clear the cached command
        self.cli_access.cached_commands = {}
        self.assertEqual(result, "", "Get the overtime cached data")

    def test_run_fetch_lines(self):
        # store the original run method
        original_run = self.cli_access.run
        # mock the result from run method
        self.cli_access.run = MagicMock(return_value=RUN_RESULT)

        result = self.cli_access.run_fetch_lines(COMMAND, COMPUTE_HOST_ID)

        # reset run method
        self.cli_access.run = original_run

        self.assertNotEqual(len(result), 1, "Can't split the command result into lines")

    def test_run_fetch_lines_with_empty_command_result(self):
        # store the original run method
        original_run = self.cli_access.run
        # mock the empty result from run method
        self.cli_access.run = MagicMock(return_value="")

        result = self.cli_access.run_fetch_lines(COMMAND, COMPUTE_HOST_ID)

        # reset run method
        self.cli_access.run = original_run

        self.assertEqual(result, [], "Can't get empty array when the command result is empty")

    def test_merge_ws_spillover_lines(self):
        fixed_lines = self.cli_access.merge_ws_spillover_lines(LINES_FOR_FIX)
        self.assertEqual(fixed_lines, FIXED_LINES)

    def test_parse_line_with_ws(self):
        parse_line = self.cli_access.parse_line_with_ws(LINE_FOR_PARSE, HEADERS)
        self.assertEqual(parse_line, PARSED_LINE, "Can't parse the line with ws")

    def test_parse_cmd_result_with_whitespace(self):
        result = self.cli_access.parse_cmd_result_with_whitespace(FIXED_LINES, HEADERS, remove_first=False)
        self.assertNotEqual(result, [], "Can't parse the cmd result with whitespace")
