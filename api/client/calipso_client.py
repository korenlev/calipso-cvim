import requests
import urlparse
import json
import time


class CalipsoClient:

    def __init__(self):
        self.api_server = "korlev-calipso-testing"
        self.username = "calipso"
        self.password = "calipso_default"
        self.port = "8000"
        self.base_url = "http://{}:{}/".format(self.api_server, self.port)
        self.auth_url = self.base_url + "/auth/tokens"
        self.headers = {'Content-type': 'application/json'}
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
            print payload
            response = requests.post(url, json=payload, headers=self.headers)
        elif method == 'delete':
            response = requests.delete(url, headers=self.headers)
        elif method == 'put':
            response = requests.put(url, data=payload, headers=self.headers)
        else:
            response = requests.get(url, params=payload, headers=self.headers)
        content = json.loads(response.content)
        return content


cc = CalipsoClient()
print cc.get_token()
print cc.headers
# get all environment_configs
print cc.call_api('get', 'environment_configs')
# get specific environment_config
print cc.call_api('get', 'environment_configs', payload={"name": "staging"})
# post a scan request for a specific environment
scan_request_payload = {
    "log_level": "warning",
    "clear": True,
    "scan_only_inventory": False,
    "scan_only_links": False,
    "scan_only_cliques": False,
    "environment": "staging"
}
# scan_request_reply = cc.call_api('post', 'scans', scan_request_payload)
# print scan_request_reply
# then here we will place a check for specific scan id status
# once VIMNET-1860 is implemented
# time.sleep(180)
# get scans made for a specific environment (for status of scan etc)
scan_params = {"env_name": "staging"}
scans_statuses = cc.call_api('get', 'scans', scan_params)
print scans_statuses
inv_params = {"env_name": "staging", "id": "01776a49-a522-41ab-ab7c-94f4297c4227"}
staging_network = cc.call_api('get', 'inventory', inv_params)
print staging_network
print "TYPE_DRIVER=", staging_network["provider:network_type"]


# consider http1.1: sess = requests.Session()
# sess.headers.update({'x-auth-token': token,'Content-type':'application/json'}  )


