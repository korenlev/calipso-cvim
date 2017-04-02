import { Meteor } from 'meteor/meteor';
import { Counts } from 'meteor/tmeasday:publish-counts';
import { Messages } from '../messages.js';

Meteor.publish('messages', function () {
  console.log('server subscribtion to: messages');
  //return Inventory.find({$where: 'this.id_path.match('^/WebEX-Mirantis@Cisco/')'});
  //return Inventory.find({ 'show_in_tree': true });
  return Messages.find({});
});

Meteor.publish('messages?_id', function (_id) {
  console.log('server subscribtion to: messages?_id');
  console.log('_id', _id);

  let query = { _id: _id };
  return Messages.find(query);
});

Meteor.publish('messages?level', function (level) {
  var query = {
    level: level
  };

  var counterName = 'messages?level!counter?' +
    'level=' + level;

  console.log('server subscription to: ' + counterName);
  Counts.publish(this, counterName, Messages.find(query));

  console.log('server subscribtion to: messages?level');
  console.log('- level: ' + level);
  return Messages.find(query);
});

Meteor.publish('messages?env+level', function (env, level) {
  var query = {
    environment: env,
    level: level
  };
  var counterName = 'messages?env+level!counter?env=' +
    env + '&level=' + level;

  console.log('server subscription to: messages - counter');
  console.log(' - name: ' + counterName);
  Counts.publish(this, counterName, Messages.find(query));

  console.log('server subscribtion to: messages');
  console.log('- env: ' + env);
  console.log('- level: ' + level);
  return Messages.find(query);
});
