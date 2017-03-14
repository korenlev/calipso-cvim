import importlib
import json
import re


from bson.objectid import ObjectId
from datetime import datetime


class Util(object):
    prettify = False
    class_instances = {}

    def __init__(self):
        super().__init__()
        # method map for stringifying the object value
        self.stringify_map = {
            ObjectId: self.stringify_object_id,
            datetime: self.stringify_datetime
        }

    def set_prettify(self, prettify):
        self.prettify = prettify

    def get_prettify(self):
        return self.prettify

    def jsonify(self, obj):
        if self.prettify:
            ret = json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            ret = json.dumps(obj)
        return ret

    # convert class name in camel case to module file name in underscores
    def get_module_file_by_class_name(self, class_name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', class_name)
        module_file = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
        return module_file

    def get_instance_of_class(self, class_name, package="discover"):
        if class_name in self.class_instances:
            return self.class_instances[class_name]
        module_file = self.get_module_file_by_class_name(class_name)
        module_parts = [package, module_file]
        module = importlib.import_module(".".join(module_parts))
        class_ = getattr(module, class_name)
        instance = class_()
        self.class_instances[class_name] = instance
        return instance

    # convert some values of the specific types of the object into string
    # e.g convert all the ObjectId to string
    #     convert all the datetime object to string
    def stringify_object_values_by_types(self, obj, object_types):
        for object_type in object_types:
            self.stringify_object_values_by_type(obj, object_type)

    def stringify_object_values_by_type(self, obj, object_type):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, object_type):
                    obj[key] = self.stringify_map[object_type](value)
                else:
                    self.stringify_object_values_by_type(value, object_type)
        elif isinstance(obj, list):
            for index, value in enumerate(obj):
                if isinstance(value, object_type):
                    obj[index] = self.stringify_map[object_type](value)
                else:
                    self.stringify_object_values_by_type(value, object_type)

    # when search in the mongo db, need to
    # generate the ObjectId with the string
    def generate_object_ids(self, keys, obj):
        for key in keys:
            if key in obj:
                o = obj.pop(key)
                if o:
                    try:
                        o = ObjectId(o)
                    except Exception as e:
                        raise Exception("{0} is not a valid object id".
                                        format(o))
                obj[key] = o

    # stringify datetime object
    def stringify_datetime(self, dt):
        return dt.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

    # stringify ObjectId
    def stringify_object_id(self, object_id):
        return str(object_id)
