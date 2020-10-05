###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import datetime
from typing import Optional, List

from dateutil.relativedelta import relativedelta

from base.utils.logging.console_logger import ConsoleLogger
from base.utils.logging.logger import Logger
from manage.async_api_client import AsyncCalipsoClient
from manage.util import Interval, parse_interval

CONFIG_PARSER_DEFAULTS = {
    'discovery_interval': Interval(number=24, unit='h'),
    'replication_interval': Interval(number=24, unit='h'),
    'volume_size': '100Gi'
}


class RemoteHealth:
    def __init__(self, env_name: str):
        self.env_name: str = env_name

        self.version: Optional[str] = None
        self.timezone: Optional[str] = None

        # Is matching environment found on remote
        self.defined: bool = False

        self.scanned: bool = False
        self.scan_in_progress: bool = False
        self.last_scanned: Optional[str] = None

    def set(self, health: dict):
        # Set health version to pod version if defined (keep last known otherwise)
        pod_version = health.get('version')
        if pod_version:
            self.version = pod_version
        pod_timezone = health.get('timezone')
        if pod_timezone:
            self.timezone = pod_timezone

        env_status = health.get('environments', {}).get(self.env_name, {})
        if env_status:
            self.defined = True
            self.scanned = env_status.get('scanned', False)
            self.scan_in_progress = env_status.get('scan_in_progress', False)
            self.last_scanned = env_status.get('last_scanned', None)

            # Set health version to env version (prioritized) if defined (keep last known otherwise)
            env_version = env_status.get('version')
            if env_version:
                self.version = env_version
            env_timezone = env_status.get('timezone')
            if isinstance(env_timezone, str):
                self.timezone = env_timezone
            elif isinstance(env_timezone, dict) and 'tz_name' in env_timezone:
                self.timezone = env_timezone['tz_name']
        else:
            self.defined = False
            self.scanned = False
            self.scan_in_progress = False
            self.last_scanned = None

    def reset(self):
        self.set(health={})

    @property
    def is_ready_for_discovery(self):
        return self.defined and not self.scan_in_progress

    @property
    def is_ready_for_replication(self):
        return self.defined and self.scanned and not self.scan_in_progress


class PodData:
    VERIFY_TLS = True

    # Project-related fields
    PROJECT_NAME_PREFIX = "cvim"
    STACK_FIELD = "{}_{}".format(PROJECT_NAME_PREFIX, "stack")
    REGION_FIELD = "{}_{}".format(PROJECT_NAME_PREFIX, "region")
    METRO_FIELD = "{}_{}".format(PROJECT_NAME_PREFIX, "metro")

    # In seconds
    DEFAULT_CONNECTION_BACKOFF = 5
    MAX_CONNECTION_BACKOFF = 3600

    def __init__(self, stack: str, region: str, metro: str, name: str, host: str,
                 calipso_api_password: str, calipso_mongo_password: str,
                 discovery_interval: Interval, replication_interval: Interval,
                 ca_cert_file: Optional[str] = None, log_level: str = Logger.WARNING):
        self.log = ConsoleLogger(name="Pod Data", level=log_level)

        self.stack = stack
        self.region = region
        self.metro = metro
        self.name = name

        self.calipso_api_password = calipso_api_password
        self.calipso_mongo_password = calipso_mongo_password
        self.ca_cert_file = ca_cert_file

        self.discovery_interval = discovery_interval
        self.replication_interval = replication_interval

        self.env_name = "{}-{}".format(self.PROJECT_NAME_PREFIX, name)
        self.full_name = "{}:{}:{}:{}".format(stack, region, metro, self.env_name)

        ip_parts = host.split(":")
        if len(ip_parts) == 1:
            self.host = host
            self.ip_version = 4
        elif len(ip_parts) == 2:
            self.host = ip_parts[0]
            self.ip_version = 4
        else:
            self.host = ":".join(ip_parts[:-1])
            self.ip_version = 6

        self.next_discovery = None
        self.next_replication = None
        self.health: RemoteHealth = RemoteHealth(env_name=self.env_name)

        self.calipso_client: Optional[AsyncCalipsoClient] = None
        self.set_api_client()

        self._connected: bool = False

        self.next_connection_attempt: Optional[datetime.datetime] = None
        self.failed_connections: int = 0
        self.failed_connection_reason: Optional[str] = None

        # Dynamic pod list support
        self.is_kept = False

    def __repr__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    @classmethod
    def set_project_prefix(cls, prefix: str):
        cls.PROJECT_NAME_PREFIX = prefix
        if cls.PROJECT_NAME_PREFIX:
            cls.STACK_FIELD = "{}_{}".format(cls.PROJECT_NAME_PREFIX, "stack")
            cls.REGION_FIELD = "{}_{}".format(cls.PROJECT_NAME_PREFIX, "region")
            cls.METRO_FIELD = "{}_{}".format(cls.PROJECT_NAME_PREFIX, "metro")
        else:
            cls.STACK_FIELD = "stack"
            cls.REGION_FIELD = "region"
            cls.METRO_FIELD = "metro"

    @property
    def is_available_to_connect(self):
        return not self.next_connection_attempt or datetime.datetime.utcnow() >= self.next_connection_attempt

    @classmethod
    def from_env_config(cls, env: dict) -> Optional['PodData']:
        """
            Try to instantiate a PodData object from environment config dictionary.
        :param env: environment config document
        :return: PodData object if environment document contains all required data, None otherwise
        """
        try:
            env_pod_data = env["pod_data"]

            pod = PodData(
                stack=env[cls.STACK_FIELD],
                region=env[cls.REGION_FIELD],
                metro=env[cls.METRO_FIELD],
                name=env_pod_data["name"],
                host=env_pod_data["host"],
                ca_cert_file=env_pod_data.get("ca_cert_file"),
                calipso_api_password=env_pod_data["api_password"],
                calipso_mongo_password=env_pod_data["mongo_password"],
                discovery_interval=parse_interval(env["discovery_interval"]),
                replication_interval=parse_interval(env["replication_interval"], ),
            )
            pod.health.version = env.get('version')
            pod.health.timezone = env.get('timezone')

            if "next_discovery" in env and "next_replication" in env:
                pod.next_discovery = env["next_discovery"]
                pod.next_replication = env["next_replication"]
            return pod
        except (KeyError, ValueError):
            return None

    def to_env_config(self) -> dict:
        """
            Convert a PodData object to a dict in environment config format.
            Resulting document should be merged with a valid environment config document.
        :return: env config document
        """
        optional_fields = {}
        if self.health.version:
            optional_fields['version'] = self.health.version
        if self.health.timezone:
            optional_fields['timezone'] = self.health.timezone

        return {
            self.STACK_FIELD: self.stack,
            self.REGION_FIELD: self.region,
            self.METRO_FIELD: self.metro,
            "name": self.full_name,
            "pod_data": {
                "name": self.name,
                "host": self.host,
                "api_password": self.calipso_api_password,
                "mongo_password": self.calipso_mongo_password,
                "ca_cert_file": self.ca_cert_file,
            },
            "discovery_interval": "{}{}".format(self.discovery_interval.number, self.discovery_interval.unit),
            "replication_interval": "{}{}".format(self.replication_interval.number, self.replication_interval.unit),
            "next_discovery": self.next_discovery,
            "next_replication": self.next_replication,
            "imported": True,
            **optional_fields
        }

    def is_same_pod(self, other: 'PodData') -> bool:
        """
            Check whether this pod data refers to the same pod as the other
        :param other: pod config to compare to
        :return: whether other pod is the same as this one
        """
        # TODO: compare ips?
        return self.name == other.name

    def config_changed(self, other: 'PodData') -> bool:
        """
            Compare this and other pods' configurations to determine whether reconnection is needed.
            Other pod is assumed to be the same as this one.
            To verify that fact call PodData.is_same_pod method against the other pod config
        :param other: pod config to compare to
        :return: whether pod config has changed considerably
        """
        # TODO: more checks?
        return (
                self.calipso_mongo_password != other.calipso_mongo_password
                or self.calipso_api_password != other.calipso_api_password
                or self.discovery_interval != other.discovery_interval
                or self.replication_interval != other.replication_interval
        )

    def backoff_connection_attempt(self):
        self.failed_connections += 1

        backoff = min(
            self.MAX_CONNECTION_BACKOFF,
            int(self.DEFAULT_CONNECTION_BACKOFF * self.failed_connections),

        )
        if not self.next_connection_attempt:
            self.next_connection_attempt = datetime.datetime.utcnow()
        self.next_connection_attempt += relativedelta(seconds=backoff)

    def reset_connection_backoff(self):
        self.next_connection_attempt = None
        self.failed_connections = 0

    def set_api_client(self):
        self.calipso_client = AsyncCalipsoClient(api_host=self.host,
                                                 api_port=8747,
                                                 api_password=self.calipso_api_password,
                                                 ca_cert_file=self.ca_cert_file,
                                                 verify_tls=self.VERIFY_TLS,
                                                 log_level=self.log.level)

    async def _connect(self):
        if not self.calipso_client:
            self.set_api_client()

        health = await self.calipso_client.connect()
        if health:
            self.health.set(health)
            return True
        else:
            self.log.warning("Failed to check health of remote '{}'".format(self.full_name))
            return False

    async def connect_api(self, force_reconnect: bool = False) -> bool:
        if self.is_connected and self.calipso_client and not force_reconnect:
            return self.is_connected

        self._connected = await self._connect()
        return self.is_connected

    @property
    def is_connected(self) -> bool:
        return self._connected

    def disconnect(self):
        self._connected = False


def _get_nested_object_list(obj: dict, obj_type_name: str, nested_field_name: str, log: Logger) -> list:
    if not isinstance(obj, dict):
        log.error("{} must be a valid dict, not {}".format(obj_type_name, type(obj)))
        return []

    obj_name = obj.get("name")
    if not obj_name or not isinstance(obj_name, str):
        log.error("{} name must be a non-empty string".format(obj_type_name))
        return []

    children = obj.get(nested_field_name)
    if not children:
        log.info("{} {} has no {}".format(obj_type_name, obj_name, nested_field_name))
        return []
    if not isinstance(children, list):
        log.error("{} must be a valid list, not {}".format(nested_field_name.capitalize(), type(children)))
        return []

    return children


def parse_pods_config(stacks_data: List[dict], log: Logger = None) -> Optional[List[PodData]]:
    """
        Parse the stacks data into PodData instances, reporting data warnings and errors along the way.
        Only the remote pod definitions that contain all required Inventory Discovery fields are added to the list.
    :param stacks_data: valid and unaltered stacks list taken from setup data
    :param log: Logger instance
    :return:
        None if stacks document has a global-level structural issue;
        List of matching remotes definitions otherwise
    """
    if not log:
        log = ConsoleLogger(name="parse_pods_config", level=Logger.INFO)

    if not stacks_data:
        log.info("Stacks data is empty")
        return []
    if not isinstance(stacks_data, list):
        log.error("Stacks data must be a list")
        return None

    pods = []
    for stack in stacks_data:
        for region in _get_nested_object_list(obj=stack, obj_type_name="Stack",
                                              nested_field_name="regions", log=log):
            for metro in _get_nested_object_list(obj=region, obj_type_name="Region",
                                                 nested_field_name="metros", log=log):
                for pod in _get_nested_object_list(obj=metro, obj_type_name="Metro",
                                                   nested_field_name="pods", log=log):
                    pod_name = pod.get("name")
                    if not pod_name or not isinstance(pod_name, str):
                        log.error("Pod name must be a non-empty string")
                        continue

                    missing_fields = [
                        field
                        for field in ("ip", "inventory_api_password", "inventory_mongo_password")
                        if field not in pod
                    ]
                    if missing_fields:
                        log.info("Pod definition for '{}:{}:{}:{}' has missing fields: {}. "
                                 "Assuming Inventory Discovery is not supported for this pod."
                                 .format(stack['name'], region['name'], metro['name'], pod_name,
                                         ", ".join(missing_fields)))
                        continue

                    discovery_interval = parse_interval(
                        interval_str=stack.get('inventory_discovery_interval', ''),
                        default_interval=CONFIG_PARSER_DEFAULTS['discovery_interval']
                    )
                    replication_interval = parse_interval(
                        interval_str=stack.get('inventory_replication_interval', ''),
                        default_interval=CONFIG_PARSER_DEFAULTS['replication_interval']
                    )

                    pod = PodData(
                        discovery_interval=discovery_interval,
                        replication_interval=replication_interval,
                        stack=stack['name'],
                        region=region['name'],
                        metro=metro['name'],
                        name=pod['name'],
                        host=pod['ip'],
                        calipso_api_password=pod['inventory_api_password'],
                        calipso_mongo_password=pod['inventory_mongo_password'],
                        ca_cert_file=pod.get('cert'),
                    )  # TODO: log level?
                    pods.append(pod)

    return pods
