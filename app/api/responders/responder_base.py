import json

from api.backends.mongo_mgr import MongoMgr
from api.exceptions import exceptions
from api.validation.data_validate import DataValidate
from utils.dict_naming_converter import DictNamingConverter
from utils.logger import Logger
from utils.util import Util


class ResponderBase(DataValidate, Util, Logger, DictNamingConverter):

    def __init__(self):
        super().__init__()
        self.mongo_mgr = MongoMgr()

    def set_successful_response(self, resp, body="", status="200"):
        if not isinstance(body, str):
            try:
                body = json.dumps(body)
            except Exception as e:
                self.log.exception(e)
                raise ValueError("The response body should be a string")
        resp.status = status
        resp.body = body

    def set_error_response(self, title="", code="", message="", body=""):
        if body:
            raise exceptions.OSDNAApiException(code, body, message)
        body = {
            "error": {
                "message": message,
                "code": code,
                "title": title
            }
        }
        body = json.dumps(body)
        raise exceptions.OSDNAApiException(code, body, message)

    def not_found(self, message="Requested resource not found"):
        self.set_error_response("Not Found", "404", message)

    def conflict(self, message="The posted data conflicts with the existing data"):
        self.set_error_response("Conflict", "409", message)

    def bad_request(self, message="Invalid request content"):
        self.set_error_response("Bad Request", "400", message)

    def unauthorized(self, message="Request requires authorization"):
        self.set_error_response("Unauthorized", "401", message)

    def validate_query_data(self, filters, filters_requirements):
        # validate the filters in the query string
        error_message = self.validate_data(filters, filters_requirements)
        if error_message:
            self.bad_request(error_message)

    def check_environment_name(self, env_name):
        query = {"name": env_name}
        objects = self.read("environments_config", query)
        if not objects:
            return False
        return True

    def get_object_by_id(self, collection, query, stringify_types, id):
        objs = self.read(collection, query)
        if not objs:
            return None
        obj = objs[0]
        self.stringify_object_values_by_types(obj, stringify_types)
        if id is "_id":
            obj['id'] = obj.get('_id')
        return obj

    def get_object_ids(self, collection, query, page, page_size, id):
        objects = self.read(collection, query, {id: True}, page, page_size)
        objects_ids = [str(obj[id]) for obj in objects]
        return objects_ids

    def parse_query_params(self, params):
        return self.change_dict_naming_convention(params, self.replace_colon_with_dot)

    def replace_colon_with_dot(self, s):
        return s.replace(':', '.')

    def get_pagination(self, filters):
        page_size = filters.get('page_size', 1000)
        page = filters.get('page', 0)
        return page, page_size

    def update_query_with_filters(self, filters, filters_keys, query):
        for filter_key in filters_keys:
            filter = filters.get(filter_key)
            if filter:
                query.update({filter_key: filter})

    def get_content_from_request(self, req):
        error = ""
        content = ""
        if not req.content_length:
            return {}
        data = req.stream.read()
        content_string = data.decode()
        try:
            content = json.loads(content_string)
        except Exception:
            error = "The request can not be fulfilled due to bad syntax"
        return error, content

    def get_constants_by_name(self, name):
        constants = self.mongo_mgr.get_collection('constants').\
            find_one({"name": name})
        return [d['value'] for d in constants['data']]

    def read(self, collection, matches={}, projection=None, skip=0, limit=1000):
        collection = self.mongo_mgr.get_collection(collection)
        skip *= limit
        query = collection.find(matches, projection).skip(skip).limit(limit)
        return list(query)

    def write(self, document, collection="inventory"):
        self.mongo_mgr.get_collection(collection).insert_one(document)

    def aggregate(self, pipeline, collection):
        collection = self.mongo_mgr.get_collection(collection)
        data = collection.aggregate(pipeline)
        return list(data)
