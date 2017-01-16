import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { portRegEx } from '/imports/lib/general-regex';

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
