import { Inventory } from '/imports/api/inventories/inventories';

export let InventoryTreeNodeBehavior = {
  subscribeGetChildrenFn: function (instance, parent) {
    instance.subscribe('inventory.children',
      parent.id, parent.type, parent.name, parent.environment);
  },

  getChildrenFn: function (parent) {
    let query = {
      $or: [{
        parent_id: parent.id,
        parent_type: parent.type,
        environment: parent.environment,
        show_in_tree: true
      }]
    };

    return Inventory.find(query);
  },

  subscribeGetFirstChildFn: function (instance, parent) {
    instance.subscribe('inventory.first-child', 
      parent.id, parent.type, parent.name, parent.environment);
  },

  hasChildrenFn: function (parent) {
    let query = {
      $or: [
        {
          parent_id: parent._id
        }
      ]
    };

    return Inventory.find(query).count() > 0;
  }
};
