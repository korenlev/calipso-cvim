import { ValidatedMethod } from 'meteor/mdg:validated-method';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';

let userSchema = new SimpleSchema({
  _id: { type: String },
  username: { type: String },
  password: { type: String }
});

export const insert = new ValidatedMethod({
  name: 'accounts.insert',
  validate: userSchema
    .pick([
      'username',
      'password'
    ]).validator({ clean: true, filter: false }),
  run({
    username,
    password
  }) {
    if (! Roles.userIsInRole(Meteor.userId(), 'manage-users', 'default-group')) {
      throw new Meteor.Error('unauthorized for removing users');
    }

    Accounts.createUser({ 
      username: username,
      password: password
    });
  }
});

export const remove = new ValidatedMethod({
  name: 'accounts.remove',
  validate: userSchema
    .pick([
      '_id',
    ]).validator({ clean: true, filter: false }),
  run({
    _id
  }) {
    if (! Roles.userIsInRole(Meteor.userId(), 'manage-users', 'default-group')) {
      throw new Meteor.Error('unauthorized for removing users');
    }

    let user = Meteor.users.findOne({ _id: _id });
    console.log('user for remove: ', user);

    Meteor.users.remove({ _id: _id });
  }
});
