import { Meteor } from 'meteor/meteor';

import { CliqueConstraints } from '../clique-constraints.js';

Meteor.publish('clique_constraints', function () {
  console.log('server subscribtion: clique_constraints');

  //let that = this;

  let query = {};
  return CliqueConstraints.find(query); 
});

Meteor.publish('clique_constraints?_id', function (_id) {
  console.log('server subscribtion: clique_constraints?_id');
  console.log(_id);

  //let that = this;

  let query = { _id: _id };
  return CliqueConstraints.find(query); 
});
