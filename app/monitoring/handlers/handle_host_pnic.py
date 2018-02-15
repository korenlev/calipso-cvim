###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
# handle monitoring event for pNIC objects

from discover.fetcher import Fetcher
from monitoring.handlers.monitoring_check_handler import MonitoringCheckHandler
from utils.special_char_converter import SpecialCharConverter


class HandleHostPnic(MonitoringCheckHandler):

    def __init__(self, args):
        super().__init__(args)
        self.env_config = self.conf.get_env_config()
        self.env = self.env_config.get('name', '')
        self.is_kubernetes = self.env_config .get('environment_type', '') == \
            Fetcher.ENV_TYPE_KUBERNETES

    def handle(self, obj_id, check_result):
        object_id = self.get_pnic_object_id(obj_id)
        doc = self.doc_by_id(object_id)
        if not doc:
            return 1
        self.keep_result(doc, check_result)
        self.propagate_error_state(doc, check_result)
        return check_result['status']

    def get_pnic_object_id(self, obj_id: str) -> str:
        object_id = obj_id[:obj_id.index('-')]
        mac = obj_id[obj_id.index('-')+1:]
        converter = SpecialCharConverter()
        mac_address = converter.decode_special_characters(mac)
        object_id += '-' + mac_address
        return object_id

    # for Kubernetes environment only:
    # - when a host pNic change status (from monitoring module) to 'Error':
    #   - all dependent objects should change status to 'Warning'
    #   - set status_text for these object to the status_text from the pnic
    # - when pnic status changes back from error: TBD
    #
    # dependent objects are objects that are part of a clique with a link
    # that includes that pNic as either source or target.
    def propagate_error_state(self, pnic: dict, check_result: dict):
        if not self.is_kubernetes:
            return
        pnic_id = pnic['id']
        # find links in this environment that have the pNic as their source
        # or their target
        condition = {'$and':
            [
                {'environment': self.env},
                {'$or':
                     [
                         {'source_id': pnic_id},
                         {'target_id': pnic_id}
                     ]
                }
            ]
        }
        related_links = self.inv.find_items(condition, collection='links')
        dependents = []
        for link in related_links:
            other_obj_id = pnic['target_id'] if link['source_id'] == pnic_id \
                else pnic['source_id']
            if other_obj_id not in dependents:
                dependents.append(other_obj_id)
        if not dependents:
            return

        fields_to_set = dict('status')
        self.keep_result(fields_to_set, check_result, add_message=False)
        self.inv.inventory_collection.update({
            'environment': self.env,
            'id': {'$in': dependents}},
            {'$set': fields_to_set},
            multi=True,
        )
