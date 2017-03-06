import { Meteor } from 'meteor/meteor';

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
