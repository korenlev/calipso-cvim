/*
 * Template Component: MessagesList 
 */
    
//import { Meteor } from 'meteor/meteor'; 
//import * as R from 'ramda';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { Messages } from '/imports/api/messages/messages';
        
import './messages-list.html';     
    
/*  
 * Lifecycles
 */   
  
Template.MessagesList.onCreated(function() {
  var instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    env: null
  });

  instance.autorun(function () {


    //let data = Template.currentData();
    
    var controller = Iron.controller();
    var params = controller.getParams();
    var query = params.query;

    new SimpleSchema({
    }).validate(query);

    instance.subscribe('messages');
  });
});  

/*
Template.MessagesList.rendered = function() {
};  
*/

/*
 * Events
 */

Template.MessagesList.events({
});
   
/*  
 * Helpers
 */

Template.MessagesList.helpers({    
  messages: function () {
    return Messages.find({}); 
  },
});
