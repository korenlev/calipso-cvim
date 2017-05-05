from discover.events.constants import PORT_OBJECT_TYPE
from discover.events.event_base import EventBase, EventResult


class EventPortUpdate(EventBase):

    OBJECT_TYPE = PORT_OBJECT_TYPE

    def handle(self, env, notification):
        # check port document.
        port = notification['payload']['port']
        port_id = port['id']
        port_document = self.inv.get_by_id(env, port_id)
        if not port_document:
            self.log.info('port document does not exist, aborting port update')
            return self.construct_event_result(result=False, retry=True)

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
        return self.construct_event_result(result=True,
                                           related_object=port_document.get('name'),
                                           display_context=port_document.get('network_id'))
