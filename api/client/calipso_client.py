import requests
import urlparse
import json


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
            response = requests.post(url, data=payload, headers=self.headers)
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
print cc.call_api('get', 'environment_configs')
scan_params = {"env_name": "staging"}
print cc.call_api('get', 'scans', scan_params)
inv_params = {"env_name": "staging", "id": "01776a49-a522-41ab-ab7c-94f4297c4227"}
staging_network = cc.call_api('get', 'inventory', inv_params)
print staging_network
print "TYPE_DRIVER=", staging_network["provider:network_type"]


# consider http1.1: sess = requests.Session()
# sess.headers.update({'x-auth-token': token,'Content-type':'application/json'}  )


