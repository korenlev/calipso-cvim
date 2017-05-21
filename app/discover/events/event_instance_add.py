from discover.events.constants import INSTANCE_OBJECT_TYPE
from discover.events.event_base import EventBase
from discover.scanner import Scanner


class EventInstanceAdd(EventBase):

    OBJECT_TYPE = INSTANCE_OBJECT_TYPE

    def handle(self, env, values):
        # find the host, to serve as parent
        instance_id = values['payload']['instance_id']
        host_id = values['payload']['host']
        instances_root_id = host_id + '-instances'
        instances_root = self.inv.get_by_id(env, instances_root_id)
        if not instances_root:
            self.log.info('instances root not found, aborting instance add')
            return self.construct_event_result(result=False,
                                               retry=True,
                                               object_id=instance_id)

        # scan instance
        scanner = Scanner()
        scanner.set_env(env)
        scanner.scan('ScanInstancesRoot', instances_root,
                     limit_to_child_id=instance_id,
                     limit_to_child_type='instance')
        scanner.scan_from_queue()

        # scan host
        host = self.inv.get_by_id(env, host_id)
        scanner.scan('ScanHost', host,
                     limit_to_child_type=['vconnectors_folder',
                                          'vedges_folder'])
        scanner.scan_from_queue()
        scanner.scan_links()
        scanner.scan_cliques()

        instance_document = self.inv.get_by_id(env, instance_id)
        db_id = instance_document.get('_id')
        return self.construct_event_result(result=True,
                                           object_id=instance_id,
                                           document_id=db_id)
