from monitoring.setup.monitoring_handler import MonitoringHandler


class MonitoringOtep(MonitoringHandler):

    def __init__(self, mongo_conf_file):
        super().__init__(mongo_conf_file)

    # add monitoring setup for remote host
    def create_setup(self, o):
        for port in o['ports'].values():
            self.create_monitoring_for_otep_port(o, port)

    def create_monitoring_for_otep_port(self, o, port):
        if port['type'] not in ['vxlan', 'gre']:
            return  # we only handle vxlan and gre
        opt = port['options']
        config = {
            "objtype": "otep",
            "objid": o['id'],
            "portid": port['name'],
            "otep_src_ip": opt['local_ip'],
            "otep_dest_ip": opt['remote_ip']}
        self.create_monitoring_for_object(o, config)
