import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
import { Constants } from '/imports/api/constants/constants';
import { MysqlSchema } from './configuration-groups/mysql-configuration';
import { OpenStackSchema } from './configuration-groups/open-stack-configuration';
import { MonitoringSchema } from './configuration-groups/monitoring-configuration';
import { CLISchema } from './configuration-groups/cli-configuration';
import { AMQPSchema } from './configuration-groups/amqp-configuration';
import { NfvProviderSchema } from './configuration-groups/nfv-provider-configuration';

export const Environments = new Mongo.Collection('environments_config');

export const requiredConfGroups = [
  'mysql',
  'OpenStack',
  'CLI',
  'AMQP',
  'Monitoring'
];

export const optionalConfGroups = [
  'NFV_provider'
];

Environments.schema = new SimpleSchema({
  _id: { type: { _str: { type: String, regEx: SimpleSchema.RegEx.Id } } },
  configuration: { 
    type: [Object],
    blackbox: true,
    autoValue: function () {
      let that = this;

      if (that.isSet) {
        let confGroups = that.value;
        confGroups = cleanOptionalGroups(confGroups, optionalConfGroups);

        let newValue = R.map(function(confGroup) {
          let schema = getSchemaForGroupName(confGroup.name);
          return schema.clean(confGroup);
        }, confGroups);

        return newValue;
      } else {
        let newValue = R.map((confName) => {
          let schema = getSchemaForGroupName(confName);
          return schema.clean({});
        }, requiredConfGroups);
        return newValue;
      }
    },
    custom: function () {
      let that = this;
      let configurationGroups = that.value;

      let subErrors = [];

      let invalidResult = R.find(function(groupName) {
        subErrors = checkGroup(groupName, configurationGroups, true);
        if (subErrors.length > 0) { return true; } 
        return false;
      }, requiredConfGroups);

      if (R.isNil(invalidResult)) {
        invalidResult = R.find(function(groupName) {
          subErrors = checkGroup(groupName, configurationGroups, false);
          if (subErrors.length > 0) { return true; } 
          return false;
        }, optionalConfGroups);
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
  user: { 
    type: String,
    defaultValue: 'osdna_user'
  }, 
  distribution: { 
    type: String, 
    defaultValue: 'Mirantis-8.0',
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
  last_scanned: { 
    type: String, defaultValue: '' 
  },
  name: { 
    type: String, 
    defaultValue: 'MyEnvironmentName',
    min: 6,
  },
  type_drivers: { 
    type: String, 
    defaultValue: 'gre',
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
    defaultValue: ['ovs'],
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
  },
  app_path: { 
    type: String, 
    autoValue: function () { 
      return '/etc/osdna/monitoring'; 
    } 
  },
  listen: { 
    type: Boolean, 
    defaultValue: true,
  }, 
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
  case 'Monitoring':
    return MonitoringSchema;
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

function cleanOptionalGroups(confGroups, optionalConfGroups) {
  return R.filter((conf) => {
    if (R.contains(conf.name, optionalConfGroups)) {
      return !isConfEmpty(conf);     
    } 

    return true;
  }, confGroups);
}

function isConfEmpty(conf) {
  return ! R.any((key) => { 
    if (key === 'name') { return false; } // We ignore the key 'name'. It is a 'type' key.
    let val = conf[key];
    return ! ( R.isNil(val) || R.isEmpty(val)); 
  })(R.keys(conf));
}
