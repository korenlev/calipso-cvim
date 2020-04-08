###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
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
            objects = [env["name"] for env in environments]
        elif target == "object_types":
            object_types = self.get_single_object(collection="constants", query={"name": "object_types"})
            if object_types:
                objects = [ot["value"] for ot in object_types["data"]]

        return self.set_ok_response(resp, objects)
