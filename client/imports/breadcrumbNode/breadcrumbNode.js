/*
 * Template Component: breadcrumbNode
 */

import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';

import './breadcrumbNode.html';

Template.breadcrumbNode.onCreated(function () {
  let instance = this;
  instance.state = new ReactiveDict();
});

Template.breadcrumbNode.helpers({
  nodeItemList: function () {
    let instance = Template.instance();
    return instance.state.get('nodeItemList');
  }
});
Template.breadcrumbNode.events({
  'click': function(event, instance) {
    event.stopPropagation();
    event.preventDefault();
    
    instance.data.onClick();
  }
});
