/*
 * Template Component: accordionNavMenuTree
 */

(function () {

/*
 * Lifecycle methods
 */

Template.accordionNavMenuTree.onCreated(function () {
  let instance = this;

  instance.autorun(function () {
    let controller = Iron.controller();
    let envName = controller.state.get('envName');

    instance.subscribe("inventory.children", envName);
  });
});

/*
Template.accordionNavMenuTree.onCreated(function() {
  var controller = Iron.controller();
  var envName = controller.state.get('envName');
  Meteor.subscribe('inventoryByEnv',envName);
});
*/

/*
Template.accordionNavMenuTree.onCreated(function() {
  var self = this;
  self.autorun(function() {
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    self.subscribe('inventoryByEnvTest', envName);
  });
});
*/

/*
 * Helpers
 */

Template.accordionNavMenuTree.helpers({
  treeItems: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    return Inventory.find({
      environment: envName,
      parent_id: envName,
      show_in_tree:true
    });
  },

  /*
  getNodeItems: function(nodeId){
    //console.log(nodeId);
    //console.log(Inventory.find({parent_id: nodeId}));
    return Inventory.find({parent_id: nodeId});
  },
  */

  createTreeNodeArgs: function(node) {
    var instance = Template.instance();
    return {
      treeItem: node,
      onClose(childNode) {
        console.log("child node on close");
      },
      onOpen(childNode) {
        console.log("child node on open");
      }
    };
  }
});

})();
