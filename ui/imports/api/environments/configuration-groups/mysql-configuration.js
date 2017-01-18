import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { portRegEx } from '/imports/lib/general-regex';

export const MysqlSchema = new SimpleSchema({
  name: { 
    type: String, 
    autoValue: function () { return 'mysql'; } 
  },
  host: { 
    type: String,
    regEx: SimpleSchema.RegEx.IP,
    defaultValue: '10.0.0.1'
  },
  password: { type: String },
  port: { 
    type: String,
    regEx: portRegEx,
    defaultValue: '3307'
  },
  user: { 
    type: String, 
    min: 3,
    defaultValue: 'mysqluser'
  },
});
