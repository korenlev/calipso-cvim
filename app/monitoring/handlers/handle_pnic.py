# handle monitoring event for pNIC objects

from monitoring.handlers.monitoring_check_handler import MonitoringCheckHandler

class HandlePnic(MonitoringCheckHandler):

  def __init__(self, args):
    super().__init__(args)

  def handle(self, id, check_result):
    object_id = id[:id.index('-')]
    object_id += self.L
    doc = self.doc_by_id(object_id)
    if not doc:
      return 1
    self.keep_result(doc, check_result)
    return check_result['status']
