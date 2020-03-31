from api.responders.responder_base import ResponderBase


class Health(ResponderBase):
    def on_get(self, req, resp):
        self.set_ok_response(resp, "We're open")
