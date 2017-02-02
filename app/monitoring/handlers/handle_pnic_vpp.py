# handle monitoring event for VPP vEdge objects

from monitoring.handlers.monitoring_check_handler import MonitoringCheckHandler


class HandlePnicVpp(MonitoringCheckHandler):

    def __init__(self, args):
        super().__init__(args)

    def handle(self, id, check_result):
        id = self.decode_special_characters(id)
        pnic = self.doc_by_id(id)
        if not pnic:
            return 1
        self.keep_result(pnic, check_result)
        # in vEdge object in corresponding port name, set attributes:
        # "status", "status_timestamp", "status_text"
        return check_result['status']
