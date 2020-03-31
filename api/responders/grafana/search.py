from api.responders.responder_base import ResponderBase


class Search(ResponderBase):
    def on_post(self, req, resp):
        if req.content_type == "application/json":
            error, request_data = self.get_content_from_request(req)
            if error:
                return self.bad_request("Failed to get json content from request")
            target = request_data.get("target")
            if not target:
                return self.bad_request("Missing search target")
        else:
            return self.bad_request("Unsupported content type: {}".format(req.content_type))

        objects = []
        if target == "environment_configs":
            environments = self.get_objects_list(collection="environments_config", query={})
            # TODO: return full objects?
            objects = [env["name"] for env in environments]
        elif target == "object_types":
            object_types = self.get_single_object(collection="constants", query={"name": "object_types"})
            if object_types:
                objects = [ot["value"] for ot in object_types["data"]]

        return self.set_ok_response(resp, objects)
