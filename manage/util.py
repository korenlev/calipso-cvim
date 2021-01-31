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
import re
from collections import namedtuple
from typing import Optional, List

from dateutil.relativedelta import relativedelta


class Interval(namedtuple('Schedule', field_names=["number", "unit"])):
    REGEX = re.compile("(?P<number>\d+)(?P<unit>[ymwdh])")  # add ('M', S') for debugging
    __slots__ = ()

    def __str__(self):
        return "{}{}".format(self.number, self.unit)


DEFAULT_INTERVAL = Interval(number=1, unit='d')


def parse_interval(interval_str: str, default_interval: Interval = DEFAULT_INTERVAL) -> Interval:
    interval_match = Interval.REGEX.match(interval_str)

    if not interval_match:
        return default_interval

    number = int(interval_match.groupdict()['number'])
    unit = interval_match.groupdict()['unit']

    return Interval(
        number=number if number > 0 else default_interval.number,
        unit=unit
    )


def get_next_schedule(last_schedule: datetime.datetime, interval: Interval,
                      align_time: bool = True, allow_past_schedules: bool = False) -> Optional[datetime.datetime]:
    """
        Calculate next schedule given last schedule datetime and a valid time interval
    :param last_schedule: last performed schedule
    :param interval: operation interval in form of {number}{time division}
        y - year, m - month, w - week, d - day, h - hour
    :param align_time: set to True if lesser time divisions
        than the one selected in interval are to be aligned to 0
        (e.g., if interval is set to 1d [day], then next operation will be performed at 0:00 next day,
               if interval is set to 1h [hour], then next operation will be performed at 00 minutes of next hour,
               etc.)
    :param allow_past_schedules: Defines whether next schedule can be in the past,
        or interval should be cycled until next schedule is in the future.
    :return: Next schedule datetime object
    """

    number, unit = interval.number, interval.unit

    delta = relativedelta(years=number if unit == "y" else 0,
                          months=number if unit == "m" else 0,
                          weeks=number if unit == "w" else 0,
                          days=number if unit == "d" else 0,
                          hours=number if unit == "h" else 0,
                          minutes=number if unit == "M" else 0,
                          seconds=number if unit == "S" else 0)

    def _calculate_next_schedule(prev_schedule: datetime.datetime) -> datetime.datetime:
        _next_schedule = (prev_schedule + delta).replace(microsecond=0)

        if align_time and unit != "S":
            _next_schedule = _next_schedule.replace(second=0)
            if unit != "M":
                _next_schedule = _next_schedule.replace(minute=0)
                if unit != "h":
                    _next_schedule = _next_schedule.replace(hour=0)
                    if unit == "w":
                        _next_schedule -= relativedelta(days=_next_schedule.isoweekday() - 1)
                    elif unit != "d":
                        _next_schedule = _next_schedule.replace(day=1)
                        if unit != "m":
                            _next_schedule = _next_schedule.replace(month=1)
        return _next_schedule

    next_schedule = _calculate_next_schedule(prev_schedule=last_schedule)
    if allow_past_schedules:
        return next_schedule

    while next_schedule < datetime.datetime.utcnow():
        next_schedule = _calculate_next_schedule(prev_schedule=next_schedule)
    return next_schedule


scan_fields = ["clear", "env_name", "es_index", "implicit_links", "inventory", "log_level",
               "object_id", "scan_only_cliques", "scan_only_inventory", "scan_only_links"]
scheduled_scan_fields = ["clear", "env_name", "es_index", "implicit_links", "log_level", "recurrence",
                         "scan_only_cliques", "scan_only_inventory", "scan_only_links", "scheduled_timestamp"]


def _clean_request(request: dict, fields: List[str]) -> dict:
    res = {}
    for field in fields:
        if field not in request:
            continue
        value = request[field]
        if isinstance(value, datetime.datetime):
            value = value.isoformat()
        res[field] = value
    return res


def clean_scan_request(request: dict, coll: str = "scans") -> dict:
    """
        Clean the scan request payload for remote API.
        TODO: API versions support (payloads may change over time)
    :param request: scan request document
    :param coll: collection to send request to. Valid options: scans, scheduled_scans
    :throws ValueError: when wrong collection is specified
    :return: scan request payload adapted for remote API
    """
    if coll == "scans":
        return _clean_request(request=request, fields=scan_fields)
    elif coll == "scheduled_scans":
        return _clean_request(request=request, fields=scheduled_scan_fields)
    else:
        raise ValueError("Unsupported collection for scan request: {}".format(coll))
