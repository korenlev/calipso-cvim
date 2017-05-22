/*
 * Template Component: GeneralNodeInfoBox 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
        
import './general-node-info-box.html';     
    
/*  
 * Lifecycles
 */   
  
Template.GeneralNodeInfoBox.onCreated(function() {
  let instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
  });

  instance.autorun(function () {
    let data = Template.currentData();
    new SimpleSchema({
      objectName: { type: String },
      type: { type: String },
      lastScanned: { type: Date, optional: true },
      description: { type: String, optional: true },
    }).validate(data);

  });

});  

/*
Template.GeneralNodeInfoBox.rendered = function() {
};  
*/

/*
 * Events
 */

Template.GeneralNodeInfoBox.events({
});
   
/*  
 * Helpers
 */

Template.GeneralNodeInfoBox.helpers({    
});


