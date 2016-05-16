import re
import xmltodict
from cli_access import CliAccess
from inventory_mgr import InventoryMgr

class CliFetchVserviceVnics(CliAccess):

  def __init__(self):
    super(CliFetchVserviceVnics, self).__init__()
    self.inv = InventoryMgr()
    self.if_header = re.compile('^[-]?(\S+)\s+(.*)$')
    self.regexps = {
      "IP Address": re.compile('^\s*inet addr:(\S+)\s.*$'),
      "IPv6 Address": re.compile('^\s*inet6 addr:\s*(\S+)(\s.*)?$')
    }

  def get(self, id):
    host = self.inv.get_by_id(self.get_env(), id)
    if not host or host["host_type"] == "Compute node":
      return []
    cmd = self.ssh_cmd + host["ip_address"] + " ip netns"
    lines = self.run_fetch_lines(cmd)
    ret = []
    for l in [l for l in lines if l.startswith("qdhcp") or l.startswith("qrouter")]:
      ret.extend(self.handle_service(host, l))
    return ret

  def handle_service(self, host, service):
    cmd = self.ssh_cmd + host["ip_address"] + " ip netns exec " + service + " ifconfig"
    lines = self.run_fetch_lines(cmd)
    interfaces = []
    current = None
    for line in lines:
      matches = self.if_header.match(line)
      if matches:
        if current:
          self.set_interface_data(current)
        name = matches.group(1)
        # ignore 'lo' interface
        if name == 'lo':
          current = None
        else:
          line_remainder = matches.group(2)
          vservice_id = host["id"] + "-"  + service[1:]
          current = {
            "id": id,
            "type": "vnic",
            "vnic_type": "vservice_vnic",
            "host": host["id"],
            "name": name,
            "master_parent_type": "vservice",
            "master_parent_id": vservice_id,
            "parent_type": "vservice_object_type",
            "parent_id": vservice_id + "-vnics",
            "parent_text": "vNICs",
            "lines": []
          }
          interfaces.append(current)
          self.handle_line(current, line_remainder)
      else:
        if current:
          self.handle_line(current, line)
    if current:
      self.set_interface_data(current)
    return interfaces

  def handle_line(self, interface, line):
    for re_name, re_value in self.regexps.items():
      matches = re_value.match(line)
      if matches:
        matched_value = matches.group(1)
        interface[re_name] = matched_value
    interface["lines"].append(line.strip())

  def set_interface_data(self, interface):
    if not interface:
      return
    interface["data"] = "\n".join(interface.pop("lines", None))

