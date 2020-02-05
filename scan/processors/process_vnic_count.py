from scan.processors.processor import Processor


class ProcessVnicCount(Processor):
    PREREQUISITES = ["ProcessVedgeType"]

    def run(self):
        super().run()

        instances = self.find_by_type("instance")
        for instance in instances:
            instance.update({
                "vpp_vnic_count": 0,
                "ovs_vnic_count": 0,
                "sriov_vnic_count": 0,
            })

            vnics = self.inv.find_items({"environment": self.env, "type": "vnic", "instance_id": instance["id"]})
            for vnic in vnics:
                vedge_type = vnic.get("vedge_type", "").upper()
                if vedge_type == "VPP":
                    instance["vpp_vnic_count"] += 1
                elif vedge_type == "OVS":
                    instance["ovs_vnic_count"] += 1
                elif vedge_type == "SRIOV":
                    instance["sriov_vnic_count"] += 1

            self.inv.set(instance)
