# handle monitoring event for VPP vEdge objects

from monitoring.handlers.monitoring_check_handler import MonitoringCheckHandler


class BasicCheckHandler(MonitoringCheckHandler):

    def __init__(self, args):
        super().__init__(args)

    def handle(self, id, check_result):
        doc = self.doc_by_id(id)
        if not doc:
            return 1
        self.keep_result(doc, check_result)
        return check_result['status']
