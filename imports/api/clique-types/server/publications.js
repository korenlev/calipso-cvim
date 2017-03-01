import { Meteor } from 'meteor/meteor';
import * as R from 'ramda';

import { CliqueTypes } from '../clique-types.js';

Meteor.publish('clique_types?env*', function (env) {
  console.log('server subscribtion: clique_types?env*');
  console.log(env);

  //let that = this;

  let query = {};
  if (! R.isNil(env)) { query = R.assoc('environment', env, query); }
  console.log('-query: ', query);
  return CliqueTypes.find(query); 
});

Meteor.publish('clique_types?_id', function (_id) {
  console.log('server subscribtion: clique_types?_id');
  console.log(_id);

  //let that = this;

  let query = { _id: _id };
  return CliqueTypes.find(query); 
});
