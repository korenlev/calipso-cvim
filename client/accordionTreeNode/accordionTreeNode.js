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
      needChildrenClosing: false,
			openedChildId: null,
      showNow: false
    });

    instance.autorun(function () {
      instance.subscribe("inventory.first-child",
        instance.data.treeItem.id);

      if (instance.data.treeItem.clique) {

        if (instance.data.treeItem.id === "aggregate-WebEx-RTP-SSD-Aggregate-node-24") {
          let objId = 'node-24' 
          instance.subscribe("inventory?type+host", "instance", objId);   

        } else {
          let objId = instance.data.treeItem._id._str;
          instance.subscribe("cliques?focal_point", objId);

          Cliques.find({ 
            focal_point: new Mongo.ObjectID(objId) 
          })
          .forEach(
            function (cliqueItem) { 
              instance.subscribe("links?_id-in", cliqueItem.links);

              Links.find({ _id: {$in: cliqueItem.links} })
              .forEach(function(linkItem) {
                let idsList = [ linkItem["source"], linkItem["target"] ]; 
                instance.subscribe("inventory?_id-in", idsList); 

                Inventory.find({ _id: { $in: idsList } })
                .forEach(function (invItem) {
                  instance.subscribe("attributes_for_hover_on_data?type", invItem.type); 
                });
              });
            });
        }
      }
    });

  });
  
  Template.accordionTreeNode.rendered = function () {
    var instance = this;       

    setTimeout(function () {
      instance.state.set("showNow", true);
    }, 50);

		instance.autorun(function () {
			var openState = instance.state.get("openState");	
			switch (openState) {
				case "opening": 
					// Blaze arcitecture bug: in render the children are not it rendered.
					// There for we need to wait until children are rendered to do the animation.
					instance.state.set("openState", "open");
          instance.data.onOpen(instance.data.treeItem.id);
					setTimeout(function () {
						animateOpening(instance.$(instance.firstNode));
					}, 10);
					break;

				case "closing": 

          animateClosing(instance.$(instance.firstNode));
					setTimeout(function () {
            instance.state.set("openState", "close");
            instance.data.onClose(instance.data.treeItem.id);
					}, 200);
					break;

				case "none":
					break;

				default:
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

		createTreeNodeChildrenArgs: function(treeItem, needChildrenClosing) {
			var instance = Template.instance();
			return {
        treeItem: treeItem,
				onClose(childNodeId) {
				}, 
				onOpen(childNodeId) {
					if (singleOpenOption) {
            instance.state.set("openedChildId", childNodeId);
						instance.state.set("needChildrenClosing", true);
            setTimeout(function () { 
              instance.state.set("needChildrenClosing", false);
            }, 10);
					}
				},
        needChildrenClosing: needChildrenClosing,
        openedChildId: instance.state.get("openedChildId")
			};
		},

		isNeedChildrenClosing: function () {
			var instance = Template.instance();
			return instance.state.get("needChildrenClosing");
		},

		closeWhenNeeded: function() {
			var instance = Template.instance();
      var openState = instance.state.get("openState");

      if (! singleOpenOption) { return; }
      if (! instance.data.openedFamilyId) { return; }
      if (openState !== "open") { return; }
      if (instance.data.treeItem.id === instance.data.openedFamilyId) { return; }
			
			instance.state.set("openState", "closing");
		},

    showNow: function () {
			var instance = Template.instance();
      return instance.state.get("showNow");
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

			}

      if (instance.data.treeItem.clique ||
          instance.data.treeItem.id === 
            "aggregate-WebEx-RTP-SSD-Aggregate-node-24") {

				var $element = instance.$(instance.firstNode);
        window.location.href = $element.children("a").attr("href");

        if (instance.data.treeItem.clique) {

          var objId = instance.data.treeItem._id._str;
          // todo: component way, not jquery
          $('.mainContentData').hide();
          $('#dgraphid').show();
          Session.set('currNodeId', objId);

          var graphData = d3Graph.getGraphDataByClique(objId);
          d3Graph.updateNetworkGraph(graphData);

        } else if (instance.data.treeItem.id === 
                     "aggregate-WebEx-RTP-SSD-Aggregate-node-24") {

            $('.mainContentData').hide();
            $('#dgraphid').show();
            Session.set('currNodeId','node-24');
            var graphData = d3Graph.getGraphData('node-24');
            d3Graph.updateNetworkGraph(graphData);
        }

			}
    },
  });

  function hasChildren(instance) {
    var counterName = "inventory.first-child!counter!id=" + instance.treeItem.id;
    return Counts.get(counterName) > 0;

    /*
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
	
		return hasChildrenQuery(instance.treeItem, envName);
    */
	}

	function hasChildrenQuery(node, envName) {
		return Inventory.find({
      parent_id: node.id,
      parent_type: node.type,
      environment: envName,
      show_in_tree: true
    }, {
      limit: 1
    }).count() > 0;
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

