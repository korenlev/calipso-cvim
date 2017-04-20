from discover.api_fetch_host_instances import ApiFetchHostInstances
from discover.events.event_base import EventResult
from discover.events.event_delete_base import EventDeleteBase


class EventPortDelete(EventDeleteBase):

    def delete_port(self, env, port_id):
        port_doc = self.inv.get_by_id(env, port_id)
        if not port_doc:
            self.log.info("Port document not found, aborting port deleting.")
            return EventResult(result=False, retry=False)

        # if port is binding to a instance, instance document needs to be updated.
        if 'compute' in port_doc['device_owner']:
            self.inv.log.info("update instance document to which port is binding.")
            self.update_instance(env, port_doc)

        # delete port document
        self.inv.delete('inventory', {'id': port_id})

        # delete vnic and related document
        vnic_doc = self.inv.get_by_field(env, 'vnic', 'mac_address', port_doc['mac_address'], get_single=True)
        if not vnic_doc:
            self.log.info("Vnic document not found, aborting vnic deleting.")
            return EventResult(result=False, retry=False)
        result = self.delete_handler(env, vnic_doc['id'], 'vnic')
        self.inv.log.info('Finished port deleting')
        return result

    def update_instance(self, env, port_doc):
        # update instance document if port
        network_id = port_doc['network_id']
        instance_doc = self.inv.get_by_field(env, 'instance', 'network_info.id', port_doc['id'], get_single=True)
        if instance_doc:
            port_num = 0

            for port in instance_doc['network_info']:
                if port['network']['id'] == network_id:
                    port_num += 1
                if port['id'] == port_doc['id']:
                    instance_doc['network_info'].remove(port)
                    self.inv.log.info("update network information of instance document.")

            if port_num == 1:
                # remove network information only when last port in network will be deleted.
                instance_doc['network'].remove(network_id)

            # update instance mac address.
            if port_doc['mac_address'] == instance_doc['mac_address']:
                instance_fetcher = ApiFetchHostInstances()
                instance_fetcher.set_env(env)
                host_id = port_doc['binding:host_id']
                instance_id = port_doc['device_id']
                instance_docs = instance_fetcher.get(host_id + '-')
                instance = next(filter(lambda i: i['id'] == instance_id, instance_docs), None)
                if instance:
                    if 'mac_address' not in instance:
                        instance_doc['mac_address'] = None
                    self.inv.log.info("update mac_address:%s of instance document." % instance_doc['mac_address'])

            self.inv.set(instance_doc)
        else:
            self.inv.log.info("No instance document binding to network:%s." % network_id)

    def handle(self, env, notification):
        port_id = notification['payload']['port_id']
        return self.delete_port(env, port_id)
