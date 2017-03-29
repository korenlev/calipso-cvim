from discover.events.event_base import EventBase


class EventPortUpdate(EventBase):

    def handle(self, env, notification):
        # check port document.
        port = notification['payload']['port']
        port_id = port['id']
        port_document = self.inv.get_by_id(env, port_id)
        if not port_document:
            self.log.info('port document does not exist, aborting port update')
            return None

        # build port document
        port_document['name'] = port['name']
        port_document['admin_state_up'] = port['admin_state_up']
        if port_document['admin_state_up']:
            port_document['status'] = 'ACTIVE'
        else:
            port_document['status'] = 'DOWN'

        port_document['binding:vnic_type'] = port['binding:vnic_type']

        # update port document.
        self.inv.set(port_document)
