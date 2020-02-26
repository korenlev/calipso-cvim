import re

from api.client.version import VERSION
from base.utils.logging.full_logger import FullLogger
from schedule.pods_config_parser import PodData


class PodManager:
    SUPPORTED_VERSIONS = ["<={}".format(VERSION)]
    OPERATOR_REGEX = re.compile("((!=?)|([<>]=?))?(\d+)")

    def __init__(self, log_level: str = None):
        self.log = FullLogger(level=log_level)
        self.supported_versions = []
        self._prepare_supported_versions()

    def _prepare_supported_versions(self):
        self.supported_versions = []
        for version_req in self.SUPPORTED_VERSIONS:
            version_req_parts = version_req.split(".")
            match = re.match(self.OPERATOR_REGEX, version_req_parts[0])
            if not match:
                raise ValueError("Illegal version requirement: '{}'".format(version_req))
            operator, version_req_parts[0] = match.groups()[0], match.groups()[3]

            try:
                version_req_parts = [int(vp) for vp in version_req_parts]
            except ValueError:
                print("Illegal version requirement: '{}'".format(version_req))
                return False

            self.supported_versions.append(
                {
                    "operator": operator if operator else "==",
                    "version_parts": version_req_parts
                }
            )

    def _validate_version(self, version: str) -> bool:
        try:
            version_parts = [int(vp) for vp in version.split(".")]
        except ValueError:
            return False

        def validate_req(req: dict):
            op = req["operator"]
            if op == "==":
                return version_parts == req["version_parts"]
            elif op == "!=":
                return version_parts != req["version_parts"]

            for i, version_req_part in enumerate(req["version_parts"]):
                part = version_parts[i]
                if op == ">=":
                    if part < version_req_part:
                        return False
                    if part > version_req_part:
                        return True
                elif op == ">":
                    if part > version_req_part:
                        return True
                    if part < version_req_part:
                        return False
                elif op == "<=":
                    if part < version_req_part:
                        return True
                    elif part > version_req_part:
                        return False
                elif op == "<":
                    if part < version_req_part:
                        return True
                    if part > version_req_part:
                        return False
            return True if op in (">=", "<=") else False

        return all(validate_req(version_req) for version_req in self.supported_versions)

    def set_pod_health(self, pod: PodData):
        try:
            pod.health = pod.api_client.call_api("GET", "/health")
        except Exception as e:  # TODO: narrow down
            self.log.warning("Failed to check health of remote {}. Error: {}".format(pod.name, e))

    def check_pod_status(self, pod: PodData) -> bool:
        version = pod.health.get('version', 'unknown')

        if not self._validate_version(version):
            self.log.info("Remote {} has unsupported API version: '{}'".format(pod.name if pod.name else "pod", version))
            return False

        # TODO: remove
        self.log.info("Remote {} has API version '{}'".format(pod.name, version))
        return True

    def check_pod_available_for_action(self, pod: PodData, env_name: str = None) -> bool:
        if not env_name:
            env_name = pod.env_name

        environments = pod.health.get("environments", {})
        if not isinstance(environments, dict) or env_name not in environments.keys():
            self.log.warning("Environment {} not found on remote {}".format(env_name, pod.name))
            return False

        environment = environments.get(env_name, {})
        if not environment or environment.get("scan_in_progress") is True:
            return False

        return True

    @staticmethod
    def send_scan_request(pod: PodData, env_name: str = None):
        return pod.api_client.scan_request(environment=env_name if env_name else pod.name)
