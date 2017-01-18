/*
 * Template Component: EnvMasterHostCredentialsInfo 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
        
import { createInputArgs } from '/imports/ui/lib/input-model';

import './env-master-host-credentials-info.html';     
    
/*  
 * Lifecycles
 */   
  
Template.EnvMasterHostCredentialsInfo.onCreated(function() {
});  

/*
Template.EnvMasterHostCredentialsInfo.rendered = function() {
};  
*/

/*
 * Events
 */

Template.EnvMasterHostCredentialsInfo.events({
  'click .sm-next-button': function () {
    let instance = Template.instance();
    instance.data.onNextRequested(); 
  }
});
   
/*  
 * Helpers
 */

Template.EnvMasterHostCredentialsInfo.helpers({    
  createInputArgs: createInputArgs
});


