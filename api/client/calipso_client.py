import argparse
import datetime
import json
import time

import requests
from dateutil.parser import parse as dateutil_parse
from dateutil.relativedelta import relativedelta

try:
    from version import VERSION
except ImportError:
    from api.client.version import VERSION

try:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except ImportError:
    import urllib3
    from urllib3.exceptions import InsecureRequestWarning

    urllib3.disable_warnings(InsecureRequestWarning)

from six.moves.urllib.parse import urljoin
from sys import exit


# This is a calipso api client designed to be small and simple
# assuming environment_config details are already deployed by CVIM (typically: cvim-<mgmt_hostname>)
# For central CVIM monitoring add this client per pod scanning and allow adding multiple environments

GUIDE_URL = "https://cloud-gogs.cisco.com/mercury/calipso/raw/master/docs/release/api-guide.rst"

SUPPORTED_METHODS = ["GET", "POST", "PUT", "DELETE"]
RECURRENCE_OPTIONS = ["ONCE", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY"]

PAGEABLE_ENDPOINTS = {"cliques", "inventory", "links", "messages", "scans", "scheduled_scans", "search"}
PER_ENVIRONMENT_ENDPOINTS = PAGEABLE_ENDPOINTS.union({"tree"})
ALLOWED_ENDPOINTS = {"clique_types", "clique_constraints", "constants", "environment_configs",
                     "health", "timezone"}.union(PER_ENVIRONMENT_ENDPOINTS)


class ConnectionError(Exception):
    pass


class APIException(Exception):
    pass


class APIAuthException(APIException):
    pass


class APICallException(APIException):
    pass


class ScanError(Exception):
    pass


def error(err, code=1):
    print(err)
    return code


class CalipsoClient:
    def __init__(self, api_host, api_port, api_password, verify_tls=False):
        self.api_server = "[{}]".format(api_host) if ":" in api_host and "[" not in api_host else api_host
        self.username = "calipso"
        self.password = api_password
        self.port = api_port
        self.schema = "https"
        self.verify_tls = verify_tls
        self.auth_url = "auth/tokens"
        self.headers = {'Content-Type': 'application/json'}
        self.token = None
        self.auth_body = {
            "auth": {
                "methods": ["credentials"],
                "credentials": {
                    "username": self.username,
                    "password": self.password
                }
            }
        }

    @property
    def base_url(self):
        return "{}://{}:{}".format(self.schema, self.api_server, self.port)

    def get_token(self):
        try:
            resp = self.send_request("POST", self.auth_url, payload=self.auth_body)
            cont = resp.json()
            if "token" not in cont:
                raise APIAuthException("Failed to fetch auth token. Response:\n{}".format(cont))
            self.token = cont["token"]
            self.headers.update({'X-Auth-Token': self.token})
        except requests.exceptions.RequestException as e:
            raise APIAuthException("Error sending request: {}".format(e))

    @staticmethod
    def pp_json(json_text, sort=True, indents=4):
        json_data = json.loads(json_text) if type(json_text) is str else json_text
        print(json.dumps(json_data, sort_keys=sort, indent=indents))

    def _send_request(self, method, url, payload):
        method = method.lower()
        if method == 'post':
            response = requests.post(url, json=payload, headers=self.headers, verify=self.verify_tls,
                                     timeout=3)
        elif method == 'delete':
            response = requests.delete(url, headers=self.headers, verify=self.verify_tls)
        elif method == 'put':
            response = requests.put(url, json=payload, headers=self.headers, verify=self.verify_tls,
                                    timeout=3)
        else:
            response = requests.get(url, params=payload, headers=self.headers, verify=self.verify_tls,
                                    timeout=3)
        return response

    def send_request(self, method, url, payload):
        try:
            return self._send_request(method, urljoin(self.base_url, url), payload)
        except requests.ConnectionError:
            raise ConnectionError("SSL Connection could not be established")

    def call_api(self, method, endpoint, payload=None, fail_on_error=True):
        if not self.token:
            self.get_token()

        response = self.send_request(method, endpoint, payload)
        err = None
        content = None
        try:
            content = json.loads(response.content)
            if "error" in content:
                err = content["error"]
        except ValueError:
            pass

        if not content:
            if response.status_code == 404:
                raise APICallException("Endpoint not found")
            if response.status_code == 400:
                raise APICallException("Environment or resource not found, or invalid keys")
            raise APICallException("API didn't return a valid JSON")
        if err and fail_on_error:
            raise APICallException(err.get('message', err))

        return content

    def scan_handler(self, environment, es_index=False):
        # post scan request, for specific environment, get doc_id
        scan_reply = self.scan_request(environment=environment, es_index=es_index)
        scan_doc_id = scan_reply["id"]
        print("Scan request posted for environment {}".format(environment))

        # check status of scan id and wait till scan status is 'completed'
        scan_status = "pending"
        while scan_status != "completed" and scan_status != "completed_with_errors":
            scan_doc = self.scan_check(environment=environment,
                                       doc_id=scan_doc_id)
            scan_status = scan_doc["status"]
            print("Waiting for scan to complete, scan status: {}".format(scan_status))
            time.sleep(2)
            if scan_status == "failed":
                raise ScanError("Scan has failed, please debug in scan container")

        if scan_status == "completed_with_errors":
            print("Inventory, links and cliques has been discovered with some errors")
        elif scan_status == "completed":
            print("Inventory, links and cliques has been discovered")

    def scan_request(self, environment, recurrence=None, es_index=False, scheduled_timestamp=None):
        if not recurrence:
            request_payload = {
                "log_level": "warning",
                "clear": True,
                "scan_only_inventory": False,
                "scan_only_links": False,
                "scan_only_cliques": False,
                "env_name": environment,
                "es_index": es_index
            }
            return self.call_api('post', 'scans', request_payload)
        else:
            request_payload = {
                "recurrence": recurrence,
                "log_level": "warning",
                "clear": True,
                "scan_only_links": False,
                "scan_only_cliques": False,
                "env_name": environment,
                "es_index": es_index,
                "scan_only_inventory": False,
                "scheduled_timestamp": scheduled_timestamp
            }
            return self.call_api('post', 'scheduled_scans', request_payload)

    def scan_check(self, environment, doc_id, scheduled=False):
        scan_params = {"env_name": environment, "id": doc_id}
        if scheduled is False:
            return self.call_api('get', 'scans', scan_params)
        else:
            return self.call_api('get', 'scheduled_scans', scan_params)


def handle_scan(client, args):
    if not args.scan_recurrence:
        if args.scan_at != "NOW":
            return error("--scan_at can only be specified for recurring scans")
        client.scan_handler(environment=args.environment)
    else:
        # TODO: timezone support
        submit_timestamp = datetime.datetime.now()
        if args.scan_at == "NOW":
            # TODO: think more about this
            scheduled_timestamp = (
                    submit_timestamp + relativedelta(hours=1 if args.scan_recurrence == "HOURLY" else 0,
                                                     days=1 if args.scan_recurrence == "DAILY" else 0,
                                                     weeks=1 if args.scan_recurrence == "WEEKLY" else 0,
                                                     months=1 if args.scan_recurrence == "MONTHLY" else 0,
                                                     years=1 if args.scan_recurrence == "YEARLY" else 0)
            )
        else:
            try:
                scheduled_timestamp = dateutil_parse(args.scan_at)
            except (ValueError, OverflowError):
                return error("Invalid datetime format for --scan_at argument")

        # post scan schedule, for specific environment, get doc_id
        schedule_reply = client.scan_request(environment=args.environment,
                                             recurrence=args.scan_recurrence,
                                             es_index=args.es_index,
                                             scheduled_timestamp=scheduled_timestamp.strftime("%Y-%m-%dT%H:%M"))

        schedule_doc_id = schedule_reply["id"]
        schedule_doc = client.scan_check(environment=args.environment,
                                         doc_id=schedule_doc_id,
                                         scheduled=True)

        print("Scheduled scan at: {}\nSubmitted at: {}\nScan recurrence: {}. Schedule status: {}."
              .format(scheduled_timestamp.strftime("%Y-%m-%dT%H:%M"),
                      submit_timestamp.strftime("%Y-%m-%dT%H:%M"),
                      schedule_doc['recurrence'],
                      schedule_doc['status']))


def handle_call(client, args):
    # currently, only 'environment_configs' and 'constants' are allowed without environment
    if args.endpoint in PER_ENVIRONMENT_ENDPOINTS and not args.environment:
        return error("This request requires an environment")
    if args.endpoint not in PER_ENVIRONMENT_ENDPOINTS and args.environment:
        return error("Environment is not needed for this request, please remove")
    if args.endpoint == 'constants' and not args.payload:
        return error("""This request requires a payload (ex: --payload '{"name": "object_types"}')""")

    params = {}
    if args.environment:
        params.update({"env_name": args.environment})
    if args.endpoint in PAGEABLE_ENDPOINTS:
        params.update({"page": args.page, "page_size": args.page_size})

    if args.payload:
        # TODO: better json cast?
        payload_str = args.payload.replace("'", "\"")
        try:
            payload_json = json.loads(payload_str)
            params.update(payload_json)
        except ValueError as e:
            return error("Unsupported payload data, should be a valid JSON. Error: {}".format(e))

    try:
        reply = client.call_api(method=args.method, endpoint=args.endpoint, payload=params)
        return client.pp_json(reply)
    except (ValueError, APIException) as e:
        return error(e)


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_server",
                        help="FQDN or IP address of the API Server"
                             " (default=localhost)",
                        type=str,
                        default="localhost",
                        required=False)
    parser.add_argument("--api_port",
                        help="TCP Port exposed on the API Server "
                             " (default=8747)",
                        type=int,
                        default=8747,
                        required=False)
    parser.add_argument("--api_password",
                        help="API password (secret) used by the API Server",
                        type=str,
                        required=False)
    parser.add_argument("--verify_tls",
                        help="verify full certificate chain from server"
                             " (default=False)",
                        action='store_true',
                        default=False,
                        required=False)
    parser.add_argument("--guide",
                        help="get a reply back with API guide location",
                        default=None,
                        action='version',
                        version="Read at: {}".format(GUIDE_URL))
    parser.add_argument("--version",
                        help="get a reply back with calipso_client version",
                        action='version',
                        default=None,
                        version='%(prog)s version: {}'.format(VERSION))

    subparsers = parser.add_subparsers(help='Request modes')

    scan_parser = subparsers.add_parser('scan', help='Scan request mode')
    scan_parser.set_defaults(handler=handle_scan)
    scan_parser.add_argument("--environment",
                             help="specify environment name(typically 'cvim-<pod_name>') configured on the API server "
                             "Note: scan request always requires an environment)",
                             type=str,
                             required=True)
    scan_parser.add_argument("--scan_at",
                             help="specify the local time for the first scan in a recurring series "
                                  "in 'yyyy-mm-ddThh:mm' format (optional with --scan_recurrence flag)"
                                  " (default='NOW')",
                             type=str,
                             default="NOW",
                             required=False)
    scan_parser.add_argument("--scan_recurrence",
                             help="specify the recurring series of scheduled scan requests - "
                                  "can be used with optional --scan_at argument (options: {})"
                                  " (default=None)".format("/".join(RECURRENCE_OPTIONS)),
                             type=str,
                             default=None,
                             choices=RECURRENCE_OPTIONS,
                             required=False)
    scan_parser.add_argument("--es_index",
                             help="index environment inventory, links and cliques on ElasticSearch DB"
                                  " options: boolean"
                                  " (default=False)",
                             action='store_true',
                             default=False,
                             required=False)

    call_parser = subparsers.add_parser('call', help='API endpoints mode')
    call_parser.set_defaults(handler=handle_call)
    call_parser.add_argument("--endpoint",
                             help="endpoint url extension to use on the API server -"
                                  " options: please see API documentation for endpoints"
                                  " (default=None)",
                             type=str,
                             default=None,
                             choices=sorted(ALLOWED_ENDPOINTS),
                             required=True)
    call_parser.add_argument("--method",
                             help="method to use on the API server - options: {}"
                                  " (default='GET')".format("/".join(SUPPORTED_METHODS)),
                             type=str.upper,
                             default='GET',
                             choices=SUPPORTED_METHODS,
                             required=False)
    call_parser.add_argument("--environment",
                             help="specify environment name(typically 'cvim-<pod_name>') configured on the API server "
                                  "Note: call request requires an environment for following the endpoints: )"
                                  "[messages, links, inventory, scans, scheduled_scans, search, tree]"
                                  " (default=None)",
                             type=str,
                             default=None,
                             required=False)
    call_parser.add_argument("--payload",
                             help="json string with parameters to send to the API -"
                                  " options: please see API documentation per endpoint"
                                  " (default=None)",
                             type=str,
                             default=None,
                             required=False)
    call_parser.add_argument("--page",
                             help="a page number for retrieval"
                                  " (default=0)",
                             type=int,
                             default=0,
                             required=False)
    call_parser.add_argument("--page_size",
                             help="a number of total objects listed per page"
                                  " (default=1000)",
                             type=int,
                             default=1000,
                             required=False)

    args = parser.parse_args()
    try:
        return args.handler(CalipsoClient(api_host=args.api_server, api_port=args.api_port,
                                          api_password=args.api_password, verify_tls=args.verify_tls),
                            args)
    except Exception as e:
        return error(e)


if __name__ == "__main__":
    exit(run())


#### Examples of running client to publish scan requests:
# Run an immediate one-off scan:
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 scan --environment staging
# Setup a scheduled one-off scan at a given time in the future:
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 scan --environment staging --scan_at 2020-03-01T10:10
# Setup a weekly scheduled scan starting now:
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 scan --environment staging --scan_recurrence WEEKLY
# Setup a weekly scheduled scan starting at a given time in the future:
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 scan --environment staging --scan_at 2020-03-01T10:10 --scan_recurrence WEEKLY

#### Examples of running client to call API endpoints:
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --endpoint environment_configs
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --endpoint environment_configs --payload "{'name': 'staging'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint messages
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint messages --payload "{'id': '5cd2c6de01b845000dbaf0d9'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint scans
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint scans --payload "{'id': '5cd2c6de01b845000dbaf0d9'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint inventory
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint inventory --payload "{'page_size': '2000'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint links
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint links --payload "{'id': '5cd2aa2699bb0dc9c2f9021f'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint cliques
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint cliques --payload "{'id': '5cd2aa3199bb0dc9c2f911fc'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint scheduled_scans
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint scheduled_scans --payload "{'id': '5cd2aad401b845000d186174'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint inventory --payload "{'id': '01776a49-a522-41ab-ab7c-94f4297c4227'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --environment staging --endpoint inventory --payload "{'type': 'instance', 'page_size': '1500'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --endpoint constants --payload "{'name': 'link_types'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --api_password 1234 call --endpoint constants --payload "{'name': 'object_types'}"
