from api.responders.responder_base import ResponderBase
from bson.objectid import ObjectId
from api.etc.data_validate import DataValidate


class Cliques(ResponderBase):

    def __init__(self):
        super().__init__()
        self.collection = "cliques"
        self.id = '_id'

    def on_get(self, req, resp):
        self.log.debug("Getting cliques")

        filters = self.parse_query_params(req.params)

        focal_point_types = self.get_constants_by_name("object_types")
        link_types = self.get_constants_by_name("link_types")

        filters_requirements = {
            'env_name': self.get_validate_requirement(str, mandatory=True),
            'id': self.get_validate_requirement(ObjectId, True),
            'focal_point': self.get_validate_requirement(ObjectId, True),
            'focal_point_type': self.get_validate_requirement(str, validate=DataValidate.LIST, requirement=focal_point_types),
            'link_type': self.get_validate_requirement(str, validate=DataValidate.LIST, requirement=link_types),
            'link_id': self.get_validate_requirement(ObjectId, True),
            'page': self.get_validate_requirement(int, True),
            'page_size': self.get_validate_requirement(int, True)
        }

        validation = self.validate_data(filters, filters_requirements)
        if not validation['passed']:
            self.bad_request(validation['error_message'])

        page, page_size = self.get_pagination(filters)
        query = self.build_query(filters)

        if self.id in query:
            clique = self.get_object_by_id(self.collection, query, [ObjectId], self.id)
            if not clique:
                self.not_found()
            self.set_successful_response(resp, clique)
        else:
            cliques_ids = self.get_object_ids(self.collection, query, page, page_size, self.id)
            self.set_successful_response(resp, {"cliques": cliques_ids})

    def build_query(self, filters):
        query = {}
        filters_keys = ['focal_point', 'focal_point_type']
        link_type = filters.get('link_type')
        link_id = filters.get('link_id')
        _id = filters.get('id')
        env_name = filters.get('env_name')

        self.update_query_with_filters(filters, filters_keys, query)

        if link_type:
            query['links_detailed.link_type'] = link_type

        if link_id:
            query['links_detailed._id'] = link_id

        if _id:
            query[self.id] = _id
        query['environment'] = env_name
        self.generate_object_ids(['links_detailed._id'], query)
        return query
