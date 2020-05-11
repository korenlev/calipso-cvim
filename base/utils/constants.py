###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from collections import namedtuple
from enum import Enum


class StringEnum(Enum):
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)

    @classmethod
    def members(cls):
        return (item.value for item in cls.__members__.values())

    @classmethod
    def members_list(cls):
        return list(cls.members())


class ConnectionTestType(StringEnum):
    AMQP = "AMQP"
    CLI = "CLI"
    ACI = "ACI"
    MYSQL = "mysql"
    OPENSTACK = "OpenStack"
    MONITORING = "Monitoring"
    KUBERNETES = "Kubernetes"


class ConnectionTestStatus(StringEnum):
    REQUEST = "request"
    RESPONSE = "response"


class ScanStatus(StringEnum):
    DRAFT = "draft"
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    COMPLETED_WITH_ERRORS = "completed_with_errors"
    FAILED = "failed"
    ABORTED = "aborted"


class ScheduledScanInterval(StringEnum):
    ONCE = "ONCE"
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"


class ScheduledScanStatus(StringEnum):
    UPCOMING = "upcoming"
    ONGOING = "ongoing"
    FINISHED = "finished"


class OperationalStatus(StringEnum):
    STOPPED = "stopped"
    RUNNING = "running"
    ERROR = "error"


class EnvironmentFeatures(StringEnum):
    SCANNING = "scanning"
    MONITORING = "monitoring"
    LISTENING = "listening"


class GraphType(StringEnum):
    INVENTORY_VEGA = "vega_tree"
    INVENTORY_FORCE = "force_tree"
    INVENTORY_TREE = "children_tree"
    CLIQUE = "clique"


class HostType(StringEnum):
    COMPUTE = "Compute"
    CONTROLLER = "Controller"
    NETWORK = "Network"
    STORAGE = "Storage"
    BAREMETAL = "Bare-metal"
    KUBEMASTER = "Kube-Master"


NetworkAgentType = namedtuple("NetworkAgentType", ["folder_text", "description"])
NETWORK_AGENT_TYPES = {
    "dhcp": NetworkAgentType(folder_text="DHCP servers", description="DHCP agent"),
    "firewall": NetworkAgentType(folder_text="Firewalls", description="Firewall agent"),
    "load_balancer": NetworkAgentType(folder_text="Load-Balancers", description="Load Balancing agent"),
    "metadata": NetworkAgentType(folder_text="Metadata", description="Metadata agent"),
    "orchestrator": NetworkAgentType(folder_text="Orchestrators", description="Orchestrator"),
    "router": NetworkAgentType(folder_text="Gateways", description="L3 agent"),
    "vconnector": NetworkAgentType(folder_text="vConnectors", description="Linux bridge agent, VPP Bridge Domains"),
    "vedge": NetworkAgentType(folder_text="vEdges", description="Open vSwitch agent, VPP agent, SRIOV agent"),
    "vpn": NetworkAgentType(folder_text="VPNs", description="VPN agent"),
}
MISC_AGENT_TYPE = NetworkAgentType(folder_text="Misc. services", description="Miscellaneous")
