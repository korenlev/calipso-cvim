/*
 * Template Component: InputModel
 */

//import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
import * as R from 'ramda';

import './input-model.html';

/*
 * Lifecycles
 */

Template.InputModel.onCreated(function() {
});

/*
Template.InputModel.rendered = function() {
};
*/

/*
 * Events
 */

Template.InputModel.events({
  'input .inputField': function (event, instance) {
    if (instance.data.type === 'checkbox') { return; }

    instance.data.setModel(event.target.value);
  },
  'click .inputField': function (event, instance) {
    if (instance.data.type !== 'checkbox') { return; }

    let element = instance.$('.inputField')[0];
    instance.data.setModel(element.checked);
  }
});

/*
 * Helpers
 */

Template.InputModel.helpers({
  calcAttrs: function () {
    let instance = Template.instance();
    let attrs = {};

    if (instance.data.type === 'checkbox') {
      if (instance.data.value) {
        attrs.checked = true;
      }
    } else {
      attrs.value = instance.data.value;
    }

    return attrs;
  },

  calcType: function () {
    let instance = Template.instance();
    return instance.data.type;
  },

  calcId: function () {
  },

  calcName: function () {
  },

  calcClass: function () {
    let instance = Template.instance();
    if (R.isNil(instance.data.classes)) {
      return 'form-control';
    } else {
      return instance.data.classes;
    }
  },

  calcPlaceholder: function () {
    let instance = Template.instance();
    if (R.isNil(instance.data.placeholder)) { return ''; }

    return instance.data.placeholder;
  },

  markIfDisabled: function () {
    let instance = Template.instance();
    let attrs = {};
    if (instance.data.disabled) {
      attrs = R.assoc('disabled', true, attrs);
    }

    return attrs;
  }
});
