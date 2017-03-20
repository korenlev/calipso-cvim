import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
import { Constants } from '/imports/api/constants/constants';
import { Environments } from '/imports/api/environments/environments';
import { LinkTypes } from '/imports/api/link-types/link-types';

export const CliqueTypes = new Mongo.Collection(
  'clique_types', { idGeneration: 'MONGO' });

let schema = {
  _id: { type: { _str: { type: String, regEx: SimpleSchema.RegEx.Id } } },

  environment: {
    type: String,
    custom: function () {
      let that = this;
      let env = Environments.findOne({ name: that.value });

      if (R.isNil(env)) {
        return 'notAllowed';
      }
    }
  },

  focal_point_type: {
    type: String,
    custom: function () {
      let that = this;
      let values = Constants.findOne({ name: 'object_types' }).data;

      if (R.isNil(R.find(R.propEq('value', that.value), values))) {
        return 'notAllowed';
      }
    }
  },

  link_types: {
    type: [String],
    minCount: 1,
    custom: function () {
      let that = this;
      let findResult = R.all(function (pLinkType) {
        if (R.isNil(LinkTypes.findOne({ type: pLinkType }))) {
          return false;
        }

        return true;
      }, that.value);

      if (! findResult) { return 'notAllowed'; }

      return;
    },
  },

  name: {
    type: String
  },
};

let simpleSchema = new SimpleSchema(schema);
simpleSchema.addValidator(function () {
  let that = this;

  let existing = CliqueTypes.findOne({ 
    environment: that.field('environment').value,
    focal_point_type: that.field('focal_point_type').value
  });

  if (! R.isNil(existing)) {
    return 'alreadyExists';
  }
});

CliqueTypes.schema = simpleSchema;
CliqueTypes.attachSchema(CliqueTypes.schema);
