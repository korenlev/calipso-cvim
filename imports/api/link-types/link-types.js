import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
import { Constants } from '/imports/api/constants/constants';
//import { Environments } from '/imports/api/environments/environments';

export const LinkTypes = new Mongo.Collection(
  'link_types', { idGeneration: 'MONGO' });

let schema = {
  _id: { type: { _str: { type: String, regEx: SimpleSchema.RegEx.Id } } },
  description: {
    type: String
  },
  type: {
    type: String
  },
  endPointA: {
    type: String,
    custom: function () {
      let that = this;
      let values = Constants.findOne({ name: 'object_types' }).data;

      if (R.isNil(R.find(R.propEq('value', that.value), values))) {
        return 'notAllowed';
      }
    }
  },
  endPointB: {
    type: String,
    custom: function () {
      let that = this;
      let values = Constants.findOne({ name: 'object_types' }).data;

      if (R.isNil(R.find(R.propEq('value', that.value), values))) {
        return 'notAllowed';
      }
    }
  }
};

let simpleSchema = new SimpleSchema(schema);

simpleSchema.addValidator(function () {
  let that = this;

  let existing = LinkTypes.findOne({
    _id: { $ne: that.docId },
    endPointA: that.field('endPointA').value,
    endPointB: that.field('endPointB').value
  });

  if (R.allPass([
    R.pipe(R.isNil, R.not), 
    R.pipe(R.propEq('_id', that.docId), R.not)
  ])(existing)) { 

    return 'alreadyExists';
  }

  existing = LinkTypes.findOne({
    _id: { $ne: that.docId },
    endPointA: that.field('endPointB').value,
    endPointB: that.field('endPointA').value
  });

  if (R.allPass([
    R.pipe(R.isNil, R.not), 
    R.pipe(R.propEq('_id', that.docId), R.not)
  ])(existing)) { 

    return 'alreadyExists';
  }
});

LinkTypes.schema = simpleSchema;

LinkTypes.attachSchema(LinkTypes.schema);
