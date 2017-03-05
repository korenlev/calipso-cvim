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
  this.state = new ReactiveDict();
  this.state.setDefault({
    data: null,
  });

  instance.autorun(function () {
    //var tempData = instance.state.get('data');
    //var node = instance.data.node;
    instance.subscribe('inventory.children',
      instance.data.node.id);
  });

});

Template.accordionTreeNodeChildren.helpers({
  reactOnNewData: function (node) {
    let instance = Template.instance();
    instance.state.set('data', { node: node });
  },

  children: function () {
    var instance = Template.instance();
    var controller = Iron.controller();
    var envName = controller.state.get('envName');

    return getChildrenQuery(instance.data.node, envName);
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

/*
function getChildren(instance) {
  var controller = Iron.controller();
  var envName = controller.state.get('envName');

  return getChildrenQuery(instance.node, envName);
}
*/

function getChildrenQuery(node, envName) {
  let query = 
    {
      $or: [
        {
          parent_id: node.id,
          parent_type: node.type,
          environment: envName,
          show_in_tree: true
        },
        {
          host_ref: node.id,
          environment: envName,
          show_in_tree: true
        }
      ]
    };

  //console.log('getChildrenQuery', query);
  return Inventory.find(query);
}	
