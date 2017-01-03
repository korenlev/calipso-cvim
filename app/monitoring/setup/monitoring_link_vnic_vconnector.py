from monitoring.setup.monitoring_check_handler import MonitoringCheckHandler


class MonitoringLinkVnicVconnector(MonitoringCheckHandler):

    def __init__(self, mongo_conf_file, env):
        super().__init__(mongo_conf_file, env)

    # add monitoring setup for remote host
    def create_setup(self, link):
        vconnector_id = link['target_id']
        vnic = self.inv.get_by_id(self.env, link['source_id'])
        if not vnic:
            self.log.error('could not find vnic for vnic-vconnector link')
            return
        if 'mac_address' not in vnic:
            self.log.error('could not find MAC address in vNIC: ' + vnic['id'])
            return
        values = {
            'linktype': 'vnic-vconnector',
            'fromobjid': link['source_id'],
            'toobjid': vconnector_id,
            'bridge': vconnector_id,
            'mac_address': vnic['mac_address']}
        self.create_monitoring_for_object(link, values)
