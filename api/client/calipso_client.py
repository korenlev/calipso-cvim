import requests
import urlparse
import json
import time
import datetime
# This is a calipso api client designed to be small and simple
# currently for single pod, single api_server and single environment
# assuming environment_config details are already deployed by CVIM automation
# for central CVIM monitoring we'll need to add to this client per pod scanning
# and allow adding multiple environments


class CalipsoClient:

    def __init__(self):
        self.api_server = "korlev-calipso-testing"
        self.client_version = "0.2.0"
        self.username = "calipso"
        self.password = "calipso_default"
        self.port = "8000"
        self.base_url = "http://{}:{}/".format(self.api_server, self.port)
        self.auth_url = self.base_url + "/auth/tokens"
        self.headers = {'Content-type': 'application/json'}
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
        content = json.loads(response.content)
        return content

    def scan_request(self, environment, scheduled=False, freq="DAILY"):
        self.time = datetime.datetime.now().isoformat()
        if scheduled is False:
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
            params = {"env_name": environment, "id": doc_id}
            return self.call_api('get', 'scans', params)
        else:
            params = {"environment": environment, "id": doc_id}
            return self.call_api('get', 'scheduled_scans', params)


cc = CalipsoClient()
# print cc.get_token()
# print cc.headers

# get all environment_configs, with their names
print cc.call_api('get', 'environment_configs')
# get a specific environment_config
print cc.call_api('get', 'environment_configs', payload={"name": "staging"})

# post a scan request, with defaults, for a specific environment, get it's id
scan_reply = cc.scan_request(environment="staging", scheduled=False)
scan_doc_id = scan_reply["id"]
# post a scheduled scan, with defaults, for a specific environment, get it's id
schedule_reply = cc.scan_request(environment="staging", scheduled=True,
                                 freq="WEEKLY")
schedule_doc_id = schedule_reply["id"]

# wait till the specific scan status is 'completed' ..
scan_status = "pending"
while scan_status != "completed":
    scan_doc = cc.scan_check(environment="staging", doc_id=scan_doc_id,
                             scheduled=False)
    scan_status = scan_doc["status"]
    print "scanning status: ", scan_status
    time.sleep(2)

# get a specific scheduled_doc scheduled time, start time and freq
schedule_doc = cc.scan_check(environment="staging", doc_id=schedule_doc_id,
                             scheduled=True)
print schedule_doc["scheduled_timestamp"], schedule_doc["freq"]

# get network object from inventory
inv_params = {"env_name": "staging",
              "id": "01776a49-a522-41ab-ab7c-94f4297c4227"}
staging_network = cc.call_api('get', 'inventory', inv_params)
print staging_network
print "TYPE_DRIVER=", staging_network["provider:network_type"]

# another inventory example for instances:
inv_params = {"env_name": "staging",
              "type": "instance"}
staging_instances = cc.call_api('get', 'inventory', inv_params)
instances = staging_instances["objects"]
for instance in instances:
    print instance["name"], instance["name_path"]

# consider http1.1: sess = requests.Session()
# sess.headers.update({'x-auth-token': token,'Content-type':'application/json'}  )


