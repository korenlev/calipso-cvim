import { ValidatedMethod } from 'meteor/mdg:validated-method';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
import { Roles } from 'meteor/alanning:roles';
import { Environments } from '/imports/api/environments/environments';

let userSchema = new SimpleSchema({
  _id: { type: String },
  username: { type: String },
  password: { type: String },
  viewEnvs: { type: [ String ] }
});

export const insert = new ValidatedMethod({
  name: 'accounts.insert',
  validate: userSchema
    .pick([
      'username',
      'password',
      'viewEnvs',
      'viewEnvs.$',
    ]).validator({ clean: true, filter: false }),
  run({
    username,
    password,
    viewEnvs,
  }) {
    if (! Roles.userIsInRole(Meteor.userId(), 'manage-users', 'default-group')) {
      throw new Meteor.Error('unauthorized for removing users');
    }

    let userId = Accounts.createUser({ 
      username: username,
      password: password
    });

    R.forEach((envName) => {
      let env = Environments.findOne({ name: envName });
      let auth = R.assocPath([ 'view-env', userId ], env.auth);
      Environments.update(env._id, {  $set: { auth: auth } });
    }, viewEnvs);
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
      'viewEnvs',
      'viewEnvs.$',
    ]).validator({ clean: true, filter: false }),
  run({
    _id,
    _password,
    viewEnvs,
  }) {
    //throw new Meteor.Error('unimplemented');
    if (! Roles.userIsInRole(Meteor.userId(), 'manage-users', 'default-group')) {
      throw new Meteor.Error('unauthorized for updating users');
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

    /*
    let item = {
      //password
    };

    Meteor.users.update({ _id: _id }, { $set: item });
    */

    let currentViewEnvs = R.map((env) => {
      return env.name;
    }, Environments.find({ 'auth.view-env': { $in: [ _id  ] }}).fetch());

    let viewEnvsForDelete = R.difference(currentViewEnvs, viewEnvs);
    let viewEnvsForAdd = R.difference(viewEnvs, currentViewEnvs);

    R.forEach((envName) => {
      let env = Environments.findOne({ name: envName });
      let auth = env.auth;
      if (R.isNil(auth)) { auth = { }; }
      if (R.isNil(R.path(['view-env'], auth))) {
        auth = R.assoc('view-env', [], auth);
      }
      auth = R.merge(auth, {
        'view-env': R.reject(R.equals(_id), auth['view-env'])
      });
      //let newEnv = R.merge(env, { auth: auth });
      console.log('update env. set: ' + R.toString(auth));
      try {
      Environments.update(env._id, {  
        $set: { 
          auth: auth,
          configuration: env.configuration,
          //distribution: distribution,
          //name: name,
          type_drivers: env.type_drivers,
          mechanism_drivers: env.mechanism_drivers,
          listen: env.listen,
        } 
      });
      } catch(e) {
        console.error('error in update: ' + R.toString(e));
        throw (e);
      }
    }, viewEnvsForDelete);

    R.forEach((envName) => {
      let env = Environments.findOne({ name: envName });
      let auth = env.auth;
      if (R.isNil(auth)) { auth = { }; }
      if (R.isNil(R.path(['view-env'], auth))) {
        auth = R.assoc('view-env', [], auth);
      }
      auth = R.merge(auth, {
        'view-env': R.append(_id, auth['view-env'])
      });
      console.log('update env. set: ' + R.toString(auth));
      try {
      Environments.update(env._id, {  
        $set: { 
          auth: auth,
          configuration: env.configuration,
          //distribution: distribution,
          //name: name,
          type_drivers: env.type_drivers,
          mechanism_drivers: env.mechanism_drivers,
          listen: env.listen,
        } 
      });
      } catch(e) {
        console.error('error in update: ' + R.toString(e));
        throw (e);
      }
    }, viewEnvsForAdd);
  }
});
