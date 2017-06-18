import { Meteor } from 'meteor/meteor';
import * as R from 'ramda';
import { Counts } from 'meteor/tmeasday:publish-counts';

import { Scans,
  subsScansEnvPageAmountSorted,
  subsScansEnvPageAmountSortedCounter,
} from '../scans.js';

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

Meteor.publish(subsScansEnvPageAmountSorted, function (
  env, page, amountPerPage, sortField, sortDirection) {

  console.log(`server subscribtion: ${subsScansEnvPageAmountSorted}`);
  console.log(env);
  console.log('page: ', page);
  console.log('amount: ', amountPerPage);
  console.log('sortField: ', sortField, R.isNil(sortField));
  console.log('sortDirection: ', sortDirection);

  let skip = (page - 1) * amountPerPage;

  let query = {};
  if (! R.isNil(env)) { query = R.assoc('environment', env, query); }
  console.log('-query: ', query);
  let sortParams = {};

  sortParams = R.ifElse(R.isNil, R.always(sortParams), 
      R.assoc(R.__, sortDirection, sortParams))(sortField);

  console.log('sort params:', sortParams);

  let qParams = {
    limit: amountPerPage,
    skip: skip,
    sort: sortParams,
  };

  Counts.publish(this, subsScansEnvPageAmountSortedCounter, Scans.find(query), {
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
