import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';

import { Distributions } from './data/distributions';
//import { NetworkPlugins } from './data/network-plugins';
import { LogLevels } from './data/log-levels';
import { MechanismDrivers } from './data/mechanism-drivers';
import { ObjectTypes } from './data/object-types';
import { TypeDrivers } from './data/type-drivers';
import { EnvTypes } from './data/env-types';
import { Statuses as ScansStatuses } from './data/scans-statuses';
import { EnvironmentMonitoringTypes } from './data/environment-monitoring-types';
import { EnvProvisionTypes } from './data/environment-provision-types';

export const Constants = new Mongo.Collection('constants');

let schema = {
  _id: { type: { _str: { type: String, regEx: SimpleSchema.RegEx.Id } } },
  name: { type: String },
  data: { type: [Object], blackbox: true },
};

let constantsDefaults = [{
  name: 'env_types',
  values: EnvTypes
}, {
  name: 'scans_statuses', 
  values: ScansStatuses
}, {
  name: 'environment_monitoring_types',
  values: EnvironmentMonitoringTypes
}, {
  name: 'distributions',
  values: Distributions
}, {
  name: 'log_levels',
  values: LogLevels
}, {
  name: 'mechanism_drivers',
  values: MechanismDrivers
}, {
  name: 'object_types',
  values: ObjectTypes
}, {
  name: 'type_drivers',
  values: TypeDrivers
}, {
  name: 'environment_provision_types',
  values: EnvProvisionTypes
}];

Constants.schema = schema;
Constants.attachSchema(schema);

/*
 * Basic Seeds
 */

if (Meteor.server) {
  R.forEach((def) => {
    insertConstants(Constants, def.name, def.values);
  }, constantsDefaults);
}

function insertConstants(collection, name, values) {
  if (collection.find({ name: name}).count() === 0) {
    Constants.insert({
      name: name,
      data: values
    });
  }
}
