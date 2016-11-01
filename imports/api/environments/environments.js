import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
import { Constants } from '/imports/api/constants/constants';

let portRegEx = /^0*(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9])$/;

let pathRegEx = /^(\/){1}([^\/\0]+(\/)?)+$/;

export const Environments = new Mongo.Collection('environments_config');

let defaultGroups = [{
  name: 'mysql',
  host: '10.0.0.1',
  password: 'abcdefg123456',
  port: '3307.0',
  user: 'user',
}, {
  name: 'OpenStack',
  host: '10.0.0.1',
  admin_token: 'abcd1234',
  port: '5000',
  user: 'admin',
  pwd: 'admin',
}, {
  name: 'CLI',
  host: '10.0.0.1',
  key: '',
  pwd: '',
  user: '',
}, {
  name: 'AMQP',
  host: '10.0.0.1',
  port: '5673',
  user: 'User',
  password: 'abcd1234'
}, {
  name: 'NFV_provider',
  host: '10.0.0.1',
  admin_token: 'abcdefg1234',
  port: '5000',
  user: 'admin',
  pwd: 'admin',
}
    ];

Environments.schema = new SimpleSchema({
  _id: { type: { _str: { type: String, regEx: SimpleSchema.RegEx.Id } } },
  configuration: { 
    type: [Object],
    blackbox: true,
    autoValue: function () {
      let that = this;
      if (that.isSet) {
        let newValue = R.map(function(confGroup) {
          let schema = getSchemaForGroupName(confGroup.name);
          return schema.clean(confGroup);
        }, that.value);

        return newValue;
      } else {
        return defaultGroups;
      }
    },
    custom: function () {
      let that = this;
      let configurationGroups = that.value;

      let requiredGroups = [
        'mysql',
        'OpenStack',
        'CLI',
        'AMQP',
      ];

      let subErrors = [];

      let invalidResult = R.find(function(groupName) {
        subErrors = checkGroup(groupName, configurationGroups, true);
        if (subErrors.length > 0) { return true; } 
        return false;
      }, requiredGroups);

      if (R.isNil(invalidResult)) {
        subErrors = checkGroup('NFV_provider', configurationGroups, false);
        if (subErrors.length > 0) {
          invalidResult = {};
        }
      }

      if (! R.isNil(invalidResult)) {
        throw {
          isError: true,
          type: 'subGroupError',
          data: subErrors,
          message: constructSubGroupErrorMessage(subErrors)
        };
      }
    },

  },
  user: { type: String }, 
  distribution: { 
    type: String, 
    defaultValue: null,
    custom: function () {
      let that = this;
      let constsDist = Constants.findOne({ name: 'distributions' });

      if (R.isNil(constsDist.data)) { return 'notAllowed'; } 
      let distributions = constsDist.data;

      if (R.isNil(R.find(R.propEq('value', that.value), distributions))) {
        return 'notAllowed';
      }
    },
  }, 
  last_scanned: { type: String, defaultValue: '' },
  name: { 
    type: String, 
    defaultValue: null,
    min: 6,
  },
  type_drivers: { 
    type: String, 
    defaultValue: null,
    custom: function () {
      let that = this;
      let TypeDriversRec = Constants.findOne({ name: 'type_drivers' });

      if (R.isNil(TypeDriversRec.data)) { return 'notAllowed'; } 
      let TypeDrivers = TypeDriversRec.data;

      if (R.isNil(R.find(R.propEq('value', that.value), TypeDrivers))) {
        return 'notAllowed';
      }
    },
  }, 
  mechanism_drivers: { 
    type: [String],
    defaultValue: [],
    minCount: 1,
    custom: function () {
      let that = this;
      let consts = Constants.findOne({ name: 'mechanism_drivers' });

      if (R.isNil(consts.data)) { return 'notAllowed'; } 
      let mechanismDrivers = consts.data;

      let result = R.find((driver) => {
        if (R.find(R.propEq('value', driver), mechanismDrivers)) {
          return false;
        }
        return true;
      }, that.value);

      if (result) { return 'notAllowed'; }

    },
  },
  operational: { 
    type: String, 
    allowedValues: ['yes', 'no'],
    defaultValue: 'no'
  },
  scanned: { type: Boolean, defaultValue: false },
  type: { 
    type: String, 
    autoValue: function () {
      return 'environment';
    },
  }
});

// Bug in simple schema. cant add custom message to instance specific
// schema.
// https://github.com/aldeed/meteor-simple-schema/issues/559
// Version 2 fixes it but it is rc.
//Environments.schema.messages({ 
SimpleSchema.messages({
  confGroupInvalid: 'Configuration group is invalid.'  
});

Environments.attachSchema(Environments.schema);

export const MysqlSchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'mysql'; } },
  host: { 
    type: String,
    regEx: SimpleSchema.RegEx.IP,
  },
  password: { type: String },
  port: { 
    type: String,
    regEx: portRegEx
  },
  user: { type: String, min: 3 },
});

export const OpenStackSchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'OpenStack'; } },
  host: { 
    type: String,
    regEx: SimpleSchema.RegEx.IP,
  },
  admin_token: { type: String },
  port: { 
    type: String, 
    regEx: portRegEx
  },
  user: { type: String },
  pwd: { type: String },
});

export const CLISchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'CLI'; } },
  host: { type: String },
  key: { 
    type: String,
    regEx: pathRegEx,
    optional: true
  },
  user: { type: String },
  pwd: { 
    type: String,
    optional: true
  },
});

CLISchema.addValidator(function () {
  let that = this;
  let password = that.field('password');
  let key = that.field('key');

  if (key.value || password.value) { return; }

  throw {
    isError: true,
    type: 'subGroupError',
    data: [],
    message: 'Master Host Group: At least one required: key or password'
  };
});

export const AMQPSchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'AMQP'; } },
  host: { 
    type: String,
    regEx: SimpleSchema.RegEx.IP,
  },
  port: { 
    type: String, 
    regEx: portRegEx
  },
  user: { type: String },
  password: { type: String },
});

export const NfvProviderSchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'NFV_provider'; } },
  host: { 
    type: String,
    regEx: SimpleSchema.RegEx.IP,
  },
  admin_token: { type: String },
  port: { 
    type: String, 
    regEx: portRegEx
  },
  user: { type: String },
  pwd: { type: String },
});

function getSchemaForGroupName(groupName) {
  switch (groupName) {
  case 'mysql': 
    return MysqlSchema;
  case 'OpenStack':
    return OpenStackSchema;
  case 'CLI':
    return CLISchema;
  case 'AMQP':
    return AMQPSchema;
  case 'NFV_provider':
    return NfvProviderSchema; 
  default:
    throw 'group name is not recognized. group: ' + groupName;
  }
}

function constructSubGroupErrorMessage(errors) {
  let message = 'Validation errors on sub groups:'; 
  message = message + R.reduce((acc, item) => {
    return acc + '\n- ' + item.group + ': ' + item.message;  
  }, '', errors);

  return message;
}

function checkGroup(groupName, configurationGroups, groupRequired) {
  let subErrors = [];
  let confGroup = R.find(R.propEq('name', groupName), configurationGroups); 
  
  if (R.isNil(confGroup)) { 
    if (groupRequired) { 
      subErrors = R.append({
        field: 'configuration',
        group: groupName, 
        message: 'group ' + groupName + ' is required'
      }, subErrors);
    }
    return subErrors;
  }

  let validationContext = getSchemaForGroupName(groupName).newContext();

  if (! validationContext.validate(confGroup)) {
    subErrors = R.reduce(function (acc, invalidField) {
      return R.append({
        field: invalidField,
        group: groupName,
        message: validationContext.keyErrorMessage(invalidField.name),
      }, acc);
    }, [], validationContext.invalidKeys());

    return subErrors; 
  }

  return subErrors;
}

export function createNewConfGroup(groupName) {
  let schema = getSchemaForGroupName(groupName);
  return schema.clean({});
}
