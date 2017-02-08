from bson.objectid import ObjectId
from datetime import datetime


class Utils:

    def __init__(self):
        super().__init__()
        # method map for stringifying the object value
        self.stringify_map = {
            ObjectId: self.stringify_object_id,
            datetime: self.stringify_datetime
        }

    # uppercase all the string key
    def convert_object_keys_to_uppercase(self, dictionary):
        outgoing_dict = {}
        for key, value in dictionary.items():
            if isinstance(key, str):
                key = key.upper()
            outgoing_dict[key] = value
        return outgoing_dict

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



