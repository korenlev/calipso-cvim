import re
import time

from discover.fetcher import Fetcher
from discover.ssh_conn import SshConn
from utils.binary_converter import BinaryConverter


class CliAccess(BinaryConverter, Fetcher):
    config = None
    connections = {}
    ssh_cmd = "ssh -o StrictHostKeyChecking=no "
    call_count_per_con = {}
    max_call_count_per_con = 100
    cache_lifetime = 60  # no. of seconds to cache results
    cached_commands = {}

    def __init__(self):
        super().__init__()

    def run(self, cmd, ssh_to_host="", enable_cache=True):
        ssh_conn = SshConn(ssh_to_host)
        if ssh_to_host and ssh_to_host != ssh_conn.get_host():
            cmd = self.ssh_cmd + ssh_to_host + " sudo " + cmd
        curr_time = time.time()
        if enable_cache and cmd in self.cached_commands:
            # try to re-use output from last call
            cached = self.cached_commands[cmd]
            if cached["timestamp"] + self.cache_lifetime < curr_time:
                # result expired
                self.cached_commands.pop(cmd, None)
            else:
                # result is good to use - skip the SSH call
                self.log.info('CliAccess: ****** using cached result, ' +
                              'cmd: %s ******', cmd)
                return cached["result"]

        ret = ssh_conn.exec(cmd)
        self.cached_commands[cmd] = {"timestamp": curr_time, "result": ret}
        return ret

    def run_fetch_lines(self, cmd, ssh_to_host="", enable_cache=True):
        out = self.run(cmd, ssh_to_host, enable_cache)
        if not out:
            return []
        # first try to split lines by whitespace
        ret = out.splitlines()
        # if split by whitespace did not work, try splitting by "\\n"
        if len(ret) == 1:
            ret = [l for l in out.split("\\n") if l != ""]
        return ret

    # parse command output columns separated by whitespace
    # since headers can contain whitespace themselves,
    # it is the caller's responsibility to provide the headers
    def parse_cmd_result_with_whitespace(self, lines, headers, remove_first):
        if remove_first:
            # remove headers line
            del lines[:1]
        results = [self.parse_line_with_ws(line, headers)
                   for line in lines]
        return results

    # parse command output with "|" column separators and "-" row separators
    def parse_cmd_result_with_separators(self, lines):
        headers = self.parse_headers_line_with_separators(lines[1])
        # remove line with headers and formatting lines above it and below it
        del lines[:3]
        # remove formatting line in the end
        lines.pop()
        results = [self.parse_content_line_with_separators(line, headers)
                   for line in lines]
        return results

    # parse a line with columns separated by whitespace
    def parse_line_with_ws(self, line, headers):
        s = line if isinstance(line, str) else self.binary2str(line)
        parts = [word.strip() for word in s.split() if word.strip()]
        ret = {}
        for i, p in enumerate(parts):
            header = headers[i]
            ret[header] = p
        return ret

    # parse a line with "|" column separators
    def parse_line_with_separators(self, line):
        s = self.binary2str(line)
        parts = [word.strip() for word in s.split("|") if word.strip()]
        # remove the ID field
        del parts[:1]
        return parts

    def parse_headers_line_with_separators(self, line):
        return self.parse_line_with_separators(line)

    def parse_content_line_with_separators(self, line, headers):
        content_parts = self.parse_line_with_separators(line)
        content = {}
        for i in range(0, len(content_parts)):
            content[headers[i]] = content_parts[i]
        return content

    def merge_ws_spillover_lines(self, lines):
        # with WS-separated output, extra output sometimes spills to next line
        # detect that and add to the end of the previous line for our procesing
        pending_line = None
        fixed_lines = []
        # remove headers line
        for l in lines:
            if l[0] == '\t':
                # this is a spill-over line
                if pending_line:
                    # add this line to the end of the previous line
                    pending_line = pending_line.strip() + "," + l.strip()
            else:
                # add the previous pending line to the fixed lines list
                if pending_line:
                    fixed_lines.append(pending_line)
                # make current line the pending line
                pending_line = l
        if pending_line:
            fixed_lines.append(pending_line)
        return fixed_lines

    """
    given output lines from CLI command like 'ip -d link show',
    find lines belonging to section describing a specific interface
    parameters:
    - lines: list of strings, output of command
    - header_regexp: regexp marking the start of the section
    - end_regexp: regexp marking the end of the section
    """
    def get_section_lines(self, lines, header_regexp, end_regexp):
        if not lines:
            return []
        header_re = re.compile(header_regexp)
        start_pos = None
        # find start_pos of section
        line_count = len(lines)
        for line_num in range(0, line_count-1):
            matches = header_re.match(lines[line_num])
            if matches:
                start_pos = line_num
                break
        if not start_pos:
            return []
        # find end of section
        end_pos = line_count
        end_re = re.compile(end_regexp)
        for line_num in range(start_pos+1, end_pos-1):
            matches = end_re.match(lines[line_num])
            if matches:
                end_pos = line_num
                break
        return lines[start_pos:end_pos]

    def get_object_data(self, o, lines, regexps):
        """
        find object data in output lines from CLI command
        parameters:
        - o: object (dict), to which we'll add attributes with the data found
        - lines: list of strings
        - regexps: dict, keys are attribute names, values are regexp to match
                    for finding the value of the attribute
        """
        for line in lines:
            self.find_matching_regexps(o, line, regexps)
        for regexp_tuple in regexps:
            name = regexp_tuple['name']
            if 'name' not in o and 'default' in regexp_tuple:
                o[name] = regexp_tuple['default']

    def find_matching_regexps(self, o, line, regexps):
        for regexp_tuple in regexps:
            name = regexp_tuple['name']
            regex = regexp_tuple['re']
            regex = re.compile(regex)
            matches = regex.match(line)
            if matches:
                o[name] = matches.group(1)
