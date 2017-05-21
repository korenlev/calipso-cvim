import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
import { Constants } from '/imports/api/constants/constants';
import { portRegEx } from '/imports/lib/general-regex';
import { hostnameRegex } from '/imports/lib/general-regex';
import { ipAddressRegex } from '/imports/lib/general-regex';
import { pathRegEx } from '/imports/lib/general-regex';

export const MonitoringSchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'Monitoring'; } },
  //app_path: { type: String, autoValue: function () { return '/etc/calipso/monitoring'; } },
  
  config_folder: { 
    type: String, 
    defaultValue: '/tmp/sensu_config',
    regEx: pathRegEx,
  },

  env_type: { 
    type: String, 
    defaultValue: 'production',
    custom: function () {
      let that = this;
      let EnvTypesRec = Constants.findOne({ name: 'env_types' });

      if (R.isNil(EnvTypesRec.data)) { return 'notAllowed'; } 
      let EnvTypes = EnvTypesRec.data;

      if (R.isNil(R.find(R.propEq('value', that.value), EnvTypes))) {
        return 'notAllowed';
      }
    },
  },

  rabbitmq_port: {
    type: String,
    defaultValue: 4567,
    regEx: portRegEx,
  },

  rabbitmq_user: { 
    type: String,
    defaultValue: 'sensu'
  }, 

  rabbitmq_pass: { type: String },

  server_ip: {
    type: String,
    regEx: new RegExp(hostnameRegex.source + '|' + ipAddressRegex.soure),
    defaultValue: '10.0.0.1',
  },

  server_name: {
    type: String,
    defaultValue: 'sensu_server',
  },

  type: {
    type: String,
    defaultValue: 'Sensu',
    custom: function () {
      let that = this;
      let values = Constants.findOne({ name: 'environment_monitoring_types' }).data;

      if (R.isNil(values)) { return 'notAllowed'; } 

      if (R.isNil(R.find(R.propEq('value', that.value), values))) {
        return 'notAllowed';
      }
    },
  },

  provision: {
    type: String,
    defaultValue: 'None',
    custom: function () {
      let that = this;
      let values = Constants.findOne({ name: 'environment_provision_types' }).data;

      if (R.isNil(values)) { return 'notAllowed'; } 

      if (R.isNil(R.find(R.propEq('value', that.value), values))) {
        return 'notAllowed';
      }
    },
  },

  ssh_port: {
    type: String,
    defaultValue: '20022',
    optional: true
  },

  ssh_user: {
    type: String,
    defaultValue: 'root',
    optional: true
  },

  ssh_password: {
    type: String,
    defaultValue: 'calipso',
    optional: true
  },
});
