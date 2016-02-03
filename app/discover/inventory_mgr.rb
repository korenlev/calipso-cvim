require 'singleton'
require_relative 'mongo_access'
require_relative 'util'

class InventoryMgr < MongoAccess
  include Singleton
  include Util
  
  @@prettify = false
  
  def get(environment, item_type, item_id)
    matches = item_id && (item_id.to_s > "") ?
      @@client[:inventory].find(:environment => environment, :type => item_type, :id => item_id) :
      @@client[:inventory].find(:environment => environment, :type => item_type)
    return matches
  end
  
  def get_children(environment, item_type, parent_id)
    matches = []
    if parent_id && (parent_id.to_s > "")
      matches = @@client[:inventory].find({:environment => environment, :type => item_type, :parent_id => parent_id})
    else
      matches = @@client[:inventory].find({:environment => environment, :type => item_type})
    end
    return matches
  end
  
  def getSingle(environment, item_type, item_id)
    matches = @@client[:configuration].find(:environment => environment,
      :type => item_type, :id => item_id)
    if (matches.count() == 0)
      raise IndexError, "No matches for item: type=" + item_type + ", id=" + item_id
    elsif (matches.count() > 1)
      raise IndexError, "Found multiple matches for item: type=" + item_type + ", id=" + item_id
    else
      matches.each {|e| return e }
    end
  end
  
  # item must contain properties 'environment', 'type' and 'id'
  def set(item)
    # convert all keys to be symbols
    symbolize_keys_deep!(item)
    # make sure we have environment, type & id
    check(item[:environment], "environment")
    check(item[:type], "type")
    check(item[:id], "id")
    curr_item_matches = get(item[:environment], item[:type], item[:id])
    if curr_item_matches.count() > 0
      update(curr_item_matches, item)
    else
      @@client[:inventory].insert_one(item)
    end
  end
  
  def update(curr_item_matches, item)
    curr_item = curr_item_matches.first
    @@client[:inventory].find_one_and_update({_id: curr_item[:_id]}, {"$set" => item})
  end
  
  def check(arg, field_name)
    if arg == nil || arg.to_s.rstrip.empty?
      raise ArgumentError,
        "Inventory item - the following field is not defined: " + field_name
    end
    #code
  end
  
end
