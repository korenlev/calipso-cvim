/*
 * Template Component: SelectModel 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import * as R from 'ramda';
//import { ReactiveDict } from 'meteor/reactive-dict';
        
import './select-model.html';     
    
/*  
 * Lifecycles
 */   
  
Template.SelectModel.onCreated(function() {
});  

/*
Template.SelectModel.rendered = function() {
};  
*/

/*
 * Events
 */

Template.SelectModel.events({
  'change .js-select': function (event) {
    event.stopPropagation();
    event.preventDefault();

    let instance = Template.instance();
    // Extract string values from select element's attribute.
    let elementSelectedValues = R.map(function (optionEl) {
      return optionEl.value;
    }, event.target.selectedOptions);

    let selectedValues = instance.data.multi ? elementSelectedValues : 
      elementSelectedValues[0];

    if (instance.data.setModel) {
      instance.data.setModel(selectedValues);
    }
  }
});
   
/*  
 * Helpers
 */

Template.SelectModel.helpers({    
  isSelected: function (optionValue) {
    let instance = Template.instance();
    let selectedValues = instance.data.values;

    if (R.isNil(selectedValues)) { return false; }
    return R.contains(optionValue, selectedValues);
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


