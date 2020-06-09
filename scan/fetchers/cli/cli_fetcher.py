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
from typing import Union

from base.fetcher import Fetcher
from base.utils.cli_access import CliAccess
from base.utils.exceptions import CredentialsError, HostAddressError, SshError


class CliFetcher(Fetcher, CliAccess):

    def run(self, cmd: str, ssh_to_host: str = "", enable_cache: bool = True, on_gateway: bool = False,
            use_sudo: bool = True, use_ssh_key: bool = True, log_errors: bool = True,
            raise_errors: bool = True) -> str:
        try:
            output = super().run(cmd=cmd, ssh_to_host=ssh_to_host, enable_cache=enable_cache,
                                 use_sudo=use_sudo, use_ssh_key=use_ssh_key, log_errors=log_errors)
        except (SshError, CredentialsError, HostAddressError) as e:
            msg = 'error running command {} (host:{}): {}'.format(cmd, ssh_to_host, e)
            if log_errors:
                self.log.error(msg)
            if raise_errors:
                raise SshError(msg)
            else:
                return ""
        return output

    def run_fetch_lines(self, cmd: str, ssh_to_host: str = "", enable_cache: bool = True,
                        use_sudo: bool = True, use_ssh_key: bool = True, log_errors: bool = True,
                        raise_errors: bool = True) -> list:
        try:
            lines = super().run_fetch_lines(cmd,
                                            ssh_to_host=ssh_to_host,
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

    def run_fetch_json_response(self, cmd: str, ssh_to_host: str = "", enable_cache: bool = True,
                                use_sudo: bool = True, use_ssh_key: bool = False,
                                log_errors: bool = True, raise_errors: bool = True) -> Union[dict, list]:
        output = self.run(cmd=cmd, ssh_to_host=ssh_to_host,
                          enable_cache=enable_cache, use_sudo=use_sudo, use_ssh_key=use_ssh_key,
                          log_errors=log_errors, raise_errors=raise_errors)
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
