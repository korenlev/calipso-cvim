import { ValidatedMethod } from 'meteor/mdg:validated-method';
import * as R from 'ramda';

import { CliqueTypes } from './clique-types';

export const insert = new ValidatedMethod({
  name: 'clique_types.insert',
  validate: CliqueTypes.simpleSchema()
    .pick([
      'environment',
      'focal_point_type',
      'link_types',
      'link_types.$',
      'name',
    ]).validator({ clean: true, filter: false }),
  run({
    environment,
    focal_point_type,
    link_types,
    name,
  }) {
    let cliqueType = CliqueTypes.schema.clean({});

    cliqueType = R.merge(cliqueType, {
      environment,
      focal_point_type,
      link_types,
      name,
    });

    CliqueTypes.insert(cliqueType);
  }
});

export const remove = new ValidatedMethod({
  name: 'clique_types.remove',
  validate: CliqueTypes.simpleSchema()
    .pick([
      '_id',
    ]).validator({ clean: true, filter: false }),
  run({
    _id
  }) {
    let cliqueType = CliqueTypes.findOne({ _id: _id });
    console.log('clique type for remove: ', cliqueType);

    CliqueTypes.remove({ _id: _id });
  }
});
