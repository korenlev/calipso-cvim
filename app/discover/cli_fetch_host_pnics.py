from cli_access import CliAccess
from inventory_mgr import InventoryMgr

import re
import logging

class CliFetchHostPnics(CliAccess):

  def __init__(self):
    super(CliFetchHostPnics, self).__init__()
    self.inv = InventoryMgr()
    self.if_header = re.compile('^[-]?(eth[0-9]\S*|eno\S*)\s+(.*)$')
    self.ethtool_attr = re.compile('^\s+([^:]+):\s(.*)$')
    self.regexps = [
      {"mac_address": re.compile('^.*\sHWaddr\s(\S+)(\s.*)?$')},
      {"mac_address": re.compile('^.*\sether\s(\S+)(\s.*)?$')},
      {"IP Address": re.compile('^\s*inet addr:(\S+)\s.*$')},
      {"IP Address": re.compile('^\s*inet (\S+)\s.*$')},
      {"IPv6 Address": re.compile('^\s*inet6 addr:\s*(\S+)(\s.*)?$')},
      {"IPv6 Address": re.compile('^\s*inet6 \s*(\S+)(\s.*)?$')}
    ]

  def get(self, id):
    host_id = id[:id.rindex("-")]
    cmd = "ip -d link show | " + \
      "grep '^[0-9]\+: \(eth\|eno\)' | " + \
      "sed 's/^[^:]*: *//' | " + \
      "sed 's/:.*//'"
    host = self.inv.get_by_id(self.get_env(), host_id)
    if not host:
      print("Error: CliFetchHostPnics: host not found: " + host_id)
      return []
    if "host_type" not in host:
      print("Error: host does not have host_type: " + host_id + \
        ", host: " + str(host))
      return []
    host_types = host["host_type"]
    if "Network" not in host_types and "Compute" not in host_types:
      return []
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
        name = matches.group(1).strip(":")
        line_remainder = matches.group(2)
        id = interface_name
        interface = {
          "host": host_id,
          "name": id,
          "local_name": interface_name,
          "lines": []
        }
        self.handle_line(interface, line_remainder)
      else:
        if interface:
          self.handle_line(interface, line)
    self.set_interface_data(interface)
    return interface

  def handle_line(self, interface, line):
    for regexp_tuple in self.regexps:
      for re_name in regexp_tuple.keys():
        re_value = regexp_tuple[re_name]
        matches = re_value.match(line)
        if matches:
          matched_value = matches.group(1)
          interface[re_name] = matched_value
          if re_name == "mac_address":
            interface["id"] = interface["name"] + "-" + interface["mac_address"]
    interface["lines"].append(line.strip())

  def set_interface_data(self, interface):
    if not interface:
      return
    interface["data"] = "\n".join(interface["lines"])
    interface.pop("lines", None)
    ethtool_ifname = interface["local_name"]
    if "@" in interface["local_name"]:
      pos = interface["local_name"].index("@")
      ethtool_ifname = ethtool_ifname[pos+1:]
    cmd = "ethtool " + ethtool_ifname
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

  def add_links(self):
    pnics = self.inv.find_items({
      "environment": self.get_env(),
      "type": "pnic"
    })
    for pnic in pnics:
      self.add_pnic_network_links(pnic)

  def add_pnic_network_links(self, pnic):
    logging.info("adding links of type: pnic-network")
    host = pnic["host"]
    # find ports for that host, and fetch just the network ID
    ports = self.inv.find_items({
      "environment": self.get_env(),
      "type": "port",
      "binding:host_id" : host
    }, {"network_id": 1})
    networks = {}
    for port in ports:
      networks[port["network_id"]] = 1
    for network_id in networks.keys():
      network = self.inv.get_by_id(self.get_env(), network_id)
      source = pnic["_id"]
      source_id = pnic["id"]
      target = network["_id"]
      target_id = network["id"]
      link_type = "pnic-network"
      link_name = "Segment-" + str(network["provider:segmentation_id"])
      state = "up" if pnic["Link detected"] == "yes" else "down"
      link_weight = 0 # TBD
      self.inv.create_link(self.get_env(), host,
        source, source_id, target, target_id,
        link_type, link_name, state, link_weight)


