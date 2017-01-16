import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
import { Constants } from '/imports/api/constants/constants';
import { portRegEx } from '/imports/lib/general-regex';
import { hostnameRegex } from '/imports/lib/general-regex';
import { ipAddressRegex } from '/imports/lib/general-regex';

export const MonitoringSchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'Monitoring'; } },
  //app_path: { type: String, autoValue: function () { return '/etc/osdna/monitoring'; } },
  config_folder: { 
    type: String, 
    autoValue: function () { return '/tmp/sensu_test'; } 
  },
  debug: { 
    type: Boolean, 
    autoValue: function () { return false; } 
  },
  event_based_scan: { 
    type: Boolean, 
    defaultValue: true 
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
  port: {
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
    regEx: new RegExp(hostnameRegex.source + '|' + ipAddressRegex.soure)
  },
  server_name: {
    type: String,
  },
  type: {
    type: String,
    defaultValue: 'Sensu'
  }
});
