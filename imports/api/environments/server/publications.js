import { Meteor } from 'meteor/meteor';
import * as R from 'ramda';
import { Roles } from 'meteor/alanning:roles';

import { Environments } from '../environments.js';

Meteor.publish('environments_config', function () {
  console.log('server subscribtion to: environments_config');
  let userId = this.userId;

  let query = {
    type: 'environment',
  };

  if (! Roles.userIsInRole(userId, 'view-env', null)) {
    query = R.merge(query, {
      'auth.view-env': { 
        $in: [ userId ] 
      }
    });
  }

  console.log('-query: ', R.toString(query));
  return Environments.find(query);
});

Meteor.publish('environments.view-env&userId', function (userId) {
  let query = {};

  if (! Roles.userIsInRole(userId, 'manage-users', Roles.GLOBAL_GROUP)) {
    this.error('unauthorized for this subscription');
  }

  query = R.merge(query, {
    'auth.view-env': { 
      $in: [ userId ] 
    }
  });

  return Environments.find(query);
});

Meteor.publish('environments.edit-env&userId', function (userId) {
  let query = {};

  if (! Roles.userIsInRole(userId, 'manage-users', Roles.GLOBAL_GROUP)) {
    this.error('unauthorized for this subscription');
  }

  query = R.merge(query, {
    'auth.edit-env': { 
      $in: [ userId ] 
    }
  });

  return Environments.find(query);
});

Meteor.publish('environments?name', function (name) {
  console.log('server subscribtion to: environments?name=' + name.toString());
  let query = {
    name: name,
    user: this.userId
  };
  return Environments.find(query);
});

Meteor.publish('environments?_id', function (_id) {
  console.log('server subscribtion to: environments?_id');
  console.log('-_id: ', R.toString(_id));

  let query = {
    _id: _id,
    user: this.userId
  };
  return Environments.find(query);
});
