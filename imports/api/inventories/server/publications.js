import { Meteor } from 'meteor/meteor';
import { Counts } from 'meteor/tmeasday:publish-counts';
import { check } from 'meteor/check';
//import * as R from 'ramda';

import { Inventory } from '../inventories.js';
import { regexEscape } from '/imports/lib/regex-utils';

Meteor.publish('inventory', function () {
  console.log('server subscribtion to: inventory');
    //return Inventory.find({$where: 'this.id_path.match('^/WebEX-Mirantis@Cisco/')'});
    //return Inventory.find({ 'show_in_tree': true });
  return Inventory.find({});
});

Meteor.publish('inventory?id', function (id) {
  console.log('server subscribtion to: inventory?id');
  return Inventory.find({id: id});
});

Meteor.publish('inventory?id_path', function (id_path) {
  console.log('server subscribtion to: inventory?id_path');
  return Inventory.find({id_path: id_path});
});

Meteor.publish('inventory?_id-in', function (idsList) {
  var query = {
    _id: { $in: idsList }
  };
  /*
    var counterName = 'inventory?env+type!counter?env=' + env + '&type=' + type;

    console.log('server subscribing to counter: ' + counterName);
    Counts.publish(this, counterName, Inventory.find(query));
  */
  console.log('server subscribtion to: inventory?_id-in');
  console.log('- id-in: ' + idsList);

  return Inventory.find(query); 
});

Meteor.publish('inventory?env+type', function (env, type) {
  var query = {
    environment: env,
    type: type
  };
  var counterName = 'inventory?env+type!counter?env=' + env + '&type=' + type;

  console.log('server subscribing to counter: ' + counterName);
  Counts.publish(this, counterName, Inventory.find(query));

  console.log('server subscribtion to: inventory-by-env-and-type');
  console.log('-env: ' + env);
  console.log('-type: ' + type);

  return Inventory.find(query); 
});

Meteor.publish('inventory?env+name', function (env, name) {
  var query = {
    name: name,
    environment: env
  };

  console.log('server subscribtion to: inventory?env+name');
  console.log('- name: ' + name);
  console.log('- env: ' + env);

  return Inventory.find(query); 
});

Meteor.publish('inventory?type+host', function (type, host) {
  var query = {
    type: type,
    host: host
  };
/*
  var counterName = 'inventory?env+type!counter?env=' + env + '&type=' + type;

  console.log('server subscribing to counter: ' + counterName);
  Counts.publish(this, counterName, Inventory.find(query));
*/

  console.log('server subscribtion to: inventory?type+host');
  console.log('- type: ' + type);
  console.log('- host: ' + host);
  return Inventory.find(query); 
});

Meteor.publish('inventory?id_path_start&type', function (id_path, type) {
  check(id_path, String);
  check(type, String);

  let idPathExp = new RegExp(`^${regexEscape(id_path)}`);

  let query = {
    id_path: idPathExp,
    type: type
  };

  var counterName = 'inventory?id_path_start&type!counter?id_path_start=' + 
    id_path + '&type=' + type;

  console.log('server subscribing to counter: ' + counterName);
  Counts.publish(this, counterName, Inventory.find(query));

  console.log('server subscribtion to: inventory?id_path_start&type');
  console.log('-id_path_start: ' + id_path);
  console.log('-type: ' + type);
  return Inventory.find(query);
});


Meteor.publish('inventory.children', function (nodeId) {
  console.log('server subscribtion to: inventory.children');
  console.log('node id: ' + nodeId.toString());

  return Inventory.find({
    parent_id: nodeId
  });    
});

Meteor.publish('inventory.first-child', function (nodeId) {
  console.log('server subscribing to: inventory.first-child');
  console.log('node id: ' + nodeId.toString());

  var counterName = 'inventory.first-child!counter!id=' + nodeId;
  Counts.publish(this, counterName, 
    Inventory.find({
      parent_id: nodeId
    }, {
      limit: 1
    }));
  console.log('server subscribing to counter: ' + counterName);

// todo: eyaltask: all criteria
  return Inventory.find({
    parent_id: nodeId
  }, {
    limit: 1
  });
});

Meteor.publish('inventoryByEnv', function (env) {
  console.log('server subscribtion to: inventoryByEnv');
  //return Inventory.find({$where: 'this.id_path.match('^/WebEX-Mirantis@Cisco/')'});
  //return Inventory.find({ 'show_in_tree': true });
  return Inventory.find({'environment':env});
});

