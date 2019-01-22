###############################################################################
# Copyright (c) 2017-2019 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import requests

from base.fetcher import Fetcher
from base.utils.configuration import Configuration


class ApiAccessBase(Fetcher):

    CONNECT_TIMEOUT = 5

    def __init__(self, api_name=None, config=None, enabled=True):
        super().__init__()

        if not enabled:
            self.config = None
            self.api_config = None
            self.host = None
            self.port = None
            return

        if api_name is None:
            raise ValueError('ApiAccessBase: api_name must be defined')
        self.config = {api_name: config} if config else Configuration()
        self.api_config = self.config.get(api_name)
        if self.api_config is None:
            raise ValueError('ApiAccessBase: section "{}" missing in config'
                             .format(api_name))
        self.host = self.api_config.get('host', '')
        self.port = self.api_config.get('port', '80')
        if not (self.host and self.port):
            raise ValueError('Missing definition of host or port ' +
                             'for {} API access'
                             .format(api_name))

    def get_url(self, req_url, headers):
        response = requests.get(req_url, headers=headers)
        if response.status_code != requests.codes.ok:
            # some error happened
            if 'reason' in response:
                msg = ', reason: {}'.format(response.reason)
            else:
                msg = ', response: {}'.format(response.text)
            self.log.error('req_url: {} {}'.format(req_url, msg))
            return None
        ret = response.json()
        return ret