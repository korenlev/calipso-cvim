from utils.logging.console_logger import ConsoleLogger


class OSDNAApiException(Exception):
    log = ConsoleLogger()

    def __init__(self, status, body="", message=""):
        super().__init__(message)
        self.message = message
        self.status = status
        self.body = body

    @staticmethod
    def handle(ex, req, resp, params):
        OSDNAApiException.log.error(ex.message)
        resp.status = ex.status
        resp.body = ex.body
