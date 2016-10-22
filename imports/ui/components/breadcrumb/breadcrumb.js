/*
 * Template Component: breadcrumb
 */

import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';

import { store } from '/client/imports/store';
import { setCurrentNode } from '/client/imports/actions/navigation';

import '../breadcrumbNode/breadcrumbNode';
import './breadcrumb.html';

Template.breadcrumb.onCreated(function () {
  let instance = this;
  instance.state = new ReactiveDict();

  instance.storeUnsubscribe = store.subscribe(() => {
    let lastActionable = store.getState().api.navigation.lastActionable;
    instance.state.set('nodeItemList', lastActionable);   
  });
});

Template.breadcrumb.onDestroyed(function () {
  let instance = this;
  instance.storeUnsubscribe();
  
});

Template.breadcrumb.helpers({
  nodeItemList: function () {
    let instance = Template.instance();
    return instance.state.get('nodeItemList');
  },

  createNodeArgs: function (node) {
    //let instance = Template.instance();

    return {
      node: node,
      onClick: function () {
        store.dispatch(setCurrentNode({
          id_path: node.fullIdPath,
          name_path: node.fullNamePath
        }));
      }
    };
  },
});
