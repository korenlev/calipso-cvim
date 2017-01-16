import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
//import * as R from 'ramda';

import { Distributions } from './data/distributions';
//import { NetworkPlugins } from './data/network-plugins';
import { LogLevels } from './data/log-levels';
import { MechanismDrivers } from './data/mechanism-drivers';
import { ObjectTypes } from './data/object-types';
import { TypeDrivers } from './data/type-drivers';
import { EnvTypes } from './data/env-types';
import { Statuses as ScansStatuses } from './data/scans-statuses';

export const Constants = new Mongo.Collection('constants');

let schema = {
  _id: { type: { _str: { type: String, regEx: SimpleSchema.RegEx.Id } } },
  name: { type: String },
  data: { type: [Object], blackbox: true },
};

Constants.schema = schema;
Constants.attachSchema(schema);

/*
 * Basic Seeds
 */

if (Meteor.server) {
  if (Constants.find({ name: 'distributions'}).count() === 0) {
    Constants.insert({
      name: 'distributions',
      data: Distributions
    });
  }

  /* depracated 
   *
  if (Constants.find({ name: 'network_plugins'}).count() === 0) {
    Constants.insert({
      name: 'network_plugins',
      data: NetworkPlugins, 
    });
  }
  */

  if (Constants.find({ name: 'log_levels'}).count() === 0) {
    Constants.insert({
      name: 'log_levels',
      data: LogLevels
    });
  }

  if (Constants.find({ name: 'mechanism_drivers'}).count() === 0) {
    Constants.insert({
      name: 'mechanism_drivers',
      data: MechanismDrivers
    });
  }

  if (Constants.find({ name: 'object_types'}).count() === 0) {
    Constants.insert({
      name: 'object_types',
      data: ObjectTypes
    });
  }

  if (Constants.find({ name: 'type_drivers'}).count() === 0) {
    Constants.insert({
      name: 'type_drivers',
      data: TypeDrivers
    });
  }

  if (Constants.find({ name: 'env_types'}).count() === 0) {
    Constants.insert({
      name: 'env_types',
      data: EnvTypes
    });
  }

  if (Constants.find({ name: 'scans_statuses'}).count() === 0) {
    Constants.insert({
      name: 'scans_statuses',
      data: ScansStatuses
    });
  }
}
