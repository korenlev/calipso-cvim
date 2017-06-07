/*
 * Template Component: MessagesInfoBox 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
//import { ReactiveDict } from 'meteor/reactive-dict';
        
import './messages-info-box.html';     
    
/*  
 * Lifecycles
 */   
  
Template.MessagesInfoBox.onCreated(function() {
  var instance = this;

  instance.autorun(function () {
    let data = Template.currentData();
    new SimpleSchema({
      title: { type: String },
      count: { type: Number },
      lastScanTimestamp: { type: String, optional: true },
      icon: { type: String },
      colorClass: { type: String },
      onMoreDetailsReq: { type: Function },
    }).validate(data);

  });
});  

/*
Template.MessagesInfoBox.rendered = function() {
};  
*/

/*
 * Events
 */

Template.MessagesInfoBox.events({
  'click .sm-more-details-btn': function (event, instance) {
    event.preventDefault();

    let data = instance.data;
    data.onMoreDetailsReq();
  }
});
   
/*  
 * Helpers
 */

Template.MessagesInfoBox.helpers({    
});


