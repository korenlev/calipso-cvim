import { ValidatedMethod } from 'meteor/mdg:validated-method';
import * as R from 'ramda';
import { Roles } from 'meteor/alanning:roles';

import { LinkTypes } from './link-types';

export const insert = new ValidatedMethod({
  name: 'links_types.insert',
  validate: LinkTypes.simpleSchema()
    .pick([
      //'environment',
      'description',
      'folder_text',
      'endPointA',
      'endPointB',
    ]).validator({ clean: true, filter: false }),
  run({
    //environment,
    description,
    folder_text,
    endPointA,
    endPointB
  }) {
    if (! Roles.userIsInRole(Meteor.userId(), 'manage-link-types', 'default-group')) {
      throw new Meteor.Error('unauthorized for inserting link type');
    }

    let linkType = LinkTypes.schema.clean({
    });

    let type = calcTypeFromEndPoints(endPointA, endPointB);

    linkType = R.merge(linkType, {
      //environment,
      description,
      folder_text,
      endPointA,
      endPointB,
      type 
    });

    LinkTypes.insert(linkType);
  }
});

export const remove = new ValidatedMethod({
  name: 'links_types.remove',
  validate: LinkTypes.simpleSchema()
    .pick([
      '_id',
    ]).validator({ clean: true, filter: false }),
  run({
    _id
  }) {
    if (! Roles.userIsInRole(Meteor.userId(), 'manage-link-types', 'default-group')) {
      throw new Meteor.Error('unauthorized for removing link type');
    }

    let linkType = LinkTypes.findOne({ _id: _id });
    console.log('link type for remove: ', linkType);
    console.log('current user', Meteor.userId());

    LinkTypes.remove({ _id: _id });
  }
});

function calcTypeFromEndPoints(endPointA, endPointB) {
  return `${endPointA}-${endPointB}`;
}
