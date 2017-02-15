import importlib
import falcon

from api.backends.ldap_access import LDAPAccess
from api.backends.mongo_mgr import MongoMgr
from api.exceptions.exceptions import OSDNAApiException
from api.middleware.authentication import AuthenticationMiddleware


class App:

    ROUTE_DECLARATIONS = {
        "/inventory": "resource.inventory.Inventory",
        "/links": "resource.links.Links",
        "/messages": "resource.messages.Messages",
        "/cliques": "resource.cliques.Cliques",
        "/clique_types": "resource.clique_types.CliqueTypes",
        "/clique_constraints": "resource.clique_constraints.CliqueConstraints",
        "/scans": "resource.scans.Scans",
        "/constants": "resource.constants.Constants",
        "/monitoring_config_templates":
            "resource.monitoring_config_templates.MonitoringConfigTemplates",
        "/aggregates": "resource.aggregates.Aggregates",
        "/environment_configs": "resource.environment_configs.EnvironmentConfigs"
    }

    responders_path = "api.responders"

    def __init__(self, mongo_config="", ldap_config="", log_level=""):
        self.mongoMgr = MongoMgr(mongo_config)
        self.mongoMgr.set_loglevel(log_level)
        self.ldap = LDAPAccess(ldap_config)
        self.middleware = AuthenticationMiddleware()
        # self.app = falcon.API(middleware=[self.middleware])
        self.app = falcon.API()
        self.app.add_error_handler(OSDNAApiException)
        self.set_routes(self.app)

    def get_app(self):
        return self.app

    def set_routes(self, app):
        for url in self.ROUTE_DECLARATIONS.keys():
            class_path = self.ROUTE_DECLARATIONS.get(url)
            module = self.responders_path + "." + \
                     class_path[:class_path.rindex(".")]
            class_name = class_path.split('.')[-1]
            module = importlib.import_module(module)
            class_ = getattr(module, class_name)
            resource = class_()
            app.add_route(url, resource)
