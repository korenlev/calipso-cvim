import { Meteor } from 'meteor/meteor';
//import * as R from 'ramda';

Meteor.publish('users', function () {
  console.log('server subscribtion to: users');
  let that = this;

  let query = {};

  if (! Roles.userIsInRole(that.userId, 'manage-users', 'default-group')) {
    query = {
      _id: that.userId
    };
  }

  return Meteor.users.find({});
});
