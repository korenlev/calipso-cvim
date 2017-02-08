from api.responders.responder_base import ResponderBase
from api.etc.data_validate import DataValidate
from bson.objectid import ObjectId


class MonitoringConfigTemplates(ResponderBase):

    def __init__(self):
        super().__init__()
        self.id = "_id"
        self.collection = "monitoring_config_templates"

    def on_get(self, req, resp):
        self.log.debug("Getting monitoring config template")

        filters = self.parse_query_params(req.params)

        sides = self.get_constants_by_name("monitoring_sides")
        filters_requirements = {
            "id": self.get_validate_requirement(ObjectId, True),
            "order": self.get_validate_requirement(str),
            "side": self.get_validate_requirement(str, validate=DataValidate.LIST, requirement=sides),
            "type": self.get_validate_requirement(str),
            "page": self.get_validate_requirement(int, True),
            "page_size": self.get_validate_requirement(int, True)
        }

        self.validate_filters(filters, filters_requirements)

        page, page_size = self.get_pagination(filters)
        query = self.build_query(filters)
        if self.id in query:
            template = self.get_object_by_id(self.collection, query, [ObjectId], self.id)
            if not template:
                self.not_found()
            self.set_successful_response(resp, template)
        else:
            templates = self.get_object_ids(self.collection, query, page, page_size, self.id)
            self.set_successful_response(resp, {"monitoring_config_templates": templates})

    def build_query(self, filters):
        query = {}
        filters_keys = ["order", "side", "type"]
        _id = filters.get('id')
        self.update_query_with_filters(filters, filters_keys, query)

        if _id:
            query[self.id] = _id
        return query