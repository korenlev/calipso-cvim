from discover.events.event_base import EventResult
from discover.events.kube.kube_event_base import KubeEventBase
from utils.exceptions import ResourceGoneError


class KubeErrorHandler(KubeEventBase):

    GONE_CODE = 410

    def handle(self, env, values):
        super().handle(env, values)
        if values['raw_object'].get('code') == self.GONE_CODE:
            raise ResourceGoneError()
        return EventResult(result=True)
