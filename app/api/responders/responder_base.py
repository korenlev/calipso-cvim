import json


from api.exceptions import exceptions
from api.validation.data_validate import DataValidate
from dateutil import parser
from utils.dict_naming_converter import DictNamingConverter
from utils.inventory_mgr import InventoryMgr
from utils.logger import Logger


class ResponderBase(DataValidate, Logger, DictNamingConverter):
    UNCHANGED_COLLECTIONS = ["monitoring_config_templates",
                             "environments_config",
                             "messages"]

    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def set_successful_response(self, resp, body="", status="200"):
        if not isinstance(body, str):
            try:
                body = self.jsonify(body)
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
        body = self.jsonify(body)
        raise exceptions.OSDNAApiException(code, body, message)

    def not_found(self, message="Requested resource not found"):
        self.set_error_response("Not Found", "404", message)

    def conflict(self,
                 message="The posted data conflicts with the existing data"):
        self.set_error_response("Conflict", "409", message)

    def bad_request(self, message="Invalid request content"):
        self.set_error_response("Bad Request", "400", message)

    def unauthorized(self, message="Request requires authorization"):
        self.set_error_response("Unauthorized", "401", message)

    def validate_query_data(self, data, data_requirements,
                            additional_key_reg=None):
        error_message = self.validate_data(data, data_requirements,
                                           additional_key_reg)
        if error_message:
            self.bad_request(error_message)

    def check_and_convert_datetime(self, time_key, data):
        time = data.get(time_key)

        if time:
            time = time.replace(' ', '+')
            try:
                data[time_key] = parser.parse(time)
            except Exception:
                self.bad_request("{0} must follow ISO 8610 date and time format,"
                                 "YYYY-MM-DDThh:mm:ss.sss+hhmm".format(time_key))

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

    def parse_query_params(self, req):
        query_string = req.query_string.strip()
        query_params = {}

        if not query_string:
            return query_params

        valid = True
        filters = query_string.split('&')
        for filter in filters:
            if '=' not in filter:
                valid = False
                break
            index = filter.index('=')
            key = filter[:index].strip()
            value = filter[index + 1:].strip()

            if not key or not value:
                valid = False
                break
            if key not in query_params:
                query_params[key] = value
            else:
                if not isinstance(query_params[key], list):
                    query_params[key] = [query_params[key]]
                query_params[key].append(value)
        if not valid:
            self.bad_request('illegal query string: {0}'
                             .format(query_string))

        return query_params

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
            error = "No data found in the request body"
            return error, content

        data = req.stream.read()
        content_string = data.decode()
        try:
            content = json.loads(content_string)
            if not isinstance(content, dict):
                error = "The data in the request body must be a dictionary"
        except Exception:
            error = "The request can not be fulfilled due to bad syntax"

        return error, content

    def get_collection_by_name(self, name):
        if name in self.UNCHANGED_COLLECTIONS:
            return self.inv.db[name]
        return self.inv.coll[name]

    def get_constants_by_name(self, name):
        constants = self.get_collection_by_name("constants").\
            find_one({"name": name})
        return [d['value'] for d in constants['data']]

    def read(self, collection, matches={}, projection=None, skip=0, limit=1000):
        collection = self.get_collection_by_name(collection)
        skip *= limit
        query = collection.find(matches, projection).skip(skip).limit(limit)
        return list(query)

    def write(self, document, collection="inventory"):
        self.get_collection_by_name(collection).\
            insert_one(document)

    def aggregate(self, pipeline, collection):
        collection = self.get_collection_by_name(collection)
        data = collection.aggregate(pipeline)
        return list(data)
