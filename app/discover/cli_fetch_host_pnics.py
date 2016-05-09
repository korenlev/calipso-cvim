from cli_access import CliAccess

import re

class CliFetchHostPnics(CliAccess):

  def __init__(self):
    super(CliFetchHostPnics, self).__init__()
    self.if_header = re.compile('^(\S+)\s+(.*)$')
    self.ethtool_attr = re.compile('^\s+([^:]+):\s(.*)$')
    self.regexps = {
      "MAC Address": re.compile('^.*\sHWaddr\s(\S+)(\s.*)?$'),
      "IP Address": re.compile('^\s*inet addr:(\S+)\s.*$'),
      "IPv6 Address": re.compile('^\s*inet6 addr:\s*(\S+)(\s.*)?$')
    }

  def get(self, id):
    host_id = id[:id.rindex("-")]
    cmd = "ssh " + host_id + ' " ifconfig"'
    lines = self.run_fetch_lines(cmd)
    interfaces = [i for i in self.find_interfaces(host_id, lines) if i]
    return interfaces

  def find_interfaces(self, host_id, lines):
    interfaces = []
    current = None
    for line in lines:
      matches = self.if_header.match(line)
      if matches:
        if current:
          self.finish_interface_handling(interfaces, current)
        name = matches.group(1)
        # look only for interfaces starting with 'eth'
        if not name.startswith("eth"):
          current = None
        else:
          line_remainder = matches.group(2)
          id = host_id + "-" + name
          current = {
            "id": id,
            "host": host_id,
            "name": id,
            "local_name": name,
            "lines": []
          }
          self.handle_line(current, line_remainder)
      else:
        if current:
          self.handle_line(current, line)
    if current:
      self.h_interface_handling(interfaces, current)
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
    if not interface:
      return
    interface["data"] = "\n".join(interface["lines"])
    interface.pop("lines", None)
    cmd = "ssh " + interface["host"] + ' " ethtool ' + interface["local_name"] + '"'
    lines = self.run_fetch_lines(cmd)
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


