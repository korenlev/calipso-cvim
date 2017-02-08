from api.etc.logger import Logger


class OSDNAApiException(Exception):

    log = Logger().log

    def __init__(self, status, body="", message=""):
        super().__init__(message)
        self.message = message
        self.status = status
        self.body = body

    @staticmethod
    def handle(ex, req, resp, params):
        OSDNAApiException.log.debug(ex.message)
        resp.status = ex.status
        resp.body = ex.body

