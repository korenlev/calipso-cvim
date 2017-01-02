/*
 * Template Component: AutoSearchResultLine 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
        
import './auto-search-result-line.html';     
    
/*  
 * Lifecycles
 */   
  
Template.AutoSearchResultLine.onCreated(function() {
});  

/*
Template.AutoSearchResultLine.rendered = function() {
};  
*/

/*
 * Events
 */

Template.AutoSearchResultLine.events({
  'click': function(event, instance) {
    event.stopPropagation();
    event.preventDefault();

    instance.data.onClick(instance.data.namePath);
  }
});
   
/*  
 * Helpers
 */

Template.AutoSearchResultLine.helpers({    
});


