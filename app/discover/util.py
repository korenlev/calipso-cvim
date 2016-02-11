import json

class Util(object):
  
  prettify = False
  
  def set_prettify(self, prettify):
    self.prettify = prettify
    
  def get_prettify(self):
    return self.prettify
  
  def jsonify(self, obj):
    if self.prettify:
      return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    else:
      return json.dumps(obj)
