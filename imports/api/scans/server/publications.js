import { Meteor } from 'meteor/meteor';
import * as R from 'ramda';

import { Scans } from '../scans.js';

Meteor.publish('scans?env', function (env_name) {
  console.log('server subscribtion: scans?env');
  console.log(env_name);

  //let that = this;

  return Scans.find({
    environment: env_name,
  }); 
});

Meteor.publish('scans?env*', function (env) {
  console.log('server subscribtion: scans?env*');
  console.log(env);

  //let that = this;

  let query = {};
  if (! R.isNil(env)) { query = R.assoc('environment', env, query); }
  console.log('-query: ', query);
  return Scans.find(query); 
});

Meteor.publish('scans?id', function (id) {
  console.log('server subscribtion: scans?id');
  console.log('-id: ', id);

  //let that = this;

  let query = { _id: id };
  return Scans.find(query); 
});
