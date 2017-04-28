import importlib
import signal
from argparse import Namespace
from typing import Dict, Callable

import os
import re


from bson.objectid import ObjectId


class MetadataParser:

    REQUIRED_EXPORTS = ('HANDLERS_PACKAGE', 'QUEUES', 'EVENT_HANDLERS')

    def __init__(self):
        self.handlers_package = None
        self.queues = []
        self.event_handlers = []

    def _parse_python_file(self, file_path: str):
        import importlib.util

        # import metadata file as a python module
        module_name = os.path.splitext(os.path.split(file_path)[1])[0]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # make sure metadata module exports all variables we need
        if not all([variable in dir(module) for variable in self.REQUIRED_EXPORTS]):
            raise TypeError("Metadata file should export all of ({}) variables"
                            .format(', '.join(self.REQUIRED_EXPORTS)))

        self.handlers_package = module.HANDLERS_PACKAGE
        self.queues = module.QUEUES
        self.event_handlers = module.EVENT_HANDLERS

    def _parse_json_file(self, file_path: str):
        # TODO: provide json parser
        pass

    def not_implemented(self, file_path: str):
        raise ValueError("Extension '{}' is not supported"
                         .format(get_extension(file_path)))

    PARSERS = {
        'py': _parse_python_file,
        'json': _parse_json_file,
    }

    def parse_metadata_file(self, file_path: str):
        extension = get_extension(file_path)
        # Try to parse metadata file if it has one of the supported extensions
        self.PARSERS.get(extension, self.not_implemented)(self, file_path)


class SignalHandler:

    def __init__(self, signals=(signal.SIGTERM, signal.SIGINT)):
        self.terminated = False
        for sig in signals:
            signal.signal(sig, self.handle)

    def handle(self, signum, frame):
        self.terminated = True


class ClassResolver:
    instances = {}

    # convert class name in camel case to module file name in underscores
    @staticmethod
    def get_module_file_by_class_name(class_name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', class_name)
        module_file = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
        return module_file

    @staticmethod
    def get_instance_of_class(class_name, package="discover"):
        if class_name in ClassResolver.instances:
            return ClassResolver.instances[class_name]
        module_file = ClassResolver.get_module_file_by_class_name(class_name)
        module_parts = [package, module_file]
        module = importlib.import_module(".".join(module_parts))
        clazz = getattr(module, class_name)
        instance = clazz()
        ClassResolver.instances[class_name] = instance
        return instance


# TODO: translate the following comment
# when search in the mongo db, need to
# generate the ObjectId with the string
def generate_object_ids(keys, obj):
    for key in keys:
        if key in obj:
            o = obj.pop(key)
            if o:
                try:
                    o = ObjectId(o)
                except Exception:
                    raise Exception("{0} is not a valid object id".
                                    format(o))
            obj[key] = o


# Get arguments from CLI or another source
# and convert them to dict to enforce uniformity.
# Throws a TypeError if arguments can't be converted to dict.
def setup_args(args: dict,
               defaults: Dict[str, object],
               get_cmd_args: Callable[[], Namespace] = None):
    if defaults is None:
        defaults = {}

    if args is None and get_cmd_args is not None:
        args = vars(get_cmd_args())
    elif not isinstance(args, dict):
        try:
            args = dict(args)
        except TypeError:
            try:
                args = vars(args)
            except TypeError:
                raise TypeError("Wrong arguments format")

    return dict(defaults, **args)


def encode_router_id(host_id: str, uuid: str):
    return '-'.join([host_id, 'qrouter', uuid])


def decode_router_id(router_id: str):
    return router_id.split('qrouter-')[-1]


def get_extension(file_path: str) -> str:
    return os.path.splitext(file_path)[1][1:]