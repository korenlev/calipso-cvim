import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';

export const Environments = new Mongo.Collection('environments_config');

Environments.schema = new SimpleSchema({
  _id: { type: String, regEx: SimpleSchema.RegEx.Id },
  configuration: { type: [Object] },
  distribution: { type: String },
  last_scanned: { type: String },
  name: { type: String },
  network_plugins: { type: [Object] },
  operational: { type: String },
  scanned: { type: Boolean },
  type: { type: String }
});
