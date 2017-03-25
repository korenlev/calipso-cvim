# HTTP status code
SUCCESSFUL_CODE = "200"
NOT_FOUND_CODE = "404"
CONFLICT_CODE = "409"
BAD_REQUEST_CODE = "400"
UNAUTHORIZED_CODE = "401"
CREATED_CODE = "201"

ENV_NAME = "Mirantis-Liberty-API"
NON_INT_PAGE = 1.4
INT_PAGE = 1
NON_INT_PAGESIZE = 300.4
INT_PAGESIZE = 300

WRONG_LINK_TYPE = "instance-host"
CORRECT_LINK_TYPE= "instance-vnic"

WRONG_LINK_STATE = "wrong"
CORRECT_LINK_STATE = "up"

WRONG_SCAN_STATE = "error"
CORRECT_SCAN_STATE = "completed"

WRONG_MONITORING_SIDE = "wrong-side"
CORRECT_MONITORING_SIDE = "client"

WRONG_MESSAGE_SEVERITY = "wrong-severity"
CORRECT_MESSAGE_SEVERITY = "warn"

WRONG_TYPE_DRIVER = "wrong_type"
CORRECT_TYPE_DRIVER = "local"

WRONG_MECHANISM_DRIVER = "wrong-mechanism-dirver"
CORRECT_MECHANISM_DRIVER = "ovs"

WRONG_LOG_LEVEL = "wrong-log-level"
CORRECT_LOG_LEVEL = "CRITICAL"

WRONG_OBJECT_TYPE = "wrong-object-type"
CORRECT_OBJECT_TYPE = "vnic"

WRONG_ENV_TYPE = ""
CORRECT_ENV_TYPE = "development"

WRONG_DISTRIBUTION = "wrong-environment"
CORRECT_DISTRIBUTION = "Mirantis-6.0"

WRONG_OBJECT_ID = "58a2406e6a283a8bee15d43"
CORRECT_OBJECT_ID = "58a2406e6a283a8bee15d43f"

NON_BOOL = "falses"
BOOL = False

# fake constants
CONSTANTS_BY_NAMES = {
    "link_types": [
        "instance-vnic",
        "otep-vconnector",
        "otep-pnic",
        "pnic-network",
        "vedge-otep",
        "vnic-vconnector",
        "vconnector-pnic",
        "vconnector-vedge",
        "vnic-vedge",
        "vedge-pnic",
        "vservice-vnic"
    ],
    "link_states": [
        "up",
        "down"
    ],
    "scan_statuses": [
        "draft",
        "pending",
        "running",
        "completed",
        "failed",
        "aborted"
    ],
    "monitoring_sides": [
        "client",
        "server"
    ],
    "messages_severity": [
        "panic",
        "alert",
        "crit",
        "error",
        "warn",
        "notice",
        "info",
        "debug"
    ],
    "type_drivers": [
        "local",
        "vlan",
        "vxlan",
        "gre",
        "flat"
    ],
    "mechanism_drivers": [
        "ovs",
        "vpp",
        "LinuxBridge",
        "Arista",
        "Nexus"
    ],
    "log_levels": [
        "CRITICAL",
        "ERROR",
        "WARNING",
        "INFO",
        "DEBUG",
        "NOTSET"
    ],
    "object_types": [
        "vnic",
        "vconnector",
        "vedge",
        "instance",
        "vservice",
        "pnic",
        "network",
        "port",
        "otep",
        "agent"
    ],
    "env_types": [
        "development",
        "testing",
        "staging",
        "production"
    ],
    "distributions": [
        "Mirantis-6.0",
        "Mirantis-7.0",
        "Mirantis-8.0",
        "Mirantis-9.0",
        "RDO-Juno"
    ]
}

# path info
RESPONDER_BASE_PATH = "api.responders.responder_base.ResponderBase"
RESPONDER_BASE_GET_OBJECTS_LIST = RESPONDER_BASE_PATH + ".get_objects_list"
RESPONDER_BASE_GET_OBJECT_BY_ID = RESPONDER_BASE_PATH + ".get_object_by_id"
RESPONDER_BASE_CHECK_ENVIRONMENT_NAME = RESPONDER_BASE_PATH + ".check_environment_name"
RESPONDER_BASE_READ = RESPONDER_BASE_PATH + ".read"
RESPONDER_BASE_WRITE = RESPONDER_BASE_PATH + ".write"
