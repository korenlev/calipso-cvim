/*
 * Template Component: EnvNfvInfo 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
        
import './env-nfv-info.html';     
    
/*  
 * Lifecycles
 */   
  
Template.EnvNfvInfo.onCreated(function() {
});  

/*
Template.EnvNfvInfo.rendered = function() {
};  
*/

/*
 * Events
 */

Template.EnvNfvInfo.events({
  'click .sm-next-button': function () {
    let instance = Template.instance();
    instance.data.onNextRequested(); 
  },

  'click .sm-submit-button': function () {
    let instance = Template.instance();
    instance.data.onSubmitRequested(); 
  },
});
   
/*  
 * Helpers
 */

Template.EnvNfvInfo.helpers({    
});


