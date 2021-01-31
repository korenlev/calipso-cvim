###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from dateutil import tz

from api.responders.resource.scans import Scans
from api.responders.resource.timezone import Timezone
from api.responders.responder_base import ResponderBase
from api.client.version import VERSION
# from scan.validators.validator_base import ValidatorBase


class Health(ResponderBase):

    @staticmethod
    def get_env_health(env: dict):
        env_health = {
            "scanned": False,
            "timezone": Timezone.get_timezone_payload(tz.gettz(env.get("timezone", "unknown"))),
            "version": env.get("version"),
        }

        latest_scans = Scans().get_latest_scan(query={})
        if latest_scans:
            env_health.update({
                "scanned": latest_scans[0]["status"] == "completed",
                "last_scan_status": latest_scans[0]["status"],
                "last_scanned": env.get("last_scanned")
            })

        # validations = self.inv.find_one({"environment": env}, collection=ValidatorBase.COLLECTION)
        # if validations:
        #     env_health["validations"] = validations["validations"]

        return env_health

    def on_get(self, req, resp):
        self.log.debug("Getting health")
        filters = self.parse_query_params(req)
        filters_requirements = {
            'env_name': self.require(str),
        }
        self.validate_query_data(filters, filters_requirements)

        env_name = filters.get("env_name")
        if env_name:
            environment = self.get_single_object(collection="environments_config",
                                                 query={"name": env_name})
            if not environment:
                self.bad_request("Unknown environment: {}".format(env_name))

            self.set_ok_response(resp, self.get_env_health(environment))
            return

        envs = self.get_objects_list(collection="environments_config", query={})

        response_doc = {
            "version": VERSION,
            "timezone": Timezone.get_timezone_payload(tz.tzlocal()),
            "environments": {
                env["name"]: self.get_env_health(env) for env in envs
            }
        }
        self.set_ok_response(resp, response_doc)

    # TODO: on_post -> async (?) trigger validations?
