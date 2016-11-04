from discover.api_access import ApiAccess
from discover.inventory_mgr import InventoryMgr


class ApiFetchPort(ApiAccess):
    def __init__(self):
        super(ApiFetchPort, self).__init__()
        self.inv = InventoryMgr()

    def get(self, id):
        if id == None:
            self.log.info("Get method needs ID parameter")
            return []
        # use project admin credentials, to be able to fetch all ports
        token = self.v2_auth_pwd("admin")
        if not token:
            return []
        ret = []
        for region in self.regions:
            ret.append(self.get_port(region, token, id))
        return ret

    def get_port(self, region, token, id):
        endpoint = self.get_region_url_nover(region, "neutron")
        req_url = endpoint + "/v2.0/ports/" + id
        headers = {
            "X-Auth-Project-Id": "admin",
            "X-Auth-Token": token["id"]
        }
        response = self.get_url(req_url, headers)
        if not "port" in response:
            return []

        doc = response["port"]
        doc["master_parent_type"] = "network"
        doc["master_parent_id"] = doc["network_id"]
        doc["parent_type"] = "ports_folder"
        doc["parent_id"] = doc["network_id"] + "-ports"
        doc["parent_text"] = "Ports"
        # get the project name
        net = self.inv.get_by_id(self.get_env(), doc["network_id"])
        if net:
            doc["name"] = doc["mac_address"]
        else:
            doc["name"] = doc["id"]
        project = self.inv.get_by_id(self.get_env(), doc["tenant_id"])
        if project:
            doc["project"] = project["name"]
        return doc
