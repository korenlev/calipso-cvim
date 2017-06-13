import { Meteor } from 'meteor/meteor';
import { SupportedEnvironments,
  subsNameSupportedEnvs
} from '../supported_environments.js';

Meteor.publish(subsNameSupportedEnvs, function () {
  console.log(`server subscribtion to: ${subsNameSupportedEnvs}`);
  return SupportedEnvironments.find({});
});
