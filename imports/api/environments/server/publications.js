import { Meteor } from 'meteor/meteor';

import { Environments } from '../environments.js';

Meteor.publish('environments_config', function () {
  console.log('server subscribtion to: environments_config');
  return Environments.find({type:'environment'});
});

Meteor.publish('environments?name', function (name) {
  console.log('server subscribtion to: environments?name=' + name.toString());
  return Environments.find({name: name});
});
