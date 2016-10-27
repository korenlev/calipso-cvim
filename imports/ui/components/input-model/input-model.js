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
  'input .inputField': function (event) {
    let instance = Template.instance();
    instance.data.setModel(event.target.value);
  }
});
   
/*  
 * Helpers
 */

Template.InputModel.helpers({    
  calcType: function () {
  },

  calcId: function () {
  },

  calcName: function () {
  },

  calcClass: function () {
    return 'form-control';
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
