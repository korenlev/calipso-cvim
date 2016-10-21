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
    let selectedValues = R.map(function (optionEl) {
      return optionEl.value;
    }, event.target.selectedOptions);

    selectedValues = instance.data.multi ? selectedValues : 
      selectedValues[0];
    instance.data.setModel(instance.data.key, selectedValues);
    //setModel(instance, event.target.value);
  }
});
   
/*  
 * Helpers
 */

Template.SelectModel.helpers({    
  isSelected: function (optionValue) {
    let instance = Template.instance();
    let key = instance.data.key;
    let context = instance.data.context;
    if (R.isNil(context)) { return false; }

    return context[key] === optionValue;
  },
});


