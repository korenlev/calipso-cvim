from api.responders.responder_base import ResponderBase
from bson.objectid import ObjectId
from datetime import datetime
from api.etc.data_validate import DataValidate


class Scans(ResponderBase):

    def __init__(self):
        super().__init__()
        self.collection = "scans"
        self.id = "_id"

    def on_get(self, req, resp):
        self.log.debug("Getting scans")
        filters = self.parse_query_params(req.params)

        scan_statuses = self.get_constants_by_name("scan_statuses")
        filters_requirements = {
            "env_name": self.get_validate_requirement(str, mandatory=True),
            "id": self.get_validate_requirement(ObjectId, True),
            "base_object": self.get_validate_requirement(str),
            "status": self.get_validate_requirement(str, False, DataValidate.LIST, scan_statuses),
            "page": self.get_validate_requirement(int, True),
            "page_size": self.get_validate_requirement(int, True)
        }

        self.validate_filters(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)

        query = self.build_query(filters)
        if "_id" in query:
            scan = self.get_object_by_id(self.collection, query, [ObjectId, datetime], self.id)
            if not scan:
                self.not_found()
            self.set_successful_response(resp, scan)
        else:
            scans_ids = self.get_object_ids(self.collection, query, page, page_size, self.id)
            self.set_successful_response(resp, {"scans": scans_ids})

    def build_query(self, filters):
        query = {}
        filters_keys = ["status"]
        env_name = filters.get("env_name")
        _id = filters.get("id")
        base_object = filters.get("base_object")

        self.update_query_with_filters(filters, filters_keys, query)
        if base_object:
            query['object_id'] = base_object

        if _id:
            query['_id'] = _id

        query['environment'] = env_name
        return query