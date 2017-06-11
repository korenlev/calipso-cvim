import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
import { Environments } from '/imports/api/environments/environments';
import { Constants } from '/imports/api/constants/constants';

export const Messages = new Mongo.Collection('messages', { idGeneration: 'MONGO' });

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

  id: {
    type: String
  }, 

  viewed: {
    type: Boolean,
    defaultValue: false
  },

  display_context: {
    type: String
  },

  message: {
    type: Object,
    blackbox: true
  },

  source_system: {
    type: String,
    custom: function () {
      let that = this;
      let values = Constants.findOne({ name: 'messages_source_systems' }).data;

      if (R.isNil(R.find(R.propEq('value', that.value), values))) {
        return 'notAllowed';
      }
    }
  },

  level: {
    type: String
  },

  timestamp: {
    type: Date
  },

  related_object_type: {
    type: String
  },

  related_object: {
    type: String
  },

  scan_id: {
    type: Date
  }
};

let simpleSchema = new SimpleSchema(schema);

Messages.schema = simpleSchema;
Messages.attachSchema(Messages.schema);
