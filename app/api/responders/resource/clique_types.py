from api.responders.responder_base import ResponderBase
from api.validation.data_validate import DataValidate
from bson.objectid import ObjectId


class CliqueTypes(ResponderBase):
    def __init__(self):
        super().__init__()
        self.COLLECTION = "clique_types"
        self.ID = "_id"

    def on_get(self, req, resp):
        self.log.debug("Getting clique types")

        filters = self.parse_query_params(req)
        focal_point_types = self.get_constants_by_name("object_types")
        link_types = self.get_constants_by_name("link_types")
        filters_requirements = {
            'env_name': self.require(str, mandatory=True),
            'id': self.require(ObjectId, True),
            'focal_point_type': self.require(str,
                                             validate=DataValidate.LIST,
                                             requirement=focal_point_types),
            'link_type': self.require([list, str],
                                      validate=DataValidate.LIST,
                                      requirement=link_types),
            'page': self.require(int, True),
            'page_size': self.require(int, True)
        }

        self.validate_query_data(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)
        query = self.build_query(filters)
        if self.ID in query:
            clique_type = self.get_object_by_id(self.COLLECTION, query,
                                                [ObjectId], self.ID)
            if not clique_type:
                self.not_found()
            self.set_successful_response(resp, clique_type)
        else:
            clique_types_ids = self.get_object_ids(self.COLLECTION,
                                                   query,
                                                   page, page_size, self.ID)
            self.set_successful_response(resp,
                                         {"clique_types": clique_types_ids})

    def on_post(self, req, resp):
        self.log.debug("Posting new clique_type")
        error, clique_type = self.get_content_from_request(req)
        if error:
            self.bad_request(error)
        focal_point_types = self.get_constants_by_name("object_types")
        link_types = self.get_constants_by_name("link_types")
        clique_type_requirements = {
            'environment': self.require(str, mandatory=True),
            'focal_point_type': self.require(str, False, DataValidate.LIST,
                                             focal_point_types, True),
            'link_types': self.require(list, False, DataValidate.LIST,
                                       link_types, True),
            'name': self.require(str, mandatory=True)
        }

        self.validate_query_data(clique_type, clique_type_requirements)
        env_name = clique_type['environment']
        focal_point_type = clique_type['focal_point_type']
        if not self.check_environment_name(env_name):
            self.bad_request("{0} doesn't exist".format(env_name))

        query = {
            'environment': env_name,
            'focal_point_type': focal_point_type
        }
        clique_types = self.read(self.COLLECTION, query)
        if clique_types:
            self.conflict("clique_type for focal_point_type {0} in "
                          "environment {1} has exists".format(focal_point_type,
                                                              env_name))

        self.write(clique_type, self.COLLECTION)
        self.set_successful_response(resp, status="201")

    def build_query(self, filters):
        query = {}
        filters_keys = ['focal_point_type']
        self.update_query_with_filters(filters, filters_keys, query)
        link_types = filters.get('link_type')
        if link_types:
            if type(link_types) != list:
                link_types = [link_types]
            query['link_types'] = {'$all': link_types}
        _id = filters.get('id')
        if _id:
            query[self.ID] = _id

        query['environment'] = filters['env_name']
        return query
