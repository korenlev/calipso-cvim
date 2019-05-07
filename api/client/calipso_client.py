import requests
import urlparse
import json
import time
import datetime
import argparse
# This is a calipso api client designed to be small and simple
# currently for single pod, single api_server and single environment
# assuming environment_config details are already deployed by CVIM automation
# for central CVIM monitoring we'll need to add to this client per pod scanning
# and allow adding multiple environments


class CalipsoClient:

    def __init__(self):
        self.api_server = args.api_server
        self.client_version = "0.2.0"
        self.username = "calipso"
        self.password = "calipso_default"
        self.port = args.api_port
        self.base_url = "http://{}:{}/".format(self.api_server, self.port)
        self.auth_url = self.base_url + "auth/tokens"
        self.headers = {'Content-Type': 'application/json'}
        self.token = None
        self.time = None
        self.auth_body = {
            "auth": {
                "methods": ["credentials"],
                "credentials": {
                    "username": self.username,
                    "password": self.password
                }
            }
        }

    def get_token(self):
        try:
            resp = requests.post(self.auth_url,
                                 data=json.dumps(self.auth_body),
                                 headers=self.headers)
            cont = resp.json()
            self.token = cont["token"]
            self.headers.update({'x-auth-token': self.token})
            return self.token
        except requests.exceptions.RequestException as e:
            return "Error sending request: {}".format(e)

    def call_api(self, method, endpoint, payload=None):
        url = urlparse.urljoin(self.base_url, endpoint)
        self.get_token()
        if method == 'post':
            response = requests.post(url, json=payload, headers=self.headers)
        elif method == 'delete':
            response = requests.delete(url, headers=self.headers)
        elif method == 'put':
            response = requests.put(url, data=payload, headers=self.headers)
        else:
            response = requests.get(url, params=payload, headers=self.headers)
        if response:
            content = json.loads(response.content)
            return content
        else:
            return " endpoint not found"

    def scan_request(self, environment, freq="NOW"):
        if freq == "NOW":
            request_payload = {
                "log_level": "warning",
                "clear": True,
                "scan_only_inventory": False,
                "scan_only_links": False,
                "scan_only_cliques": False,
                "environment": environment
            }
            return self.call_api('post', 'scans', request_payload)
        else:
            self.time = datetime.datetime.now().isoformat()
            request_payload = {
                "freq": freq,
                "log_level": "warning",
                "clear": True,
                "scan_only_links": False,
                "scan_only_cliques": False,
                "environment": environment,
                "scan_only_inventory": False,
                "submit_timestamp": self.time
            }
            return self.call_api('post', 'scheduled_scans', request_payload)

    def scan_check(self, environment, doc_id, scheduled=False):
        if scheduled is False:
            scan_params = {"env_name": environment, "id": doc_id}
            return self.call_api('get', 'scans', scan_params)
        else:
            scan_params = {"environment": environment, "id": doc_id}
            return self.call_api('get', 'scheduled_scans', scan_params)


# parser for getting mandatory and some optional command arguments:
parser = argparse.ArgumentParser()
parser.add_argument("--api_server",
                    help="FQDN (ex:mysrv.cisco.com) or IP address of API Server"
                         " (default=localhost)",
                    type=str,
                    default="localhost",
                    required=True)
parser.add_argument("--api_port",
                    help="TCP Port exposed for the Calipso API Server "
                         " (default=8000)",
                    type=int,
                    default="8000",
                    required=True)
parser.add_argument("--environment",
                    help="specify environment name configured on calipso server"
                         " (default=None)",
                    type=str,
                    default=None,
                    required=False)
parser.add_argument("--scan",
                    help="scan/discover the specific cloud environment -"
                         " options: NOW/HOURLY/DAILY/WEEKLY/MONTHLY/YEARLY"
                         " (default=None)",
                    type=str,
                    default=None,
                    required=False)
parser.add_argument("--method",
                    help="method to use on the calipso API server -"
                         " options: get/post/delete/put"
                         " (default=None)",
                    type=str,
                    default=None,
                    required=False)
parser.add_argument("--endpoint",
                    help="endpoint url extension to use on calipso API server -"
                         " options: please see API documentation on endpoints"
                         " (default=None)",
                    type=str,
                    default=None,
                    required=False)
parser.add_argument("--payload",
                    help="dict string with parameters to send to calipso API -"
                         " options: please see API documentation per endpoint"
                         " (default=None)",
                    type=str,
                    default=None,
                    required=False)

args = parser.parse_args()

cc = CalipsoClient()

# only interaction with environment_configs is allowed without environment name
if not args.environment:
    if args.endpoint == "environment_configs":
        if args.payload:  # case for a specific environment
            payload_str = args.payload.replace("'", "\"")
            payload_json = json.loads(payload_str)
            env_reply = cc.call_api(args.method, args.endpoint, payload_json)
        else:  # case for all environments
            env_reply = cc.call_api(args.method, args.endpoint)
        print env_reply
        exit()
    else:
        print " environment and payload are needed with this requested endpoint"
        exit()
# ex1: get all environment_configs, with their names
# print cc.call_api('get', 'environment_configs')
# ex2: get a specific environment_config
# print cc.call_api('get', 'environment_configs', payload={"name": "staging"})

scan_options = ["NOW", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY"]
if args.scan:
    if args.scan not in scan_options:
        print " unaccepted scan option, use --help for more details"
        exit()
    if args.method:
        print " method not needed for scan requests, please remove"
        exit(0)
    if args.endpoint:
        print " endpoint not needed for scan requests, please remove"
        exit()
    else:
        if args.scan == "NOW":
            # post scan request, for specific environment, get doc_id
            scan_reply = cc.scan_request(environment=args.environment)
            print " scan request posted for environment", args.environment, ".."
            scan_doc_id = scan_reply["id"]
            # wait till the specific scan status is 'completed'
            scan_status = "pending"
            while scan_status != "completed":
                scan_doc = cc.scan_check(environment=args.environment,
                                         doc_id=scan_doc_id)
                scan_status = scan_doc["status"]
                print " wait for scan to complete, scan status: ", scan_status
                time.sleep(2)
                if scan_status == "failed":
                    print "scan has failed, please debug in scan container"
            print " inventory, links and cliques has been discovered"
            exit()
        else:
            # post scan schedule, for specific environment, get doc_id
            schedule_reply = cc.scan_request(environment=args.environment,
                                             freq=args.scan)
            schedule_doc_id = schedule_reply["id"]
            schedule_doc = cc.scan_check(environment=args.environment,
                                         doc_id=schedule_doc_id,
                                         scheduled=True)
            print "\n scheduled scan at:", schedule_doc["scheduled_timestamp"],\
                "\n submitted at:", schedule_doc["submit_timestamp"],\
                "\n scan frequency:", schedule_doc["freq"]

#  generic request for items from any endpoint using any method, per environment
if not args.endpoint or not args.method:
    print " endpoint and method are needed for this type of request"
method_options = ["get", "post", "delete", "put"]
if args.method not in method_options:
    print " unaccepted method option, use --help for more details"
    exit()
params = {"env_name": args.environment}
if args.payload:
    payload_str = args.payload.replace("'", "\"")
    payload_json = json.loads(payload_str)
    params.update(payload_json)
reply = cc.call_api(args.method, args.endpoint, params)
print reply

# examples of some working arguments:

# --api_server korlev-calipso-testing.cisco.com --api_port 8000 --method get --endpoint environment_configs
# --api_server korlev-calipso-testing.cisco.com --api_port 8000 --method get --endpoint environment_configs --payload "{'name': 'staging'}"

# --api_server korlev-calipso-testing.cisco.com --api_port 8000 --environment staging --scan NOW
# --api_server korlev-calipso-testing.cisco.com --api_port 8000 --environment staging --scan WEEKLY

# --api_server korlev-calipso-testing.cisco.com --api_port 8000 --method get --environment staging --endpoint messages
# --api_server korlev-calipso-testing.cisco.com --api_port 8000 --method get --environment staging --endpoint scans
# --api_server korlev-calipso-testing.cisco.com --api_port 8000 --method get --environment staging --endpoint inventory
# --api_server korlev-calipso-testing.cisco.com --api_port 8000 --method get --environment staging --endpoint links
# --api_server korlev-calipso-testing.cisco.com --api_port 8000 --method get --environment staging --endpoint cliques
# --api_server korlev-calipso-testing.cisco.com --api_port 8000 --method get --environment staging --endpoint scheduled_scans
# --api_server korlev-calipso-testing.cisco.com --api_port 8000 --method get --environment staging --endpoint inventory --payload "{'id': '01776a49-a522-41ab-ab7c-94f4297c4227'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8000 --method get --environment staging --endpoint inventory --payload "{'type': 'instance'}"
