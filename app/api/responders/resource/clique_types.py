from api.responders.responder_base import ResponderBase
from bson.objectid import ObjectId
from api.etc.data_validate import DataValidate


class CliqueTypes(ResponderBase):

    def __init__(self):
        super().__init__()
        self.collection = "clique_types"
        self.id = '_id'

    def on_get(self, req, resp):
        self.log.debug("Getting clique types")

        filters = self.parse_query_params(req.params)
        focal_point_types = self.get_constants_by_name("object_types")
        link_types = self.get_constants_by_name("link_types")

        filters_requirements = {
            'env_name': self.get_validate_requirement(str, mandatory=True),
            'id': self.get_validate_requirement(ObjectId, True),
            'focal_point_type': self.get_validate_requirement(str, validate=DataValidate.LIST, requirement=focal_point_types),
            'link_type': self.get_validate_requirement([list, str], validate=DataValidate.LIST, requirement=link_types),
            'page': self.get_validate_requirement(int, True),
            'page_size': self.get_validate_requirement(int, True)
        }

        self.validate_filters(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)
        query = self.build_query(filters)

        if self.id in query:
            clique_type = self.get_object_by_id(self.collection, query, [ObjectId], self.id)
            if not clique_type:
                self.not_found()
            self.set_successful_response(resp, clique_type)
        else:
            clique_types_ids = self.get_object_ids(self.collection, query, page, page_size, self.id)
            self.set_successful_response(resp, {"clique_types": clique_types_ids})

    def on_post(self, req, resp):
        self.log.debug("Posting new clique_type")

        error, clique_type = self.get_content_from_request(req)
        if error:
            self.bad_request(error)

        focal_point_types = self.get_constants_by_name("object_types")
        link_types = self.get_constants_by_name("link_types")

        clique_type_requirements = {
            'environment': self.get_validate_requirement(str, mandatory=True),
            'focal_point_type': self.get_validate_requirement(str, False, DataValidate.LIST, focal_point_types, True),
            'link_types': self.get_validate_requirement(list, False, DataValidate.LIST, link_types, True),
            'name': self.get_validate_requirement(str, mandatory=True)
        }

        validation = self.validate_data(clique_type, clique_type_requirements)
        if not validation['passed']:
            self.bad_request(validation['error_message'])

        env_name = clique_type['environment']
        focal_point_type = clique_type['focal_point_type']
        if not self.check_environment_name(env_name):
            self.bad_request("{0} doesn't exist in the system".format(env_name))

        query = {
            'environment': env_name,
            'focal_point_type': focal_point_type
        }
        clique_types = self.read(self.collection, query)
        if clique_types:
            self.conflict("clique_type for focal_point_type {0} in environment {1} has exists".
                          format(focal_point_type, env_name))

        self.write(clique_type, self.collection)
        self.set_successful_response(resp, status="201")

    def build_query(self, filters):
        query = {}
        filters_keys = ['focal_point_type']
        env_name = filters.get('env_name')
        _id = filters.get('id')
        link_types = filters.get('link_type')

        self.update_query_with_filters(filters, filters_keys, query)
        if link_types:
            if type(link_types) != list:
                link_types = [link_types]

            query['link_types'] = {
                '$all': link_types
            }

        if _id:
            query[self.id] = _id

        query['environment'] = env_name
        return query
