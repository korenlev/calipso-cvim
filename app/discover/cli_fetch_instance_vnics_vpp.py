from discover.cli_fetch_instance_vnics_base import CliFetchInstanceVnicsBase


class CliFetchInstanceVnicsVpp(CliFetchInstanceVnicsBase):
    def __init__(self):
        super().__init__()

    def get_vnic_name(self, v, instance):
        return instance["name"] + "-" + v["@type"] + "-" + v["mac"]["@address"]
