###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import importlib

import falcon

from api.auth.token import Token
from api.backends import auth_backend
from api.backends.credentials_backend import CredentialsBackend
from api.backends.ldap_backend import LDAPBackend
from api.exceptions.exceptions import CalipsoApiException
from api.middleware import AuthenticationMiddleware, CORSMiddleware
from base.utils.inventory_mgr import InventoryMgr
from base.utils.logging.full_logger import FullLogger
from base.utils.mongo_access import MongoAccess


class App:

    CORE_ENDPOINTS = {
        "/aggregates": "resource.aggregates.Aggregates",
        "/clique_constraints": "resource.clique_constraints.CliqueConstraints",
        "/clique_types": "resource.clique_types.CliqueTypes",
        "/cliques": "resource.cliques.Cliques",
        "/connection_tests": "resource.connection_tests.ConnectionTests",
        "/constants": "resource.constants.Constants",
        "/environment_configs": "resource.environment_configs.EnvironmentConfigs",
        "/graph": "resource.graph.Graph",
        "/health": "resource.health.Health",
        "/inventory": "resource.inventory.Inventory",
        "/links": "resource.links.Links",
        "/messages": "resource.messages.Messages",
        "/monitoring_config_templates": "resource.monitoring_config_templates.MonitoringConfigTemplates",
        "/scans": "resource.scans.Scans",
        "/scheduled_scans": "resource.scheduled_scans.ScheduledScans",
        "/schema": "resource.schema.Schema",
        "/search": "resource.search.Search",
        "/timezone": "resource.timezone.Timezone",
    }
    BASE_GRAFANA_ENDPOINTS = {
        "/grafana": "grafana.__init__.Health",
        "/grafana/search": "grafana.search.Search",
        "/grafana/query": "grafana.query.Query",
    }
    ROUTE_DECLARATIONS = {
        "/auth/tokens": "auth.tokens.Tokens",
        **CORE_ENDPOINTS,
        **BASE_GRAFANA_ENDPOINTS,
        **{"/grafana/query{}".format(k): v for k, v in CORE_ENDPOINTS.items()}
    }

    responders_path = "api.responders"

    def __init__(self, mongo_config: str = "", ldap_enabled: bool = True, ldap_config: str = "", auth_config: str = "",
                 log_level: str = "", log_file: str = "", inventory: str = "", token_lifetime: int = 86400):
        MongoAccess.set_config_file(mongo_config)
        self.inv = InventoryMgr()
        self.inv.set_collections(inventory)

        self.log = FullLogger(name="API", log_file=log_file, level=log_level)
        self.setup_auth_backend(ldap_enabled=ldap_enabled, ldap_config=ldap_config, auth_config=auth_config,
                                log_file=log_file, log_level=log_level)
        Token.set_token_lifetime(token_lifetime)
        self.middleware = [
            AuthenticationMiddleware(log_file=log_file, log_level=log_level),
            CORSMiddleware()
        ]

        self.app = falcon.API(middleware=self.middleware)
        self.app.add_error_handler(CalipsoApiException)
        self.app.req_options.strip_url_path_trailing_slash = True
        self.set_routes(self.app)

    def get_app(self):
        return self.app

    def set_routes(self, app):
        for url in self.ROUTE_DECLARATIONS.keys():
            class_path = self.ROUTE_DECLARATIONS.get(url)
            module = self.responders_path + "." + class_path[:class_path.rindex(".")]
            class_name = class_path.split('.')[-1]
            module = importlib.import_module(module)
            class_ = getattr(module, class_name)
            resource = class_()
            app.add_route(url, resource)

    def setup_auth_backend(self, ldap_enabled: bool, ldap_config: str, auth_config: str = "",
                           log_file: str = "", log_level: str = ""):
        if ldap_enabled:
            try:
                auth_backend.ApiAuth = LDAPBackend(config_file_path=ldap_config, log_file=log_file, log_level=log_level)
                return
            except ValueError as e:
                self.log.error("Failed to setup LDAP access. Exception: {}".format(e))
                raise ValueError("LDAP authentication required.")
        elif auth_config:
            try:
                auth_backend.ApiAuth = CredentialsBackend(auth_config)
                self.log.info("Set up credentials authentication")
                return
            except ValueError as e:
                self.log.error("Failed to setup credentials access. Exception: {}".format(e))
                raise ValueError("Credentials authentication required.")
        else:
            self.log.info("Skipping LDAP authentication")

        # TODO: try mongo auth
        self.log.warning("Falling back to no authentication")
