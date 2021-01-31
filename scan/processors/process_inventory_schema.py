###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from genson import SchemaBuilder

from base.utils.mongo_access import MongoAccess
from base.utils.string_utils import stringify_doc
from scan.processors.processor import Processor


class ProcessInventorySchema(Processor):
    # Prerequisites should include all processors that modify the inventory fields
    PREREQUISITES = ["ProcessVedgeType", "ProcessVnicCount"]
    COLLECTION = "schemas"

    def run(self):
        super().run()

        objects_by_type_groups = self.inv.collections["inventory"].aggregate([
            {
                "$group": {
                    "_id": "$type",
                    "objects": {"$push": "$$ROOT"}
                }
            }
        ])

        for objects_by_type in objects_by_type_groups:
            schema_builder = SchemaBuilder()
            schema_builder.add_schema({"type": "object", "properties": {}})

            for obj in objects_by_type["objects"]:
                stringify_doc(obj)
                schema_builder.add_object(obj)

            self.inv.collections["schemas"].update_one({
                "type": objects_by_type["_id"],
            }, {
                "$set": {
                    "type": objects_by_type["_id"],
                    "schema": MongoAccess.encode_mongo_keys(schema_builder.to_schema())
                }
            },
                upsert=True
            )
