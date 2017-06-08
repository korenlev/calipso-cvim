import { Meteor } from 'meteor/meteor';
import * as R from 'ramda';
import { Counts } from 'meteor/tmeasday:publish-counts';

import { Scans } from '../scans.js';

Meteor.publish('scans?env', function (env_name) {
  console.log('server subscribtion: scans?env');
  console.log(env_name);

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

Meteor.publish('scans?env*&page&amount', function (env, page, amountPerPage) {
  console.log('server subscribtion: scans?env*&page&amount');
  console.log(env);
  console.log('page: ', page);
  console.log('amount: ', amountPerPage);

  let skip = (page - 1) * amountPerPage;

  let query = {};
  if (! R.isNil(env)) { query = R.assoc('environment', env, query); }
  console.log('-query: ', query);

  let qParams = {
    limit: amountPerPage,
    skip: skip
  };

  Counts.publish(this, 'scans?env*&page&amount!count', Scans.find(query), {
    noReady: true
  });

  return Scans.find(query, qParams); 
});

Meteor.publish('scans?id', function (id) {
  console.log('server subscribtion: scans?id');
  console.log('-id: ', id);

  //let that = this;

  let query = { _id: id };
  return Scans.find(query); 
});
