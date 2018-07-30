from time import strftime

from monitoring.handlers.monitoring_check_handler import MonitoringCheckHandler


class HandleInstanceVnics(MonitoringCheckHandler):
    def handle(self, object_id, check_result):
        doc = self.doc_by_id(object_id)
        if not doc:
            self.log.error('unable to find instance with id={}'.format(object_id))
            return 1
        doc['vnics_status'] = check_result['status']
        doc['vnics_status_text'] = check_result['output']
        doc['vnics_status_timestamp'] = strftime(self.TIME_FORMAT,
                                                 self.check_ts(check_result))
        self.inv.set(doc)
        return check_result['status']
