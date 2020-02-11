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
