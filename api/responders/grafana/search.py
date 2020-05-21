###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import json
from json import JSONDecodeError

from api.responders.responder_base import ResponderBase


class Search(ResponderBase):
    def on_post(self, req, resp):
        if req.content_type != "application/json":
            return self.bad_request("Unsupported content type: {}".format(req.content_type))

        error, request_data = self.get_content_from_request(req)
        if error:
            return self.bad_request("Failed to get json content from request")

        target = request_data.get("target")
        if not target:
            return self.bad_request("Missing search target")

        try:
            target = json.loads(target)
            if isinstance(target, dict):
                if len(target.keys()) > 1:
                    return self.bad_request("Multiple targets are not supported")
            else:
                return self.bad_request("Target must either be a string or a valid JSON object")

            target, target_filters = list(target.items())[0]
            if not isinstance(target_filters, dict):
                return self.bad_request("Target filters must be a valid JSON object")
        except JSONDecodeError:
            target_filters = {}

        objects = []
        if target == "regions":
            objects = self.distinct(collection="environments_config", field="cvim_region")
        elif target == "metros":
            filters = {}
            regions_filter = target_filters.get("regions", "All")
            if regions_filter and regions_filter != "All":
                filters["cvim_region"] = target_filters["regions"]

            objects = self.distinct(collection="environments_config", field="cvim_metro", query=filters)
        elif target == "environment_configs":
            filters = {}
            regions_filter = target_filters.get("regions", "All")
            if regions_filter and regions_filter != "All":
                filters["cvim_region"] = target_filters["regions"]
            metros_filter = target_filters.get("metros", "All")
            if metros_filter and metros_filter != "All":
                filters["cvim_metro"] = target_filters["metros"]

            objects = self.distinct(collection="environments_config", field="name", query=filters)
        elif target == "object_types":
            objects = self.get_constants_by_name("object_types")
        else:
            return self.bad_request("Unknown target: {}".format(target))

        return self.set_ok_response(resp, objects)
