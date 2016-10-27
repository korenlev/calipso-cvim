/*
 * Template Component: EnvNfvInfo 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
        
import { createInputArgs } from '/imports/ui/lib/input-model';

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
  'click .sm-submit-button': function () {
    let instance = Template.instance();
    instance.data.onSubmitRequested(); 
  },
});
   
/*  
 * Helpers
 */

Template.EnvNfvInfo.helpers({    
  createInputArgs: createInputArgs
});


