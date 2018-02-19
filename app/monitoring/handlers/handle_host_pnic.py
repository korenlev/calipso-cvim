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

from bson import ObjectId

from discover.fetcher import Fetcher
from monitoring.handlers.monitoring_check_handler \
    import MonitoringCheckHandler, ERROR_LEVEL
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

    @staticmethod
    def get_pnic_object_id(obj_id: str) -> str:
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
    # dependent objects are all objects that are part of a clique that has
    # a link that includes that pNic as either source or target.
    def propagate_error_state(self, pnic: dict, check_result: dict):
        if not self.is_kubernetes:
            return
        # find cliques where the pNIC appears in the list of nodes
        related_cliques = self.inv.find_items({'environment': self.env,
                                               'nodes': ObjectId(pnic['_id'])},
                                              projection=['nodes'],
                                              collection='cliques')
        dependents = []
        for clique in related_cliques:
            dependents.extend(clique['nodes'])
        if not dependents:
            return

        is_error = check_result['status'] != 0
        fields_to_set = {}
        self.keep_result(fields_to_set, check_result, add_message=False)
        fields_to_set['status_value'] = 1
        fields_to_set['status'] = \
            ERROR_LEVEL[fields_to_set['status_value']]
        fields_to_set['root_cause'] = dict(id=pnic['id'], name=pnic['name'],
                                           type=pnic['type'],
                                           status_text=pnic['status_text'])
        if is_error:
            # set status fields
            action = {'$set': fields_to_set}
        else:
            fields_to_remove = {k: '' for k in fields_to_set.keys()}
            # clear status fields from dependents
            action = {'$unset': fields_to_remove}
        self.inv.inventory_collection.update(
            {
                'environment': self.env,
                '_id': {'$in': dependents},
                # do not change state for other pNIC objects
                'type': {'$ne': pnic['type']}
            },
            action,
            multi=True,
        )
