###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################

from discover.fetchers.api.api_access import ApiAccess
from discover.fetchers.db.db_access import DbAccess
from utils.cli_access import CliAccess
from utils.ssh_connection import SshError


class CliFetchHostDetails(CliAccess):

    def fetch_host_os_details(self, doc):
        cmd = 'cat /etc/os-release && echo "ARCHITECURE=`arch`"'
        try:
            lines = self.run_fetch_lines(cmd, ssh_to_host=doc['host'])
        except SshError as e:
            self.log.error('{}: {}', cmd, str(e))
        os_attributes = {}
        attributes_to_fetch = {
            'NAME': 'name',
            'VERSION': 'version',
            'ID': 'ID',
            'ID_LIKE': 'ID_LIKE',
            'ARCHITECURE': 'architecure'
        }
        for attr in attributes_to_fetch:
            matches = [l for l in lines if l.startswith(attr + '=')]
            if matches:
                line = matches[0]
                attr_name = attributes_to_fetch[attr]
                os_attributes[attr_name] = line[line.index('=')+1:].strip('"')
        if os_attributes:
            doc['OS'] = os_attributes
