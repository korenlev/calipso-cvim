import { Meteor } from 'meteor/meteor';
import * as R from 'ramda';

import { Environments } from '../environments.js';

Meteor.publish('environments_config', function () {
  console.log('server subscribtion to: environments_config');
  let query = {
    type:'environment',
    user: this.userId
  };
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
