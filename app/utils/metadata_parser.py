import os

from utils.util import get_extension


class MetadataParser:

    REQUIRED_EXPORTS = {
        'py': ('HANDLERS_PACKAGE', 'QUEUES', 'EVENT_HANDLERS')
    }


    def __init__(self):
        self.handlers_package = None
        self.queues = []
        self.event_handlers = []
        self.errors = []

    def _parse_python_file(self, file_path: str):
        import importlib.util

        # import metadata file as a python module
        module_name = os.path.splitext(os.path.split(file_path)[1])[0]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # make sure metadata module exports all variables we need
        if not all([variable in dir(module) for variable in self.REQUIRED_EXPORTS['py']]):
            self.errors.append("Metadata file should export all of ({}) variables"
                               .format(', '.join(self.REQUIRED_EXPORTS['py'])))
            return

        if not module.HANDLERS_PACKAGE \
           or not isinstance(module.HANDLERS_PACKAGE, str):
            self.errors.append("Handlers package '{}' is invalid"
                               .format(module.HANDLERS_PACKAGE))

        if not module.QUEUES \
           or not isinstance(module.QUEUES, list):
            self.errors.append("Queues variable is invalid or empty "
                               "(should be a non-empty list)")

        if not module.EVENT_HANDLERS \
           or not isinstance(module.EVENT_HANDLERS, dict):
            self.errors.append("Event handlers variable is invalid or empty"
                               "(should be a non-empty dict)")

        # We shouldn't continue parsing if metadata file has any errors
        if self.errors:
            return

        # Prepare variables for EventHandler-friendly format
        self.handlers_package = module.HANDLERS_PACKAGE
        self.queues = [{"queue": q[0], "exchange": q[1]}
                       for q in module.QUEUES]
        self.event_handlers = list(module.EVENT_HANDLERS.items())

    def _parse_json_file(self, file_path: str):
        # TODO: provide json parser
        pass

    PARSERS = {
        'py': _parse_python_file,
        'json': _parse_json_file,
    }

    def parse_metadata_file(self, file_path: str):

        extension = get_extension(file_path)
        if extension not in self.PARSERS.keys():
            raise ValueError("Extension '{}' is not supported. "
                             "Please specify a file with one of the following extensions: ({})"
                             .format(extension, ", ".join(self.PARSERS.keys())))

        if not os.path.isfile(file_path):
            raise ValueError("Couldn't load metadata file. Path '{}' doesn't exist or is not a file"
                             .format(file_path))

        # Try to parse metadata file if it has one of the supported extensions
        self.PARSERS[extension](self, file_path)
        if self.errors:
            raise TypeError("Errors encountered during metadata file parsing:\n{}"
                            .format("\n".join(self.errors)))