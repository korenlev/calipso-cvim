from discover.events.constants import SUBNET_OBJECT_TYPE
from discover.events.event_base import EventResult
from discover.events.event_delete_base import EventDeleteBase


class EventSubnetDelete(EventDeleteBase):

    OBJECT_TYPE = SUBNET_OBJECT_TYPE

    def delete_children_documents(self, env, vservice_id):
        vnic_parent_id = vservice_id + '-vnics'
        vnic = self.inv.get_by_field(env, 'vnic', 'parent_id', vnic_parent_id, get_single=True)
        if not vnic:
            self.log.info("Vnic document not found, aborting subnet deleting.")
            return self.construct_event_result(result=False, retry=False)

        # delete port and vnic together by mac address.
        self.inv.delete('inventory', {"mac_address": vnic.get("mac_address")})
        return self.delete_handler(env, vservice_id, 'vservice')

    def handle(self, env, notification):
        subnet_id = notification['payload']['subnet_id']
        network_document = self.inv.get_by_field(env, "network", "subnet_ids", subnet_id, get_single=True)
        if not network_document:
            self.log.info("network document not found, aborting subnet deleting")
            return self.construct_event_result(result=False, retry=False, object_id=subnet_id)

        # remove subnet_id from subnet_ids array
        network_document["subnet_ids"].remove(subnet_id)

        # find the subnet in network_document by subnet_id
        subnet = next(
            filter(lambda s: s['id'] == subnet_id,
                   network_document['subnets'].values()),
            None)

        # remove cidr from cidrs and delete subnet document.
        if subnet:
            network_document['cidrs'].remove(subnet['cidr'])
            del network_document['subnets'][subnet['name']]

        self.inv.set(network_document)

        # when network does not have any subnet, delete vservice DHCP, port and vnic documents.
        if len(network_document["subnet_ids"]) == 0:
            vservice_dhcp_id = 'qdhcp-' + network_document['id']
            result = self.delete_children_documents(env, vservice_dhcp_id)
            result.object_id = subnet_id
            result.document_id = network_document.get('_id')
            return result
        return self.construct_event_result(result=True,
                                           object_id=subnet_id,
                                           document_id=network_document.get('_id'))
