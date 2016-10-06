/*
 * Template Component: accordionTreeNode
 */

(function() {
	var subMenuClass = "submenu";
	var switchingSpeed = 200;

  Template.accordionTreeNode.onCreated(function () {
    var instance = this;
    this.state = new ReactiveDict();
    this.state.setDefault({
      isOpen: false,
			needsAnimation: "none"
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

		instance.autorun(function () {
			var needsAnimation = instance.state.get("needsAnimation");	
			switch (needsAnimation) {
				case "opening": 
					console.log("opening");
					// Blaze arcitecture bug: in render the children are not it rendered.
					// There for we need to wait until children are rendered to do the animation.
					setTimeout(function () {
						animateOpening(instance.$(instance.firstNode));
						instance.state.set("needsAnimation", "none");
					}, 0);
					break;

				case "closing": 
					console.log("closing");
					instance.state.set("needsAnimation", "none");
					break;

				case "none":
					console.log("no animation");
					break;

				default:
					console.log("default: no animation");
					break;
			}
		});
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
    },

		children: function () {
			return getChildren(this);
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
				instance.state.set("needsAnimation", "closing");
			}
    },
  });

  function hasChildren(instance) {
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
	
		return hasChildrenQuery(instance.treeItem, envName);
	}

	function getChildren(instance) {
    var controller = Iron.controller();
    var envName = controller.state.get('envName');

		return getChildrenQuery(instance.treeItem, envName);
	}

	function hasChildrenQuery(node, envName) {
		return Inventory.find({
      parent_id: node.id,
      parent_type: node.type,
      environment: envName,
      show_in_tree: true
    }).count() > 0;
	}

	function getChildrenQuery(node, envName) {
		return Inventory.find({
			parent_id: node.id,
			parent_type: node.type,
			environment: envName,
			show_in_tree: true
		});
	}	

	function animateOpening($element) {
		$subMenu = $element.children("." + subMenuClass);
		$subMenu.slideDown(switchingSpeed);
	}

})();

