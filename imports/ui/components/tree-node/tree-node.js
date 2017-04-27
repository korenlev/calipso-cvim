/*
 * Template Component: TreeNode
 */

//import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
import { EJSON } from 'meteor/ejson';
//import { ReactiveDict } from 'meteor/reactive-dict';
import { ReactiveVar } from 'meteor/reactive-var';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { InventoryTreeNodeBehavior } from '/imports/ui/lib/inventory-tree-node-behavior';
import * as R from 'ramda';
import { calcColorMem } from '/imports/lib/utilities';

import './tree-node.html';

/*
 * Lifecycles
 */

Template.TreeNode.onCreated(function() {
  let instance = this;
  instance.state = new ReactiveDict();
  instance.state.setDefault({
    node: null,
    openState: 'closed',
    orderDataSubscribe: { counter: 0, data: { node: null, forOpen: false } },
    needOpenCloseAnimation: { counter: 0, data: { type: 'opening', node: null } },
  });

  //console.log('tree-node - on create', R.path(['data', 'node', '_id', '_str'], instance));

  //let oldData = null;

  createAttachedFns(instance);

  instance.currentData = new ReactiveVar(null, EJSON.equals);

  instance.autorun((function(_this) {
    return function(_computation) {
      return _this.currentData.set(Template.currentData());
    };
  })(instance));

  instance.autorun(function () {
    //let data = Template.currentData();
    let data = instance.currentData.get();
    //let data = instance.data;

    new SimpleSchema({
      behavior: {
        type: { isOpenDefault: { type: Boolean } },
        blackbox: true
      },
      showDetailsLine: { type: Boolean },
      openState: { type: String },
      node: { type: Object, blackbox: true },
      children: { type: [Object], blackbox: true },
      childDetected: { type: Boolean },
      level: { type: Number },
      onResetChildren: { type: Function },
      onChildRead: { type: Function },
      onChildrenRead: { type: Function },
      onStartOpenReq: { type: Function },
      onOpeningDone: { type: Function },
      onStartCloseReq: { type: Function },
      onClosingDone: { type: Function },
      onChildDetected: { type: Function },
      onNodeSelected: { type: Function },
    }).validate(data);

    instance.state.set('openState', data.openState);
    instance.state.set('node', data.node);

    //console.log('tree-node - main autorun - ' + data.node._id._str);

    /*
    R.forEach((keyName) => {
      if (R.isNil(oldData)) { return; }

      if (! R.equals(R.prop(keyName, data), R.prop(keyName, oldData)) ) {
        console.log('tree-node - main autorun - prop change: ' + keyName);
          //R.path([keyName], data), R.path([keyName], oldData));
      }
    }, R.keys(data));

    if (oldData !== data) { console.log('tree-node - main autorn - data ob change'); }

    oldData = data;
    */

  });

  instance.autorun(function () {
    let node = instance.state.get('node');
    let openState = instance.state.get('openState');

    switch (openState) {
    case 'start_open':
      issueOrder(instance, 'orderDataSubscribe', { node: node, forOpen: true });
      setTimeout(() => { 
        instance.data.onOpeningDone([node._id._str], node);
      }, 100);
      break;
    case 'opened':
      issueOrder(instance, 'needOpenCloseAnimation', { type: 'opening', node: node});  
      break;
    case 'start_close':
      issueOrder(instance, 'needOpenCloseAnimation', { type: 'closing', node: node });  
      setTimeout(() => {
        instance.data.onClosingDone([node._id._str]);
      }, 200);
      break;
    case 'closed':
      issueOrder(instance, 'orderDataSubscribe', { node: node, forOpen: false });
      break;
    }
  });

  instance.autorun(() => {
    let order = instance.state.get('orderDataSubscribe');
    if (order.counter == 0) { return; }

    instance.data.onResetChildren(R.append(R.path(['_id', '_str'], order.data.node), []));
    // console.log('reset children in autoron order data sub: ' + order.data.node._id._str);

    if (order.data.forOpen) {
      instance.data.behavior.subscribeGetChildrenFn(instance, order.data.node);

      let children = [];
      let onChildReadThrottle = _.throttle(() => {
        instance.data.onChildrenRead([ order.data.node._id._str ], children);
        children = [];
      }, 200);

      instance.data.behavior.getChildrenFn(order.data.node).forEach((child) => {
        // todo: aggregate the collection into threshold and then dispatch. 
        // debounce/throttle
        // https://lodash.com/docs#debounce
        
        //instance.data.onChildRead(
        //  [order.data.node._id._str, child._id._str], child);

        children = R.append(child, children);
        onChildReadThrottle();
      });
    } else {
      instance.data.behavior.subscribeGetFirstChildFn(instance, order.data.node);
      // todo: let childDetectedSubmited = false;
      instance.data.behavior.getChildrenFn(order.data.node).forEach((_child) => {
        instance.data.onChildDetected([order.data.node._id._str]);
      });
    }
  });

});

Template.TreeNode.rendered = function() {
  let instance = Template.instance();
  // Detect change in isOpen.
  instance.autorun(() => {
    let order = instance.state.get('needOpenCloseAnimation');
    if (order.counter == 0) { return; }

    let $childrenList;

    switch(order.data.type) {
    case 'opening':
      // The children list element is not present on first isOpen change render. We
      // need to wait out of loop inorder to let the render first render to list then 
      // we animate the opening/closing action.
      
      //$childrenList = instance.$('>.sm-children-list');
      $childrenList = instance.$(instance.firstNode).children('.sm-children-list');
      $childrenList.slideDown(200);
      break;

    case 'closing':
      //$childrenList = instance.$('>.sm-children-list');
      $childrenList = instance.$(instance.firstNode).children('.sm-children-list');
      $childrenList.slideUp(200);
      break;
    }

  });
};

/*
 * Events
 */

Template.TreeNode.events({
  'click .sm-details-line': function (event, _instance) {
    event.preventDefault();
    event.stopPropagation();

    let data = Template.currentData();

    switch(data.openState) {
    case 'opened':
      R.when(R.pipe(R.isNil, R.not),
        (fn) => fn([data.node._id._str])
      )(data.onStartCloseReq);
      break;

    case 'closed':
      R.when(R.pipe(R.isNil, R.not),
        (fn) => fn([data.node._id._str])
      )(data.onStartOpenReq);
      break;
    }

    data.onNodeSelected(data.node);
  }
});

/*
 * Helpers
 */

Template.TreeNode.helpers({
  argsChild: function (child, _node) {
    let instance = Template.instance();
    //let data = Template.currentData();

    return {
      behavior: InventoryTreeNodeBehavior,
      showDetailsLine: true,
      openState: child.openState,
      node: child.nodeInfo,
      children: child.children,
      childDetected: child.childDetected,
      level: child.level,
      onChildRead: instance._fns.onChildRead,
      onChildrenRead: instance._fns.onChildrenRead,
      onResetChildren: instance._fns.onResetChildren,
      onStartOpenReq: instance._fns.onStartOpenReq,
      onOpeningDone: instance._fns.onOpeningDone,
      onStartCloseReq: instance._fns.onStartCloseReq,
      onClosingDone: instance._fns.onClosingDone,
      onChildDetected: instance._fns.onChildDetected,
      onNodeSelected: instance._fns.onNodeSelected,
    };
  },

  isOpen: function () {
    let instance = Template.instance();
    return R.equals('opened', instance.state.get('openState'));
  },

  calcColor: function (level) {
    return calcColorMem(level);
  },
}); // end: helpers

function issueOrder(instance, name, data) {
  let val = JSON.parse(instance.state.keys[name]);
  val = R.merge(val, {
    counter: val.counter + 1,
    data: data
  });
  
  instance.state.set(name, val);
}

function createAttachedFns(instance) {

  instance._fns = {
    onChildRead: function (reqPath, nodeInfo) {
      instance.data.onChildRead(
        R.prepend(instance.data.node._id._str, reqPath), nodeInfo);
    },
    onChildrenRead: function (reqPath, childrenInfo) {
      instance.data.onChildrenRead(
        R.prepend(instance.data.node._id._str, reqPath), childrenInfo);
    },
    onResetChildren: function (reqPath) {
      instance.data.onResetChildren(
        R.prepend(instance.data.node._id._str, reqPath));
    },
    onStartOpenReq: (reqPath) => {
      instance.data.onStartOpenReq(
        R.prepend(instance.data.node._id._str, reqPath));
    },
    onOpeningDone: (reqPath, nodeInfo) => {
      instance.data.onOpeningDone(
        R.prepend(instance.data.node._id._str, reqPath), nodeInfo);
    },
    onStartCloseReq: (reqPath) => {
      instance.data.onStartCloseReq(
        R.prepend(instance.data.node._id._str, reqPath));
    },
    onClosingDone: (reqPath) => {
      instance.data.onClosingDone(
        R.prepend(instance.data.node._id._str, reqPath));
    },
    onChildDetected: (reqPath) => {
      instance.data.onChildDetected(
        R.prepend(instance.data.node._id._str, reqPath));
    },
    onNodeSelected: (nodeInfo) => {
      instance.data.onNodeSelected(nodeInfo);
    },
  };
}
