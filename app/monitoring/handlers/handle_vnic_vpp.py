# handle monitoring event for VPP vEdge objects

from monitoring.handlers.monitoring_check_handler import MonitoringCheckHandler


class HandleVnicVpp(MonitoringCheckHandler):

    def __init__(self, args):
        super().__init__(args)

    def handle(self, id, check_result):
        is_instance_vnic = id.startswith('instance_vnic')
        vnic_type = 'instance_vnic' if is_instance_vnic else 'vservice_vnic'
        id = id[len(vnic_type)+1:]
        if is_instance_vnic:
            # last part of ID is MAC address, for which we need to
            # recreate the ':' which is removed from Mongo Keys
            mac_address_no_colons = id[id.rindex('-')+1:]
            mac_parts = []
            for i in range(0, 6):
                mac_parts.append(mac_address_no_colons[i*2:i*2+2])
            mac_address = ':'.join(mac_parts)
            id = id[:id.rindex('-')+1] + mac_address
        doc = self.doc_by_id(id)
        if not doc:
            return 1
        self.keep_result(doc, check_result)
        return check_result['status']
