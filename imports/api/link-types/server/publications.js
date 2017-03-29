import { Meteor } from 'meteor/meteor';
import * as R from 'ramda';

import { LinkTypes } from '../link-types.js';

Meteor.publish('link_types', function () {
  console.log('server subscribtion: link_types');

  //let that = this;

  let query = {};
  return LinkTypes.find(query); 
});

Meteor.publish('link_types?env*', function (env) {
  console.log('server subscribtion: link_types?env*');
  console.log(env);

  //let that = this;

  let query = {};
  if (! R.isNil(env)) { query = R.assoc('environment', env, query); }
  console.log('-query: ', query);
  return LinkTypes.find(query); 
});

Meteor.publish('link_types?_id', function (_id) {
  console.log('server subscribtion: link_types?_id');
  console.log(_id);

  //let that = this;

  let query = { 
    _id: _id,
  };
  console.log('-query: ', query);
  return LinkTypes.find(query); 
});
