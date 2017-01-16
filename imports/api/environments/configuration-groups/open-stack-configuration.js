import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { portRegEx } from '/imports/lib/general-regex';

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
