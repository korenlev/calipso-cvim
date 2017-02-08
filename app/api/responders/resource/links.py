from api.responders.responder_base import ResponderBase
from bson.objectid import ObjectId
from api.etc.data_validate import DataValidate


class Links(ResponderBase):

    def __init__(self):
        super().__init__()
        self.collection = 'links'
        self.id = '_id'

    def on_get(self, req, resp):
        self.log.debug("Getting links from links")

        filters = self.parse_query_params(req.params)

        link_types = self.get_constants_by_name("link_types")
        link_states = self.get_constants_by_name("link_states")
        filters_requirements = {
            'env_name': self.get_validate_requirement(str, mandatory=True),
            'id': self.get_validate_requirement(ObjectId, True),
            'host': self.get_validate_requirement(str),
            'link_type': self.get_validate_requirement(str, validate=DataValidate.LIST, requirement=link_types),
            'link_name': self.get_validate_requirement(str),
            'source_id': self.get_validate_requirement(str),
            'target_id': self.get_validate_requirement(str),
            'state': self.get_validate_requirement(str, validate=DataValidate.LIST, requirement=link_states),
            'page': self.get_validate_requirement(int, True),
            'page_size': self.get_validate_requirement(int, True)
        }

        self.validate_filters(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)
        query = self.build_query(filters)
        if self.id in query:
            link = self.get_object_by_id(self.collection, query, [ObjectId], self.id)
            if not link:
                self.not_found()
            self.set_successful_response(resp, link)
        else:
            links_ids = self.get_object_ids(self.collection, query, page, page_size, self.id)
            self.set_successful_response(resp, {"links": links_ids})

    def build_query(self, filters):
        query = {}
        filters_keys = ['host', 'link_type', 'link_name', 'source_id', 'target_id', 'state']
        env_name = filters.get('env_name')
        _id = filters.get('id')

        self.update_query_with_filters(filters, filters_keys, query)

        # add attributes to the query
        for key in filters.keys():
            if key.startswith("attributes."):
                query[key] = filters[key]
        if _id:
            query[self.id] = _id
        query['environment'] = env_name
        return query
