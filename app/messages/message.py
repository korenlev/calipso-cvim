from typing import Union

from bson import ObjectId


class Message:

    LEVELS = ['info', 'warn', 'error']
    DEFAULT_LEVEL = LEVELS[0]

    def __init__(self, msg_id: str, env: str, source: str,
                 object_id: Union[str, ObjectId],
                 display_context: Union[str, ObjectId],
                 msg: dict, level: str = DEFAULT_LEVEL,
                 object_type: str = None, ts: str = None,
                 received_ts: str = None, finished_ts: str = None):

        if level and level.lower() in self.LEVELS:
            self.level = level.lower()
        else:
            self.level = self.DEFAULT_LEVEL

        self.id = msg_id
        self.environment = env
        self.source_system = source
        self.related_object = object_id
        self.related_object_type = object_type
        self.display_context = display_context
        self.message = msg
        self.timestamp = ts if ts else received_ts
        self.received_timestamp = received_ts
        self.finished_timestamp = finished_ts
        self.viewed = False

    def get(self):
        return {
            "id": self.id,
            "environment": self.environment,
            "source_system": self.source_system,
            "related_object": self.related_object,
            "related_object_type": self.related_object_type,
            "display_context": self.display_context,
            "level": self.level,
            "message": self.message,
            "timestamp": self.timestamp,
            "received_timestamp": self.received_timestamp,
            "finished_timestamp": self.finished_timestamp,
            "viewed": self.viewed
        }
