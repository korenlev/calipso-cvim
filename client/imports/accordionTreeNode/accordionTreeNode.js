/*
 * Template Component: accordionTreeNode
 */

/* eslint no-undef: off */

import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';

//import { store } from '/client/imports/store';
//import { setCurrentNode } from '/client/imports/actions/navigation';
import '/client/imports/accordionTreeNodeChildren/accordionTreeNodeChildren';
import './accordionTreeNode.html';

var subMenuClass = 'submenu';
var switchingSpeed = 200;

Template.accordionTreeNode.onCreated(function () {
  var instance = this;
  this.state = new ReactiveDict();
  this.state.setDefault({
    openState: 'close',
    needChildrenClosing: false,
    openedChildId: null,
    showNow: false,
    startAsClickedState: 'not_done'
  });

  instance.autorun(function () {
    instance.subscribe('inventory.first-child',
      instance.data.node.id);

    if (instance.data.node.clique) {

      if (instance.data.node.id === 'aggregate-WebEx-RTP-SSD-Aggregate-node-24') {
        let objId = 'node-24';
        instance.subscribe('inventory?type+host', 'instance', objId);   

      } else {
        let objId = instance.data.node._id._str;
        instance.subscribe('cliques?focal_point', objId);

        Cliques.find({ 
          focal_point: new Mongo.ObjectID(objId) 
        })
        .forEach(
          function (cliqueItem) { 
            instance.subscribe('links?_id-in', cliqueItem.links);

            Links.find({ _id: {$in: cliqueItem.links} })
            .forEach(function(linkItem) {
              let idsList = [ linkItem['source'], linkItem['target'] ]; 
              instance.subscribe('inventory?_id-in', idsList); 

              Inventory.find({ _id: { $in: idsList } })
              .forEach(function (invItem) {
                instance.subscribe('attributes_for_hover_on_data?type', invItem.type); 
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
    instance.state.set('showNow', true);
  }, 50);

  instance.autorun(function () {
    var openState = instance.state.get('openState');	
    switch (openState) {
    case 'opening': 
      // Blaze arcitecture bug: in render the children are not it rendered.
      // There for we need to wait until children are rendered to do the animation.
      instance.state.set('openState', 'open');
      activateNodeAction(instance);
      setTimeout(function () {
        animateOpening(instance.$(instance.firstNode));
      }, 10);
      break;

    case 'closing': 

      animateClosing(instance.$(instance.firstNode));
      setTimeout(function () {
        instance.state.set('openState', 'close');
        //instance.data.onClose(instance.data.node.id);
      }, 200);
      break;

    case 'none':
      break;

    default:
      break;
    }
  });

};

Template.accordionTreeNode.helpers({
  reactOnShowOpen: function (showOpen) {
    let instance = Template.instance();
    let openState = instance.state.get('openState');
    let nextOpenState = null;
    
    if (showOpen === false) {
      if (openState === 'open' || 
          openState === 'opening') {
        nextOpenState = 'closing';
      } 
    } else if (showOpen === true) {
      if (openState === 'close' || 
          openState === 'closing') {
        nextOpenState = 'opening';
      }
    }

    if (nextOpenState) {
      setTimeout(function () {
        instance.state.set('openState', nextOpenState);
      }, 10);
    }
  },

  isNot: function (condition) {
    return ! condition;
  },

  isNotClose: function () {
    var instance = Template.instance();
    var openState = instance.state.get('openState');
    return (openState !== 'close');
  },

  hasClique: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');

    if(Inventory.find({
      parent_id: this.node.id,
      parent_type: this.node.type,
      environment: envName,
      clique:true,
      show_in_tree:true
    }).count() > 0){

      return 'true';
    }
    else{
      return 'false';
    }

  },

  hasChildren: function(){
    return hasChildren(this);
  },

  isOpen: function () {
    var instance = Template.instance();
    return instance.state.get('openState') === 'open';
  },

  isOpenOrOpening: function () {
    var instance = Template.instance();
    var openState = instance.state.get('openState');
    return (openState === 'open' || openState === 'opening');
  },

  createChildrenArgs: function(
    parentNode, 
    selectedNode
    ) {

    let instance = Template.instance();
    return {
      node: parentNode,
      selectedNode: selectedNode,
      onClick(childNode) {
        // todo: remove console
        console.log('on click fron child node');
        console.log(childNode);

        instance.data.onClick(childNode);
      },
    };
  },

  isNeedChildrenClosing: function () {
    var instance = Template.instance();
    return instance.state.get('needChildrenClosing');
  },

  closeWhenNeeded: function() {
    var instance = Template.instance();
    var openState = instance.state.get('openState');

    if (! singleOpenOption) { return; }
    if (! instance.data.openedFamilyId) { return; }
    if (openState !== 'open') { return; }
    if (instance.data.node.id === instance.data.openedFamilyId) { return; }
    
    instance.state.set('openState', 'closing');
  },

  showNow: function () {
    var instance = Template.instance();
    return instance.state.get('showNow');
  },
});

Template.accordionTreeNode.events({
  'click': function(event, instance){
    event.stopPropagation();
    event.preventDefault();

    instance.data.onClick(instance.data.node);

    /*
     * todo : remove code
    store.dispatch(setCurrentNode(
      instance.data.node.id_path,
      instance.data.node.name_path));

    var openState  = instance.state.get('openState');
    var nextState = openState;

    if (hasChildren(instance.data)) {
      switch (openState) {
      case 'open':
        nextState = 'closing';
        break;
    
      case 'opening':	
        break;

      case 'close':
        nextState = 'opening';
        break;	

      case 'closing':
        break;
      }

      instance.state.set('openState', nextState);

    }

    
    */
  },
});

function activateNodeAction (instance) {
  if (instance.data.node.clique ||
      instance.data.node.id === 
        'aggregate-WebEx-RTP-SSD-Aggregate-node-24') {

    var $element = instance.$(instance.firstNode);
    window.location.href = $element.children('a').attr('href');

    if (instance.data.node.clique) {

      var objId = instance.data.node._id._str;
      // todo: component way, not jquery
      $('.mainContentData').hide();
      $('#dgraphid').show();
      Session.set('currNodeId', objId);

      let graphData = d3Graph.getGraphDataByClique(objId);
      d3Graph.updateNetworkGraph(graphData);

    } else if (instance.data.node.id === 
                 'aggregate-WebEx-RTP-SSD-Aggregate-node-24') {

      $('.mainContentData').hide();
      $('#dgraphid').show();
      Session.set('currNodeId','node-24');
      let graphData = d3Graph.getGraphData('node-24');
      d3Graph.updateNetworkGraph(graphData);
    }
  }
}

function hasChildren(instance) {
  var counterName = 'inventory.first-child!counter!id=' + instance.node.id;
  return Counts.get(counterName) > 0;

  /*
  var controller = Iron.controller();
  var envName = controller.state.get('envName');

  return hasChildrenQuery(instance.node, envName);
  */
}

/*
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
*/

function animateOpening($element) {
  $subMenu = $element.children('.' + subMenuClass);
  $subMenu.slideDown(switchingSpeed);
}

function animateClosing($element) {
  $subMenu = $element.children('.' + subMenuClass);
  $subMenu.slideUp(switchingSpeed);
}
