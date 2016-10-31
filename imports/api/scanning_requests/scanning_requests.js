import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';

export const ScanningRequests = new Mongo.Collection('scanning_requests');
console.log('creating collection: scanning_requests');

ScanningRequests.schemaRelated = {
  environment_name: {
    label: 'Environment',
    description: 'name of environment to scan (default: WebEX-Mirantis@Cisco)',
    command: 'env',
    shortCommand: 'e',
  },
  cgi: {
    label: 'CGI',
    description: 'read argument from CGI (true/false) (default: false)',
    command: 'cgi',
    shortCommand: 'c',
  },
  mongo_config: {
    label: 'Mongo config',
    description: 'name of config file with MongoDB servr access details',
    command: 'mongo_config',
    shortCommand: 'm',
  },
  type: {
    label: 'Type',
    description: 'type of object to scan (default: environment)',
    command: 'type',
    shortCommand: 't',
  },
  inventory: {
    label: 'Inventory',
    description: 'name of inventory collection (default: inventory)',
    command: 'inventory',
    shortCommand: 'y',
  },
  scan_self: {
    label: 'Scan self',
    description: 'scan changes to a specific object (default: False)',
    command: 'scan_self',
    shortCommand: 's',
  },
  id: {
    label: 'Object Id',
    description: 'ID of object to scan (when scan_self=true)',
    command: 'id',
    shortCommand: 'i',
  },
  parent_id: {
    label: 'Parent ID',
    description: 'ID of parent object (when scan_self=true)',
    command: 'parent_id',
    shortCommand: 'p',
  },
  parent_type: {
    label: 'Parent type',
    description: 'type of parent object (when scan_self=true)',
    command: 'parent_type',
    shortCommand: 'a',
  },
  id_field: {
    label: 'Id field',
    description: ' name of ID field (when scan_self=true) (default: "id",use "name" for projects)',
    command: 'id_field',
    shortCommand: 'f', 
  },
  loglevel: {
    label: 'Log level',
    description: 'logging level (default: "INFO")',
    command: 'loglevel',
    shortCommand: 'l',
  },
  inventory_only: {
    label: 'Inventory only',
    description: 'do only scan to inventory (default: False)',
    command: 'inventory_only',
  },
  links_only: {
    label: 'Links only',
    description: 'do only links creation (default: False)',
    command: 'links_only',
  },
  cliques_only: {
    label: 'Cliques only',
    description: 'do only cliques creation (default: False)',
    command: 'cliques_only',
  },
  clear: {
    label: 'Clear only',
    description: 'clear all data prior to scanning (default: False)',
    command: 'clear'
  }
};

let schema = {
  _id: { type: { _str: { type: String, regEx: SimpleSchema.RegEx.Id } } },
  environment_name: { 
    type: String 
  }, 
  cgi: { 
    type: Boolean, 
    defaultValue: false,
    optional: true,
  },
  mongo_config: { 
    type: String, 
    optional: true,
  },
  type: {
    type: String,
    optional: true,
  },
  inventory: {
    type: String,
    optional: true,
  },
  scan_self: {
    type: String,
    optional: true,
  },
  id: {
    type: String,
    optional: true,
  },
  parent_id: {
    type: String,
    optional: true,
  },
  parent_type: {
    type: String,
    optional: true,
  },
  id_field: {
    type: String,
    optional: true,
  },
  loglevel: {
    type: String,
    optional: true,
  },
  inventory_only: {
    type: Boolean,
    optional: true,
  },
  links_only: {
    type: Boolean,
    optional: true,
  },
  cliques_only: {
    type: Boolean,
    optional: true,
  },
  clear: {
    type: Boolean,
    optional: true,
  },
};

ScanningRequests.schema = new SimpleSchema(schema);
ScanningRequests.attachSchema(ScanningRequests.schema);

ScanningRequests.schemaRelated = R.mapObjIndexed((relatedItem, key) => {
  return R.merge(relatedItem, {
    type: schema[key].type 
  });

}, ScanningRequests.schemaRelated);
