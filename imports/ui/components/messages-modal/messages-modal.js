/*
 * Template Component: MessagesModal 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import * as R from 'ramda';
import { Messages } from '/imports/api/messages/messages';
import { Environments } from '/imports/api/environments/environments';
import { idToStr } from '/imports/lib/utilities';
        
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
    listHeader: null,
    envName: null
  });

  instance.autorun(function () {
    let messageLevel = instance.state.get('messageLevel');
    let envName = instance.state.get('envName');
    if (R.isNil(messageLevel)) { return; }

    if (R.isNil(envName)) {
      instance.subscribe('messages?level', messageLevel);
    } else {
      instance.subscribe('messages?env+level', envName, messageLevel);
    }
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
    setParams(data.messageLevel, data.envName, instance);
  },

  'click .sm-display-context-link': function (event, instance) {
    event.preventDefault();
    let envName = event.target.dataset.envName;
    let nodeId = event.target.dataset.itemId;

    let environment = Environments.findOne({ name: envName });

    Meteor.apply('inventoryFindNode?env&id', [
      environment.name,
      nodeId,
    ], {
      wait: false
    }, function (err, resp) {
      if (err) { 
        console.error(R.toString(err));
        return; 
      }

      if (R.isNil(resp.node)) {
        console.error('error finding node related to message', R.toString(nodeId));
        return;
      }

      Router.go('environment', { 
        _id: idToStr(environment._id) 
      }, { 
        query: {
          selectedNodeId: idToStr(resp.node._id)
        } 
      });

      instance.$('#messagesModalGlobal').modal('hide');

    });

  }
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

  envName: function () {
    let instance = Template.instance();
    return instance.state.get('envName');
  },

  messages: function () {
    let instance = Template.instance();
    let level = instance.state.get('messageLevel');
    let envName = instance.state.get('envName');

    if (R.isNil(envName)) {
      return Messages.find({ level: level });
    } else {
      return Messages.find({ level: level, environment: envName });
    }
  },
}); // end: helpers

function setParams(messageLevel, envName, instance) {
  instance.state.set('messageLevel', messageLevel);
  instance.state.set('iconType', calcIconType(messageLevel));
  instance.state.set('listHeader', calcListHeader(messageLevel, envName));
  instance.state.set('envName', envName);
}

function calcIconType(messageLevel) {
  switch (messageLevel) {
  case 'notify':
    return 'notifications';
  case 'info':
    return 'notifications';
  case 'warning':
    return 'warning';
  case 'error':
    return 'error';
  default:
    throw 'unimplemented message level for icon';
  }
}

function calcListHeader(messageLevel, envName) {
  let header;

  switch (messageLevel) {
  case 'notify':
    header = 'List of notifications';
    break;
  case 'info':
    header = 'List of info messages';
    break;
  case 'warning':
    header = 'List of warnings';
    break;
  case 'error':
    header = 'List of errors';
    break;
  default:
    throw 'unimplemented message level for list header';
  }

  if (! R.isNil(envName)) {
    header = header + ` for environment ${envName}.`;
  }

  return header;
}
