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
