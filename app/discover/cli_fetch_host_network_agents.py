import json
import re
from cli_access import CliAccess
from network_agents_list import NetworkAgentsList

class CliFetchHostNetworkAgents(CliAccess):

  def __init__(self):
    super(CliFetchHostNetworkAgents, self).__init__()
    self.agents_list = NetworkAgentsList()
    self.if_header = re.compile('^(\S+)\s+(.*)$')
    self.regexps = {
      "MAC Address": re.compile('^.*\sHWaddr\s(\S+)(\s.*)?$'),
      "IP Address": re.compile('^\s*inet addr:(\S+)\s.*$'),
      "IPv6 Address": re.compile('^\s*inet6 addr:\s*(\S+)(\s.*)?$')
    }

  def get(self, id):
    services_ids = self.run_fetch_lines("source openrc; ip netns")
    results = []
    for id in services_ids:
      result = self.get_details_from_ifconfig(id)
      if result:
        self.get_details_from_brctl_show(result)
        results.append(result)
    return results

  def get_details_from_ifconfig(self, id):
    cmd = "ip netns exec {0} ifconfig".format(id)
    lines = self.run_fetch_lines(cmd)
    interfaces = self.find_interfaces(lines)
    return interfaces

  def find_interfaces(self, lines):
    interfaces = []
    current = None
    for line in lines:
      matches = self.if_header.match(line)
      if matches:
        if current:
          self.finish_interface_handling(interfaces, current)
        name = matches.group(1)
        if name == "lo":
          current = None
        else:
          line_remainder = matches.group(2)
          current = {"name": name, "lines": []}
          self.handle_line(current, line_remainder)
      else:
        if current:
          self.handle_line(current, line)
    self.finish_interface_handling(interfaces, current)
    return interfaces

  def finish_interface_handling(self, interfaces, interface):
    interfaces.append(interface)
    self.set_interface_data(interface)

  def handle_line(self, interface, line):
    for re_name, re_value in self.regexps.items():
      matches = re_value.match(line)
      if matches:
        matched_value = matches.group(1)
        interface[re_name] = matched_value
    interface["lines"].append(line.strip())

  def set_interface_data(self, interface):
    if interface:
      interface["data"] = "\n".join(interface["lines"])
      interface.pop("lines", None)

  def get_details_from_brctl_show(self, result):
    out = self.run_fetch_lines("brctl show")
    #if out:
    #  result["brctl_show_output"] = out
