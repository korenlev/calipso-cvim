from api.responders.responder_base import ResponderBase
from api.etc.data_validate import DataValidate


class Aggregates(ResponderBase):

    def on_get(self, req, resp):
        self.log.debug("Getting aggregates information")

        filters = self.parse_query_params(req.params)
        filters_requirements = {
            "env_name": self.get_validate_requirement(str),
            "type": self.get_validate_requirement(str, validate=DataValidate.LIST, requirement=["environment", "message", "constant"])
        }

        validation = self.validate_data(filters, filters_requirements)
        if not validation['passed']:
            self.bad_request(validation['error_message'])

        query = self.build_query(filters)
        if not query:
            self.bad_request("Please specify the type of aggregates, we support three types of aggregates, "
                             "they are environment, message and constant")
        print(query)
        if query['type'] == "environment":
            if not query.get('env_name'):
                self.bad_request("Please specify the environment name for the environment aggregates")
            env_name = query['env_name']
            if not self.check_environment_name(env_name):
                self.bad_request("{0} doesn't exist".format(env_name))

        aggregates = self.get_aggregates(query)
        self.set_successful_response(resp, aggregates)

    def build_query(self, filters):
        query = {}
        env_name = filters.get("env_name")
        query_type = filters.get("type")
        if not query_type:
            return query
        query['type'] = query_type
        if query_type == "environment":
            if env_name:
                query['env_name'] = env_name
            return query
        return query

    def get_aggregates(self, query):
        aggregates_map = {
            "environment": self.get_environments_aggregates,
            "message": self.get_messages_aggregates,
            "constant": self.get_constants_aggregates
        }
        return aggregates_map[query['type']](query)

    def get_environments_aggregates(self, query):
        env_name = query['env_name']
        type = query['type']
        aggregates = {
            "type": type,
            "env_name": env_name,
            "aggregates": {
                "object_types": {

                }
            }
        }
        pipeline = [
            {
                '$match': {
                    'environment': env_name
                }
            },
            {
                '$group': {
                    '_id': '$type',
                    'total': {
                        '$sum': 1
                    }
                }
            }
        ]
        groups = self.aggregate(pipeline, "inventory")
        for group in groups:
            aggregates['aggregates']['object_types'][group['_id']] = group['total']
        return aggregates

    def get_messages_aggregates(self, query):
        aggregates = {
            "type": query['type'],
            "aggregates": {
                "levels": {},
                "environments": {}
            }
        }
        env_pipeline = [
            {
                '$group': {
                    '_id': '$environment',
                    'total': {
                        '$sum': 1
                    }
                }
            }
        ]
        environments = self.aggregate(env_pipeline, "messages")
        for environment in environments:
            aggregates['aggregates']['environments'][environment['_id']] = environment['total']
        level_pipeline = [
            {
                '$group': {
                    '_id': '$level',
                    'total': {
                        '$sum': 1
                    }
                }
            }
        ]
        levels = self.aggregate(level_pipeline, "messages")

        for level in levels:
            aggregates['aggregates']['levels'][level['_id']] = level['total']

        return aggregates

    def get_constants_aggregates(self, query):
        aggregates = {
            "type": query['type'],
            "aggregates": {
                "names": {}
            }
        }
        pipeline = [
            {
                '$project': {
                    '_id': 0,
                    'name': 1,
                    'total': {
                        '$size': '$data'
                    }
                }
            }
        ]
        constants = self.aggregate(pipeline, "constants")
        for constant in constants:
            aggregates['aggregates']['names'][constant['name']] = constant['total']

        return aggregates