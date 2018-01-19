from enum import Enum


class Origins(Enum):
    pass


class ScanOrigins(Origins):
    MANUAL = 'manual scan'
    SCHEDULED = 'scheduled scan'
    EVENT = 'event based scan'
    TEST = 'test'
    UNKNOWN = 'unknown'


class Origin:
    def __init__(self, origin_id=None,
                 origin_type: Origins = None):
        self.origin_id = origin_id
        self.origin_type = origin_type
        # Names of extra fields for mongo logging handler
        self.extra = []


class ScanOrigin(Origin):
    def __init__(self, origin_id=None,
                 origin_type: ScanOrigins = ScanOrigins.UNKNOWN):
        super().__init__(origin_id=origin_id,
                         origin_type=origin_type)
