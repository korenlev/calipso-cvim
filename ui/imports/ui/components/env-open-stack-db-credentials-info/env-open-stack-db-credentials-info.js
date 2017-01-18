/*
 * Template Component: EnvOpenStackDbCredentialsInfo 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
        
import { createInputArgs } from '/imports/ui/lib/input-model';

import './env-open-stack-db-credentials-info.html';     
    
/*  
 * Lifecycles
 */   
  
Template.EnvOpenStackDbCredentialsInfo.onCreated(function() {
});  

/*
Template.EnvOpenStackDbCredentialsInfo.rendered = function() {
};  
*/

/*
 * Events
 */

Template.EnvOpenStackDbCredentialsInfo.events({
  'click .sm-next-button': function () {
    let instance = Template.instance();
    instance.data.onNextRequested(); 
  }
});
   
/*  
 * Helpers
 */

Template.EnvOpenStackDbCredentialsInfo.helpers({    
  createInputArgs: createInputArgs
});


