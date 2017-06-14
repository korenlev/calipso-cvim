import importlib
import signal
from argparse import Namespace
from typing import Dict, Callable

import os
import re

from bson.objectid import ObjectId


class SignalHandler:

    def __init__(self, signals=(signal.SIGTERM, signal.SIGINT)):
        super().__init__()
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

    # convert module file name in underscores to class name in camel case
    @staticmethod
    def get_class_name_by_module(module_name):
        name_parts = [word.captialize() for word in module_name.split('_')]
        class_name = ''.join(name_parts)
        return class_name

    @staticmethod
    def get_instance_of_class(class_name: str = None, package: str ="discover",
                              module_name: str =None):
        if not class_name and not module_name:
            raise ValueError('class_name or module_name must be provided')
        if not class_name:
            class_name = ClassResolver.get_class_name_by_module(module_name)
        if class_name in ClassResolver.instances:
            return ClassResolver.instances[class_name]
        module_file = module_name if module_name \
            else ClassResolver.get_module_file_by_class_name(class_name)
        module_parts = [package, module_file]
        module_name = ".".join(module_parts)
        class_module = importlib.import_module(module_name)
        if not class_module:
            raise ValueError('could not import module {}'.format(module_name))
        clazz = getattr(class_module, class_name)
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
