from api.responders.responder_base import ResponderBase
from bson.objectid import ObjectId
from api.etc.data_validate import DataValidate


class CliqueConstraints(ResponderBase):

    def __init__(self):
        super().__init__()
        self.id = '_id'
        self.collection = 'clique_constraints'

    def on_get(self, req, resp):
        self.log.debug("Getting clique_constraints")

        filters = self.parse_query_params(req.params)

        focal_point_types = self.get_constants_by_name("object_types")
        filters_requirements = {
            'id': self.get_validate_requirement(ObjectId, True),
            'focal_point_type': self.get_validate_requirement(str, False, DataValidate.LIST, focal_point_types),
            'constraint': self.get_validate_requirement([list, str]),
            'page': self.get_validate_requirement(int, True),
            'page_size': self.get_validate_requirement(int, True)
        }

        self.validate_filters(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)

        query = self.build_query(filters)
        if self.id in query:
            clique_constraint = self.get_object_by_id(self.collection, query, [ObjectId], self.id)
            if not clique_constraint:
                self.not_found()
            self.set_successful_response(resp, clique_constraint)
        else:
            clique_constraints_ids = self.get_object_ids(self.collection, query, page, page_size, self.id)
            self.set_successful_response(resp, {"clique_constraints": clique_constraints_ids})

    def build_query(self, filters):
        query = {}
        filters_keys = ['focal_point_type']
        _id = filters.get('id')
        constraints = filters.get('constraint')
        self.update_query_with_filters(filters, filters_keys, query)

        if constraints:
            if type(constraints) != list:
                constraints = [constraints]

            query['constraints'] = {
                '$all': constraints
            }

        if _id:
            query[self.id] = _id
        return query
