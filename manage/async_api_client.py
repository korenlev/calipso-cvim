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
from typing import Optional, Union
from urllib.parse import urljoin

from aiohttp import ClientSession, ClientResponse, BasicAuth

from api.client.calipso_client import APIAuthException, APICallException
from base.utils.logging.console_logger import ConsoleLogger
from base.utils.logging.logger import Logger


class AsyncCalipsoClient:
    VERIFY_TLS = True
    REQUEST_TIMEOUT = 10

    def __init__(self, api_host: str, api_password: str, api_port: int = 8747,
                 verify_tls: Optional[bool] = None, ca_cert_file: Optional[str] = None,
                 log_level: str = Logger.WARNING):
        self.log: Logger = ConsoleLogger(name="Async API Client", level=log_level)
        self.api_server: str = "[{}]".format(api_host) if ":" in api_host and "[" not in api_host else api_host

        self.port: int = api_port
        self.schema: str = "https"
        self.auth_ur: str = "auth/tokens"
        self.headers: dict = {}

        self.ca_cert_file: str = ca_cert_file
        self.ca_cert_data: Optional[str] = None
        self.ssl_context: Union[bool, ssl.SSLContext, None] = False
        self.verify_tls: bool = False
        self._setup_tls_configuration(verify_tls)

        self.username: str = "calipso"
        self.password: str = api_password
        self.auth: BasicAuth = BasicAuth(login=self.username, password=self.password)

    @property
    def base_url(self) -> str:
        return "{}://{}:{}".format(self.schema, self.api_server, self.port)

    def _setup_tls_configuration(self, verify_tls: bool):
        # TODO: make sure TLS verification works as intended
        self.verify_tls = verify_tls if verify_tls is not None else self.VERIFY_TLS
        if self.verify_tls:
            if not self.ca_cert_file:
                self.log.warning("Empty CA certificate file path, unable to setup TLS verification.")
                return

            try:
                with open(self.ca_cert_file) as f:
                    self.ca_cert_data = f.read()

                if self.verify_tls and self.ca_cert_data:
                    self.ssl_context = ssl.create_default_context(cadata=self.ca_cert_data)
            except FileNotFoundError:
                self.log.warning("Failed to read CA certificate file: {}".format(self.ca_cert_file))
                return
            except ssl.SSLError:
                self.log.warning("Failed to get a valid CA certificate from file: {}".format(self.ca_cert_file))
                return

    async def _send_request(self, method: str, endpoint: str, payload: Optional[dict] = None) -> ClientResponse:
        method = method.lower()
        url = urljoin(self.base_url, endpoint)
        async with ClientSession(headers={'Content-Type': 'application/json'}) as session:
            if method == 'post':
                response = await session.post(url, data=json.dumps(payload, default=str),
                                              headers=self.headers, ssl=self.ssl_context,
                                              timeout=self.REQUEST_TIMEOUT, auth=self.auth)
            elif method == 'delete':
                response = await session.delete(url,
                                                headers=self.headers, ssl=self.ssl_context,
                                                timeout=self.REQUEST_TIMEOUT, auth=self.auth)
            elif method == 'put':
                response = await session.put(url, data=json.dumps(payload, default=str),
                                             headers=self.headers, ssl=self.ssl_context,
                                             timeout=self.REQUEST_TIMEOUT, auth=self.auth)
            else:
                response = await session.get(url, params=payload,
                                             headers=self.headers, ssl=self.ssl_context,
                                             timeout=self.REQUEST_TIMEOUT, auth=self.auth)
        return response

    async def send_get(self, endpoint: str, params: Optional[dict] = None) -> ClientResponse:
        return await self._send_request(method="get", endpoint=endpoint, payload=params)

    async def send_post(self, endpoint: str, payload: Optional[dict] = None) -> ClientResponse:
        return await self._send_request(method="post", endpoint=endpoint, payload=payload)

    async def send_put(self, endpoint: str, payload: Optional[dict] = None) -> ClientResponse:
        return await self._send_request(method="put", endpoint=endpoint, payload=payload)

    async def send_delete(self, endpoint: str, payload: Optional[dict] = None) -> ClientResponse:
        return await self._send_request(method="delete", endpoint=endpoint, payload=payload)

    # TODO: rework?
    async def call_api(self, method: str, endpoint: str, payload: dict = None, fail_on_error: bool = True) -> dict:
        try:
            response = await self._send_request(method=method, endpoint=endpoint, payload=payload)
        except ssl.SSLError as e:
            raise APICallException(message="SSL Error while executing request: {}".format(e),
                                   url=endpoint) from e
        except Exception as e:
            raise APICallException(url=endpoint) from e

        err = None
        content = None
        try:
            content = await response.json()
            if "error" in content:
                err = content["error"]
        except ValueError:
            pass

        if not content:
            if response.status == 404:
                raise APICallException(message="Endpoint not found",
                                       url=endpoint)
            if response.status == 400:
                raise APICallException(message="Environment or resource not found, or invalid keys",
                                       url=endpoint)
            raise APICallException(message="API didn't return a valid JSON",
                                   url=endpoint)
        if err and fail_on_error:
            raise APICallException(message=err.get('message', err),
                                   url=endpoint)

        return content

    async def scan_request(self, environment, implicit_links=False):
        request_payload = {
            "log_level": Logger.WARNING.lower(),
            "clear": True,
            "implicit_links": implicit_links,
            "env_name": environment
        }
        return await self.call_api(method="POST", endpoint="scans", payload=request_payload)

    async def connect(self) -> Optional[dict]:
        """
            Connect and return remote health status
        :return:
        """
        try:
            return await self.call_api(method="GET", endpoint="health")
        except (APIAuthException, APICallException) as e:
            self.log.warning("Failed to connect to host '{}'. Error: {}"
                             .format(self.api_server, e))
            return None
