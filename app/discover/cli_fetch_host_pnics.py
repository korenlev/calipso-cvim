from cli_access import CliAccess

import re

class CliFetchHostPnics(CliAccess):

  def __init__(self):
    super(CliFetchHostPnics, self).__init__()
    self.if_header = re.compile('^[-]?(eth\S+)\s+(.*)$')
    self.ethtool_attr = re.compile('^\s+([^:]+):\s(.*)$')
    self.regexps = {
      "mac_address": re.compile('^.*\sHWaddr\s(\S+)(\s.*)?$'),
      "IP Address": re.compile('^\s*inet addr:(\S+)\s.*$'),
      "IPv6 Address": re.compile('^\s*inet6 addr:\s*(\S+)(\s.*)?$')
    }

  def get(self, id):
    host_id = id[:id.rindex("-")]
    cmd = "ip -d link show | grep '^[0-9]\+: eth' | sed 's/^[^:]*: *//' | sed 's/:.*//'"
    interfaces_names = self.run_fetch_lines(cmd, host_id)
    interfaces = []
    for i in interfaces_names:
      # run ifconfig with specific interface name,
      # since running it with no name yields a list without inactive pNICs
      interface = self.find_interface_details(host_id, i)
      if interface:
        interfaces.append(interface)
    return interfaces

  def find_interface_details(self, host_id, interface_name):
    lines = self.run_fetch_lines("ifconfig " + interface_name, host_id)
    interface = None
    for line in lines:
      matches = self.if_header.match(line)
      if matches:
        name = matches.group(1)
        line_remainder = matches.group(2)
        id = interface_name
        interface = {
          "host": host_id,
          "name": id,
          "local_name": interface_name,
          "lines": []
        }
        self.handle_line(interface, line_remainder)
        interface["id"] = interface_name + interface["mac_address"]
      else:
        if interface:
          self.handle_line(interface, line)
    self.set_interface_data(interface)
    return interface

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
    interface["data"] = "\n".join(interface["lines"])
    interface.pop("lines", None)
    cmd = "ethtool " + interface["local_name"]
    lines = self.run_fetch_lines(cmd, interface["host"])
    attr = None
    for line in lines[1:]:
      matches = self.ethtool_attr.match(line)
      if matches:
        # add this attribute to the interface
        attr = matches.group(1)
        value = matches.group(2)
        interface[attr] = value.strip()
      else:
        # add more values to the current attribute as an array
        if isinstance(interface[attr], str):
          interface[attr] = [interface[attr], line.strip()]
        else:
          interface[attr].append(line.strip())


