import json
import re


class Util(object):
    prettify = False
    class_instances = {}

    def __init__(self):
        super().__init__()

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
