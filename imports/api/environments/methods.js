//import { Meteor } from 'meteor/meteor';
//import * as R from 'ramda';
import { ValidatedMethod } from 'meteor/mdg:validated-method';

//import { SimpleSchema } from 'meteor/aldeed:simple-schema';

import { Environments } from './environments';

export const insert = new ValidatedMethod({
  name: 'environments.insert',
  validate: null,
  run({
    configuration,
    distribution,
    name,
    network_plugins,
  }) {
    const environment = {
      configuration,
      distribution,
      name,
      network_plugins,
      type: 'environment'
    };

    Environments.insert(environment);
  },
});

export const update = new ValidatedMethod({
  name: 'environments.update',
  validate: null,
  run({
    itemId,
    configuration,
    distribution,
    name,
    network_plugins,
  }) {
    //const environment = Environments.findOne(environmentId);

    Environments.update(itemId, {
      $set: {
        configuration: configuration,
        distribution: distribution,
        name: name,
        network_plugins: network_plugins,
      },
    });
  }
});
