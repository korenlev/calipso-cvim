/*
 * Template Component: breadcrumbNode
 */

import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';

import './breadcrumbNode.html';

Template.breadcrumbNode.onCreated(function () {
  let instance = this;
  instance.state = new ReactiveDict();

  instance.autorun(function () {
    let data = Template.currentData();
    new SimpleSchema({
      node: { type: Object, blackbox: true },
      onClick: { type: Function },
    }).validate(data);
  });

});

Template.breadcrumbNode.helpers({
});

Template.breadcrumbNode.events({
  'click': function(event, instance) {
    event.stopPropagation();
    event.preventDefault();
    
    instance.data.onClick();
  }
});
