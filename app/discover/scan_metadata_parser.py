from discover.folder_fetcher import FolderFetcher
from utils.metadata_parser import MetadataParser
from utils.mongo_access import MongoAccess
from utils.util import ClassResolver


class ScanMetadataParser(MetadataParser):

    SCANNERS_PACKAGE = 'scanners_package'
    SCANNERS = 'scanners'

    TYPE = 'type'
    FETCHER = 'fetcher'
    CHILDREN_SCANNER = 'children_scanner'
    ENVIRONMENT_CONDITION = 'environment_condition'
    OBJECT_ID_TO_USE_IN_CHILD = 'object_id_to_use_in_child'

    COMMENT = '_comment'

    REQUIRED_SCANNER_ATTRIBUTES = [TYPE, FETCHER]
    ALLOWED_SCANNER_ATTRIBUTES = [TYPE, FETCHER, CHILDREN_SCANNER,
                                  ENVIRONMENT_CONDITION,
                                  OBJECT_ID_TO_USE_IN_CHILD]

    MECHANISM_DRIVER = 'mechanism_driver'

    def __init__(self, inventory_mgr):
        super().__init__()
        self.inv = inventory_mgr
        self.scanners = {}
        self.constants = {}

    def get_required_fields(self):
        return [self.SCANNERS_PACKAGE, self.SCANNERS]

    def validate_fetcher(self, scanner_name: str, scan_type: dict,
                         type_index: int, package: str):
        fetcher = scan_type.get(self.FETCHER, '')
        if not fetcher:
            self.add_error('missing or empty fetcher in scanner {} type #{}'
                           .format(scanner_name, str(type_index)))
        elif isinstance(fetcher, str):
            instance = ClassResolver.get_instance_of_class(fetcher, package)
            if not instance:
                self.add_error('failed to find fetcher class {} in scanner {}'
                               ' type #{}'
                               .format(fetcher, scanner_name, type_index))
            scan_type[self.FETCHER] = instance
        elif isinstance(fetcher, dict):
            is_folder = fetcher.get('folder')
            if not is_folder or is_folder != 1:
                self.add_error('scanner {} type #{}: only folder dict accepted'
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
                                  scanners: dict):
        scanner = scanners[scanner_name]
        if 'children_scanner' in scanner:
            children_scanner = scanner.get('children_scanner')
            if not isinstance(children_scanner, str):
                self.add_error('scanner {} type #{}: '
                               'children_scanner must be a string'
                               .format(scanner_name, type_index))
            elif children_scanner not in scanners:
                self.add_error('scanner {} type #{}: '
                               'children_scanner {} not found '
                               .format(scanner_name, type_index,
                                       children_scanner))

    def validate_environment_condition(self, scanner_name: str, type_index: int,
                                       scanner: dict):
        if self.ENVIRONMENT_CONDITION not in scanner:
            return
        condition = scanner[self.ENVIRONMENT_CONDITION]
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
            for driver in drivers:
                if not isinstance(driver, str):
                    self.add_error('scanner {} type #{}: '
                                   '{} must be a list of strings'
                                   .format(scanner_name, type_index,
                                           self.MECHANISM_DRIVER))
                else:
                    self.validate_constant(scanner_name,
                                           driver,
                                           'mechanism_drivers',
                                           'mechanism drivers')

    def validate_scanner(self, scanners: dict, name: str, package: str):
        scanner = scanners.get(name)
        if not scanner:
            self.add_error('failed to find scanner: {}')
            return

        # make sure only allowed attributes are supplied
        for i in range(0, len(scanner)):
            scan_type = scanner[i]
            self.validate_scan_type(scanners, name, i, scan_type, package)

    def validate_scan_type(self, scanners: dict, scanner_name: str,
                           type_index: int, scan_type: dict, package: str):
        # keep previous error count to know if errors were detected here
        error_count = len(self.errors)
        # ignore comments
        scan_type.pop(self.COMMENT, '')
        for attribute in scan_type.keys():
            if attribute not in self.ALLOWED_SCANNER_ATTRIBUTES:
                self.add_error('unknown attribute {} '
                               'in scanner {}, type #{}'
                               .format(attribute, scanner_name,
                                       str(type_index)))

        # make sure required attributes are supplied
        for attribute in ScanMetadataParser.REQUIRED_SCANNER_ATTRIBUTES:
            if attribute not in scan_type:
                self.add_error('scanner {}, type #{}: missing attribute {}'
                               .format(scanner_name, str(type_index),
                                       attribute))
        # the following checks depend on previous checks,
        # so return if previous checks found errors
        if len(self.errors) > error_count:
            return

        # type must be valid object type
        self.validate_constant(scanner_name, scan_type[self.TYPE],
                               'object_types', 'types')
        self.validate_fetcher(scanner_name, scan_type, type_index, package)
        self.validate_children_scanner(scanner_name, type_index, scanners)
        self.validate_environment_condition(scanner_name, type_index,
                                            scan_type)

    def get_constants(self, scanner_name, items_desc, constant_type):
        if not self.constants.get(constant_type):
            constants = MongoAccess.db['constants']
            values_list = constants.find_one({'name': constant_type})
            if not values_list:
                raise ValueError('scanner {}: '
                                 'could not find {} list in DB'
                                 .format(scanner_name, items_desc))
            self.constants[constant_type] = values_list
        return self.constants[constant_type]

    def validate_constant(self,
                          scanner_name: str,
                          value_to_check: str,
                          constant_type: str,
                          items_desc: str = None):
        values_list = self.get_constants(scanner_name, items_desc, constant_type)
        values = [t['value'] for t in values_list['data']]
        if value_to_check not in values:
            self.add_error('scanner {}: value not in {}: {}'
                           .format(scanner_name, items_desc, value_to_check))

    def validate_metadata(self, metadata: dict) -> bool:
        super().validate_metadata(metadata)
        scanners = metadata.get(self.SCANNERS, [])
        package = metadata.get(self.SCANNERS_PACKAGE)
        for name in scanners.keys():
            self.validate_scanner(scanners, name, package)
        return len(self.errors) == 0
