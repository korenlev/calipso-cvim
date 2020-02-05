from base.utils.util import ClassResolver

from base.utils.metadata_parser import MetadataParser


class ProcessorsMetadataParser(MetadataParser):

    PROCESSORS_FILE = "processors.json"

    PROCESSORS_PACKAGE = "processors_package"
    BASE_PROCESSOR = "base_processor"
    PROCESSORS = "processors"

    def __init__(self):
        super().__init__()
        self.processors_package = None
        self.base_processor_class = None
        self.base_processor = None
        self.processors = []
        self.prerequisites = {}

    # Find out whether processor prerequisites chain form a dependency loop
    # In this case none of the affected processors can run since they require
    # that their prerequisite is run first
    def find_prerequisite_loops(self, source, current_prerequisites) -> (bool, str):
        if source in current_prerequisites:
            return False, "Inside loop: {}".format(current_prerequisites)

        if not current_prerequisites:
            # Chain resolved
            return True, ""

        new_prerequisites = set()
        for src in current_prerequisites:
            new_prerequisites = new_prerequisites.union(self.prerequisites.get(src, set()))
        if new_prerequisites == current_prerequisites:
            return False, "Outside loop"

        return self.find_prerequisite_loops(source, new_prerequisites)

    def validate_processor(self, processor_class):
        try:
            module_name = ClassResolver.get_module_file_by_class_name(processor_class)
            instance = ClassResolver.get_instance_of_class(package_name=self.processors_package,
                                                           module_name=module_name,
                                                           class_name=processor_class)

        except ValueError:
            instance = None

        if not instance:
            self.add_error('Failed to import processor class "{}"'
                           .format(processor_class))
            return

        if not isinstance(instance, self.base_processor.__class__):
            self.add_error('Processor "{}" should subclass base processor "{}"'
                           .format(processor_class, self.base_processor_class))
            return

        self.processors.append(instance)
        self.prerequisites[processor_class] = set(getattr(instance, "PREREQUISITES", []))

    def validate_prerequisites(self):
        for class_name, prereqs in self.prerequisites.items():
            resolves, error_msg = self.find_prerequisite_loops(class_name, prereqs)
            if not resolves:
                self.add_error("Processor {} has a dependency loop. Error msg: {}".format(class_name, error_msg))

    def validate_metadata(self, metadata: dict):
        super().validate_metadata(metadata)
        self.processors_package = metadata[self.PROCESSORS_PACKAGE]
        self.base_processor_class = metadata[self.BASE_PROCESSOR]
        base_processor_module = ClassResolver.get_module_file_by_class_name(self.base_processor_class)

        try:
            self.base_processor = ClassResolver.get_instance_of_class(package_name=self.processors_package,
                                                                      module_name=base_processor_module,
                                                                      class_name=self.base_processor_class)
        except ValueError:
            self.base_processor = None

        if not self.base_processor:
            self.add_error("Couldn't create base processor instance"
                           "for class name '{}'".format(self.base_processor_class))
            return False

        for processor in metadata[self.PROCESSORS]:
            self.validate_processor(processor_class=processor)
        metadata[self.PROCESSORS] = self.processors

        self.validate_prerequisites()

        return len(self.errors) == 0

    def get_required_fields(self) -> list:
        return [self.PROCESSORS_PACKAGE, self.BASE_PROCESSOR, self.PROCESSORS]
