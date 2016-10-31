import { Meteor } from 'meteor/meteor';

import { ScanningRequests } from '../scanning_requests.js';

Meteor.publish('scanning_requests?env+current_user', function (environment_name) {
  console.log('server subscribtion: scanning_requests?env+current_user');
  console.log(environment_name);

  let that = this;

  return ScanningRequests.find({
    environment_name: environment_name,
    userId: that.userId
  }); 
});
