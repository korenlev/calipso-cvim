from api.validation.data_validate import DataValidate
from api.responders.responder_base import ResponderBase
from bson.objectid import ObjectId
from datetime import datetime


class Scans(ResponderBase):
    def __init__(self):
        super().__init__()
        self.COLLECTION = "scans"
        self.ID = "_id"

    def on_get(self, req, resp):
        self.log.debug("Getting scans")
        filters = self.parse_query_params(req.params)

        scan_statuses = self.get_constants_by_name("scan_statuses")
        filters_requirements = {
            "env_name": self.require(str, mandatory=True),
            "id": self.require(ObjectId, True),
            "base_object": self.require(str),
            "status": self.require(str, False, DataValidate.LIST, scan_statuses),
            "page": self.require(int, True),
            "page_size": self.require(int, True)
        }

        self.validate_query_data(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)

        query = self.build_query(filters)
        if "_id" in query:
            scan = self.get_object_by_id(self.COLLECTION, query,
                                         [ObjectId, datetime], self.ID)
            if not scan:
                self.not_found()
            self.set_successful_response(resp, scan)
        else:
            scans_ids = self.get_object_ids(self.COLLECTION, query,
                                            page, page_size, self.ID)
            self.set_successful_response(resp, {"scans": scans_ids})

    def build_query(self, filters):
        query = {}
        filters_keys = ["status"]
        self.update_query_with_filters(filters, filters_keys, query)
        base_object = filters.get("base_object")
        if base_object:
            query['object_id'] = base_object
        _id = filters.get("id")
        if _id:
            query['_id'] = _id
        query['environment'] = filters['env_name']
        return query
