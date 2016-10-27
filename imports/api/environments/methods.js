//import { Meteor } from 'meteor/meteor';
import * as R from 'ramda';
import { ValidatedMethod } from 'meteor/mdg:validated-method';

//import { SimpleSchema } from 'meteor/aldeed:simple-schema';

import { Environments } from './environments';

export const insert = new ValidatedMethod({
  name: 'environments.insert',
  validate: Environments.simpleSchema()
    .pick([
      'configuration', 'configuration.$', 
      'distribution', 'name', 
      'network_plugins', 'network_plugins.$'
    ]).validator({ clean: true, filter: false }), 
  //validate: null, 
  run({
    configuration,
    distribution,
    name,
    network_plugins,
  }) {
    // todo: create clean object instance.
    let environment = Environments.schema.clean({});
    environment = R.merge(environment, {
      configuration,
      distribution,
      name,
      network_plugins,
    });

    Environments.insert(environment);
  },
});

export const update = new ValidatedMethod({
  name: 'environments.update',
  validate: Environments.simpleSchema().pick([
    '_id',
    'configuration', 'configuration.$', 
    'distribution', 'name', 
    'network_plugins', 'network_plugins.$'
  ]).validator({ clean: true, filter: false }),
  run({
    _id,
    configuration,
    distribution,
    name,
    network_plugins,
  }) {
    //const environment = Environments.findOne(environmentId);

    Environments.update(_id, {
      $set: {
        configuration: configuration,
        distribution: distribution,
        name: name,
        network_plugins: network_plugins,
      },
    });
  }
});
