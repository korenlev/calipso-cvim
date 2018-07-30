from monitoring.handlers.monitoring_check_handler import MonitoringCheckHandler


class HandleInstanceVm(MonitoringCheckHandler):
    def handle(self, object_id, check_result):
        doc = self.doc_by_id(object_id)
        if not doc:
            self.log.error('unable to find instance with id={}'.format(object_id))
            return 1
        self.keep_result(doc, check_result)
        return check_result['status']
