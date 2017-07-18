import json

import requests

from discover.configuration import Configuration
from discover.fetcher import Fetcher


class AciAccess(Fetcher):

    RESPONSE_FORMAT = "json"
    cookie_token = None

    def __init__(self):
        super().__init__()
        self.configuration = Configuration()
        self.aci_configuration = self.configuration.get("ACI")
        self.host = self.aci_configuration["host"]

    def get_base_url(self):
        return "https://{}/api".format(self.host)

    @staticmethod
    def get_object_by_field_name(payload, field_name):
        imdata = payload.get("imdata", [])
        if not imdata:
            return None

        return imdata[0].get(field_name, {})

    @staticmethod
    def get_objects_by_field_names(payload, *field_names):
        results = payload.get("imdata", [])
        if not results:
            return []

        for field in field_names:
            results = [entry[field] for entry in results]
        return results

    # Set auth tokens in request headers and cookies
    @staticmethod
    def _insert_tokens(cookies):
        return dict(cookies, **AciAccess.cookie_token) \
            if cookies \
            else AciAccess.cookie_token

    def login(self):
        url = "/".join((self.get_base_url(), "aaaLogin.json"))
        payload = {
            "aaaUser": {
                "attributes": {
                    "name": self.aci_configuration["user"],
                    "pwd": self.aci_configuration["pwd"]
                }
            }
        }

        response = requests.post(url, json=payload, verify=False)
        response.raise_for_status()

        response_object = self.get_object_by_field_name(payload=response.json(),
                                                        field_name="aaaLogin")
        token = response_object["attributes"]["token"]

        AciAccess.cookie_token = {"APIC-Cookie": token}

    # Refresh token or login if token has expired
    def refresh_token(self):
        # First time login
        if not AciAccess.cookie_token:
            self.login()
            return

        url = "/".join((self.get_base_url(), "aaaRefresh.json"))

        response = requests.get(url, verify=False)

        # Login again if the token has expired
        if response.status_code == requests.codes.forbidden:
            self.login()
            return
        # Propagate any other error
        elif response.status_code != requests.codes.ok:
            response.raise_for_status()

        response_object = self.get_object_by_field_name(payload=response.json(),
                                                        field_name="aaaLogin")
        token = response_object["attributes"]["token"]

        AciAccess.cookie_token = token

    def send_get(self, url, params, headers, cookies):
        self.refresh_token()

        cookies = self._insert_tokens(cookies)

        response = requests.get(url, params=params, headers=headers,
                                cookies=cookies, verify=False)
        # Let client handle HTTP errors
        response.raise_for_status()

        return response.json()

    # Search ACI for Managed Objects (MOs) of a specific class
    def fetch_objects_by_class(self,
                               class_name: str,
                               params: dict = None,
                               headers: dict = None,
                               cookies: dict = None,
                               response_format: str = RESPONSE_FORMAT):

        url = "/".join((self.get_base_url(),
                        "class", "{cn}.{f}".format(cn=class_name, f=response_format)))

        response_json = self.send_get(url, params, headers, cookies)
        return self.get_objects_by_field_names(response_json, class_name)

    # Fetch data for a specific Managed Object (MO)
    def fetch_mo_data(self,
                      dn: str,
                      params: dict = None,
                      headers: dict = None,
                      cookies: dict = None,
                      response_format: str = RESPONSE_FORMAT):
        url = "/".join((self.get_base_url(), "mo", "topology",
                        "{dn}.{f}".format(dn=dn, f=response_format)))

        response_json = self.send_get(url, params, headers, cookies)
        return response_json
