import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { portRegEx } from '/imports/lib/general-regex';

export const AMQPSchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'AMQP'; } },
  host: { 
    type: String,
    regEx: SimpleSchema.RegEx.IP,
    defaultValue: '10.0.0.1',
  },
  port: { 
    type: String, 
    regEx: portRegEx,
    defaultValue: '5673',
  },
  user: { 
    type: String, 
    defaultValue: 'rabbitmquser'
  },
  password: { type: String },
});
