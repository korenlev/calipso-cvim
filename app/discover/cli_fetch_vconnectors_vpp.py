from cli_fetch_vconnectors import CliFetchVconnectors

class CliFetchVconnectorsVpp(CliFetchVconnectors):

  def __init__(self):
    super().__init__()

  def get_vconnectors(self, host):
    lines = self.run_fetch_lines("sudo vppctl show mode", host['id'])
    ret = []
    for l in lines:
      if not l.startswith('l2 bridge'):
        continue
      line_parts = l.split(' ')
      name = line_parts[2]
      bd_id = line_parts[4]
      v = self.get_vconnector(host, name, bd_id)
      ret.append(v)
    return ret

  def get_vconnector(self, host, name, bd_id):
    vconnector = {
      "host": host['id'],
      "id": host['id'] + '-vconnector-' + bd_id,
      "name": "bridge-domain-" + bd_id
    }
    # find vconnector interfaces
    lines = self.run_fetch_lines("sudo vppctl show hardware-int " + name)
    # remove header line
    lines.pop(0)
    interface = None
    vconnector['interfaces'] = []
    for l in lines:
      if not l.strip():
        continue # ignore empty lines
      if not l.startswith(' '):
        if interface:
          vconnector['interfaces'].append(interface)
        line_parts = l.split()
        interface = {
          "name": line_parts[0],
          "hardware": line_parts[3],
          "state": line_parts[2],
          "id": line_parts[1],
        }
      elif l.startswith('  Ethernet address '):
        interface['mac_address'] = l[l.rindex(' ')+1:]
    if interface:
      vconnector['interfaces'].append(interface)

    return vconnector

