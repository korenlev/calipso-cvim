/*
 * Template Component: Icon 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
        
import './icon.html';     
    
/*  
 * Lifecycles
 */   
  
Template.Icon.onCreated(function() {
});  

/*
Template.Icon.rendered = function() {
};  
*/

/*
 * Events
 */

Template.Icon.events({
});
   
/*  
 * Helpers
 */

Template.Icon.helpers({    
  iconType: function (type, targetType) {
    return type === targetType;
  }
});


