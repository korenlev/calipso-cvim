import time

from fetcher import Fetcher
from ssh_conn import SshConn


class CliAccess(Fetcher):
    config = None
    connections = {}
    ssh_cmd = "ssh -o StrictHostKeyChecking=no "
    call_count_per_con = {}
    max_call_count_per_con = 100
    cache_lifetime = 60  # no. of seconds to cache results
    cached_commands = {}

    def __init__(self):
        super().__init__()

    def run(self, cmd, ssh_to_host=""):
        ssh_conn = SshConn(ssh_to_host)
        if ssh_to_host and ssh_to_host != ssh_conn.get_host():
            cmd = self.ssh_cmd + ssh_to_host + " sudo " + cmd
        curr_time = time.time()
        if cmd in self.cached_commands:
            # try to re-use output from last call
            cached = self.cached_commands[cmd]
            if cached["timestamp"] + self.cache_lifetime < curr_time:
                # result expired
                self.cached_commands.pop(cmd, None)
            else:
                # result is good to use - skip the SSH call
                self.log.info("CliAccess: ****** using cached result, cmd: %s ******",
                              cmd)
                return cached["result"]

        ret = ssh_conn.exec(cmd)
        self.cached_commands[cmd] = {"timestamp": curr_time, "result": ret}
        return ret

    def run_fetch_lines(self, cmd, ssh_to_host=""):
        out = self.run(cmd, ssh_to_host)
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
        # with WS-separated output, extra output is sometimes spilled to next line
        # detect that and add them to the end of the previous line for our procesing
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
