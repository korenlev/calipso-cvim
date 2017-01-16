import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { portRegEx } from '/imports/lib/general-regex';

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
