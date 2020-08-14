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
from typing import Optional

from dateutil.relativedelta import relativedelta

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
        self.defined: bool = False
        self.scanned: bool = False
        self.scan_in_progress: bool = False
        self.last_scanned: Optional[str] = None

    def set(self, health: dict):
        self.version = health.get('version', 'unknown')

        env_status = health.get('environments', {}).get(self.env_name, {})
        if env_status:
            self.defined = True
            self.scanned = env_status.get('scanned', False)
            self.scan_in_progress = env_status.get('scan_in_progress', False)
            self.last_scanned = env_status.get('last_scanned', None)
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
    # In seconds
    DEFAULT_CONNECTION_BACKOFF = 5
    MAX_CONNECTION_BACKOFF = 3600

    def __init__(self, stack: str, region: str, metro: str, name: str, host: str,
                 calipso_api_password: str, calipso_mongo_password: str,
                 discovery_interval: Interval, replication_interval: Interval):
        self.stack = stack
        self.region = region
        self.metro = metro
        self.name = name

        self.calipso_api_password = calipso_api_password
        self.calipso_mongo_password = calipso_mongo_password
        self.discovery_interval = discovery_interval
        self.replication_interval = replication_interval

        # TODO: verify naming logic
        self.env_name = "cvim-{}".format(name)
        self.full_name = "{}|{}|{}".format(region, metro, self.env_name)

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

    @property
    def is_available_to_connect(self):
        return not self.next_connection_attempt or datetime.datetime.utcnow() >= self.next_connection_attempt

    @staticmethod
    def from_env_config(env: dict) -> Optional['PodData']:
        """
            Try to instantiate a PodData object from environment config dictionary.
        :param env: environment config document
        :return: PodData object if environment document contains all required data, None otherwise
        """
        try:
            env_pod_data = env["pod_data"]
            pod = PodData(
                stack=env["cvim_stack"],
                region=env["cvim_region"],
                metro=env["cvim_metro"],
                name=env_pod_data["name"],
                host=env_pod_data["host"],
                calipso_api_password=env_pod_data["api_password"],
                calipso_mongo_password=env_pod_data["mongo_password"],
                discovery_interval=parse_interval(env["discovery_interval"]),
                replication_interval=parse_interval(env["replication_interval"])
            )
            if "next_discovery" in env and "next_replication" in env:
                # TODO: test timezones
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
        return {
            "name": self.full_name,
            "cvim_stack": self.stack,
            "cvim_region": self.region,
            "cvim_metro": self.metro,
            "pod_data": {
                "name": self.name,
                "host": self.host,
                "api_password": self.calipso_api_password,
                "mongo_password": self.calipso_mongo_password,
            },
            "discovery_interval": "{}{}".format(self.discovery_interval.number, self.discovery_interval.unit),
            "replication_interval": "{}{}".format(self.replication_interval.number, self.replication_interval.unit),
            "next_discovery": self.next_discovery,
            "next_replication": self.next_replication
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
                                                 api_password=self.calipso_api_password)

    async def _connect(self):
        if not self.calipso_client:
            self.set_api_client()

        health = await self.calipso_client.connect()
        if health:
            self.health.set(health)
            return True
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


def parse_pods_config(stacks_data: dict) -> list:
    if not stacks_data:
        return []

    pods = []
    for stack in stacks_data:
        for region in stack.get('regions', []):
            for metro in region.get('metros', []):
                for pod in metro.get('pods', []):
                    # TODO: field namings
                    if any(field not in pod for field in ("ip", "inventory_api_password", "inventory_mongo_password")):
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
                        stack=stack['name'],
                        discovery_interval=discovery_interval,
                        replication_interval=replication_interval,
                        region=region['name'],
                        metro=metro['name'],
                        name=pod['name'],
                        host=pod['ip'],
                        calipso_api_password=pod['inventory_api_password'],
                        calipso_mongo_password=pod['inventory_mongo_password'],
                    )
                    pods.append(pod)

    return pods
