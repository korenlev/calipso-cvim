import json
import os
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

    def get_instance_of_class(self, class_name):
        if class_name in self.class_instances:
            return self.class_instances[class_name]
        module_file = self.get_module_file_by_class_name(class_name)
        module = __import__(module_file, globals(), level=1)
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

    def get_config_file(self, config_file):
        # try to look in the current work directory
        # as defined by PYTHONPATH
        python_path = os.environ['PYTHONPATH']
        if os.pathsep in python_path:
            python_path = python_path.split(os.pathsep)[0]
        return python_path + "/config/" + config_file

    # read config info from config file
    def read_config_from_config_file(self, config_file):
        params = {}
        try:
            with open(config_file) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("#") or " " not in line:
                        continue
                    index = line.index(" ")
                    key = line[: index].strip()
                    value = line[index + 1:].strip()
                    if value:
                        params[key] = value
        except Exception as e:
            raise e
        return params

    # stringify datetime object
    def stringify_datetime(self, dt):
        return dt.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

    # stringify ObjectId
    def stringify_object_id(self, object_id):
        return str(object_id)
