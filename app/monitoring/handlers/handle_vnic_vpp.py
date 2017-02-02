# handle monitoring event for VPP vEdge objects

from monitoring.handlers.monitoring_check_handler import MonitoringCheckHandler


class HandleVnicVpp(MonitoringCheckHandler):

    def __init__(self, args):
        super().__init__(args)

    def handle(self, id, check_result):
        is_instance_vnic = id.startswith('instance_vnic')
        vnic_type = 'instance_vnic' if is_instance_vnic else 'vservice_vnic'
        id = self.decode_special_characters(id[len(vnic_type)+1:])
        doc = self.doc_by_id(id)
        if not doc:
            return 1
        self.keep_result(doc, check_result)
        return check_result['status']
