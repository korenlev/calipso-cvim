import { ValidatedMethod } from 'meteor/mdg:validated-method';
import * as R from 'ramda';

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
    let linkType = LinkTypes.schema.clean({
      user_id: Meteor.user()._id
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
    let linkType = LinkTypes.findOne({ _id: _id });
    console.log('link type for remove: ', linkType);
    console.log('current user', Meteor.userId());

    if (linkType.user_id !== Meteor.userId()) {
      throw new Meteor.Error('not-auth', 'User not authorized to perform action');
    }

    LinkTypes.remove({ _id: _id });
  }
});

function calcTypeFromEndPoints(endPointA, endPointB) {
  return `${endPointA}-${endPointB}`;
}