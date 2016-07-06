from cli_fetch_instance_vnics import CliFetchInstanceVnics

class CliFetchInstanceVnicsOvs(CliFetchInstanceVnics):

  def __init__(self):
    super().__init__()

  def set_vnic_properties(self, v, instance):
    super().set_vnic_properties(v, instance)
    v["source_bridge"] = v["source"]["@bridge"]

