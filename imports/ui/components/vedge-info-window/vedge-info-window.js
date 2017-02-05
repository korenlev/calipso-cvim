/*
 * Template Component: VedgeInfoWindow 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
        
import './vedge-info-window.html';     
    
/*  
 * Lifecycles
 */   
  
Template.VedgeInfoWindow.onCreated(function() {
  let instance = this;

  instance.autorun(() => {
    new SimpleSchema({
      node: { type: Object, blackbox: true },
      left: { type: Number },
      top: { type: Number },
      show: { type: Boolean },
      onCloseRequested: { type: Function }
    }).validate(Template.currentData());
  });
});  

/*
Template.VedgeInfoWindow.rendered = function() {
};  
*/

/*
 * Events
 */

Template.VedgeInfoWindow.events({
  'click .sm-close-button': function (event, instance) {
    event.stopPropagation();
    instance.data.onCloseRequested();
  }
});
   
/*  
 * Helpers
 */

Template.VedgeInfoWindow.helpers({    
});


