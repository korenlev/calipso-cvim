/*
 * Template Component: MessagesModal 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import * as R from 'ramda';
import { Messages } from '/imports/api/messages/messages';
        
import './messages-modal.html';     
    
/*  
 * Lifecycles
 */   
  
Template.MessagesModal.onCreated(function() {
  let instance = this;
  instance.state = new ReactiveDict();
  instance.state.setDefault({
    messageLevel: null,
    iconType: null,
    listHeader: null
  });

  instance.autorun(function () {
    let messageLevel = instance.state.get('messageLevel');
    if (R.isNil(messageLevel)) { return; }

    instance.subscribe('messages?level', messageLevel);
  });
});  

/*
Template.MessagesModal.rendered = function() {
};  
*/

/*
 * Events
 */

Template.MessagesModal.events({
  'show.bs.modal #messagesModalGlobal': function (event, instance) {
    let data = event.relatedTarget.dataset;
    setParams(data.messageLevel, instance);
  },
});
   
/*  
 * Helpers
 */

Template.MessagesModal.helpers({    
  iconType: function () {
    let instance = Template.instance();
    return instance.state.get('iconType');
  },

  listHeader: function () {
    let instance = Template.instance();
    return instance.state.get('listHeader');
  },

  messages: function () {
    let instance = Template.instance();
    let level = instance.state.get('messageLevel');

    return Messages.find({ level: level });
  },
}); // end: helpers

function setParams(messageLevel, instance) {
  instance.state.set('messageLevel', messageLevel);
  instance.state.set('iconType', calcIconType(messageLevel));
  instance.state.set('listHeader', calcListHeader(messageLevel));
}

function calcIconType(messageLevel) {
  switch (messageLevel) {
  case 'notify':
    return 'notifications';
  case 'warn':
    return 'warning';
  case 'error':
    return 'error';
  default:
    throw 'unimplemented message level for icon';
  }
}

function calcListHeader(messageLevel) {
  switch (messageLevel) {
  case 'notify':
    return 'List of notifications';
  case 'warn':
    return 'List of warnings';
  case 'error':
    return 'List of errors';
  default:
    throw 'unimplemented message level for list header';
  }
}
