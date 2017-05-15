import json
import os
from abc import abstractmethod, ABCMeta
from utils.util import get_extension


class MetadataParser(metaclass=ABCMeta):

    def __init__(self):
        self.errors = []

    @abstractmethod
    def get_required_fields(self) -> list:
        pass

    def validate_metadata(self, metadata: dict) -> bool:
        # make sure metadata json contains all fields we need
        required_fields = self.get_required_fields()
        if not all([field in metadata for field in required_fields]):
            self.add_error("Metadata json should contain "
                           "all the following fields: {}"
                           .format(', '.join(required_fields)))
            return False
        return True

    def _parse_json_file(self, file_path: str):
        with open(file_path) as data_file:
            metadata = json.load(data_file)

        # validate metadata correctness
        if not self.validate_metadata(metadata):
            return None

        return metadata

    def parse_metadata_file(self, file_path: str) -> dict:
        extension = get_extension(file_path)
        if extension != 'json':
            raise ValueError("Extension '{}' is not supported. "
                             "Please provide a .json metadata file."
                             .format(extension))

        if not os.path.isfile(file_path):
            raise ValueError("Couldn't load metadata file. "
                             "Path '{}' doesn't exist or is not a file"
                             .format(file_path))

        # Try to parse metadata file if it has one of the supported extensions
        metadata = self._parse_json_file(file_path)
        if self.errors:
            raise TypeError("Errors encountered during "
                            "metadata file parsing:\n{}"
                            .format("\n".join(self.errors)))
        return metadata

    def add_error(self, msg):
        self.errors.append(msg)

    def check_errors(self):
        if self.errors:
            raise ValueError("Errors encountered during "
                             "metadata file parsing:\n{}"
                             .format("\n".join(self.errors)))
