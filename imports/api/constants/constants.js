/////////////////////////////////////////////////////////////////////////////////////////
// Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems) and others /
//                                                                                      /
// All rights reserved. This program and the accompanying materials                     /
// are made available under the terms of the Apache License, Version 2.0                /
// which accompanies this distribution, and is available at                             /
// http://www.apache.org/licenses/LICENSE-2.0                                           /
/////////////////////////////////////////////////////////////////////////////////////////
import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';

import { Distributions } from './data/distributions';
//import { NetworkPlugins } from './data/network-plugins';
import { LogLevels } from './data/log-levels';
import { MechanismDrivers } from './data/mechanism-drivers';
import { ObjectTypesForLinks } from './data/object-types-for-links';
import { TypeDrivers } from './data/type-drivers';
import { EnvTypes } from './data/env-types';
import { Statuses as ScansStatuses } from './data/scans-statuses';
import { EnvironmentMonitoringTypes } from './data/environment-monitoring-types';
import { EnvProvisionTypes } from './data/environment-provision-types';
import { MessageSourceSystems } from './data/message-source-systems';

export const Constants = new Mongo.Collection('constants', { idGeneration: 'MONGO' });

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
  name: 'object_types_for_links',
  values: ObjectTypesForLinks
}, {
  name: 'type_drivers',
  values: TypeDrivers
}, {
  name: 'environment_provision_types',
  values: EnvProvisionTypes
}, {
  name: 'message_source_systems',
  values: MessageSourceSystems
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
