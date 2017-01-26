/*
 * Template Component: DataCubic 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { Icon } from '/imports/lib/icon';
        
import './data-cubic.html';     
    
/*  
 * Lifecycles
 */   
  
Template.DataCubic.onCreated(function() {
  this.autorun(() => {
    new SimpleSchema({
      header: { type: String },
      dataInfo: { type: String },
      icon: { type: Icon },
      theme: { type: String, optional: true }
    }).validate(Template.currentData());
  });
});  

/*
Template.DataCubic.rendered = function() {
};  
*/

/*
 * Events
 */

Template.DataCubic.events({
});
   
/*  
 * Helpers
 */

Template.DataCubic.helpers({    
});


