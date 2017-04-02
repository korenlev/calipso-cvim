from enum import Enum


class ScanStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

    def __repr__(self):
        return repr(self.value)


class OperationalStatus(Enum):
    STOPPED = "stopped"
    RUNNING = "running"
    ERROR = "error"

    def __repr__(self):
        return repr(self.value)