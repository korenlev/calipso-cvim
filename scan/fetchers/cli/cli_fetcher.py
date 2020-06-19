###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import json
from typing import Union, Optional

from base.fetcher import Fetcher
from base.utils.cli_access import CliAccess
from base.utils.exceptions import CredentialsError, HostAddressError, SshError


class CliFetcher(Fetcher, CliAccess):

    @staticmethod
    def validate_host_ssh(host: dict) -> bool:
        """
            Validate host SSH capabilities.
            Currently, CVIM ironic nodes do not support SSH
        :param host: host document
        :return: whether SSH is supported for host
        """
        # SSH to ironic hosts is not available
        if not host or host.get("ironic") is True:
            return False
        return True

    def get_host_route(self, host_id: str) -> Optional[str]:
        """
            Validate host and return a routable hostname or ip address (for CVIM mgmt nodes)
        :param host_id: host document id
        :return: hostname or ip address for SSH access; or None if host doesn't support SSH
        """
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not self.validate_host_ssh(host):
            return None
        if host.get("management_node") is True:
            ip_address = host.get("ip_address")
            if ip_address:
                return ip_address
            else:
                self.log.error("IP address is undefined for mgmt node host '{}'. "
                               "Defaulting to host name".format(host['id']))
                return host['id']
        return host['id']

    def run(self, cmd: str, ssh_to_host: str = "", find_route_to_host: bool = True,
            enable_cache: bool = True, on_gateway: bool = False, use_sudo: bool = True, use_ssh_key: bool = True,
            log_errors: bool = True, raise_errors: bool = True) -> str:
        try:
            output = super().run(cmd,
                                 ssh_to_host=ssh_to_host,
                                 find_route_to_host=find_route_to_host,
                                 enable_cache=enable_cache,
                                 use_sudo=use_sudo,
                                 use_ssh_key=use_ssh_key,
                                 log_errors=log_errors)
        except (SshError, CredentialsError, HostAddressError) as e:
            msg = 'error running command {} (host:{}): {}'.format(cmd, ssh_to_host, e)
            if log_errors:
                self.log.error(msg)
            if raise_errors:
                raise SshError(msg)
            else:
                return ""
        return output

    def run_fetch_lines(self, cmd: str, ssh_to_host: str = "", find_route_to_host: bool = True,
                        enable_cache: bool = True, use_sudo: bool = True, use_ssh_key: bool = True,
                        log_errors: bool = True, raise_errors: bool = True) -> list:
        try:
            lines = super().run_fetch_lines(cmd,
                                            ssh_to_host=ssh_to_host,
                                            find_route_to_host=find_route_to_host,
                                            enable_cache=enable_cache,
                                            use_sudo=use_sudo,
                                            use_ssh_key=use_ssh_key,
                                            log_errors=False)
        except (SshError, CredentialsError, HostAddressError) as e:
            msg = 'error running command {} (host:{}): {}'.format(cmd, ssh_to_host, e)
            if log_errors:
                self.log.error(msg)
            if raise_errors:
                raise SshError(msg)
            else:
                return []
        return lines

    def run_fetch_json_response(self, cmd: str, ssh_to_host: str = "", find_route_to_host: bool = True,
                                enable_cache: bool = True, use_sudo: bool = True, use_ssh_key: bool = False,
                                log_errors: bool = True, raise_errors: bool = True) -> Union[dict, list]:
        output = self.run(cmd=cmd, ssh_to_host=ssh_to_host, find_route_to_host=find_route_to_host,
                          enable_cache=enable_cache, use_sudo=use_sudo, use_ssh_key=use_ssh_key,
                          log_errors=log_errors, raise_errors=raise_errors)
        if not output:
            return {}
        try:
            return json.loads(output)
        except (ValueError, TypeError) as e:
            msg = 'error parsing json from command response {} (host:{}): {}'.format(cmd, ssh_to_host, e)
            if log_errors:
                self.log.error(msg)
            if raise_errors:
                raise e
            else:
                return {}
