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
    instance.data.setModel(instance.data.key, 
      event.target.value);
    //setModel(instance, event.target.value);
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

  calcValue: function () {
    let instance = Template.instance();
    return getModel(instance);
  }
});

function getModel(instance) {
  let key = instance.data.key;
  let context = instance.data.context;

  if (R.isNil(context)) { return null; }

  return context[key];
}

function setModel(instance, value) {
  /*
  let modelName = instance.data.modelName;
  let context = instance.data.context;

  if (R.isNil(context)) { return null; }

  context[modelName] =  value;
  */

}
