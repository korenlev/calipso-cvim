from api.responders.responder_base import ResponderBase
from api.validation.data_validate import DataValidate
from bson.objectid import ObjectId


class CliqueConstraints(ResponderBase):
    def __init__(self):
        super().__init__()
        self.ID = '_id'
        self.COLLECTION = 'clique_constraints'

    def on_get(self, req, resp):
        self.log.debug("Getting clique_constraints")
        filters = self.parse_query_params(req)
        focal_point_types = self.get_constants_by_name("object_types")
        filters_requirements = {
            'id': self.require(ObjectId, True),
            'focal_point_type': self.require(str, False, DataValidate.LIST,
                                             focal_point_types),
            'constraint': self.require([list, str]),
            'page': self.require(int, True),
            'page_size': self.require(int, True)
        }
        self.validate_query_data(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)
        query = self.build_query(filters)
        if self.ID in query:
            clique_constraint = self.get_object_by_id(self.COLLECTION,
                                                      query,
                                                      [ObjectId], self.ID)
            self.set_successful_response(resp, clique_constraint)
        else:
            clique_constraints_ids = self.get_object_ids(self.COLLECTION,
                                                         query,
                                                         page, page_size, self.ID)
            self.set_successful_response(
                resp, {"clique_constraints": clique_constraints_ids}
            )

    def build_query(self, filters):
        query = {}
        filters_keys = ['focal_point_type']
        self.update_query_with_filters(filters, filters_keys, query)
        constraints = filters.get('constraint')
        if constraints:
            if type(constraints) != list:
                constraints = [constraints]

            query['constraints'] = {
                '$all': constraints
            }
        _id = filters.get('id')
        if _id:
            query[self.ID] = _id
        return query
