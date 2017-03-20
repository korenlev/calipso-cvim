import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
import { Constants } from '/imports/api/constants/constants';
//import { Environments } from '/imports/api/environments/environments';

export const LinkTypes = new Mongo.Collection(
  'link_types', { idGeneration: 'MONGO' });

let schema = {
  _id: { type: { _str: { type: String, regEx: SimpleSchema.RegEx.Id } } },
  user_id: { type: String }, 
  /*
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
  */
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

LinkTypes.schema = new SimpleSchema(schema);
LinkTypes.attachSchema(LinkTypes.schema);
