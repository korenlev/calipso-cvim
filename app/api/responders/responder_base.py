import json

from api.backends.mongo_access import MongoAccess
from api.etc.data_validate import DataValidate
from api.exceptions import exceptions


class ResponderBase(MongoAccess, DataValidate):

    def __init__(self):
        super().__init__()

    def set_successful_response(self, resp, body="", status="200"):
        if not isinstance(body, str):
            try:
                body = str(body)
            except Exception as e:
                self.log.exception(e)
                raise ValueError("The request content is invalid")
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

    def not_found(self, message="The requested resource can't be found"):
        self.set_error_response("Not Found", "404", message)

    def conflict(self, message="The post data conflict with the existing data"):
        self.set_error_response("Conflict", "409", message)

    def bad_request(self, message="The request can't be handled due to the request content"):
        self.set_error_response("Bad Request", "400", message)

    def unauthorized(self, message="The request you have made requires authentication."):
        self.set_error_response("Unauthorized", "401", message)

    def validate_filters(self, filters, filters_requirements):
        # validate the filters in the query string
        data_validation = self.validate_data(filters, filters_requirements)
        if not data_validation['passed']:
            self.bad_request(data_validation['error_message'])

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
        """
        parse filter names to the keys we can use in mongo query,
        e.g attributes:network => attributes.network
        :param params: the filters parameters
        :return: parsed parameters
        """
        parsed_params = {}
        for key, value in params.items():
            key = key.replace(":", ".")
            parsed_params[key] = value
        return parsed_params

    def get_pagination(self, filters):
        page_size = filters.get('page_size')
        page = filters.get('page')
        if not page_size:
            page_size = 1000

        if not page:
            page = 0
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



