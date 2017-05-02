/*
 * Template Component: alarmIcons
 */

import '/imports/ui/components/breadcrumb/breadcrumb';
import '/imports/ui/components/messages-modal/messages-modal';
import { Messages } from '/imports/api/messages/messages';
import { Roles } from 'meteor/alanning:roles';

import './alarm-icons.html';     

/*
 * Lifecycle
 */
 
Template.alarmIcons.onCreated(function () {
  let instance = this;

  instance.autorun(function () {
    instance.subscribe('messages?level', 'notify');
    instance.subscribe('messages?level', 'warn');
    instance.subscribe('messages?level', 'error');
  });
});

/*
 * Helpers
 */  

Template.alarmIcons.helpers({
  isAdmin: function () {
    return Roles.userIsInRole(Meteor.userId(), 'manage-users', 'default-group'); 
  },

  notificationsCount: function(){
    return Messages.find({level:'notify'}).count();
  },

  warningsCount: function(){
    return Messages.find({level:'warn'}).count();
  },

  errorsCount: function(){
    return Messages.find({level:'error'}).count();
  },
});
