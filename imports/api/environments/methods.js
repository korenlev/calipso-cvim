//import { Meteor } from 'meteor/meteor';
import * as R from 'ramda';
import { ValidatedMethod } from 'meteor/mdg:validated-method';

//import { SimpleSchema } from 'meteor/aldeed:simple-schema';

import { Environments } from './environments';
import { Inventory } from '/imports/api/inventories/inventories';
import { Links } from '/imports/api/links/links';
import { Cliques } from '/imports/api/cliques/cliques';
import { CliqueTypes } from '/imports/api/clique-types/clique-types';
import { Messages } from '/imports/api/messages/messages';
import { Scans } from '/imports/api/scans/scans';

export const insert = new ValidatedMethod({
  name: 'environments.insert',
  validate: Environments.simpleSchema()
    .pick([
      'configuration', 
      'configuration.$', 
      'user', 
      'distribution', 
      'name', 
      'type_drivers',
      'mechanism_drivers',
      'mechanism_drivers.$',
      'listen',
    ]).validator({ clean: true, filter: false }), 
  //validate: null, 
  run({
    configuration,
    user,
    distribution,
    name,
    type_drivers,
    mechanism_drivers,
    listen,
  }) {
    // todo: create clean object instance.
    let environment = Environments.schema.clean({});

    environment = R.merge(environment, {
      configuration,
      user,
      distribution,
      name,
      type_drivers,
      mechanism_drivers,
      listen,
    });

    Environments.insert(environment);
  },
});

export const update = new ValidatedMethod({
  name: 'environments.update',
  validate: Environments.simpleSchema().pick([
    '_id',
    'configuration', 
    'configuration.$', 
    'user', 
    'distribution', 
    'name', 
    'type_drivers', 
    'mechanism_drivers', 
    'mechanism_drivers.$',
    'listen',
  ]).validator({ clean: true, filter: false }),
  run({
    _id,
    configuration,
    user,
    distribution,
    name,
    type_drivers,
    mechanism_drivers,
    listen,
  }) {
    //const environment = Environments.findOne(environmentId);

    Environments.update(_id, {
      $set: {
        configuration: configuration,
        user: user,
        distribution: distribution,
        name: name,
        type_drivers,
        mechanism_drivers,
        listen,
      },
    });
  }
});

export const remove = new ValidatedMethod({
  name: 'environments.remove',
  validate: Environments.simpleSchema().pick([
    '_id',
  ]).validator({ clean: true, filter: false }),
  run({
    _id,
  }) {
    const env = Environments.findOne({ _id: _id });
    console.log('environment for remove: ', env);

    Inventory.remove({ environment: env.name }); 
    Links.remove({ environment: env.name });
    Cliques.remove({ environment: env.name });
    CliqueTypes.remove({ environment: env.name });
    Messages.remove({ environment: env.name });
    Scans.remove({ environment: env.name });
    Environments.remove({ _id: _id });
  }
});
