import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';

export const Environments = new Mongo.Collection('environments_config');

export const Distributions = [{
  label: 'Mirantis-6.0',
}, {
  label: 'Mirantis-7.0',
}, {
  label: 'Mirantis-8.0',
}, {
  label: 'Mirantis-9.0',
}, { 
  label: 'RDO-Mitaka',
}, {
  label: 'RDO-Liberty',
}, {
  label: 'RDO-Juno',
}, {
  label: 'RDO-kilo',
}, {
  label: 'devstack-liberty',
}, {
  label: 'Canonical-icehouse', 
}, {
  label: 'Canonical-juno',
}, {
  label: 'Canonical-liberty',
}, {
  label: 'Canonical-mitaka',
}, {
  label: 'Apex-Mitaka',
}, {
  label: 'Devstack-Mitaka',
}, {
  label: 'packstack-7.0.0-0.10.dev1682'
}
]; 

export const NetworkPlugins = [{
  label: 'OVS',
}, {
  label: 'VPP',
}];

let defaultGroups = [{
  name: 'mysql',
  host: '10.0.0.1',
  password: 'abcdefg123456',
  port: '3307.0',
  user: 'user',
  schema: '',
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
  name: 'NFV provider',
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
        'NFV provider',
      ];

      let subErrors = null;

      let invalidResult = R.find(function(groupName) {
        let confGroup = R.find(R.propEq('name', groupName), configurationGroups); 
        if (R.isNil(confGroup)) { 
          console.log('validation error  - conf group missing - ' + groupName);
          return true; 
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

          return true; 
        }

        return false;
      }, requiredGroups);

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
  distribution: { 
    type: String, 
    allowedValues: R.map(R.prop('label'), Distributions),
    defaultValue: null,
  }, 
  last_scanned: { type: String, defaultValue: '' },
  name: { 
    type: String, 
    defaultValue: null,
    min: 6,
  },
  network_plugins: { 
    type: [String],
    allowedValues: R.map(R.prop('label'), NetworkPlugins),
    defaultValue: [],
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
  host: { type: String },
  password: { type: String },
  port: { type: String },
  user: { type: String, min: 3 },
  schema: { type: String },
});

export const OpenStackSchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'OpenStack'; } },
  host: { type: String },
  admin_token: { type: String },
  port: { type: String },
  user: { type: String },
  pwd: { type: String },
});

export const CLISchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'CLI'; } },
  host: { type: String },
  key: { type: String },
  user: { type: String },
  pwd: { type: String },
});

export const AMQPSchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'AMQP'; } },
  host: { type: String },
  port: { type: String },
  user: { type: String },
  password: { type: String },
});

export const NfvProviderSchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'NFV provider'; } },
  host: { type: String },
  admin_token: { type: String },
  port: { type: String },
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
  case 'NFV provider':
    return NfvProviderSchema; 
  default:
    throw 'not implemented';
  }
}

function constructSubGroupErrorMessage(errors) {
  let message = 'Validation errors on sub groups:'; 
  message = message + R.reduce((acc, item) => {
    return acc + '\n- ' + item.group + ': ' + item.message;  
  }, '', errors);

  return message;
}

export function createNewConfGroup(groupName) {
  let schema = getSchemaForGroupName(groupName);
  return schema.clean({});
}
