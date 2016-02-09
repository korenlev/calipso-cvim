#!/usr/bin/env ruby

# base class for scanners

require_relative 'inventory_mgr'
require_relative 'cli_access'
require_relative 'util'

class Scanner
  include Util
  
  @@inventory = nil
  
  def initialize(types_to_fetch)
    @types_to_fetch = types_to_fetch
    !@@inventory && (@@inventory = InventoryMgr.instance)
  end
  
  def set_env(environment)
    @@environment = environment
  end
  
  def scan(obj, id_field)
    obj && symbolize_keys_deep!(obj)
    @obj_to_scan = obj
    @types_to_fetch.each {|t|
      scan_type(t, obj, id_field)
    }
  end
  
  def scan_type(type_to_fetch, parent, id_field)
    @id = @obj_to_scan ?
      (id_field == "name" ? @obj_to_scan[:name].to_s : @obj_to_scan[:id].to_s) : nil
    if @obj_to_scan && (@id == nil || @id.rstrip.empty?)
      raise ArgumentError, "Object missing " + id_field + " attribute"
    end
    fetcher = type_to_fetch[:fetcher]
    children_scanner = type_to_fetch[:children_scanner]
    escaped_id = @id ? fetcher.escape(@id.to_s) : @id
    db_results = fetcher.get(escaped_id)
    case
    when db_results.class.name == "Hash"
      results = db_results["rows"] || [db_results]
    when db_results.class.name == "Array"
      results = db_results
    end
    child_id_field = type_to_fetch[:object_id_to_use_in_child] || "id"
    results.each {|o|
      o[:environment] = @@environment
      o[:type] ||= type_to_fetch[:type]
      if parent
        o[:parent_id] = parent[:id].to_s
        o[:parent_type] = parent[:type]
      end
      @@inventory.set(o)
      children_scanner && children_scanner.scan(o, child_id_field)
    }
  end
  
end