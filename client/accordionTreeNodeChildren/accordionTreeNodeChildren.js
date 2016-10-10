/*
 * Template Component: accordionTreeNodeChildren
 */

(function() {
  Template.accordionTreeNodeChildren.onCreated(function () {
    var instance = this;

    this.autorun(function () {
      instance.subscribe("inventory.children",
        instance.data.treeItem.id);
    });

  });

  Template.accordionTreeNodeChildren.helpers({
		children: function () {
			return getChildren(this);
		},

		createTreeNodeArgs: function(node, needChildrenClosing, childNodeRequested) {

			var instance = Template.instance();

      var firstChildRequested = null
      var nextChildNodeRequested = null;  

      if (childNodeRequested && childNodeRequested.length > 0) {
        // todo: remove console
        console.log("childnode requested: " + childNodeRequested.toString());
        firstChildRequested = childNodeRequested[0];
        nextChildNodeRequested = childNodeRequested.slice(1);
      }

			return {
				treeItem: node,
        onClose: instance.data.onClose,
        onOpen: instance.data.onOpen,
        needClosing: needChildrenClosing,
        childNodeRequested: 
          (firstChildRequested === node.id) ? 
            nextChildNodeRequested : null,
        startAsClicked: 
          (firstChildRequested === node.id) ? true : false,
				openedFamilyId: instance.data.openedChildId
			};
		},


  });

  Template.accordionTreeNodeChildren.events({
  });

	function getChildren(instance) {
    var controller = Iron.controller();
    var envName = controller.state.get('envName');

		return getChildrenQuery(instance.treeItem, envName);
	}

	function getChildrenQuery(node, envName) {
		return Inventory.find({
			parent_id: node.id,
			parent_type: node.type,
			environment: envName,
			show_in_tree: true
		});
	}	

})();

