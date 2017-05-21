/*
 * Template Component: alarmIcons
 */

import '/imports/ui/components/breadcrumb/breadcrumb';
import { Messages } from '/imports/api/messages/messages';
import { Roles } from 'meteor/alanning:roles';

import './alarm-icons.html';     

/*
 * Lifecycle
 */
 
Template.alarmIcons.onCreated(function () {
  let instance = this;

  instance.autorun(function () {
    instance.subscribe('messages?level', 'info');
    instance.subscribe('messages?level', 'warn');
    instance.subscribe('messages?level', 'error');
  });
});

/*
 * Helpers
 */  

Template.alarmIcons.helpers({
  isAdmin: function () {
    return Roles.userIsInRole(Meteor.userId(), 'manage-users', Roles.GLOBAL_GROUP); 
  },

  infosCount: function(){
    return Messages.find({level:'info'}).count();
  },

  warningsCount: function(){
    return Messages.find({level:'warn'}).count();
  },

  errorsCount: function(){
    return Messages.find({level:'error'}).count();
  },
});
