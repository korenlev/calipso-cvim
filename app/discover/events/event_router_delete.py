from discover.events.constants import ROUTER_OBJECT_TYPE
from discover.events.event_base import EventResult
from discover.events.event_delete_base import EventDeleteBase
from utils.util import encode_router_id


class EventRouterDelete(EventDeleteBase):

    OBJECT_TYPE = ROUTER_OBJECT_TYPE

    def handle(self, env, values):
        payload = values['payload']

        if 'publisher_id' not in values:
            self.log.error("Publisher_id is not in event values. Aborting router delete")
            return self.construct_event_result(result=False, retry=False)

        host_id = values['publisher_id'].replace('network.', '', 1)
        if 'router_id' in payload:
            router_id = payload['router_id']
        elif 'id' in payload:
            router_id = payload['id']
        else:
            router_id = payload.get('router', {}).get('id')

        if not router_id:
            self.log.error("Router id is not in payload. Aborting router delete")
            return self.construct_event_result(result=False, retry=False)

        router_full_id = encode_router_id(host_id, router_id)
        return self.delete_handler(env, router_full_id, "vservice")
