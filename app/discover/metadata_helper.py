import json
from typing import List, Tuple

import os

from utils.util import get_extension


class MetadataParser:

    HANDLERS_PACKAGE = 'handlers_package'
    QUEUES = 'queues'
    EVENT_HANDLERS = 'event_handlers'

    REQUIRED_EXPORTS = (HANDLERS_PACKAGE, EVENT_HANDLERS)

    def __init__(self):
        self.handlers_package = None
        self.queues = []
        self.event_handlers = []
        self.errors = []

    def _validate_required_fields(self, handlers_package, event_handlers):
        if not handlers_package \
           or not isinstance(handlers_package, str):
            self.errors.append("Handlers package '{}' is invalid"
                               .format(handlers_package))

        if not event_handlers \
           or not isinstance(event_handlers, dict):
            self.errors.append("Event handlers variable is invalid or empty"
                               "(should be a non-empty dict)")

        return len(self.errors) == 0

    def _finalize_parsing(self,
                          handlers_package: str,
                          queues: List[dict],
                          event_handlers: dict):
        # We shouldn't continue parsing if metadata file has any errors
        if not self._validate_required_fields(handlers_package, event_handlers):
            return

        # Convert variables to EventHandler-friendly format
        self.handlers_package = handlers_package

        try:
            if queues and isinstance(queues, list):
                self.queues = [{"queue": q["queue"],
                                "exchange": q["exchange"]}
                               for q in queues]
        except KeyError:
            self.errors.append("Queues variable has invalid format")
            return

        self.event_handlers = event_handlers

    def _parse_json_file(self, file_path: str):
        with open(file_path) as data_file:
            metadata = json.load(data_file)

        # make sure metadata json contains all fields we need
        if not all([field in metadata for field in self.REQUIRED_EXPORTS]):
            self.errors.append("Metadata json should contain all the following fields: {}"
                               .format(', '.join(self.REQUIRED_EXPORTS)))
            return

        handlers_package = metadata[self.HANDLERS_PACKAGE]
        queues = metadata.get(self.QUEUES, None)
        event_handlers = metadata[self.EVENT_HANDLERS]

        self._finalize_parsing(handlers_package, queues, event_handlers)

    def parse_metadata_file(self, file_path: str):
        extension = get_extension(file_path)
        if extension != 'json':
            raise ValueError("Extension '{}' is not supported. "
                             "Please provide a .json metadata file."
                             .format(extension))

        if not os.path.isfile(file_path):
            raise ValueError("Couldn't load metadata file. Path '{}' doesn't exist or is not a file"
                             .format(file_path))

        # Try to parse metadata file if it has one of the supported extensions
        self._parse_json_file(file_path)
        if self.errors:
            raise TypeError("Errors encountered during metadata file parsing:\n{}"
                            .format("\n".join(self.errors)))


def parse_metadata_file(file_path: str) -> Tuple[str, List[dict], dict]:
    parser = MetadataParser()
    parser.parse_metadata_file(file_path)
    return parser.handlers_package, parser.queues, parser.event_handlers
