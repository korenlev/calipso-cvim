from api.responders.responder_base import ResponderBase
from base.utils.constants import GraphType


class Graph(ResponderBase):
    COLLECTION = "graphs"

    def on_get(self, req, resp):
        filters = self.parse_query_params(req)
        filters_requirements = {
            'env_name': self.require(str, mandatory=True),
        }

        self.validate_query_data(filters, filters_requirements)
        query = self.build_query(filters)

        graph = self.get_single_object(collection=self.COLLECTION, query=query)
        self.set_ok_response(resp, graph)

    def build_query(self, filters):
        query = super().build_query(filters=filters)
        query["type"] = GraphType.INVENTORY.value  # TODO: support clique graphs
        return query
