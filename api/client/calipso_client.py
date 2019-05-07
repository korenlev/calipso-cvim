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
        self.client_version = "0.1.9"
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

    def scan_status(self, environment, scheduled=False):
        if scheduled is False:
            params = {"env_name": environment}
            reply = self.call_api('get', 'scans', params)
            scans = reply["scans"]
            for scan in scans:
                print scan["status"], scan["id"]
        else:
            params = {"environment": environment}
            reply = self.call_api('get', 'scheduled_scans', params)
            schedules = reply["scheduled_scans"]
            for schedule in schedules:
                print schedule["scheduled_timestamp"], schedule["id"]


cc = CalipsoClient()
# print cc.get_token()
# print cc.headers

# get all environment_configs, with their names
print cc.call_api('get', 'environment_configs')
# get a specific environment_config
print cc.call_api('get', 'environment_configs', payload={"name": "staging"})

# post a scan request, with defaults, for a specific environment
print cc.scan_request(environment="staging", scheduled=False)
# post a scheduled scan, with defaults, for a specific environment
print cc.scan_request(environment="staging", scheduled=True, freq="WEEKLY")

# then here we will place a check for specific scan id status
# once VIMNET-1860 is implemented - to add scan 'id' into reply
time.sleep(120)
# get scans made for a specific environment (for status of scan etc)
cc.scan_status(environment="staging", scheduled=False)
cc.scan_status(environment="staging", scheduled=True)


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


