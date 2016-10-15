/*
 * Template Component: breadcrumb
 */

import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';

import { store } from '/client/imports/store';
import '/client/imports/breadcrumbNode/breadcrumbNode';
import './breadcrumb.html';

Template.breadcrumb.onCreated(function () {
  let instance = this;
  instance.state = new ReactiveDict();

  instance.storeUnsubscribe = store.subscribe(() => {
    instance.state.set('nodeItemList', store.getState());   
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
  }
});
