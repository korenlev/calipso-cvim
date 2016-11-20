# handle monitoring event for links

from monitoring.handlers.monitoring_check_handler import MonitoringCheckHandler

class HandleLink(MonitoringCheckHandler):

  def __init__(self, args):
    super().__init__(args)

  def handle(self, db_id, check_result):
    doc = self.doc_by_db_id(db_id, 'links')
    if not doc:
      return 1
    self.keep_result(doc, check_result)
    return check_result['status']
