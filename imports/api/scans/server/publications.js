import { Meteor } from 'meteor/meteor';

import { Scans } from '../scans.js';

Meteor.publish('scans?env', function (env_name) {
  console.log('server subscribtion: scans?env');
  console.log(env_name);

  //let that = this;

  return Scans.find({
    environment: env_name,
  }); 
});
