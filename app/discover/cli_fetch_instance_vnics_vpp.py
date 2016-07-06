from cli_fetch_instance_vnics import CliFetchInstanceVnics

class CliFetchInstanceVnicsVpp(CliFetchInstanceVnics):

  def __init__(self):
    super().__init__()

  def get_vnic_name(self, v, instance):
    return instance["name"] + "-" + v["@type"] + "-" + v["mac"]["@address"]

