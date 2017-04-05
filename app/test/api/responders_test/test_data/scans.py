from test.api.responders_test.test_data import base

URL = "/scans"

WRONG_ID = base.WRONG_OBJECT_ID
NONEXISTENT_ID = "58c96a075eb66a121cc4e750"
CORRECT_ID = base.CORRECT_OBJECT_ID

BASE_OBJECT = "node-2.cisco.com"

WRONG_STATUS = base.WRONG_SCAN_STATUS
CORRECT_STATUS = base.CORRECT_SCAN_STATUS

SCANS = [
    {
        "status": "pending",
        "environment": "Mirantis-Liberty-API",
        "id": "58c96a075eb66a121cc4e75f",
        "scan_completed": True
    },
    {
        "status": "completed",
        "environment": "Mirantis-Liberty-API",
        "id": "58c96a075eb66a121cc4e75e",
        "scan_completed": True
    }
]

SCANS_RESPONSE = {
    "scans": SCANS
}

SCANS_WITH_SPECIFIC_ID = [
    {
        "status": "pending",
        "environment": "Mirantis-Liberty-API",
        "id": CORRECT_ID,
        "scan_completed": True
    }
]

SCANS_WITH_SPECIFIC_BASE_OBJ = [
    {
        "status": "pending",
        "environment": "Mirantis-Liberty-API",
        "id": "58c96a075eb66a121cc4e75f",
        "object_id": BASE_OBJECT
    },
    {
        "status": "completed",
        "environment": "Mirantis-Liberty-API",
        "id": "58c96a075eb66a121cc4e75e",
        "object_id": BASE_OBJECT
    }
]

SCANS_WITH_SPECIFIC_BASE_OBJ_RESPONSE = {
    "scans": SCANS_WITH_SPECIFIC_BASE_OBJ
}

SCANS_WITH_SPECIFIC_STATUS = [
    {
        "status": CORRECT_STATUS,
        "environment": "Mirantis-Liberty-API",
        "id": "58c96a075eb66a121cc4e75f",
    },
    {
        "status": CORRECT_STATUS,
        "environment": "Mirantis-Liberty-API",
        "id": "58c96a075eb66a121cc4e75e",
        "scan_completed": True
    }
]

SCANS_WITH_SPECIFIC_STATUS_RESPONSE = {
    "scans": SCANS_WITH_SPECIFIC_STATUS
}

NON_DICT_SCAN = base.NON_DICT_OBJ

SCAN = {
       "status": "pending",
       "log_level": "warning",
       "clear": True,
       "scan_only_inventory": True,
       "scan_only_links": True,
       "scan_only_cliques": True,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITHOUT_ENV = {
       "status": "pending",
       "log_level": "warning",
       "clear": True,
       "scan_only_inventory": True,
       "scan_only_links": True,
       "scan_only_cliques": True,
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITH_UNKNOWN_ENV = {
       "status": "pending",
       "log_level": "warning",
       "clear": True,
       "scan_only_inventory": True,
       "scan_only_links": True,
       "scan_only_cliques": True,
       "environment": base.UNKNOWN_ENV,
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITHOUT_STATUS = {
       "log_level": "warning",
       "clear": True,
       "scan_only_inventory": True,
       "scan_only_links": True,
       "scan_only_cliques": True,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITH_WRONG_STATUS = {
       "status": WRONG_STATUS,
       "log_level": "warning",
       "clear": True,
       "scan_only_inventory": True,
       "scan_only_links": True,
       "scan_only_cliques": True,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITHOUT_LOG_LEVEL = {
       "status": "pending",
       "clear": True,
       "scan_only_inventory": True,
       "scan_only_links": True,
       "scan_only_cliques": True,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITH_WRONG_LOG_LEVEL = {
       "status": "pending",
       "log_level": base.WRONG_LOG_LEVEL,
       "clear": True,
       "scan_only_inventory": True,
       "scan_only_links": True,
       "scan_only_cliques": True,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITHOUT_CLEAR = {
       "status": "pending",
       "log_level": "warning",
       "scan_only_inventory": True,
       "scan_only_links": True,
       "scan_only_cliques": True,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITH_NON_BOOL_CLEAR = {
       "status": "pending",
       "log_level": "warning",
       "clear": base.NON_BOOL,
       "scan_only_inventory": True,
       "scan_only_links": True,
       "scan_only_cliques": True,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITHOUT_SCAN_ONLY_INVENTORY = {
       "status": "pending",
       "log_level": "warning",
       "clear": True,
       "scan_only_links": True,
       "scan_only_cliques": True,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITH_NON_BOOL_SCAN_ONLY_INVENTORY = {
       "status": "pending",
       "log_level": "warning",
       "clear": True,
       "scan_only_inventory": base.NON_BOOL,
       "scan_only_links": True,
       "scan_only_cliques": True,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITHOUT_SCAN_ONLY_LINKS = {
       "status": "pending",
       "log_level": "warning",
       "clear": True,
       "scan_only_inventory": True,
       "scan_only_cliques": True,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITH_NON_BOOL_SCAN_ONLY_LINKS = {
       "status": "pending",
       "log_level": "warning",
       "clear": True,
       "scan_only_inventory": True,
       "scan_only_links": base.NON_BOOL,
       "scan_only_cliques": True,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITHOUT_SCAN_ONLY_CLIQUES = {
       "status": "pending",
       "log_level": "warning",
       "clear": True,
       "scan_only_inventory": True,
       "scan_only_links": True,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITH_NON_BOOL_SCAN_ONLY_CLIQUES = {
       "status": "pending",
       "log_level": "warning",
       "clear": True,
       "scan_only_inventory": True,
       "scan_only_links": True,
       "scan_only_cliques": base.NON_BOOL,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
       "object_id": "ff"
}

SCAN_WITHOUT_INVENTORY_NAME = {
       "status": "pending",
       "log_level": "warning",
       "clear": True,
       "scan_only_inventory": True,
       "scan_only_links": True,
       "scan_only_cliques": True,
       "environment": "Mirantis-Liberty-API",
       "object_id": "ff"
}

SCAN_WITHOUT_OBJ_ID = {
       "status": "pending",
       "log_level": "warning",
       "clear": True,
       "scan_only_inventory": True,
       "scan_only_links": True,
       "scan_only_cliques": True,
       "environment": "Mirantis-Liberty-API",
       "inventory": "inventory",
}
