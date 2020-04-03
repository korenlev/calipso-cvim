###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import datetime

import dateutil.tz

from api.responders.responder_base import ResponderBase


class Timezone(ResponderBase):
    def on_get(self, req, resp):
        self.log.debug("Getting timezone")

        local_time = datetime.datetime.now(dateutil.tz.tzlocal())
        offset_seconds = local_time.utcoffset().total_seconds()
        offset_hours = offset_seconds // 3600
        offset_minutes = offset_hours * 3600 - offset_seconds
        self.set_ok_response(resp, {
            "tz_name": local_time.tzname(),
            "utc_offset": {
                "hours": offset_hours,
                "minutes": offset_minutes
            }
        })
