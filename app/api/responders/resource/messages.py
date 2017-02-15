from datetime import datetime

from api.responders.responder_base import ResponderBase
from api.validation.data_validate import DataValidate
from bson.objectid import ObjectId
from dateutil import parser


class Messages(ResponderBase):
    def __init__(self):
        super().__init__()
        self.ID = "id"
        self.COLLECTION = 'messages'

    def on_get(self, req, resp):
        self.log.debug("Getting messages from messages")
        filters = self.parse_query_params(req.params)
        messages_severity = self.get_constants_by_name("messages_severity")
        object_types = self.get_constants_by_name("object_types")
        filters_requirements = {
            'env_name': self.require(str, mandatory=True),
            'source_system': self.require(str),
            'id': self.require(str),
            'level': self.require(str, validate=DataValidate.LIST,
                                  requirement=messages_severity),
            'related_object': self.require(str),
            'related_object_type': self.require(str, validate=DataValidate.LIST,
                                                requirement=object_types),
            'start_time': self.require(str),
            'end_time': self.require(str),
            'page': self.require(int, True),
            'page_size': self.require(int, True)
        }
        self.validate_query_data(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)
        self.check_and_convert_datetime(filters)

        query = self.build_query(filters)
        if self.ID in query:
            message = self.get_object_by_id(self.COLLECTION, query,
                                            [ObjectId, datetime], self.ID)
            if not message:
                self.not_found()
            self.set_successful_response(resp, message)
        else:
            objects_ids = self.get_object_ids(self.COLLECTION, query,
                                              page, page_size, self.ID)
            self.set_successful_response(resp, {'messages': objects_ids})

    def check_and_convert_datetime(self, filters):
        start_time = filters.get('start_time')
        end_time = filters.get('end_time')

        if start_time:
            start_time = start_time.replace(' ', '+')
            try:
                filters['start_time'] = parser.parse(start_time)
            except Exception:
                self.bad_request("start_time must follow ISO 8610 date and time format,"
                                 "YYYY-MM-DDThh:mm:ss.sss+hhmm")

        if end_time:
            end_time = end_time.replace(' ', '+')
            try:
                filters['end_time'] = parser.parse(end_time)
            except Exception:
                self.bad_request("end_time must follow ISO 8610 date and time format,"
                                 "YYYY-MM-DDThh:mm:ss.sss+hhmm")

    def build_query(self, filters):
        query = {}
        filters_keys = ['source_system', 'id', 'level', 'related_object',
                        'related_object_type']
        self.update_query_with_filters(filters, filters_keys, query)
        start_time = filters.get('start_time')
        if start_time:
            query['timestamp'] = {"$gte": start_time}
        end_time = filters.get('end_time')
        if end_time:
            if 'timestamp' in query:
                query['timestamp'].update({"$lte": end_time})
            else:
                query['timestamp'] = {"$lte": end_time}
        query['environment'] = filters['env_name']
        return query
