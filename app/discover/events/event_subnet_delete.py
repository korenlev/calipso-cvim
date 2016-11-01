from discover.events.event_delete_base import EventDeleteBase
from discover.inventory_mgr import InventoryMgr


class EventSubnetDelete(EventDeleteBase):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def delete_children_documents(self, env, vservice_id):
        vnic_parent_id = vservice_id + '-vnics'
        matches = self.inv.get_by_field(env, 'vnic', 'parent_id', vnic_parent_id)
        if len(matches) == 0:
            return
        vnic = matches[0]

        # delete port and vnic together by mac address.
        self.inv.delete('inventory', {"mac_address": vnic["mac_address"]})
        self.delete_handler(env, vservice_id, 'vservice')

    def handle(self, env, notification):
        subnet_id = notification['payload']['subnet_id']
        matches = self.inv.get_by_field(self.env, "network", "subnets_id", subnet_id)
        if len(matches) == 0:
            self.log.info('network document is not found, aborting subnet delete')
            return None
        network_document = matches[0]

        # remove subnet_id from subnet_ids array
        network_document["subnets_id"].remove(subnet_id)

        # remove cidr from cidrs and delete subnet document.
        for subnet in network_document['subnets'].values():
            if subnet['id'] == subnet_id:
                network_document['cidrs'].remove(subnet['cidr'])
                subnet_name = subnet['name']
                del network_document['subnets'][subnet_name]
                break
        self.inv.set(network_document)

        # when network does not have any subnet, delete vservice DHCP, port and vnic documents.
        if len(network_document["subnets_id"]) == 0:
            vservice_dhcp_id = 'qdhcp-' + network_document['id']
            self.delete_children_documents(env, vservice_dhcp_id)
