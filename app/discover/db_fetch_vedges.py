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
      self.get_overlay_tunnels(doc, vsctl_lines)
    return results

  def fetch_ports(self, host_id, vsctl_lines):
    host = self.inv.get_by_id(self.get_env(), host_id)
    host_types = host["host_type"]
    if "Network" not in host_types and "Compute" not in host_types:
      return []
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
    port_line_header_prefix = " " * 8 + "Port "
    port = None
    for l in vsctl_lines:
      if l.startswith(port_line_header_prefix):
        port = None
        port_name = l[len(port_line_header_prefix):]
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
      return

    conf = doc["configurations"]
    if not conf ["tunneling_ip"] or not conf["tunnel_types"]:
      self.overlay_tunnels_null(doc)
    else:
      self.overlay_tunnels_extract(doc, vsctl_lines)

  def overlay_tunnels_null(self, doc):
    if "bridge_mappings" not in doc["configurations"]:
      return
    bridge_mappings = doc["configurations"]["bridge_mappings"]
    for bridge in bridge_mappings.values():
      self.find_vedge_ovs_tunnel_pnics_for_bridge(doc, bridge)

  # on every host in the environment, run "ovs-vsctl list-ifaces " + bridge
  def find_vedge_ovs_tunnel_pnics_for_bridge(self, doc, bridge):
    cmd = "ovs-vsctl list-ifaces " + bridge
    host = doc["host"]
    lines = self.run_fetch_lines(cmd, host)
    # output we're looking for looks like this:
    # br-prv--br-eth0
    # i.e. <bridge>--br-<interface>
    # we need the interface name to look for the pNIC
    interfaces = [l[l.index("--br-")+1:] for l in lines]
    for iname in interfaces:
      matches = self.inv.find_items({
        "environment": self.get_env(),
        "type": "pnic",
        "host": host,
        "local_name": iname
      })
      if not matches:
        continue
      for pnic in matches:
        self.log.info("found pnic for bridge: " + bridge +
          ", pnic local_name: " + iname)
      # found a matching pnic - create its vedge-pnic and pnic-network links
      # document, and later skip creating them in add_links

      # If any pNIC name exists in the list output
      # then we have that specific vedge-pnic and pnic-network links
      # (excluding all others!)

  def overlay_tunnels_extract(self, doc, vsctl_lines):
    # Read the 'tunneling_ip' IP address
    conf = doc["configurations"]
    if "tunneling_ip" not in conf:
      return
    tunneling_ip = conf["tunneling_ip"]
    # Use this ip address to find the associated vedge port from 'ovs-vsctl show'
    # For example 'local_ip="192.168.2.2"'
    #  Add that port to the vEdge list of ports.
    #  For example:
    #  Port "vxlan-c0a80203" on node-4 in Mirantis-Liberty
    #  run ifconfig | grep -B 2 192.168.2.2 on that host
    # to find the pNIC making these tunnels
    # if that is br-[] or []-br type of pNIC make further command:
    #   "brctl show juju-br0" (in thundercloud) - to find the associated pNIC (under interfaces) - eth6
    #   "brctl show br-mesh" (in Mirantis-Liberty) - to find the associated pNIC (under interfaces) - eno33554952.103
    pass


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

