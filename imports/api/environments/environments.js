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
  label: 'OSV',
}, {
  label: 'VPP',
}];

Environments.schema = new SimpleSchema({
  _id: { type: String, regEx: SimpleSchema.RegEx.Id },
  configuration: { 
    type: [Object],
    custom: function () {
      let that = this;
      let configurationGroups = that.value;

      let requiredGroups = [
        'mysql',
        'OpenStack',
        'CLI',
        'AMQP'
      ];

      let invalidResult = R.find(function(groupName) {
        let confGroup = R.find(R.propEq('name', groupName), configurationGroups); 
        if (R.isNil(confGroup)) { return true; }

        let validationContext = getSchemaForGroupName(groupName).newContext();
        if (! validationContext.validate(confGroup)) {
          return true; 
        }

        return false;
      }, requiredGroups);

      if (! R.isNil(invalidResult)) {
        return 'keyNotISchema';
        // todo: return custom message.
      }
    },
    defaultValue: [{
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
      password: 'admin',
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
      user: '',
      password: ''
    }
    ]
  },
  distribution: { 
    type: String, 
    allowedValues: Distributions
  }, 
  last_scanned: { type: String },
  name: { type: String, defaultValue: 'Env Name' },
  network_plugins: { 
    type: [Object],
    allowedValues: NetworkPlugins
  },
  operational: { type: String },
  scanned: { type: Boolean },
  type: { type: String }
});

export const MysqlSchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'mysql'; } },
  host: { type: String },
  password: { type: String },
  port: { type: String },
  user: { type: String },
  schema: { type: String },
});

export const OpenStackSchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'OpenStack'; } },
  host: { type: String },
  asmin_token: { type: String },
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

function getSchemaForGroupName(groupName) {
  switch (groupName) {
  case 'mysql': 
    return MysqlSchema;
  case 'OpenStack':
    return OpenStackSchema;
  case 'CLI':
    return CLISchema;
  case 'AMQPSchema':
    return AMQPSchema;
  default:
    throw 'not implemented';
  }
}
