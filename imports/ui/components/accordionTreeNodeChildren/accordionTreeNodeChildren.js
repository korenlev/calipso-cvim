/*
 * Template Component: accordionTreeNodeChildren
 */

/* eslint no-undef: off */

import * as R from 'ramda';
import { Template } from 'meteor/templating';

import { Inventory } from '/imports/api/inventories/inventories';

import './accordionTreeNodeChildren.html';

Template.accordionTreeNodeChildren.onCreated(function () {
  var instance = this;

  this.autorun(function () {
    instance.subscribe('inventory.children',
      instance.data.node.id);
  });

});

Template.accordionTreeNodeChildren.helpers({
  children: function () {
    return getChildren(this);
  },

  createTreeNodeArgs: function(
    node,
    selectedNode
    ) {

    var instance = Template.instance();

    let firstChild = null;
    let restOfChildren = null;  
    let showOpen = false;

    if ((! R.isNil(selectedNode)) &&
          selectedNode.length > 0
    ) {
      firstChild = selectedNode[0];
      restOfChildren = selectedNode.length > 1 ? 
        R.slice(1, Infinity, selectedNode) : null;
      showOpen = firstChild.id === node.id ? true : false;
    }

    return {
      node: node,
      showOpen: showOpen,
      selectedNode: restOfChildren,
      onClick: instance.data.onClick
    };
  },


});

Template.accordionTreeNodeChildren.events({
});

function getChildren(instance) {
  var controller = Iron.controller();
  var envName = controller.state.get('envName');

  return getChildrenQuery(instance.node, envName);
}

function getChildrenQuery(node, envName) {
  return Inventory.find({
    parent_id: node.id,
    parent_type: node.type,
    environment: envName,
    show_in_tree: true
  });
}	
