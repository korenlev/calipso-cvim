from api.responders.responder_base import ResponderBase
from api.etc.data_validate import DataValidate


class EnvironmentConfigs(ResponderBase):

    def __init__(self):
        super(EnvironmentConfigs, self).__init__()
        self.collection = "environments_config"
        self.mandatory_configurations_names = ["mysql", "OpenStack", "CLI", "AMQP"]
        self.optional_configurations_names = ["Monitoring"]
        self.config_validation_map = {
            "mysql": self.validate_mysql_config,
            "OpenStack": self.validate_openstack_config,
            "CLI": self.validate_cli_config,
            "AMQP": self.validate_amqp_config,
            "Monitoring": self.validate_monitoring_config
        }

    def on_post(self, req, resp):
        self.log.debug("Creating a new environment config")

        error, env_config = self.get_content_from_request(req)
        if error:
            self.bad_request(error)

        distributions = self.get_constants_by_name("distributions")
        mechanism_drivers = self.get_constants_by_name("mechanism_drivers")
        type_drivers = self.get_constants_by_name("type_drivers")

        environment_config_requirement = {
            "configuration": self.get_validate_requirement(list, mandatory=True),
            "distribution": self.get_validate_requirement(str, False, DataValidate.LIST, distributions, True),
            "last_scanned": self.get_validate_requirement(str, mandatory=True),
            "mechanism_drivers": self.get_validate_requirement(list, False, DataValidate.LIST, mechanism_drivers, True),
            "monitoring_setup_done": self.get_validate_requirement(bool, True, mandatory=True),
            "name": self.get_validate_requirement(str, mandatory=True),
            "operational": self.get_validate_requirement(bool, True, mandatory=True),
            "scanned": self.get_validate_requirement(bool, True, mandatory=True),
            "type": self.get_validate_requirement(str, mandatory=True),
            "type_drivers": self.get_validate_requirement(str, False, DataValidate.LIST, type_drivers, True)
        }

        env_validation = self.validate_data(env_config, environment_config_requirement)
        if not env_validation['passed']:
            self.bad_request(env_validation['error_message'])

        # validate the configurations
        configurations = env_config['configuration']
        config_validation = self.validate_environment_config(configurations)

        if not config_validation['passed']:
            self.bad_request(config_validation['error_message'])

        env_name = env_config['name']
        db_environment_config = self.read(self.collection, {"name": env_name})
        if db_environment_config:
            self.conflict("configuration for environment {0} has existed".format(env_name))

        self.write(env_config, "environments_config")
        self.set_successful_response(resp, "201")

    def validate_environment_config(self, configurations):
        configurations_of_names = {}
        validation = {"passed": True}

        for name in self.mandatory_configurations_names:
            configuration = [config for config in configurations if config['name'] == name]
            if not configuration:
                validation["passed"] = False
                validation['error_message'] = "configuration for {0} is mandatory".format(name)
                return validation
            if len(configuration) > 1:
                validation["passed"] = False
                validation['error_message'] = "environment configurations should only contain one" \
                                              "configuration for {0}".format(name)
                return validation
            configurations_of_names[name] = configuration[0]

        for name in self.optional_configurations_names:
            configuration = [config for config in configurations if config['name'] == name]
            if len(configuration) > 1:
                validation["passed"] = False
                validation['error_message'] = "environment configuration should only contain one" \
                                              "configuration for {0}".format(name)
                return validation
            if configuration:
                configurations_of_names[name] = configuration[0]

        for name, config in configurations_of_names.items():
            config_validation = self.config_validation_map[name](config)
            if not config_validation['passed']:
                validation['passed'] = False
                validation['error_message'] = config_validation['error_message']
                break

        return validation

    def validate_mysql_config(self, mysql_config):
        mysql_requirements = {
            "host": self.get_validate_requirement(str, mandatory=True),
            "password": self.get_validate_requirement(str, mandatory=True),
            "port": self.get_validate_requirement(int, True, mandatory=True),
            "user": self.get_validate_requirement(str, mandatory=True)
        }
        return self.validate_data(mysql_config, mysql_requirements)

    def validate_openstack_config(self, openstack_config):
        openstack_requirements = {
            "host": self.get_validate_requirement(str, mandatory=True),
            "admin_project": self.get_validate_requirement(str, mandatory=True),
            "admin_token": self.get_validate_requirement(str, mandatory=True),
            "port": self.get_validate_requirement(int, True, mandatory=True),
            "user": self.get_validate_requirement(str, mandatory=True),
            "pwd": self.get_validate_requirement(str, mandatory=True)
        }
        return self.validate_data(openstack_config, openstack_requirements)

    def validate_cli_config(self, cli_config):
        cli_requirements = {
            "host": self.get_validate_requirement(str, mandatory=True),
            "key": self.get_validate_requirement(str, mandatory=True),
            "pwd": self.get_validate_requirement(str, mandatory=True),
            "user": self.get_validate_requirement(str, mandatory=True)
        }
        return self.validate_data(cli_config, cli_requirements)

    def validate_amqp_config(self, amqp_config):
        ampd_requirements = {
            "host": self.get_validate_requirement(str, mandatory=True),
            "port": self.get_validate_requirement(int, True, mandatory=True),
            "user": self.get_validate_requirement(str, mandatory=True),
            "password": self.get_validate_requirement(str, mandatory=True)
        }
        return self.validate_data(amqp_config, ampd_requirements)

    def validate_monitoring_config(self, monitoring_config):
        monitoring_requirements = {
            "app_path": self.get_validate_requirement(str, mandatory=True),
            "config_folder": self.get_validate_requirement(str, mandatory=True),
            "debug": self.get_validate_requirement(bool, True, mandatory=True),
            "env_type": self.get_validate_requirement(str, False, DataValidate.LIST, ["development", "product"],
                                                      mandatory=True),
            "osdna_path": self.get_validate_requirement(str, mandatory=True),
            "port": self.get_validate_requirement(int, True, mandatory=True),
            "rabbitmq_pass": self.get_validate_requirement(str, mandatory=True),
            "rabbitmq_user": self.get_validate_requirement(str, mandatory=True),
            "server_ip": self.get_validate_requirement(str, mandatory=True),
            "server_name": self.get_validate_requirement(str, mandatory=True),
            "type": self.get_validate_requirement(str, mandatory=True)
        }
        return self.validate_data(monitoring_config, monitoring_requirements)