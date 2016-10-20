/*
 * Template Component: EnvOsApiEndpointInfo 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
        
import './env-os-api-endpoint-info.html';     
    
/*  
 * Lifecycles
 */   
  
Template.EnvOsApiEndpointInfo.onCreated(function() {
});  

/*
Template.EnvOsApiEndpointInfo.rendered = function() {
};  
*/

/*
 * Events
 */

Template.EnvOsApiEndpointInfo.events({
  'click .sm-next-button': function () {
    let instance = Template.instance();
    instance.data.onNextRequested(); 
  }
});
   
/*  
 * Helpers
 */

Template.EnvOsApiEndpointInfo.helpers({    
});


