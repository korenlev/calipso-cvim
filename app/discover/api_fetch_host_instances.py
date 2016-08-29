from api_access import ApiAccess
from db_access import DbAccess
from db_fetch_instances import DbFetchInstances
from inventory_mgr import InventoryMgr
from singleton import Singleton


class ApiFetchHostInstances(ApiAccess, DbAccess, metaclass=Singleton):
    def __init__(self):
        super(ApiFetchHostInstances, self).__init__()
        self.inv = InventoryMgr()
        self.endpoint = ApiAccess.base_url.replace(":5000", ":8774")
        self.projects = None
        self.db_fetcher = DbFetchInstances()

    def get_projects(self):
        if not self.projects:
            projects_list = self.inv.get(self.get_env(), "project", None)
            self.projects = [p["name"] for p in projects_list]

    def get(self, id):
        self.get_projects()
        host_id = id[:id.rindex("-")]
        host = self.inv.get_by_id(self.get_env(), host_id)
        if "Compute" not in host["host_type"]:
            return []
        instances_found = self.get_instances_from_api(host_id)
        self.db_fetcher.get_instance_data(instances_found)
        return instances_found

    def get_instances_from_api(self, host_name):
        token = self.v2_auth_pwd("admin")
        if not token:
            return []
        tenant_id = token["tenant"]["id"]
        req_url = self.endpoint + "/v2/" + tenant_id + \
                  "/os-hypervisors/" + host_name + "/servers"
        response = self.get_url(req_url, {"X-Auth-Token": token["id"]})
        ret = []
        if not "hypervisors" in response:
            return []
        if not "servers" in response["hypervisors"][0]:
            return []
        for doc in response["hypervisors"][0]["servers"]:
            doc["id"] = doc["uuid"]
            doc["host"] = host_name
            doc["local_name"] = doc.pop("name")
            ret.append(doc)
        self.log.info("found %s instances for host: %s", str(len(ret)), host_name)
        return ret
