/*
 * Template Component: accordionTreeNode
 */

(function() {
  Template.accordionTreeNode.onCreated(function () {
    var instance = this;
    this.state = new ReactiveDict();
    this.state.setDefault({
      isOpen: false,
    });

    this.autorun(function () {
			// todo: eyaltask: next 
/*
      instance.subscribe("inventory.get-one-child",
        instance.data.treeItem.id);
*/
    });
  });
  
  Template.accordionTreeNode.rendered = function () {
    var instance = this;       
  };

  Template.accordionTreeNode.helpers({
    hasClique: function(){
      var controller = Iron.controller();
      var envName = controller.state.get('envName');

      if(Inventory.find({
        parent_id: this.treeItem.id,
        parent_type: this.treeItem.type,
        environment: envName,
        clique:true,
        show_in_tree:true
      }).count() > 0){

        console.log("clique=True");
        return "true";
      }
      else{
        return "false";
      }

    },

    hasChildren: function(){
      return hasChildren(this);
    },

    isOpen: function () {
      var instance = Template.instance();
      return instance.state.get("isOpen");
    }
  });

  Template.accordionTreeNode.events({
    "click": function(event, instance){
      event.stopPropagation();
      event.preventDefault();

      var isOpen = instance.state.get("isOpen");
			isOpen = ! isOpen;
      instance.state.set("isOpen", isOpen);
			if (isOpen) {
				instance.state.set("needsAnimation", "opening");
			} else {
				instance.state.set("needsAnimatin", "closing");
			}
    },
  });

  function hasChildren(instance) {
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
	
		return hasChildrenQuery(instance.treeItem, envName);
	}

	function hasChildrenQuery(node, envName) {
		return Inventory.find({
      parent_id: node.id,
      parent_type: node.type,
      environment: envName,
      show_in_tree: true
    }).count() > 0;
	}

})();

