from api.responders.resource.scans import Scans
from api.responders.responder_base import ResponderBase
from api.client.version import VERSION


class Health(ResponderBase):
    def on_get(self, req, resp):
        envs = self.get_objects_list(collection="environments_config", query={})

        response_doc = {"version": VERSION, "environments": {}}
        for env in envs:
            env_health = {"scanned": False}

            latest_scans = Scans().get_latest_scan(query={})
            if latest_scans:
                env_health.update({
                    "scanned": latest_scans[0]["status"] == "completed",
                    "scan_in_progress": latest_scans[0]["status"] == "running",
                    "last_scanned": env.get("last_scanned")
                })

            response_doc["environments"][env["name"]] = env_health

        self.set_ok_response(resp, response_doc)
