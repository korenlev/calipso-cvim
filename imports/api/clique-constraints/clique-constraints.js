import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
import { Constants } from '/imports/api/constants/constants';

export const CliqueConstraints = new Mongo.Collection(
  'clique_constraints', { idGeneration: 'MONGO' });

let schema = {
  _id: { type: { _str: { type: String, regEx: SimpleSchema.RegEx.Id } } },

  focal_point_type: {
    type: String,
    custom: function () {
      let that = this;
      let values = Constants.findOne({ name: 'object_types_for_links' }).data;

      if (R.isNil(R.find(R.propEq('value', that.value), values))) {
        return 'notAllowed';
      }
    }
  },

  constraints: {
    type: [String],
    minCount: 1,
    custom: function () {
      let that = this;
      let objectTypes = Constants.findOne({ name: 'object_types_for_links' }).data;

      let findResult = R.intersection(that.value, R.pluck('value', objectTypes));
      if (findResult.length !== that.value.length) { return 'notAllowed'; }

      return;
    },
  },
};

CliqueConstraints.schema = new SimpleSchema(schema);
CliqueConstraints.attachSchema(CliqueConstraints.schema);
