import { ValidatedMethod } from 'meteor/mdg:validated-method';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
//import * as R from 'ramda';
import { Roles } from 'meteor/alanning:roles';

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

export const update = new ValidatedMethod({
  name: 'accounts.update',
  validate: userSchema
    .pick([
      '_id',
      'password',
    ]).validator({ clean: true, filter: false }),
  run({
    _id,
    password
  }) {
    throw new Meteor.Error('unimplemented');
    if (! Roles.userIsInRole(Meteor.userId(), 'manage-users', 'default-group')) {
      throw new Meteor.Error('unauthorized for removing users');
    }

    /*
    let item = Meteor.users.findOne({ _id: _id });
    console.log('user for update: ', item);

    item = R.merge(R.pick([
      'password',
    ], item), {
      password
    });
    */
    let item = {
      password
    };

    Meteor.users.update({ _id: _id }, { $set: item });
  }
});
