/*
 * Template Component: GraphTooltipWindow 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
        
import './graph-tooltip-window.html';     
    
/*  
 * Lifecycles
 */   
  
Template.GraphTooltipWindow.onCreated(function() {
  let instance = this;

  instance.autorun(() => {
    new SimpleSchema({
      label: { type: String },
      title: { type: String },
      left: { type: Number },
      top: { type: Number },
      show: { type: Boolean }
    }).validate(Template.currentData());
  });
});  

/*
Template.GraphTooltipWindow.rendered = function() {
};  
*/

/*
 * Events
 */

Template.GraphTooltipWindow.events({
});
   
/*  
 * Helpers
 */

Template.GraphTooltipWindow.helpers({    
});


