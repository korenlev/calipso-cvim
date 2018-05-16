import { Roles } from 'meteor/alanning:roles';

import { ReactiveDict } from 'meteor/reactive-dict';

import { UserSettings } from '/imports/api/user-settings/user-settings';

import './settings-list.html';


Template.settingsList.onCreated(function () {
  let instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    msgsViewBackDelta: 1
  });

  instance.autorun(function () {
    instance.subscribe('user_settings?user');
    UserSettings.find({user_id: Meteor.userId()}).forEach((userSettings) => {
      instance.state.set('msgsViewBackDelta', userSettings.messages_view_backward_delta); 
    });
  });

  instance.autorun(function () {
    let msgsViewBackDelta = instance.state.get('msgsViewBackDelta');

    instance.subscribe('messages/count?backDelta&level', msgsViewBackDelta, 'info');
    instance.subscribe('messages/count?backDelta&level', msgsViewBackDelta, 'warning');
    instance.subscribe('messages/count?backDelta&level', msgsViewBackDelta, 'error');
  });
});

Template.settingsList.helpers({
  isAdmin: function () {
    return Roles.userIsInRole(Meteor.userId(), 'manage-users', Roles.GLOBAL_GROUP); 
  },
});