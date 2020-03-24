from api.responders.responder_base import ResponderBase


class Tree(ResponderBase):
    COLLECTION = "trees"

    def on_get(self, req, resp):
        filters = self.parse_query_params(req)
        filters_requirements = {
            'env_name': self.require(str, mandatory=True),
        }

        self.validate_query_data(filters, filters_requirements)
        query = self.build_query(filters)

        tree = self.get_single_object(collection=self.COLLECTION, query=query)
        print(tree)
        self.set_ok_response(resp, tree)
