/*
 * Template Component: accordionTreeNode
 */

(function() {
	var subMenuClass = "submenu";
	var switchingSpeed = 200;
	var singleOpenOption = true;

  Template.accordionTreeNode.onCreated(function () {
    var instance = this;
    this.state = new ReactiveDict();
    this.state.setDefault({
			openState: "close",
			openedChildNodeId: null
    });

/*
    this.autorun(function () {
			// todo: eyaltask: next 
      instance.subscribe("inventory.get-one-child",
        instance.data.treeItem.id);

    });
*/

  });
  
  Template.accordionTreeNode.rendered = function () {
    var instance = this;       

		instance.autorun(function () {
			var openState = instance.state.get("openState");	
			switch (openState) {
				case "opening": 
					console.log("opening");
					// Blaze arcitecture bug: in render the children are not it rendered.
					// There for we need to wait until children are rendered to do the animation.
					setTimeout(function () {
						animateOpening(instance.$(instance.firstNode));
						instance.state.set("openState", "open");
						instance.data.onOpen(instance.data.treeItem.id);
					}, 0);
					break;

				case "closing": 
					console.log("closing");
					// Blaze arcitecture bug: in render the children are not it rendered.
					// There for we need to wait until children are rendered to do the animation.
					setTimeout(function () {
						animateClosing(instance.$(instance.firstNode));
						setTimeout(function () {
							instance.state.set("openState", "close");
							instance.data.onClose(instance.data.treeItem.id);
						}, 100);
					}, 0);
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
      return instance.state.get("openState") === "open";
    },

		isOpenOrOpening: function () {
      var instance = Template.instance();
      var openState = instance.state.get("openState");
			return (openState === "open" || openState === "opening");
    },

		isNotClose: function () {
      var instance = Template.instance();
      var openState = instance.state.get("openState");
			return (openState !== "close");
    },

		children: function () {
			return getChildren(this);
		},

		createTreeNodeArgs: function(node, openedChildNodeId) {
			var instance = Template.instance();
			return {
				treeItem: node,
				onClose(childNodeId) {
					console.log("child node on close");
				}, 
				onOpen(childNodeId) {
					console.log("child node on open: " + childNodeId);
					if (singleOpenOption) {
						instance.state.set("openedChildNodeId", childNodeId);
					}
				},
				openedFamilyNodeId: openedChildNodeId
			};
		},

		openedChildNodeId: function () {
			var instance = Template.instance();
			return instance.state.get("openedChildNodeId");
		},

		closeWhenNeeded: function(familyNodeId) {
			var instance = Template.instance();
			console.log("close when needed: ")
			console.log("- family: " + familyNodeId);
			console.log("- node: " + instance.data.treeItem.name_path);

			if (singleOpenOption) {
				if (instance.data.openedFamilyNodeId && 
					instance.data.openedFamilyNodeId !== instance.data.treeItem.id) {
			
					console.log("closin from family: ");
					instance.state.set("openState", "closing");
				}
			}
		}

  });

  Template.accordionTreeNode.events({
    "click": function(event, instance){
      event.stopPropagation();
      event.preventDefault();

      var openState  = instance.state.get("openState");
			var nextState = openState;

			if (hasChildren(instance.data)) {
				switch (openState) {
					case "open":
						nextState = "closing";
						break;
				
					case "opening":	
						break;

					case "close":
						nextState = "opening";
						break;	

					case "closing":
						break;
				}

				instance.state.set("openState", nextState);

			} else { 
				console.log("click on leaf");
				var $element = instance.$(instance.firstNode);
        window.location.href = $element.children("a").attr("href");
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

	function animateClosing($element) {
		$subMenu = $element.children("." + subMenuClass);
		$subMenu.slideUp(switchingSpeed);
	}

})();

