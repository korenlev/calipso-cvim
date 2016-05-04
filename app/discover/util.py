import json

class Util(object):
  
  prettify = False
  
  def __init__(self):
    super().__init__()

  def set_prettify(self, prettify):
    self.prettify = prettify
    
  def get_prettify(self):
    return self.prettify
  
  def jsonify(self, obj):
    if self.prettify:
      ret = json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    else:
      ret = json.dumps(obj)
    return ret
