import { ValidatedMethod } from 'meteor/mdg:validated-method';
import * as R from 'ramda';

import { CliqueConstraints } from './clique-constraints';

export const insert = new ValidatedMethod({
  name: 'clique_constraints.insert',
  validate: CliqueConstraints.simpleSchema()
    .pick([
//      'environment',
      'focal_point_type',
      'constraints',
      'constraints.$',
    ]).validator({ clean: true, filter: false }),
  run({
 //   environment,
    focal_point_type,
    constraints,
  }) {
    let cliqueConstraint = CliqueConstraints.schema.clean({});

    cliqueConstraint = R.merge(cliqueConstraint, {
  //    environment,
      focal_point_type,
      constraints,
    });

    CliqueConstraints.insert(cliqueConstraint);
  }
});

export const remove = new ValidatedMethod({
  name: 'clique_constraints.remove',
  validate: CliqueConstraints.simpleSchema()
    .pick([
      '_id',
    ]).validator({ clean: true, filter: false }),
  run({
    _id
  }) {
    let cliqueConstraint = CliqueConstraints.findOne({ _id: _id });
    console.log('clique constraint for remove: ', cliqueConstraint);

    CliqueConstraints.remove({ _id: _id });
  }
});

export const update = new ValidatedMethod({
  name: 'clique_constraints.update',
  validate: CliqueConstraints.simpleSchema()
    .pick([
      '_id',
      'focal_point_type',
      'constraints',
      'constraints.$',
    ]).validator({ clean: true, filter: false }),
  run({
    _id,
    focal_point_type,
    constraints,
  }) {

    let item = CliqueConstraints.findOne({ _id: _id });
    console.log('clique constraints for update: ', item);
    console.log('current user', Meteor.userId());

    item = R.merge(
      R.pick([
        'focal_point_type',
        'constraints',
      ], item), {
        focal_point_type,
        constraints,
      });

    CliqueConstraints.update({ _id: _id }, { $set: item });
  }
});
