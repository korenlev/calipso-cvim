from db_access import DbAccess
from cli_access import CliAccess
from singleton import Singleton
from inventory_mgr import InventoryMgr

import json
import re

class DbFetchVedges(DbAccess, CliAccess, metaclass=Singleton):

  def __init__(self):
    super().__init__()
    self.inv = InventoryMgr()
    self.port_re = re.compile("^\s*port (\d+): ([^(]+)( \(internal\))?$")
    self.port_line_header_prefix = " " * 8 + "Port "

  def get(self, id):
    host_id = id[:id.rindex('-')]
    results = self.get_objects_list_for_id(
      """
        SELECT *
        FROM neutron.agents
        WHERE host = %s AND agent_type = 'Open vSwitch agent'
      """,
      "vedge", host_id)
    vsctl_lines = self.run_fetch_lines("ovs-vsctl show", host_id)
    ports = self.fetch_ports(host_id, vsctl_lines)
    for doc in results:
      doc["name"] = doc["host"] + "-OVS"
      doc["configurations"] = json.loads(doc["configurations"])
      doc["ports"] = ports
      doc["tunnel_ports"] = self.get_overlay_tunnels(doc, vsctl_lines)
    return results

  def fetch_ports(self, host_id, vsctl_lines):
    host = self.inv.get_by_id(self.get_env(), host_id)
    if not host:
      self.log.error("unable to find host in inventory: %s", host_id)
      return {}
    host_types = host["host_type"]
    if "Network" not in host_types and "Compute" not in host_types:
      return {}
    ports = self.fetch_ports_from_dpctl(host_id)
    self.fetch_port_tags_from_vsctl(vsctl_lines, ports)
    return ports

  def fetch_ports_from_dpctl(self, host_id):
    cmd = "ovs-dpctl show"
    lines = self.run_fetch_lines(cmd, host_id)
    ports = {}
    for l in lines:
      port_matches = self.port_re.match(l)
      if not port_matches:
        continue
      port = {}
      id = port_matches.group(1)
      name = port_matches.group(2)
      is_internal = port_matches.group(3) == " (internal)"
      port["internal"] = is_internal
      port["id"] = id
      port["name"] = name
      ports[name] = port
    return ports

  # from ovs-vsctl, fetch tags of ports
  # example format of ovs-vsctl output for a specific port:
  #        Port "tap9f94d28e-7b"
  #            tag: 5
  #            Interface "tap9f94d28e-7b"
  #                type: internal
  def fetch_port_tags_from_vsctl(self, vsctl_lines, ports):
    port = None
    for l in vsctl_lines:
      if l.startswith(self.port_line_header_prefix):
        port = None
        port_name = l[len(self.port_line_header_prefix):]
        # remove quotes from port name
        if '"' in port_name:
          port_name = port_name[1:][:-1]
        if port_name in ports:
          port = ports[port_name]
        continue
      if not port:
        continue
      if l.startswith(" " * 12 + "tag: "):
        port["tag"] = l[l.index(":")+2:]
        ports[port["name"]] = port
    return ports

  def get_overlay_tunnels(self, doc, vsctl_lines):
    if doc["agent_type"] != "Open vSwitch agent":
      return []
    if "tunneling_ip" not in doc["configurations"]:
      return []
    if not doc["configurations"]["tunneling_ip"]:
      return []

    # read the 'br-tun' interface ports
    # this will be used later in the OTEP
    tunnel_bridge_header = " " * 4 + "Bridge br-tun"
    try:
      br_tun_loc = vsctl_lines.index(tunnel_bridge_header)
    except ValueError:
      return []
    lines = vsctl_lines[br_tun_loc+1:]
    tunnel_ports = {}
    port = None
    for l in lines:
      # if we have only 4 or less spaces in the beginng,
      # the br-tun section ended so return
      if not l.startswith(" " * 5):
        break
      if l.startswith(self.port_line_header_prefix):
        if port:
          tunnel_ports[port["name"]] = port
        name = l[len(self.port_line_header_prefix):].strip('" ')
        port = {"name": name}
      elif port and l.startswith(" " * 12 + "Interface "):
        interface = l[10 + len("Interface ")+1:].strip('" ')
        port["interface"] = interface
      elif port and l.startswith(" " * 16):
        colon_pos = l.index(":")
        attr = l[:colon_pos].strip()
        val = l[colon_pos+2:].strip('" ')
        if attr == "options":
          opts = val.strip('{}')
          val = {}
          for opt in opts.split(", "):
            opt_name = opt[:opt.index("=")]
            opt_val = opt[opt.index("=")+1:].strip('" ')
            val[opt_name] = opt_val
        port[attr] = val
    if port:
      tunnel_ports[port["name"]] = port
    return tunnel_ports

  def add_links(self):
    self.log.info("adding link types: vnic-vedge, vconnector-vedge, vedge-pnic")
    vedges = self.inv.find_items({
      "environment": self.get_env(),
      "type": "vedge"
    })
    for vedge in vedges:
      ports = vedge["ports"]
      for p in ports.values():
        self.add_link_for_vedge(vedge, p)

  def add_link_for_vedge(self, vedge, port):
    vnic = self.inv.get_by_id(self.get_env(), port["name"])
    if not vnic:
      self.find_matching_vconnector(vedge, port)
      self.find_matching_pnic(vedge, port)
      return
    source = vnic["_id"]
    source_id = vnic["id"]
    target = vedge["_id"]
    target_id = vedge["id"]
    link_type = "vnic-vedge"
    link_name = vnic["name"] + "-" + vedge["name"]
    if "tag" in port:
      link_name += "-" + port["tag"]
    state = "up" # TBD
    link_weight = 0 # TBD
    source_label = vnic["mac_address"]
    target_label = port["id"]
    self.inv.create_link(self.get_env(), vedge["host"],
      source, source_id, target, target_id,
      link_type, link_name, state, link_weight, source_label, target_label)

  def find_matching_vconnector(self, vedge, port):
    if not port["name"].startswith("qv"):
      return
    base_id = port["name"][3:]
    vconnector_interface_name = "qvb" + base_id
    vconnector = self.inv.get_by_field(self.get_env(), "vconnector",
      "interfaces", vconnector_interface_name)
    if not vconnector:
      return
    vconnector = vconnector[0]
    source = vconnector["_id"]
    source_id = vconnector["id"]
    target = vedge["_id"]
    target_id = vedge["id"]
    link_type = "vconnector-vedge"
    link_name = "port-" + port["id"]
    if "tag" in port:
      link_name += "-" + port["tag"]
    state = "up" # TBD
    link_weight = 0 # TBD
    source_label = vconnector_interface_name
    target_label = port["name"]
    self.inv.create_link(self.get_env(), vedge["host"],
      source, source_id, target, target_id,
      link_type, link_name, state, link_weight, source_label, target_label)

  def find_matching_pnic(self, vedge, port):
    if not port["name"].startswith("eth") and not port["name"].startswith("eno"):
      return
    pnic = self.inv.find_items({
      "environment": self.get_env(),
      "type": "pnic",
      "host": vedge["host"],
      "name": port["name"]
    })
    if not pnic:
      return
    pnic = pnic[0]
    source = vedge["_id"]
    source_id = vedge["id"]
    target = pnic["_id"]
    target_id = pnic["id"]
    link_type = "vedge-pnic"
    link_name = "Port-" + port["id"]
    state = "up" if pnic["Link detected"] == "yes" else "down"
    link_weight = 0 # TBD
    self.inv.create_link(self.get_env(), vedge["host"],
      source, source_id, target, target_id,
      link_type, link_name, state, link_weight)

