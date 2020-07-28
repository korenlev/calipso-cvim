###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from datetime import datetime
from dateutil import tz
from dateutil.relativedelta import relativedelta

from api.responders.responder_base import ResponderBase


class Timezone(ResponderBase):
    def on_get(self, req, resp):
        self.log.debug("Getting timezone")
        filters = self.parse_query_params(req)
        filters_requirements = {
            'env_name': self.require(str),
        }
        self.validate_query_data(filters, filters_requirements)

        env_name = filters.get("env_name")
        tzinfo = None
        if env_name:
            environment = self.get_single_object(collection="environments_config",
                                                 query={"name": env_name})
            if not environment:
                self.bad_request("Unknown environment: {}".format(env_name))

            tzinfo = tz.gettz(environment.get("timezone"))
        if not tzinfo:
            tzinfo = tz.tzlocal()

        local_time = datetime.now(tz=tzinfo)
        lt_offset = local_time.utcoffset()
        utc_offset = relativedelta(days=lt_offset.days, seconds=lt_offset.seconds)

        self.set_ok_response(resp, {
            "tz_name": local_time.tzname(),
            "utc_offset": {
                "hours": utc_offset.days * 24 + utc_offset.hours,
                "minutes": utc_offset.minutes
            }
        })
