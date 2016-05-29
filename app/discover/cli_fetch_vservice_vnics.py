import re
from cli_access import CliAccess
from inventory_mgr import InventoryMgr

class CliFetchVserviceVnics(CliAccess):

  def __init__(self):
    super(CliFetchVserviceVnics, self).__init__()
    self.inv = InventoryMgr()
    self.if_header = re.compile('^[-]?(\S+)\s+(.*)$')
    self.regexps = [
      {"mac_address": re.compile('^.*\sHWaddr\s(\S+)(\s.*)?$')},
      {"mac_address": re.compile('^.*\sether\s(\S+)(\s.*)?$')},
      {"IP Address": re.compile('^\s*inet addr:(\S+)\s.*$')},
      {"IP Address": re.compile('^\s*inet (\S+)\s.*$')},
      {"IPv6 Address": re.compile('^\s*inet6 addr:\s*(\S+)(\s.*)?$')},
      {"IPv6 Address": re.compile('^\s*inet6 \s*(\S+)(\s.*)?$')}
    ]

  def get(self, host_id):
    host = self.inv.get_by_id(self.get_env(), host_id)
    if not host:
      self.log.error("CliFetchVserviceVnics: host not found: " + host_id)
      return []
    if "host_type" not in host:
      self.log.error("host does not have host_type: " + host_id + \
        ", host: " + str(host))
      return []
    if "Network" not in host["host_type"]:
      return []
    lines = self.run_fetch_lines("ip netns", host_id)
    ret = []
    for l in [l for l in lines if l.startswith("qdhcp") or l.startswith("qrouter")]:
      ret.extend(self.handle_service(host_id, l))
    return ret

  def handle_service(self, host, service):
    cmd = "ip netns exec " + service.strip() + " ifconfig"
    lines = self.run_fetch_lines(cmd, host)
    interfaces = []
    current = None
    for line in lines:
      matches = self.if_header.match(line)
      if matches:
        if current:
          self.set_interface_data(current)
        name = matches.group(1).strip(":")
        # ignore 'lo' interface
        if name == 'lo':
          current = None
        else:
          line_remainder = matches.group(2)
          vservice_id = service
          current = {
            "id": name,
            "type": "vnic",
            "vnic_type": "vservice_vnic",
            "host": host,
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
    for regexp_tuple in self.regexps:
      for re_name in regexp_tuple.keys():
        re_value = regexp_tuple[re_name]
        matches = re_value.match(line)
        if matches:
          matched_value = matches.group(1)
          interface[re_name] = matched_value
    interface["lines"].append(line.strip())

  def set_interface_data(self, interface):
    if not interface:
      return
    interface["data"] = "\n".join(interface.pop("lines", None))

  def add_links(self):
    self.log.info("adding links of type: vservice-vnic")
    vnics = self.inv.find_items({
      "environment": self.get_env(),
      "type": "vnic",
      "vnic_type": "vservice_vnic"
    })
    for v in vnics:
      self.add_link_for_vnic(v)

  def add_link_for_vnic(self, v):
    vservice_id = v["parent_id"]
    vservice_id = vservice_id[:vservice_id.rindex('-')]
    vservice = self.inv.get_by_id(self.get_env(), vservice_id)
    source = vservice["_id"]
    source_id = vservice_id
    target = v["_id"]
    target_id = v["id"]
    link_type = "vservice-vnic"
    # set link name by network name
    # for DHCP, fetch the network ID from the vservice ID
    if source_id.startswith("qdhcp"):
      network_id = source_id[source_id.index('-')+1:]
      network = self.inv.get_by_id(self.get_env(), network_id)
      link_name = network["name"]
    else:
      # for router: match the vNIC IP address to the network gateway IP
      ip_addr = v["IP Address"]
      #gateway_ip = ip_addr[:ip_addr.rindex('.')] + ".1"
      # XXX TBD - we only check for exact equality, missing qg* routers
      gateway_ip = ip_addr
      network = self.inv.get_by_field(self.get_env(), "network", "gateway_ips",
        gateway_ip)
      if not network:
        return
      link_name = network[0]["name"]
    state = "up" # TBD
    link_weight = 0 # TBD
    self.inv.create_link(self.get_env(), v["host"], source, source_id,
      target, target_id, link_type, link_name, state, link_weight)
