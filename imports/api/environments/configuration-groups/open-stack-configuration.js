import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { portRegEx } from '/imports/lib/general-regex';

export const OpenStackSchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'OpenStack'; } },
  host: { 
    type: String,
    regEx: SimpleSchema.RegEx.IP,
    defaultValue: '10.0.0.1',
  },
  admin_token: { type: String },
  port: { 
    type: String, 
    regEx: portRegEx,
    defaultValue: '5000',
  },
  user: { 
    type: String,
    defaultValue: 'adminuser'
  },
  pwd: { type: String },
});