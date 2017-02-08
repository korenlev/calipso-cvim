import importlib
import falcon

from api.middle_ware.authentication import AuthenticationMiddleware
from api.exceptions import exceptions


ROUTE_DECLARATIONS = {
    "/inventory": "resource.inventory.Inventory",
    "/links": "resource.links.Links",
    "/messages": "resource.messages.Messages",
    "/cliques": "resource.cliques.Cliques",
    "/clique_types": "resource.clique_types.CliqueTypes",
    "/clique_constraints": "resource.clique_constraints.CliqueConstraints",
    "/scans": "resource.scans.Scans",
    "/constants": "resource.constants.Constants",
    "/monitoring_config_templates": "resource.monitoring_config_templates.MonitoringConfigTemplates",
    "/aggregates": "resource.aggregates.Aggregates",
    "/environment_configs": "resource.environment_configs.EnvironmentConfigs"
}

responders_path = "api.responders"

app = falcon.API(middleware=[
    AuthenticationMiddleware()
])

app.add_error_handler(exceptions.OSDNAApiException)

for url in ROUTE_DECLARATIONS.keys():
    class_path = ROUTE_DECLARATIONS.get(url)
    module_relative_path = ""
    for module in class_path.split('.')[:-1]:
        module_relative_path += module + "."

    module_abs_path = responders_path + '.' + module_relative_path
    module_abs_path = module_abs_path.rstrip(".")

    class_name = class_path.split('.')[-1]
    module = importlib.import_module(module_abs_path)
    class_ = getattr(module, class_name)
    resource = class_()

    app.add_route(url, resource)