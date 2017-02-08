import dateutil.parser

from api.responders.responder_base import ResponderBase
from bson.objectid import ObjectId
from api.etc.data_validate import DataValidate
from datetime import datetime


class Messages(ResponderBase):

    def __init__(self):
        super().__init__()
        self.id = "id"
        self.collection = 'messages'

    def on_get(self, req, resp):
        self.log.debug("Getting messages from messages")
        filters = self.parse_query_params(req.params)
        messages_severity = self.get_constants_by_name("messages_severity")
        object_types = self.get_constants_by_name("object_types")
        filters_requirements = {
            'env_name': self.get_validate_requirement(str, mandatory=True),
            'source_system': self.get_validate_requirement(str),
            'id': self.get_validate_requirement(str),
            'level': self.get_validate_requirement(str, validate=DataValidate.LIST, requirement=messages_severity),
            'related_object': self.get_validate_requirement(str),
            'related_object_type': self.get_validate_requirement(str, validate=DataValidate.LIST, requirement=object_types),
            'start_time': self.get_validate_requirement(str),
            'end_time': self.get_validate_requirement(str),
            'page': self.get_validate_requirement(int, True),
            'page_size': self.get_validate_requirement(int, True)
        }
        self.validate_filters(filters, filters_requirements)

        page, page_size = self.get_pagination(filters)
        try:
            self.check_and_convert_datetime(filters)
        except Exception as e:
            self.bad_request(str(e))

        query = self.build_query(filters)

        if self.id in query:
            message = self.get_object_by_id(self.collection, query, [ObjectId, datetime], self.id)
            if not message:
                self.not_found()
            self.set_successful_response(resp, message)
        else:
            objects_ids = self.get_object_ids(self.collection, query, page, page_size, self.id)
            self.set_successful_response(resp, {'messages': objects_ids})

    def check_and_convert_datetime(self, filters):
        start_time = filters.get('start_time')
        end_time = filters.get('end_time')

        if start_time:
            start_time = self.replace_space_with_plus_sign(start_time)
            try:
                filters['start_time'] = dateutil.parser.parse(start_time)
            except Exception:
                raise ValueError("start_time follows ISO 8610 date and time format,"
                                 "YYYY-MM-DDThh:mm:ss.sss+hhmm")

        if end_time:
            end_time = self.replace_space_with_plus_sign(end_time)
            try:
                filters['end_time'] = dateutil.parser.parse(end_time)
            except Exception:
                raise ValueError("end_time follows ISO 8610 date and time format,"
                                 "YYYY-MM-DDThh:mm:ss.sss+hhmm")

    # the plus sign is treated as space in the query string, after
    # we get the string replace it with '+'
    def replace_space_with_plus_sign(self, time):
        time = time.replace(" ", "+")
        return time

    def build_query(self, filters):
        query = {}
        filters_keys = ['source_system', 'id', 'level', 'related_object', 'related_object_type']
        start_time = filters.get('start_time')
        end_time = filters.get('end_time')
        env_name = filters.get('env_name')
        self.update_query_with_filters(filters, filters_keys, query)

        if start_time:
            query['timestamp'] = {"$gte": start_time}

        if end_time:
            if 'timestamp' in query:
                query['timestamp'].update({"$lte": end_time})
            else:
                query['timestamp'] = {"$lte": end_time}

        query['environment'] = env_name
        return query