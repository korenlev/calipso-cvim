/*
 * Template Component: MessagesList 
 */
    
//import { Meteor } from 'meteor/meteor'; 
//import * as R from 'ramda';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { Messages } from '/imports/api/messages/messages';
import { Environments } from '/imports/api/environments/environments';
import { idToStr } from '/imports/lib/utilities';
        
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
    instance.subscribe('environments_config');
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
  'click .sm-display-context-link': function (event, _instance) {
    event.preventDefault();
    let envName = event.target.dataset.envName;
    let nodeId = event.target.dataset.itemId;

    let environment = Environments.findOne({ name: envName });
    Router.go('environment', { 
      _id: idToStr(environment._id) 
    }, { 
      query: {
        selectedNodeId: idToStr(nodeId)
      } 
    });
  }
});
   
/*  
 * Helpers
 */

Template.MessagesList.helpers({    
  messages: function () {
    return Messages.find({}); 
  },
});
