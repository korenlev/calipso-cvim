import re

from api.responders.responder_base import ResponderBase
from api.validation.data_validate import DataValidate


class Search(ResponderBase):

    ID = 'id'
    PROJECTION = {
        ID: True,
        "name": True,
        "type": True,
        "last_scanned": True
    }

    # TODO: list of searchable collections with corresponding field names to search against?
    SEARCHABLE_COLLECTIONS = {
        "inventory": ["name"]
    }

    def on_get(self, req, resp):
        filters = self.parse_query_params(req)
        filters_requirements = {
            'env_name': self.require(str, mandatory=True),
            'query': self.require(str, mandatory=True),
            'source': self.require(str, validate=DataValidate.LIST, requirement=self.SEARCHABLE_COLLECTIONS.keys(),
                                   mandatory=True),
            'page': self.require(int, convert_to_type=True),
            'page_size': self.require(int, convert_to_type=True),
            'all': self.require(bool, convert_to_type=True),
        }

        self.validate_query_data(filters, filters_requirements)
        page, page_size = (0, 0) if filters.get('all') is True else self.get_pagination(filters)
        query = self.build_query(filters)

        objects = self.get_objects_list(collection=filters["source"], query=query,
                                        page=page, page_size=page_size,
                                        projection=self.PROJECTION)
        self.set_ok_response(resp, {"objects": objects})

    def build_query(self, filters):
        query = super().build_query(filters)

        fields = self.SEARCHABLE_COLLECTIONS[filters["source"]]
        query["$or"] = []
        for field in fields:
            query["$or"].append({field: re.compile(".*{}.*".format(re.escape(filters["query"])), re.IGNORECASE)})

        return query
