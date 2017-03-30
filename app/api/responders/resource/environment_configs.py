from api.validation.data_validate import DataValidate
from api.responders.responder_base import ResponderBase
from bson.objectid import ObjectId
from datetime import datetime


class EnvironmentConfigs(ResponderBase):
    def __init__(self):
        super(EnvironmentConfigs, self).__init__()
        self.ID = "name"
        self.PROJECTION = {
            self.ID: True,
            "_id": False,
            "name": True,
            "distribution": True
        }
        self.COLLECTION = "environments_config"
        self.CONFIGURATIONS_NAMES = ["mysql", "OpenStack",
                                     "CLI", "AMQP", "Monitoring"]
        self.OPTIONAL_CONFIGURATIONS_NAMES = ["Monitoring"]
        self.REQUIREMENTS = {
            "name": self.require(str, mandatory=True),
            "host": self.require(str, mandatory=True),
            "password": self.require(str, mandatory=True),
            "port": self.require(int, True, mandatory=True),
            "user": self.require(str, mandatory=True),
            "admin_project": self.require(str, mandatory=True),
            "admin_token": self.require(str, mandatory=True),
            "pwd": self.require(str, mandatory=True),
            "key": self.require(str, mandatory=True),
            "app_path": self.require(str, mandatory=True),
            "config_folder": self.require(str, mandatory=True),
            "debug": self.require(bool, True, mandatory=True),
            "env_type": self.require(str, False, DataValidate.LIST,
                                     ["development", "product"],
                                     mandatory=True),
            "osdna_path": self.require(str, mandatory=True),
            "api_port": self.require(int, True, mandatory=True),
            "rabbitmq_pass": self.require(str, mandatory=True),
            "rabbitmq_user": self.require(str, mandatory=True),
            "ssh_port": self.require(int, True, mandatory=True),
            "ssh_pass": self.require(str, mandatory=True),
            "ssh_user": self.require(str, mandatory=True),
            "server_ip": self.require(str, mandatory=True),
            "server_name": self.require(str, mandatory=True),
            "type": self.require(str, mandatory=True)
        }
        self.CONFIGURATIONS_KEYS = {
            "mysql":
                ["name", "host", "password", "port", "user"],
            "OpenStack":
                ["name", "host", "admin_project", "admin_token",
                 "port", "user", "pwd"],
            "CLI":
                ["name", "host", "key", "pwd", "user"],
            "AMQP":
                ["name", "host", "port", "user", "password"],
            "Monitoring":
                ["name", "app_path", "config_folder", "debug",
                "env_type", "osdna_path", "api_port",
                "rabbitmq_pass", "rabbitmq_user",
                 "ssh_port", "ssh_password", "ssh_user",
                "server_ip", "server_name", "type"]
        }

    def on_get(self, req, resp):
        self.log.debug("Getting environment config")
        filters = self.parse_query_params(req)

        distributions = self.get_constants_by_name("distributions")
        mechanism_drivers = self.get_constants_by_name("mechanism_drivers")
        type_drivers = self.get_constants_by_name("type_drivers")

        filters_requirements = {
            "name": self.require(str),
            "distribution": self.require(str, False, DataValidate.LIST, distributions),
            "mechanism_drivers": self.require([str, list], False, DataValidate.LIST, mechanism_drivers),
            "type_drivers": self.require(str, False, DataValidate.LIST, type_drivers),
            "user": self.require(str),
            "listen": self.require(bool, True),
            "scanned": self.require(bool, True),
            "monitoring_setup_done": self.require(bool, True),
            "operational": self.require(str, False, DataValidate.LIST, ["yes", "no"])
        }

        self.validate_query_data(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)

        query = self.build_query(filters)

        if self.ID in query:
            environment_config = self.get_object_by_id(self.COLLECTION, query,
                                                       [ObjectId, datetime], self.ID)
            self.set_successful_response(resp, environment_config)
        else:
            objects_ids = self.get_objects_list(self.COLLECTION, query,
                                                page, page_size, self.PROJECTION)
            self.set_successful_response(resp, {'environment_configs': objects_ids})

    def build_query(self, filters):
        query = {}
        filters_keys = ["name", "distribution", "type_drivers", "user",
                        "listen", "monitoring_setup_done", "scanned",
                        "operational"]
        self.update_query_with_filters(filters, filters_keys, query)
        mechanism_drivers = filters.get("mechanism_drivers")
        if mechanism_drivers:
            if type(mechanism_drivers) != list:
                mechanism_drivers = [mechanism_drivers]
            query['mechanism_drivers'] = {'$all': mechanism_drivers}

        return query

    def on_post(self, req, resp):
        self.log.debug("Creating a new environment config")

        error, env_config = self.get_content_from_request(req)
        if error:
            self.bad_request(error)

        distributions = self.get_constants_by_name("distributions")
        mechanism_drivers = self.get_constants_by_name("mechanism_drivers")
        type_drivers = self.get_constants_by_name("type_drivers")
        environment_config_requirement = {
            "configuration": self.require(list, mandatory=True),
            "distribution": self.require(str, False, DataValidate.LIST,
                                         distributions, True),
            "last_scanned": self.require(str, mandatory=True),
            "mechanism_drivers": self.require(list, False, DataValidate.LIST,
                                              mechanism_drivers, True),
            "monitoring_setup_done": self.require(bool, True, mandatory=True),
            "name": self.require(str, mandatory=True),
            "operational": self.require(str, True, DataValidate.LIST,
                                        ["yes", "no"], mandatory=True),
            "scanned": self.require(bool, True, mandatory=True),
            "type": self.require(str, mandatory=True),
            "type_drivers": self.require(str, False, DataValidate.LIST,
                                         type_drivers, True)
        }
        self.validate_query_data(env_config,
                                 environment_config_requirement)
        # validate the configurations
        configurations = env_config['configuration']
        config_validation = self.validate_environment_config(configurations)

        if not config_validation['passed']:
            self.bad_request(config_validation['error_message'])

        self.write(env_config, self.COLLECTION)
        self.set_successful_response(resp,
                                     {"message": "created environment_config "
                                                 "for {0}"
                                                 .format(env_config["name"])},
                                     "201")

    def validate_environment_config(self, configurations):
        configurations_of_names = {}
        validation = {"passed": True}
        if [config for config in configurations
            if 'name' not in config]:
            validation['passed'] = False
            validation['error_message'] = "configuration must have name"
            return validation
        for name in self.CONFIGURATIONS_NAMES:
            if not name in self.OPTIONAL_CONFIGURATIONS_NAMES:
                configuration = self.get_configuration_by_name(name,
                                                               configurations,
                                                               True,
                                                               validation)

                if not validation['passed']:
                    return validation
                configurations_of_names[name] = configuration
            else:
                configuration = self.get_configuration_by_name(name,
                                                               configurations,
                                                               False,
                                                               validation)
                if not validation["passed"]:
                    return validation
                if configuration:
                    configurations_of_names[name] = configuration
        for name, config in configurations_of_names.items():
            error_message = self.validate_configuration(name, config)
            if error_message:
                validation['passed'] = False
                validation['error_message'] = error_message
                break
        return validation

    def get_configuration_by_name(self, name, configurations, is_mandatory,
                                  validation):
        configurations = [config for config in configurations
                         if config['name'] == name]
        if not configurations and is_mandatory:
            validation["passed"] = False
            validation['error_message'] = "configuration for {0} " \
                                          "is mandatory".format(name)
            return None
        if len(configurations) > 1:
            validation["passed"] = False
            validation['error_message'] = "environment configurations can " \
                                          "only contain one " \
                                          "configuration for {0}".format(name)
            return None

        if not configurations:
            return None
        return configurations[0]

    def validate_configuration(self, name, configuration):
        requirements = {}
        for key in self.CONFIGURATIONS_KEYS[name]:
            requirements[key] = self.REQUIREMENTS[key]
        return self.validate_data(configuration, requirements)
