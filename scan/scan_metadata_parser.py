###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from typing import Optional, Union

from base.utils.metadata_parser import MetadataParser
from base.utils.mongo_access import MongoAccess
from base.utils.util import ClassResolver
from scan.fetchers.folder_fetcher import FolderFetcher


class ScanMetadataParser(MetadataParser):

    SCANNERS_PACKAGE = 'scanners_package'
    SCANNERS_FILE = 'scanners.json'
    SCANNERS = 'scanners'

    TYPE = 'type'
    FETCHER = 'fetcher'
    CHILDREN_SCANNER = 'children_scanner'
    ENVIRONMENT_CONDITION = 'environment_condition'
    ENVIRONMENT_RESTRICTION = 'environment_restriction'
    OBJECT_ID_TO_USE_IN_CHILD = 'object_id_to_use_in_child'

    COMMENT = '_comment'

    REQUIRED_SCANNER_ATTRIBUTES = [TYPE, FETCHER]
    ALLOWED_SCANNER_ATTRIBUTES = [TYPE, FETCHER, CHILDREN_SCANNER,
                                  ENVIRONMENT_CONDITION, ENVIRONMENT_RESTRICTION,
                                  OBJECT_ID_TO_USE_IN_CHILD]

    MECHANISM_DRIVER = 'mechanism_driver'

    def __init__(self, inventory_mgr):
        super().__init__()
        self.inv = inventory_mgr
        self.constants = MongoAccess.db['constants']
        self.environment_types = [et["value"] for et in self.constants.find_one({"name": "environment_types"})["data"]]

    def get_required_fields(self):
        return [self.SCANNERS_PACKAGE, self.SCANNERS]

    def validate_fetcher(self, scanner_name: str, scan_type: dict,
                         type_index: int, package: str):
        fetcher = scan_type.get(self.FETCHER, '')
        if not fetcher:
            self.add_error('missing or empty fetcher in scanner {} type #{}'
                           .format(scanner_name, str(type_index)))
        elif isinstance(fetcher, str):
            error_str = None
            try:
                get_module = ClassResolver.get_module_file_by_class_name
                module_name = get_module(fetcher)
                fetcher_package = module_name.split("_")[0]
                if package:
                    fetcher_package = ".".join((package, fetcher_package))
                # get the fetcher qualified class but not a class instance
                # instances will be created just-in-time (before fetching):
                # this avoids init of access classes not needed in some envs
                get_class = ClassResolver.get_fully_qualified_class
                class_qualified = get_class(fetcher, fetcher_package,
                                            module_name)
            except ValueError as e:
                class_qualified = None
                error_str = str(e)
            if not class_qualified:
                self.add_error('failed to find fetcher class {} in scanner {}'
                               ' type #{} ({})'
                               .format(fetcher, scanner_name, type_index,
                                       error_str))
            scan_type[self.FETCHER] = class_qualified
        elif isinstance(fetcher, dict):
            is_folder = fetcher.get('folder', False)
            if not is_folder:
                self.add_error('scanner {} type #{}: '
                               'only folder dict accepted in fetcher'
                               .format(scanner_name, type_index))
            else:
                instance = FolderFetcher(fetcher['types_name'],
                                         fetcher['parent_type'],
                                         fetcher.get('text', ''))
                scan_type[self.FETCHER] = instance
        else:
            self.add_error('incorrect type of fetcher for scanner {} type #{}'
                           .format(scanner_name, type_index))

    def validate_children_scanner(self, scanner_name: str, type_index: int,
                                  scanners: dict, scan_type: dict):
        if 'children_scanner' in scan_type:
            children_scanner = scan_type.get('children_scanner')
            if not isinstance(children_scanner, str):
                self.add_error('scanner {} type #{}: '
                               'children_scanner must be a string'
                               .format(scanner_name, type_index))
            elif children_scanner not in scanners:
                self.add_error('scanner {} type #{}: '
                               'children_scanner {} not found '
                               .format(scanner_name, type_index,
                                       children_scanner))

    def _validate_condition(self, scanner_name: str, type_index: int, condition: dict,
                            environment_types: Optional[Union[list, str]] = None):
        if not isinstance(condition, dict):
            self.add_error('scanner {} type #{}: condition must be dict'
                           .format(scanner_name, str(type_index)))
            return
        if self.MECHANISM_DRIVER in condition.keys():
            drivers = condition[self.MECHANISM_DRIVER]
            if not isinstance(drivers, list):
                self.add_error('scanner {} type #{}: '
                               '{} must be a list of strings'
                               .format(scanner_name, type_index,
                                       self.MECHANISM_DRIVER))
            elif not all((isinstance(driver, str) for driver in drivers)):
                self.add_error('scanner {} type #{}: '
                               '{} must be a list of strings'
                               .format(scanner_name, type_index,
                                       self.MECHANISM_DRIVER))
            else:
                for driver in drivers:
                    self.validate_constant(scanner_name=scanner_name,
                                           value_to_check=driver,
                                           environment_types=environment_types,
                                           constant_type='mechanism_drivers',
                                           items_desc='mechanism drivers')

    def validate_environment_condition(self, scanner_name: str, type_index: int, scanner: dict):
        if self.ENVIRONMENT_CONDITION not in scanner:
            return
        condition = scanner[self.ENVIRONMENT_CONDITION]
        return self._validate_condition(scanner_name=scanner_name, type_index=type_index, condition=condition,
                                        environment_types=condition.get("environment_type"))

    def validate_environment_restriction(self, scanner_name: str, type_index: int, scanner: dict):
        if self.ENVIRONMENT_RESTRICTION not in scanner:
            return
        restriction = scanner[self.ENVIRONMENT_RESTRICTION]

        env_type_restriction = restriction.get("environment_type")
        if env_type_restriction:
            if isinstance(env_type_restriction, str):
                env_type_restriction = [env_type_restriction]
            env_type_condition = [et for et in self.environment_types if et not in env_type_restriction]
        else:
            env_type_condition = self.environment_types

        return self._validate_condition(scanner_name=scanner_name, type_index=type_index, condition=restriction,
                                        environment_types=env_type_condition)

    def validate_scanner(self, scanners: dict, name: str, package: str):
        scanner = scanners.get(name)
        if not scanner:
            self.add_error('failed to find scanner: {}')
            return

        # make sure only allowed attributes are supplied
        for i in range(0, len(scanner)):
            scan_type = scanner[i]
            self.validate_scan_type(scanners=scanners, scanner_name=name, type_index=i+1,
                                    scanner=scan_type, package=package)

    def validate_scan_type(self, scanners: dict, scanner_name: str,
                           type_index: int, scanner: dict, package: str):
        # keep previous error count to know if errors were detected here
        error_count = len(self.errors)
        # ignore comments
        scanner.pop(self.COMMENT, '')
        for attribute in scanner.keys():
            if attribute not in self.ALLOWED_SCANNER_ATTRIBUTES:
                self.add_error('unknown attribute {} '
                               'in scanner {}, type #{}'
                               .format(attribute, scanner_name,
                                       str(type_index)))

        # make sure required attributes are supplied
        for attribute in ScanMetadataParser.REQUIRED_SCANNER_ATTRIBUTES:
            if attribute not in scanner:
                self.add_error('scanner {}, type #{}: '
                               'missing attribute "{}"'
                               .format(scanner_name, str(type_index),
                                       attribute))
        # the following checks depend on previous checks,
        # so return if previous checks found errors
        if len(self.errors) > error_count:
            return

        # Validate fields listed in environment conditions
        self.validate_environment_condition(scanner_name=scanner_name, type_index=type_index, scanner=scanner)
        self.validate_environment_restriction(scanner_name=scanner_name, type_index=type_index, scanner=scanner)

        # Scan of the selected type should be supported for this environment type
        self.validate_constant(scanner_name=scanner_name, value_to_check=scanner[self.TYPE],
                               environment_types=scanner.get(self.ENVIRONMENT_CONDITION, {}).get("environment_type"),
                               constant_type='scan_object_types', items_desc='types')

        # Validate fetcher class and try to create an instance
        self.validate_fetcher(scanner_name=scanner_name, scan_type=scanner,
                              type_index=type_index, package=package)
        self.validate_children_scanner(scanner_name=scanner_name, type_index=type_index,
                                       scanners=scanners, scan_type=scanner)

    def get_constants(self, scanner_name: str, items_desc: str, constant_type: str,
                      environment_types: Optional[Union[list, str]] = None):

        query = {'name': constant_type}
        if environment_types:
            if isinstance(environment_types, str):
                environment_types = [environment_types]

            query['environment_type'] = {'$in': [None, *environment_types]}
        else:
            query['environment_type'] = {'$in': [None, "OpenStack"]}

        objects_list = list(self.constants.find(query))
        if not objects_list:
            raise ValueError('scanner {}: '
                             'could not find {} list in DB'
                             .format(scanner_name, items_desc))

        values_list = set()
        for obj in objects_list:
            values_list = values_list.union([d['value'] for d in obj['data']])

        return values_list

    def validate_constant(self, scanner_name: str, value_to_check: str, constant_type: str,
                          environment_types: Optional[Union[list, str]], items_desc: Optional[str] = None):

        values = self.get_constants(scanner_name=scanner_name, items_desc=items_desc,
                                    constant_type=constant_type, environment_types=environment_types)
        if value_to_check not in values:
            self.add_error('scanner {}: value not in {}: {}'
                           .format(scanner_name, items_desc, value_to_check))

    def validate_metadata(self, metadata: dict) -> bool:
        super().validate_metadata(metadata)
        scanners = metadata.get(self.SCANNERS, {})
        package = metadata.get(self.SCANNERS_PACKAGE)
        if not scanners:
            self.add_error('no scanners found in scanners list')
        else:
            for name in scanners.keys():
                self.validate_scanner(scanners, name, package)
        return len(self.errors) == 0
