/*
 * Template Component: DetailedNodeInfoBox 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { ReactiveDict } from 'meteor/reactive-dict';
        
import './detailed-node-info-box.html';     
    
/*  
 * Lifecycles
 */   
  
Template.DetailedNodeInfoBox.onCreated(function() {
  var instance = this;
  instance.state = new ReactiveDict();
  instance.state.setDefault({
  });

  instance.autorun(function () {
    let data = Template.currentData();
    new SimpleSchema({
      node: { type: Object, blackbox: true },
    }).validate(data);
  });
});  

/*
Template.DetailedNodeInfoBox.rendered = function() {
};  
*/

/*
 * Events
 */

Template.DetailedNodeInfoBox.events({
});
   
/*  
 * Helpers
 */

Template.DetailedNodeInfoBox.helpers({    
});


