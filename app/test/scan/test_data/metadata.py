METADATA_EMPTY = {}

METADATA_SCANNERS_MISSING = {"scanners_package": "discover"}

METADATA_NO_PACKAGE = {
  "scanners": {}
}

METADATA_NO_SCANNERS = {
  "scanners_package": "discover"
}

METADATA_ZERO_SCANNERS = {
  "scanners_package": "discover",
  "scanners": {}
}

METADATA_SIMPLE_SCANNER = {
  "scanners_package": "discover",
  "scanners": {
    "ScanAggregate": [
      {
        "type": "host_ref",
        "fetcher": "DbFetchAggregateHosts"
      }
    ]
  }
}

METADATA_SCANNER_UNKNOWN_ATTRIBUTE = {
  "scanners_package": "discover",
  "scanners": {
    "ScanAggregate": [
      {
        "xyz": "123",
        "type": "host_ref",
        "fetcher": "DbFetchAggregateHosts"
      }
    ]
  }
}

METADATA_SCANNER_NO_TYPE = {
  "scanners_package": "discover",
  "scanners": {
    "ScanAggregate": [
      {
        "fetcher": "DbFetchAggregateHosts"
      }
    ]
  }
}

METADATA_SCANNER_NO_FETCHER = {
  "scanners_package": "discover",
  "scanners": {
    "ScanAggregate": [
      {
        "type": "host_ref"
      }
    ]
  }
}

METADATA_SCANNER_INCORRECT_TYPE = {
  "scanners_package": "discover",
  "scanners": {
    "ScanAggregate": [
      {
        "type": "t1",
        "fetcher": "DbFetchAggregateHosts"
      }
    ]
  }
}

METADATA_SCANNER_INCORRECT_FETCHER = {
  "scanners_package": "discover",
  "scanners": {
    "ScanAggregate": [
      {
        "type": "host_ref",
        "fetcher": "f1"
      }
    ]
  }
}

METADATA_SCANNER_WITH_CHILD = {
  "scanners_package": "discover",
  "scanners": {
    "ScanAggregatesRoot": [
      {
        "type": "aggregate",
        "fetcher": "DbFetchAggregates",
        "children_scanner": "ScanAggregate"
      }
    ],
    "ScanAggregate": [
      {
        "type": "host_ref",
        "fetcher": "DbFetchAggregateHosts"
      }
    ]
  }
}

METADATA_SCANNER_WITH_INCORRECT_CHILD = {
  "scanners_package": "discover",
  "scanners": {
    "ScanAggregatesRoot": [
      {
        "type": "aggregate",
        "fetcher": "DbFetchAggregates",
        "children_scanner": 1
      }
    ]
  }
}

METADATA_SCANNER_WITH_MISSING_CHILD = {
  "scanners_package": "discover",
  "scanners": {
    "ScanAggregatesRoot": [
      {
        "type": "aggregate",
        "fetcher": "DbFetchAggregates",
        "children_scanner": "ScanAggregate"
      }
    ]
  }
}

METADATA_SCANNER_FETCHER_INVALID_DICT = {
  "scanners_package": "discover",
  "scanners": {
    "ScanEnvironment": [
      {
        "type": "regions_folder",
        "fetcher": {
          "types_name": "regions",
          "parent_type": "environment"
        }
      },
    ]

  }
}

METADATA_SCANNER_WITH_FOLDER = {
  "scanners_package": "discover",
  "scanners": {
    "ScanEnvironment": [
      {
        "type": "regions_folder",
        "fetcher": {
          "folder": 1,
          "types_name": "regions",
          "parent_type": "environment"
        }
      },
      {
        "type": "projects_folder",
        "fetcher": {
          "folder": 1,
          "types_name": "projects",
          "parent_type": "environment"
        }
      }
    ]
  }
}

METADATA_SCANNER_WITH_INVALID_CONDITION = {
  "scanners_package": "discover",
  "scanners": {
    "ScanHost": [
      {
        "type": "pnics_folder",
        "fetcher": "DbFetchAggregateHosts",
        "environment_condition": 1
      }
    ]
  }
}

METADATA_SCANNER_WITH_INVALID_MECHANISM_DRIVER_CONDITION = {
  "scanners_package": "discover",
  "scanners": {
    "ScanHost": [
      {
        "type": "pnics_folder",
        "fetcher": {
          "folder": 1,
          "types_name": "pnics",
          "parent_type": "host",
          "text": "pNICs"
        },
        "environment_condition": {
          "mechanism_drivers": ""
        }
      }
    ]
  }
}

METADATA_SCANNER_WITH_INVALID_MECHANISM_DRIVER = {
  "scanners_package": "discover",
  "scanners": {
    "ScanHost": [
      {
        "type": "pnics_folder",
        "fetcher": {
          "folder": 1,
          "types_name": "pnics",
          "parent_type": "host",
          "text": "pNICs"
        },
        "environment_condition": {
          "mechanism_drivers": [ 1, 2]
        }
      }
    ]
  }
}

METADATA_SCANNER_WITH_CONDITION = {
  "scanners_package": "discover",
  "scanners": {
    "ScanHost": [
      {
        "type": "pnics_folder",
        "fetcher": {
          "folder": 1,
          "types_name": "pnics",
          "parent_type": "host",
          "text": "pNICs"
        },
        "environment_condition": {
          "mechanism_drivers": [
            "OVS",
            "LXB"
          ]
        }
      }
    ]
  }
}

