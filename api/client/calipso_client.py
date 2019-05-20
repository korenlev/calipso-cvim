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

    def __init__(self, api_host, api_port, api_password):
        self.api_server = api_host
        self.username = "calipso"
        self.password = api_password
        self.port = api_port
        self.base_url = "http://{}:{}".format(self.api_server, self.port)
        self.auth_url = urlparse.urljoin(self.base_url, "auth/tokens")
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

    def get_token(self):
        # print("Getting auth token")
        try:
            resp = requests.post(self.auth_url,
                                 data=json.dumps(self.auth_body),
                                 headers=self.headers, timeout=3)
            cont = resp.json()
            if "token" not in cont:
                fatal("Failed to fetch auth token. Response:\n{}".format(cont))
            self.token = cont["token"]
            self.headers.update({'X-Auth-Token': self.token})
            return self.token
        except requests.exceptions.RequestException as e:
            fatal("Error sending request: {}".format(e))

    @staticmethod
    def pp_json(json_text, sort=True, indents=4):
        json_data = json.loads(json_text) if type(json_text) is str else json_text
        print(json.dumps(json_data, sort_keys=sort, indent=indents))

    def call_api(self, method, endpoint, payload=None, fail_on_error=True):
        url = urlparse.urljoin(self.base_url, endpoint)
        if not self.token:
            self.get_token()
        # print("Calling API: {}.\nMethod:{}.\nPayload:{}.\nHeaders:{}."
        #       .format(url, method, payload, self.headers))

        method = method.lower()
        if method == 'post':
            response = requests.post(url, json=payload, headers=self.headers,
                                     timeout=3)
        elif method == 'delete':
            response = requests.delete(url, headers=self.headers)
        elif method == 'put':
            response = requests.put(url, json=payload, headers=self.headers,
                                    timeout=3)
        else:
            response = requests.get(url, params=payload, headers=self.headers,
                                    timeout=3)

        if response.status_code == 404:
            fatal("Endpoint or payload item not found")
        elif response.status_code == 400:
            fatal("Environment or resource not found, or invalid keys. "
                  "Response: {}".format(response.content))

        content = json.loads(response.content)
        if 'error' in content and fail_on_error:
            fatal(content['error'])
        return content

    def scan_request(self, environment, freq="NOW"):
        if freq == "NOW":
            request_payload = {
                "log_level": "warning",
                "clear": True,
                "scan_only_inventory": False,
                "scan_only_links": False,
                "scan_only_cliques": False,
                "env_name": environment
            }
            return self.call_api('post', 'scans', request_payload)
        else:
            request_payload = {
                "freq": freq,
                "log_level": "warning",
                "clear": True,
                "scan_only_links": False,
                "scan_only_cliques": False,
                "env_name": environment,
                "scan_only_inventory": False,
                "submit_timestamp": datetime.datetime.now().isoformat()
            }
            return self.call_api('post', 'scheduled_scans', request_payload)

    def scan_check(self, environment, doc_id, scheduled=False):
        scan_params = {"env_name": environment, "id": doc_id}
        if scheduled is False:
            return self.call_api('get', 'scans', scan_params)
        else:
            return self.call_api('get', 'scheduled_scans', scan_params)


def fatal(err):
    print(err)
    exit(1)


def run():
    # parser for getting mandatory and some optional command arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_server",
                        help="FQDN (ex:mysrv.cisco.com) or IP address of API Server"
                             " (default=localhost)",
                        type=str,
                        default="localhost",
                        required=False)
    parser.add_argument("--api_port",
                        help="TCP Port exposed for the Calipso API Server "
                             " (default=8747)",
                        type=int,
                        default=8747,
                        required=False)
    parser.add_argument("--api_password",
                        help="API password (secret) used for the Calipso API Server "
                             " (default=calipso_default)",
                        type=str,
                        default="calipso_default",
                        required=False)
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
    parser.add_argument("--guide",
                        help="get a reply back with calipso api guide location",
                        dest='guide',
                        default=False,
                        action='store_true',
                        required=False)

    parser.add_argument("--version",
                        help="get a reply back with calipso_client version",
                        action='version',
                        default=None,
                        version='%(prog)s version: 0.2.3')

    args = parser.parse_args()

    if args.guide:
        guide_url = "https://cloud-gogs.cisco.com/mercury/calipso/src/master/docs/release/api-guide.rst"
        # guide = requests.get(guide_url)
        # print(guide.content)
        print ("wget/curl from: {}".format(guide_url))
        exit(0)

    cc = CalipsoClient(args.api_server, args.api_port, args.api_password)

    # only interaction with environment_configs is allowed without environment name
    if not args.environment:
        if args.endpoint == "environment_configs":
            if args.payload:  # case for a specific environment
                payload_str = args.payload.replace("'", "\"")
                payload_json = json.loads(payload_str)
                env_reply = cc.call_api(args.method, args.endpoint, payload_json)
            else:  # case for all environments
                env_reply = cc.call_api(args.method, args.endpoint)
            cc.pp_json(env_reply)
            exit(0)
        else:
            fatal("Enter well-known endpoint, method and/or environment")
    # ex1: get all environment_configs, with their names
    # print cc.call_api('get', 'environment_configs')
    # ex2: get a specific environment_config
    # print cc.call_api('get', 'environment_configs', payload={"name": "staging"})

    scan_options = ["NOW", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY"]
    if args.scan:
        if args.scan not in scan_options:
            fatal("Unaccepted scan option, use --help for more details")
        if args.method:
            fatal("Method not needed for scan requests, please remove")
        if args.endpoint:
            fatal("Endpoint not needed for scan requests, please remove")
        else:
            if args.scan == "NOW":
                # post scan request, for specific environment, get doc_id
                scan_reply = cc.scan_request(environment=args.environment)
                print("Scan request posted for environment {}".format(args.environment))
                scan_doc_id = scan_reply["id"]
                # wait till the specific scan status is 'completed'
                scan_status = "pending"
                while scan_status != "completed":
                    scan_doc = cc.scan_check(environment=args.environment,
                                             doc_id=scan_doc_id)
                    scan_status = scan_doc["status"]
                    print("Wait for scan to complete, scan status: {}".format(scan_status))
                    time.sleep(2)
                    if scan_status == "failed":
                        fatal("Scan has failed, please debug in scan container")
                print("Inventory, links and cliques has been discovered")
            else:
                # post scan schedule, for specific environment, get doc_id
                schedule_reply = cc.scan_request(environment=args.environment,
                                                 freq=args.scan)
                schedule_doc_id = schedule_reply["id"]
                time.sleep(2)
                schedule_doc = cc.scan_check(environment=args.environment,
                                             doc_id=schedule_doc_id,
                                             scheduled=True)
                print("Scheduled scan at: {}\nSubmitted at: {}\nScan frequency: {}"
                      .format(schedule_doc['scheduled_timestamp'], schedule_doc['submit_timestamp'], schedule_doc['freq']))
            exit(0)

    #  generic request for items from any endpoint using any method, per environment
    if not args.endpoint or not args.method:
        fatal("Endpoint and method are needed for this type of request")
    method_options = ["get", "post", "delete", "put"]
    if args.method not in method_options:
        fatal("Unaccepted method option, use --help for more details")
    params = {"env_name": args.environment}
    if args.payload:
        payload_str = args.payload.replace("'", "\"")
        payload_json = json.loads(payload_str)
        params.update(payload_json)
    reply = cc.call_api(args.method, args.endpoint, params)
    cc.pp_json(reply)
    exit(0)


if __name__ == "__main__":
    run()

# examples of some working arguments:

# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --endpoint environment_configs
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --endpoint environment_configs --payload "{'name': 'staging'}"

# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --environment staging --scan NOW
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --environment staging --scan WEEKLY

# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --environment staging --endpoint messages
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --environment staging --endpoint messages --payload "{'id': '17678.55917.5562'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --environment staging --endpoint scans
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --environment staging --method get --endpoint scans --payload "{'id': '5cd2c6de01b845000dbaf0d9'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --environment staging --endpoint inventory
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --environment staging --endpoint inventory --payload "{'page_size': '2000'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --environment staging --endpoint links
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --environment staging --endpoint links --payload "{'id': '5cd2aa2699bb0dc9c2f9021f'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --environment staging --endpoint cliques
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --environment staging --endpoint cliques --payload "{'id': '5cd2aa3199bb0dc9c2f911fc'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --environment staging --endpoint scheduled_scans
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --environment staging --endpoint scheduled_scans --payload "{'id': '5cd2aad401b845000d186174'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --environment staging --endpoint inventory --payload "{'id': '01776a49-a522-41ab-ab7c-94f4297c4227'}"
# --api_server korlev-calipso-testing.cisco.com --api_port 8747 --method get --environment staging --endpoint inventory --payload "{'type': 'instance', 'page_size': '1500'}"
