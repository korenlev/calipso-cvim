###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import re

from scan.fetchers.cli.cli_fetch_vconnectors import CliFetchVconnectors


class CliFetchVconnectorsOvs(CliFetchVconnectors):
    def __init__(self):
        super().__init__()

    def get_vconnectors(self, host_id):
        # we handle cases where 'brctl' utility isn't available and will populate same data with 'ip' utility instead
        lines = self.run_fetch_lines('brctl show', ssh_to_host=host_id)
        results = []
        if len(lines) <= 1:
            ip_link_details = self.run_fetch_json_response('ip -d -j link show', ssh_to_host=host_id)
            # TODO there are many more details here for host_pnics and vconnectors that we can add in the future
            for link in ip_link_details:
                doc = {}
                kind = ''
                data = {}
                doc['bridge_name'] = ''
                info = link.get('linkinfo', '')
                if info:
                    kind = info.get('info_kind', '')
                    data: dict = info.get('info_data', '')
                if kind == 'bridge':
                    doc = data
                    doc['bridge_name'] = link['ifname']
                    doc['bridge_id'] = data.get('bridge_id', '')
                    doc['stp_enabled'] = data.get('stp_state')
                    del doc['stp_state']
                    doc['interfaces'] = ''
                    for interface in ip_link_details:
                        master = interface.get('master', '')
                        if master == doc['bridge_name']:
                            doc['interfaces'] = ','.join((doc['interfaces'], interface['ifname']))
                    doc['interfaces'] = doc['interfaces'].replace(',', '', 1)
                    results.append(doc)
        else:
            headers = ['bridge_name', 'bridge_id', 'stp_enabled', 'interfaces']
            headers_count = len(headers)
            # since we hard-coded the headers list, remove the headers line
            del lines[:1]
            # intefaces can spill to next line - need to detect that and add
            # them to the end of the previous line for our procesing
            fixed_lines = self.merge_ws_spillover_lines(lines)
            results = self.parse_cmd_result_with_whitespace(fixed_lines, headers, False)
        ret = []
        for doc in results:
            doc['name'] = '{}-{}'.format(host_id, doc['bridge_name'])
            doc['id'] = '{}-{}'.format(doc['name'], doc.pop('bridge_id'))
            doc['host'] = host_id
            doc['connector_type'] = 'bridge'
            self.get_vconnector_interfaces(doc, host_id)
            ret.append(doc)
        return ret

    def get_vconnector_interfaces(self, doc, host_id):
        if 'interfaces' not in doc:
            doc['interfaces'] = []
            doc['interfaces_names'] = []
            return
        interfaces = []
        interface_names = doc['interfaces'].split(',')
        for interface_name in interface_names:
            # find MAC address for this interface from ports list
            port_id_prefix = interface_name[3:]
            port = self.inv.find_items({
                'environment': self.get_env(),
                'type': 'port',
                'binding:host_id': host_id,
                'id': {'$regex': r'^' + re.escape(port_id_prefix)}
            }, get_single=True)
            mac_address = '' if not port else port['mac_address']
            interface = {'name': interface_name, 'mac_address': mac_address}
            interfaces.append(interface)
        doc['interfaces'] = interfaces
        doc['interfaces_names'] = interface_names
