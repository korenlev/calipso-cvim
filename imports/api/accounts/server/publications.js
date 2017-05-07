import { Meteor } from 'meteor/meteor';
//import * as R from 'ramda';
//import { Environments } from '/imports/api/environments/environments';
//import { Roles } from 'meteor/alanning:roles';

Meteor.publish('users', function () {
  console.log('server subscribtion to: users');
  /*
  let that = this;

  let query = {};

  if (! Roles.userIsInRole(that.userId, 'manage-users', 'default-group')) {
    query = {
      _id: that.userId
    };
  }
  */

  return Meteor.users.find({});
});
