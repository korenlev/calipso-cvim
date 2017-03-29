import re

from discover.events.event_base import EventBase


class EventNetworkUpdate(EventBase):

    def handle(self, env, notification):
        network = notification['payload']['network']
        network_id = network['id']

        network_document = self.inv.get_by_id(env, network_id)
        if network_document:
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
