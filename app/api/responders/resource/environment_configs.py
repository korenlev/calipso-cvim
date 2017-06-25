########################################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems) and others #
#                                                                                      #
# All rights reserved. This program and the accompanying materials                     #
# are made available under the terms of the Apache License, Version 2.0                #
# which accompanies this distribution, and is available at                             #
# http://www.apache.org/licenses/LICENSE-2.0                                           #
########################################################################################
from api.validation import regex
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
                                     "CLI", "AMQP", "Monitoring", "NFV_provider"]
        self.OPTIONAL_CONFIGURATIONS_NAMES = ["Monitoring", "NFV_provider"]

        self.provision_types = self.\
            get_constants_by_name("environment_provision_types")
        self.env_types = self.get_constants_by_name("env_types")
        self.monitoring_types = self.\
            get_constants_by_name("environment_monitoring_types")
        self.distributions = self.\
            get_constants_by_name("distributions")
        self.mechanism_drivers = self.\
            get_constants_by_name("mechanism_drivers")
        self.operational_values = self.\
            get_constants_by_name("environment_operational_status")
        self.type_drivers = self.\
            get_constants_by_name("type_drivers")

        self.CONFIGURATIONS_REQUIREMENTS = {
            "mysql": {
                "name": self.require(str, mandatory=True),
                "host": self.require(str,
                                     validate=DataValidate.REGEX,
                                     requirement=[regex.IP, regex.HOSTNAME],
                                     mandatory=True),
                "password": self.require(str, mandatory=True),
                "port": self.require(int,
                                     True,
                                     DataValidate.REGEX,
                                     regex.PORT,
                                     mandatory=True),
                "user": self.require(str, mandatory=True)
            },
            "OpenStack": {
                "name": self.require(str, mandatory=True),
                "admin_token": self.require(str, mandatory=True),
                "host": self.require(str,
                                     validate=DataValidate.REGEX,
                                     requirement=[regex.IP, regex.HOSTNAME],
                                     mandatory=True),
                "port": self.require(int,
                                     True,
                                     validate=DataValidate.REGEX,
                                     requirement=regex.PORT,
                                     mandatory=True),
                "pwd": self.require(str, mandatory=True),
                "user": self.require(str, mandatory=True)
            },
            "CLI": {
                "name": self.require(str, mandatory=True),
                "host": self.require(str,
                                     validate=DataValidate.REGEX,
                                     requirement=[regex.IP, regex.HOSTNAME],
                                     mandatory=True),
                "user": self.require(str, mandatory=True),
                "pwd": self.require(str),
                "key": self.require(str,
                                    validate=DataValidate.REGEX,
                                    requirement=regex.PATH)
            },
            "AMQP": {
                "name": self.require(str, mandatory=True),
                "host": self.require(str,
                                     validate=DataValidate.REGEX,
                                     requirement=[regex.IP, regex.HOSTNAME],
                                     mandatory=True),
                "password": self.require(str, mandatory=True),
                "port": self.require(int,
                                     True,
                                     validate=DataValidate.REGEX,
                                     requirement=regex.PORT,
                                     mandatory=True),
                "user": self.require(str, mandatory=True)
            },
            "Monitoring": {
                "name": self.require(str, mandatory=True),
                "config_folder": self.require(str,
                                              validate=DataValidate.REGEX,
                                              requirement=regex.PATH,
                                              mandatory=True),
                "provision": self.require(str,
                                          validate=DataValidate.LIST,
                                          requirement=self.provision_types,
                                          mandatory=True),
                "env_type": self.require(str,
                                         validate=DataValidate.LIST,
                                         requirement=self.env_types,
                                         mandatory=True),
                "api_port": self.require(int, True, mandatory=True),
                "rabbitmq_pass": self.require(str, mandatory=True),
                "rabbitmq_user": self.require(str, mandatory=True),
                "ssh_port": self.require(int,
                                         True,
                                         validate=DataValidate.REGEX,
                                         requirement=regex.PORT),
                "ssh_user": self.require(str),
                "ssh_password": self.require(str),
                "server_ip": self.require(str,
                                          validate=DataValidate.REGEX,
                                          requirement=[regex.IP, regex.HOSTNAME],
                                          mandatory=True),
                "server_name": self.require(str, mandatory=True),
                "type": self.require(str,
                                     validate=DataValidate.LIST,
                                     requirement=self.monitoring_types,
                                     mandatory=True)
            },
            "NFV_provider": {
                "name": self.require(str, mandatory=True),
                "host": self.require(str,
                                     validate=DataValidate.REGEX,
                                     requirement=[regex.IP, regex.HOSTNAME],
                                     mandatory=True),
                "nfv_token": self.require(str, mandatory=True),
                "port": self.require(int,
                                     True,
                                     DataValidate.REGEX,
                                     regex.PORT,
                                     True),
                "user": self.require(str, mandatory=True),
                "pwd": self.require(str, mandatory=True)
            }
        }

    def on_get(self, req, resp):
        self.log.debug("Getting environment config")
        filters = self.parse_query_params(req)

        filters_requirements = {
            "name": self.require(str),
            "distribution": self.require(str, False,
                                         DataValidate.LIST,
                                         self.distributions),
            "mechanism_drivers": self.require([str, list],
                                              False,
                                              DataValidate.LIST,
                                              self.mechanism_drivers),
            "type_drivers": self.require(str, False,
                                         DataValidate.LIST,
                                         self.type_drivers),
            "user": self.require(str),
            "listen": self.require(bool, True),
            "scanned": self.require(bool, True),
            "monitoring_setup_done": self.require(bool, True),
            "operational": self.require(str, False,
                                        DataValidate.LIST,
                                        self.operational_values),
            "page": self.require(int, True),
            "page_size": self.require(int, True)
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

        environment_config_requirement = {
            "app_path": self.require(str, mandatory=True),
            "configuration": self.require(list, mandatory=True),
            "distribution": self.require(str, False, DataValidate.LIST,
                                         self.distributions, True),
            "listen": self.require(bool, True, mandatory=True),
            "user": self.require(str),
            "mechanism_drivers": self.require(list, False, DataValidate.LIST,
                                              self.mechanism_drivers, True),
            "name": self.require(str, mandatory=True),
            "operational": self.require(str, True, DataValidate.LIST,
                                        self.operational_values, mandatory=True),
            "scanned": self.require(bool, True),
            "last_scanned": self.require(str),
            "type": self.require(str, mandatory=True),
            "type_drivers": self.require(str, False, DataValidate.LIST,
                                         self.type_drivers, True)
        }
        self.validate_query_data(env_config,
                                 environment_config_requirement)
        self.check_and_convert_datetime("last_scanned", env_config)
        # validate the configurations
        configurations = env_config['configuration']
        config_validation = self.validate_environment_config(configurations)

        if not config_validation['passed']:
            self.bad_request(config_validation['error_message'])

        if "scanned" not in env_config:
            env_config["scanned"] = False

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

        unknown_configs = [config['name'] for config in configurations
                           if config['name'] not in self.CONFIGURATIONS_NAMES]
        if unknown_configs:
            validation['passed'] = False
            validation['error_message'] = 'Unknown configurations: {0}'. \
                format(' and '.join(unknown_configs))
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
                validation['error_message'] = "{0} error: {1}".\
                    format(name, error_message)
                break
            if name is 'CLI':
                if 'key' not in config and 'pwd' not in config:
                    validation['passed'] = False
                    validation['error_message'] = 'CLI error: either key ' \
                                                  'or pwd must be provided'
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
        return self.validate_data(configuration,
                                  self.CONFIGURATIONS_REQUIREMENTS[name])
