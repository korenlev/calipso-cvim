###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import asyncio
import re

from base.utils.logging.full_logger import FullLogger
from base.utils.logging.logger import Logger
from manage.pod_data import PodData


class PodManager:
    LOG_FILE = "pod_manager.log"
    LOG_LEVEL = Logger.INFO

    SUPPORTED_VERSIONS = []  # TODO: ["<={}".format(VERSION)]
    OPERATOR_REGEX = re.compile("((!=?)|([<>]=?))?(\d+)")

    def __init__(self):
        self.log = FullLogger(name="Pod Manager", log_file=self.LOG_FILE, level=self.LOG_LEVEL)
        self.supported_versions = []
        self._prepare_supported_versions()

    def _prepare_supported_versions(self):
        self.supported_versions = []
        for version_req in self.SUPPORTED_VERSIONS:
            version_req_parts = version_req.split(".")
            match = re.match(self.OPERATOR_REGEX, version_req_parts[0])
            if not match:
                raise ValueError("Illegal version requirement: '{}'".format(version_req))
            operator, version_req_parts[0] = match.groups()[0], match.groups()[3]

            try:
                version_req_parts = [int(vp) for vp in version_req_parts]
            except ValueError:
                self.log.error("Illegal version requirement: '{}'".format(version_req))
                return False

            self.supported_versions.append(
                {
                    "operator": operator if operator else "==",
                    "version_parts": version_req_parts
                }
            )

    def _validate_version(self, version: str) -> bool:
        if not version:
            return False

        try:
            version_parts = [int(vp) for vp in version.split(".")]
        except (ValueError, AttributeError):
            return False

        def validate_req(req: dict):
            op = req["operator"]
            if op == "==":
                return version_parts == req["version_parts"]
            elif op == "!=":
                return version_parts != req["version_parts"]

            for i, version_req_part in enumerate(req["version_parts"]):
                part = version_parts[i]
                if op == ">=":
                    if part < version_req_part:
                        return False
                    if part > version_req_part:
                        return True
                elif op == ">":
                    if part > version_req_part:
                        return True
                    if part < version_req_part:
                        return False
                elif op == "<=":
                    if part < version_req_part:
                        return True
                    elif part > version_req_part:
                        return False
                elif op == "<":
                    if part < version_req_part:
                        return True
                    if part > version_req_part:
                        return False
            return True if op in (">=", "<=") else False

        return all(validate_req(version_req) for version_req in self.supported_versions)

    async def set_pod_health(self, pod: PodData):
        pod.health.reset()
        response = None
        try:
            response = await pod.calipso_client.send_get(endpoint="/health")
            response.raise_for_status()
            pod.health.set(await response.json())
        except asyncio.TimeoutError:
            self.log.warning("Timed out while checking health of remote {}".format(pod.name))
        except Exception as e:
            self.log.warning(
                "Failed to check health of remote {}. HTTP code: {}. Error: {}"
                    .format(pod.name, response.status if response else "unknown", e)
            )
            # Pod is disconnected/unresponsive
            pod.disconnect()

    def is_pod_compatible(self, pod: PodData) -> bool:
        """
            Check remote pod's connection, version and health
        :return: whether pod is fully connected and compatible with schedule manager
        """
        if not pod.is_connected:
            return False

        if not self._validate_version(pod.health.version):
            self.log.info(
                "Remote {} has unsupported API version: '{}'"
                    .format(pod.name, pod.health.version if pod.health.version else "unknown"))
            return False

        self.log.debug("Remote {} has API version '{}'".format(pod.name, pod.health.version))
        return True

    def check_pod_available_for_action(self, pod: PodData, action: str = None) -> bool:
        if not pod.is_connected:
            self.log.debug("Remote {} is not connected".format(pod.name))
            return False

        if not pod.health.defined:
            self.log.debug("Environment {} not found on remote {}".format(pod.env_name, pod.name))
            return False

        if action == "discovery":
            return pod.health.is_ready_for_discovery
        elif action == "replication":
            return pod.health.is_ready_for_replication

        return True
