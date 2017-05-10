import re

from discover.events.constants import NETWORK_OBJECT_TYPE
from discover.events.event_base import EventBase, EventResult


class EventNetworkUpdate(EventBase):

    OBJECT_TYPE = NETWORK_OBJECT_TYPE

    def handle(self, env, notification):
        network = notification['payload']['network']
        network_id = network['id']

        network_document = self.inv.get_by_id(env, network_id)
        if not network_document:
            self.log.info('Network document not found, aborting network update')
            return self.construct_event_result(result=False, retry=True)

        # update network document
        name = network['name']
        if name != network_document['name']:
            network_document['name'] = name
            network_document['object_name'] = name

            name_path = network_document['name_path']
            network_document['name_path'] = name_path[:name_path.rindex('/') + 1] + name

            # TBD: fix name_path for descendants
            self.inv.values_replace({"environment": env,
                                     "name_path": {"$regex": r"^" + re.escape(name_path + '/')}},
                                    {"name_path": {"from": name_path, "to": network_document['name_path']}})

        network_document['admin_state_up'] = network['admin_state_up']
        self.inv.set(network_document)
        return self.construct_event_result(result=True,
                                           related_object=network_id,
                                           display_context=network_id)
