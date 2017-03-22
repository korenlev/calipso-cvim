import datetime


class Message:

    def __init__(self, msg_id, env, source, object_id, object_type,
                 display_context, level, msg, ts):
        self.id = msg_id
        self.environment = env
        self.source_system = source
        self.related_object = object_id
        self.related_object_type = object_type
        self.display_context = display_context
        self.level = level
        self.message = msg
        self.timestamp = ts
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
            "viewed": self.viewed
        }
