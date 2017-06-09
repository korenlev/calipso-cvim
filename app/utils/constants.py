from enum import Enum


class StringEnum(Enum):
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)


class ScanStatus(StringEnum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class OperationalStatus(StringEnum):
    STOPPED = "stopped"
    RUNNING = "running"
    ERROR = "error"


class EnvironmentFeatures(StringEnum):
    SCANNING = "scanning"
    MONITORING = "monitoring"
    LISTENING = "listening"
