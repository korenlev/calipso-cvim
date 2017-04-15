/*
 * Template Component: TreeNode
 */

//import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { InventoryTreeNodeBehavior } from '/imports/ui/lib/inventory-tree-node-behavior';
import * as R from 'ramda';

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

  instance.autorun(function () {
    let data = Template.currentData();

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
      onStartOpenReq: { type: Function },
      onOpeningDone: { type: Function },
      onStartCloseReq: { type: Function },
      onClosingDone: { type: Function },
      onChildDetected: { type: Function },
    }).validate(data);

    instance.state.set('openState', data.openState);
    instance.state.set('node', data.node);
  });

  instance.autorun(function () {
    let node = instance.state.get('node');
    let openState = instance.state.get('openState');

    switch (openState) {
    case 'start_open':
      issueOrder(instance, 'orderDataSubscribe', { node: node, forOpen: true });
      setTimeout(() => { 
        instance.data.onOpeningDone([node._id._str]);
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

    if (order.data.forOpen) {
      instance.data.behavior.subscribeGetChildrenFn(instance, order.data.node);

      instance.data.behavior.getChildrenFn(order.data.node).forEach((child) => {
        // todo: aggregate the collection into threshold and then dispatch. 
        // debounce/throttle
        // https://lodash.com/docs#debounce
        instance.data.onChildRead(
          [order.data.node._id._str, child._id._str], child);
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
  }
});

/*
 * Helpers
 */

Template.TreeNode.helpers({
  argsChild: function (child, node) {
    //let instance = Template.instance();
    let data = Template.currentData();

    return {
      behavior: InventoryTreeNodeBehavior,
      showDetailsLine: true,
      openState: child.openState,
      node: child.nodeInfo,
      children: child.children,
      childDetected: child.childDetected,
      level: child.level,
      onChildRead: function (reqPath, nodeInfo) {
        data.onChildRead(R.prepend(node._id._str, reqPath), nodeInfo);
      },
      onResetChildren: function (reqPath) {
        data.onResetChildren(R.prepend(node._id._str, reqPath));
      },
      onStartOpenReq: (reqPath) => {
        data.onStartOpenReq(R.prepend(node._id._str, reqPath));
      },
      onOpeningDone: (reqPath) => {
        data.onOpeningDone(R.prepend(node._id._str, reqPath));
      },
      onStartCloseReq: (reqPath) => {
        data.onStartCloseReq(R.prepend(node._id._str, reqPath));
      },
      onClosingDone: (reqPath) => {
        data.onClosingDone(R.prepend(node._id._str, reqPath));
      },
      onChildDetected: (reqPath) => {
        data.onChildDetected(R.prepend(node._id._str, reqPath));
      },
    };
  },

  isOpen: function () {
    let instance = Template.instance();
    return R.equals('opened', instance.state.get('openState'));
  },

  calcColor: function (level) {
    let r = 11;
    let g = 122;
    let b = 209;
    //let a = 1;
    let factor = level / 15;
    factor = factor < 0 ? 0 : 1 - factor;

    let nR = Math.floor(r * factor);
    let nG = Math.floor(g * factor);
    let nB = Math.floor(b * factor);
    //let nA = a;
    let colorStr = R.reduce((acc, colorPart) => { 
      let digits =  colorPart.toString(16); 
      if (colorPart < 16) { digits = '0' + digits; }
      return acc + digits;
    }, '#', [nR, nG, nB]); 
    
    return colorStr;
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
