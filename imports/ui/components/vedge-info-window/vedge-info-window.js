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
      show: { type: Boolean }
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
});
   
/*  
 * Helpers
 */

Template.VedgeInfoWindow.helpers({    
});


