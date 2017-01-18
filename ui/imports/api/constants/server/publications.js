import { Meteor } from 'meteor/meteor';

import { Constants } from '../constants.js';

Meteor.publish('constants', function () {
  console.log('server subscribtion to: constants');
  return Constants.find({});
});
