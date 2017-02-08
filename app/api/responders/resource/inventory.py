from api.responders.responder_base import ResponderBase
from bson.objectid import ObjectId
from datetime import datetime


class Inventory(ResponderBase):

    def __init__(self):
        super().__init__()
        self.collection = 'inventory'
        self.id = 'id'

    def on_get(self, req, resp):
        self.log.debug("Getting objects from inventory")

        filters = self.parse_query_params(req.params)
        filters_requirements = {
            'env_name': self.get_validate_requirement(str, mandatory=True),
            'id': self.get_validate_requirement(str),
            'id_path': self.get_validate_requirement(str),
            'parent_id': self.get_validate_requirement(str),
            'parent_path': self.get_validate_requirement(str),
            'sub_tree': self.get_validate_requirement(bool, True),
            'page': self.get_validate_requirement(int, True),
            'page_size': self.get_validate_requirement(int, True)
        }
        self.validate_filters(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)
        query = self.build_query(filters)
        if self.id in query:
            obj = self.get_object_by_id(self.collection, query, [ObjectId, datetime], self.id)
            if not obj:
                self.not_found()
            self.set_successful_response(resp, obj)
        else:
            objects_ids = self.get_object_ids(self.collection, query, page, page_size, self.id)
            self.set_successful_response(resp, {"objects": objects_ids})

    def build_query(self, filters):
        query = {}
        filters_keys = ['parent_id', 'id_path', 'id']
        sub_tree = filters.get('sub_tree', False)
        parent_path = filters.get('parent_path')
        env_name = filters.get('env_name')

        self.update_query_with_filters(filters, filters_keys, query)
        if parent_path:
            regular_expression = parent_path
            if sub_tree:
                regular_expression += "[/]?"
            else:
                regular_expression += "/[^/]+$"
            query['id_path'] = {
                    "$regex": regular_expression
                }

        query['environment'] = env_name
        return query