###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import time

import re

from base.utils.cli_dist_translator import CliDistTranslator
from base.utils.configuration import Configuration
from base.utils.logging.console_logger import ConsoleLogger
from base.utils.logging.logger import Logger
from base.utils.ssh_tunnel_connection import SshTunnelConnection, MasterHostDetails
from base.utils.string_utils import binary2str


class CliAccess:
    LOG_LEVEL = Logger.INFO

    MULTI_COMMAND_SEPARATOR = ';;;'

    call_count_per_con = {}  # TODO: deprecate?
    max_call_count_per_con = 100  # TODO: deprecate?
    cache_lifetime = 3600  # no. of seconds to cache results
    cached_commands = {}

    def __init__(self):
        super().__init__()
        self.configuration = Configuration()
        self.ssh_connection = SshTunnelConnection(master_host_details=MasterHostDetails.from_configuration())
        self.log = ConsoleLogger(name="CliAccess", level=self.LOG_LEVEL)

    def get_host_route(self, host_id: str) -> str:
        """
            To be overridden in subclasses
        :param host_id: host id/name to lookup route for
        :return: routable ip or hostname
        """
        return host_id

    def run(self, cmd: str, ssh_to_host: str = "", find_route_to_host: bool = True,
            enable_cache: bool = True, use_sudo: bool = True, use_ssh_key: bool = True,
            log_errors: bool = True):
        commands = self.adapt_cmd_to_env(cmd=cmd, use_sudo=use_sudo)
        out = ''

        if find_route_to_host and ssh_to_host:
            host_route = self.get_host_route(host_id=ssh_to_host)
            if not host_route:
                return ""
        else:
            host_route = ssh_to_host

        for c in commands:
            ret = self.run_single_command(cmd=c, ssh_to_host=host_route, enable_cache=enable_cache)
            out += ret if ret is not None else ''
        return out

    def run_single_command(self, cmd: str, ssh_to_host: str = "", enable_cache: bool = True) -> str:
        curr_time = time.time()
        cmd_path = '{},{}'.format(ssh_to_host, cmd)
        if enable_cache and cmd_path in self.cached_commands:
            # try to re-use output from last call
            cached = self.cached_commands[cmd_path]
            if cached["timestamp"] + self.cache_lifetime < curr_time:
                # result expired
                self.cached_commands.pop(cmd_path, None)
            else:
                # result is good to use - skip the SSH call
                self.log.info('CliAccess: ****** using cached result, '
                              'host: {}, cmd: {} ******'.format(ssh_to_host, cmd))
                return cached["result"]

        self.log.info('CliAccess: host: {}, cmd: {}'.format(ssh_to_host, cmd))
        ret = self.ssh_connection.exec_on_host(cmd, host=ssh_to_host)
        self.cached_commands[cmd_path] = {"timestamp": curr_time, "result": ret}
        return ret

    def run_fetch_lines(self, cmd: str, ssh_to_host: str = "", find_route_to_host: bool = True,
                        enable_cache: bool = True, use_sudo: bool = True, use_ssh_key: bool = True,
                        log_errors: bool = True):
        out = self.run(cmd=cmd, ssh_to_host=ssh_to_host, find_route_to_host=find_route_to_host,
                       enable_cache=enable_cache, use_sudo=use_sudo, use_ssh_key=use_ssh_key,
                       log_errors=log_errors)
        if not out:
            return []
        # first try to split lines by whitespace
        ret = out.splitlines()
        # if split by whitespace did not work, try splitting by "\\n"
        if len(ret) == 1:
            ret = [line for line in out.split("\\n") if line != ""]
        return ret

    @staticmethod
    def handle_split_cmd(cmd: str):
        return cmd.split(CliAccess.MULTI_COMMAND_SEPARATOR)

    def adapt_cmd_to_env(self, cmd: str, use_sudo: bool, remote_user: str = "root"):
        cmd = self.adapt_cmd_to_dist(cmd)
        commands = self.handle_split_cmd(cmd)
        return [self._adapt_cmd_to_env(cmd=c, use_sudo=use_sudo, remote_user=remote_user) for c in commands]

    def _adapt_cmd_to_env(self, cmd: str, remote_user: str = "root", use_sudo: bool = False):
        if self.configuration.environment["distribution"] == "Mercury" or remote_user == 'root':
            use_sudo = False
        if use_sudo and not cmd.strip().startswith("sudo "):
            cmd = "sudo {}".format(cmd)
        return cmd

    def adapt_cmd_to_dist(self, cmd):
        env_conf = self.configuration.get_env_config()
        translator = CliDistTranslator(env_conf)
        cmd = translator.translate(cmd)
        return cmd

    #######################
    # CONVENIENCE METHODS #
    #######################

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
        s = line if isinstance(line, str) else binary2str(line)
        parts = [word.strip() for word in s.split() if word.strip()]
        ret = {}
        for i, p in enumerate(parts):
            header = headers[i]
            ret[header] = p
        return ret

    # parse a line with "|" column separators
    def parse_line_with_separators(self, line):
        s = binary2str(line)
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

    @staticmethod
    def merge_ws_spillover_lines(lines):
        # with WS-separated output, extra output sometimes spills to next line
        # detect that and add to the end of the previous line for our processing
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
    @staticmethod
    def get_section_lines(lines, header_regexp, end_regexp):
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
            if name not in o and 'default' in regexp_tuple:
                o[name] = regexp_tuple['default']

    def find_matching_regexps(self, o, line, regexps):
        for regexp_tuple in regexps:
            name = regexp_tuple['name']
            regex = regexp_tuple['re']
            regex = re.compile(regex)
            matches = regex.search(line)
            if matches and name not in o:
                try:
                    o[name] = matches.group(1)
                except IndexError:
                    self.log.error('failed to find group 1 in match, {}'
                                   .format(str(regexp_tuple)))

    @classmethod
    def reset_cache(cls):
        cls.cached_commands = {}
