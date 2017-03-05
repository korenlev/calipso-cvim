/*
 * Template Component: EnvDeleteModal 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
        
import './env-delete-modal.html';     
    
/*  
 * Lifecycles
 */   
  
Template.EnvDeleteModal.onCreated(function() {
  this.autorun(() => {
    new SimpleSchema({
      onDeleteReq: { type: Function },
    }).validate(Template.currentData());
  });
});  

/*
Template.EnvDeleteModal.rendered = function() {
};  
*/

/*
 * Events
 */

Template.EnvDeleteModal.events({
  'click .sm-button-delete': function (_event, _instance) {
    let onDeleteReq = Template.currentData().onDeleteReq;
    onDeleteReq();
  }
});
   
/*  
 * Helpers
 */

Template.EnvDeleteModal.helpers({    
});


