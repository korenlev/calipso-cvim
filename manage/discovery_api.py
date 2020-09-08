###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import json
import ssl
from http.client import BAD_REQUEST, CREATED, OK
from json import JSONDecodeError
from typing import Optional, Union

from aiohttp import web

from base.utils.logging.full_logger import FullLogger
from base.utils.logging.logger import Logger
from manage.auth_middleware import BasicAuthMiddleware
from manage.discovery_manager import DiscoveryManager
from manage.pod_data import parse_pods_config

routes = web.RouteTableDef()
discovery_manager: Optional[DiscoveryManager] = None


def json_response(body: Union[dict, list], status_code: int = OK):
    return web.Response(status=status_code,
                        text=json.dumps(body, default=str),
                        content_type="application/json")


@routes.post("/set_remotes")
async def set_remotes(request: web.Request) -> web.Response:
    if request.content_type != "application/json":
        return web.Response(status=BAD_REQUEST,
                            text="Only application/json content type is supported")

    try:
        stacks = json.loads(await request.content.read())
    except JSONDecodeError:
        return web.Response(status=BAD_REQUEST,
                            text="Request body must be a valid JSON")

    remotes = parse_pods_config(stacks)
    discovery_manager.schedule_manager.set_new_pods(remotes)
    return json_response(status_code=CREATED, body={"submitted": len(remotes)})


@routes.get("/get_remotes")
async def get_remotes(request: web.Request) -> web.Response:
    remotes = [{
        "name": pod.full_name,
        "next_discovery": pod.next_discovery,
        "next_replication": pod.next_replication,
        "api_version": pod.health.version,
        "env_timezone": pod.health.timezone,
        "connected": pod.is_connected,
        "environment_defined": pod.health.defined,
        "environment_discovered": pod.health.scanned,
        "scan_in_progress": pod.health.scan_in_progress,
        "last_scanned": pod.health.last_scanned,
    } for pod in discovery_manager.schedule_manager.pods.values()]
    return json_response(body=remotes)


@routes.get("/debug")
async def debug(request: web.Request) -> web.Response:
    m = discovery_manager.schedule_manager
    response = {
        "task": {
            "status": m.task,
        },
        "failing_streak": m.failing_streak,
        "latest_error": m.latest_error,
        "current_op": m.current_op,
        "pods": {
            "connected": [pod.full_name for pod in m.pods.values() if pod.is_connected],
            "disconnected": [pod.full_name for pod in m.pods.values() if not pod.is_connected],
            "new": [pod.full_name for pod in m.new_pods],
            "refresh": m.refresh_pods,
        },
    }
    return json_response(body=response)


@routes.get("/next_schedules")
async def next_schedules(request: web.Request) -> web.Response:
    limit = request.query.get("limit")
    if limit:
        try:
            limit = int(limit)
            if limit <= 0:
                raise ValueError()
        except (ValueError, TypeError):
            return web.Response(status=BAD_REQUEST, text="limit must be a positive integer")
    else:
        limit = 50

    schedule_manager = discovery_manager.schedule_manager
    schedules = []
    for pod in schedule_manager.pods.values():
        if not pod.next_discovery or not pod.next_replication:
            continue
        schedules.extend([
            {
                "remote": pod.name,
                "full_env_name": pod.full_name,
                "operation": "discovery",
                "datetime": pod.next_discovery
            },
            {
                "remote": pod.name,
                "full_env_name": pod.full_name,
                "operation": "replication",
                "datetime": pod.next_replication
            }
        ])
    schedules.sort(key=lambda k: k["datetime"])
    return json_response(body=schedules[:limit])


# TODO: remove
@routes.post("/log")
async def log_post(request: web.Request) -> web.Response:
    discovery_manager.log.info(await request.text())
    return web.Response(text="ok")


class DiscoveryAPI:
    LOG_FILE = "discovery_api.log"
    LOG_LEVEL = Logger.INFO

    DEFAULT_HOST = "localhost"
    DEFAULT_PORT = 8757

    def __init__(self, discovery_mgr: DiscoveryManager,
                 host: Optional[str] = None, port: Optional[int] = None,
                 user: str = None, password: str = None,
                 tls: bool = True, key_file: str = "", cert_file: str = ""):
        global discovery_manager
        discovery_manager = discovery_mgr

        self.hosts = host.split(",") if host else [self.DEFAULT_HOST]
        self.port = port if port else self.DEFAULT_PORT

        self.user = user
        self.password = password

        self.tls = tls
        self.key_file = key_file
        self.cert_file = cert_file
        self.log = FullLogger(name="Discovery API", log_file=self.LOG_FILE, level=self.LOG_LEVEL)

        self.middlewares = []

    def setup_auth(self) -> None:
        """
            Setup authentication middleware(s).
            This method should be called as the first middleware-setting action to prioritize authentication
        :return:
        """
        if self.user and self.password:
            self.log.info("Setting up Basic Auth middleware")
            self.middlewares.append(BasicAuthMiddleware(user=self.user, password=self.password, realm="Discovery API"))
        else:
            self.log.warning("No authentication middleware set")

    def run(self):
        self.setup_auth()

        app = web.Application(logger=self.log.log, middlewares=self.middlewares)
        app.add_routes(routes)

        ssl_context = None
        if self.tls:
            ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            ssl_context.load_cert_chain(self.cert_file, self.key_file)

        web.run_app(app, host=self.hosts, port=self.port, ssl_context=ssl_context)
