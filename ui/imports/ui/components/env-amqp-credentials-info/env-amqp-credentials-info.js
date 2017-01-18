/*
 * Template Component: EnvAmqpCredentialsInfo 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
        
import { createInputArgs } from '/imports/ui/lib/input-model';

import './env-amqp-credentials-info.html';     
    
/*  
 * Lifecycles
 */   
  
Template.EnvAmqpCredentialsInfo.onCreated(function() {
});  

/*
Template.EnvAmqpCredentialsInfo.rendered = function() {
};  
*/

/*
 * Events
 */

Template.EnvAmqpCredentialsInfo.events({
  'click .sm-next-button': function () {
    let instance = Template.instance();
    instance.data.onNextRequested(); 
  }
});
   
/*  
 * Helpers
 */

Template.EnvAmqpCredentialsInfo.helpers({    
  createInputArgs: createInputArgs
});


