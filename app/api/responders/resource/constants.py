from api.responders.responder_base import ResponderBase
from bson.objectid import ObjectId


class Constants(ResponderBase):
    def __init__(self):
        super().__init__()
        self.ID = '_id'
        self.COLLECTION = 'constants'

    def on_get(self, req, resp):
        self.log.debug("Getting constants with name")
        filters = self.parse_query_params(req.params)
        filters_requirements = {
            "name": self.require(str, mandatory=True),
        }
        self.validate_query_data(filters, filters_requirements)
        query = {"name": filters['name']}
        constant = self.get_object_by_id(self.COLLECTION, query,
                                         [ObjectId], self.ID)
        if not constant:
            self.not_found()
        self.set_successful_response(resp, constant)
