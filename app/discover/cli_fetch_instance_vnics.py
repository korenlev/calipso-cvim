from discover.cli_fetch_instance_vnics_base import CliFetchInstanceVnicsBase


class CliFetchInstanceVnics(CliFetchInstanceVnicsBase):
    def __init__(self):
        super().__init__()

    def set_vnic_properties(self, v, instance):
        super().set_vnic_properties(v, instance)
        v["source_bridge"] = v["source"]["@bridge"]

    def get_vnic_name(self, v, instance):
        return v["target"]["@dev"]
