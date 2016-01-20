module Util
  
  def symbolize_keys_deep!(h)
    h.keys.each do |k|
      ks = k.to_sym
      h[ks] = h.delete k
      symbolize_keys_deep! h[ks] if h[ks].kind_of? Hash
    end
  end
  
  
  def set_prettify(pretty)
    @@prettify = pretty
  end
  
  def jsonify(object)
    object_class = object.class.name
    case
    when object_class == "Mongo::Collection::View"
      matches = []
      object.each {|e| matches.push(e)}
      object = matches
    end
    
    return @prettify != false ? JSON.pretty_generate(object) :
      JSON.generate(object)
  end
  
end
