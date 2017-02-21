from api.validation.data_validate import DataValidate
from api.responders.responder_base import ResponderBase
from bson.objectid import ObjectId


class MonitoringConfigTemplates(ResponderBase):
    def __init__(self):
        super().__init__()
        self.ID = "_id"
        self.COLLECTION = "monitoring_config_templates"

    def on_get(self, req, resp):
        self.log.debug("Getting monitoring config template")

        filters = self.parse_query_params(req.params)

        sides = self.get_constants_by_name("monitoring_sides")
        filters_requirements = {
            "id": self.require(ObjectId, True),
            "order": self.require(str),
            "side": self.require(str, validate=DataValidate.LIST,
                                 requirement=sides),
            "type": self.require(str),
            "page": self.require(int, True),
            "page_size": self.require(int, True)
        }

        self.validate_query_data(filters, filters_requirements)

        page, page_size = self.get_pagination(filters)
        query = self.build_query(filters)
        if self.ID in query:
            template = self.get_object_by_id(self.COLLECTION, query,
                                             [ObjectId], self.ID)
            if not template:
                self.not_found()
            self.set_successful_response(resp, template)
        else:
            templates = self.get_object_ids(self.COLLECTION, query,
                                            page, page_size, self.ID)
            self.set_successful_response(
                resp,
                {"monitoring_config_templates": templates}
            )

    def build_query(self, filters):
        query = {}
        filters_keys = ["order", "side", "type"]
        self.update_query_with_filters(filters, filters_keys, query)
        _id = filters.get('id')
        if _id:
            query[self.ID] = _id
        return query
