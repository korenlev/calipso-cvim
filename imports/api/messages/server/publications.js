import { Meteor } from 'meteor/meteor';
import { Counts } from 'meteor/tmeasday:publish-counts';
import { Messages } from '../messages.js';
import * as R from 'ramda';

Meteor.publish('messages', function () {
  console.log('server subscribtion to: messages');
  //return Inventory.find({$where: 'this.id_path.match('^/WebEX-Mirantis@Cisco/')'});
  //return Inventory.find({ 'show_in_tree': true });
  return Messages.find({});
});

Meteor.publish('messages?page&amount&sortField&sortDirection', function (
  page, amountPerPage, sortField, sortDirection) {

  console.log('server subscribtion to: messages?page&amount&sortField&sortDirection');
  console.log('page: ', page);
  console.log('amount: ', amountPerPage);
  console.log('sortField: ', sortField, R.isNil(sortField));
  console.log('sortDirection: ', sortDirection);

  let skip = (page - 1) * amountPerPage;

  let query = {};
  let sortParams = {};

  sortParams = R.ifElse(R.isNil, R.always(sortParams), 
      R.assoc(R.__, sortDirection, sortParams))(sortField);

  console.log('sort params:', sortParams);

  let qParams = {
    limit: amountPerPage,
    skip: skip,
    sort: sortParams,
  };

  let counterName = 'messages?page&amount!count?page=' + R.toString(page) + 
    '&amount=' + R.toString(amountPerPage);

  Counts.publish(this, counterName, Messages.find(query), {
    noReady: true
  });

  console.log('counter name', counterName);

  return Messages.find(query, qParams);
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

Meteor.publish('messages?env&level&page&amount', function (env, level, page, amountPerPage) {
  console.log('subscribe: messages?env&level&page&amount');
  console.log('-env', env);
  console.log('-level', level);
  console.log('-page', page);
  console.log('-amountPerPage', amountPerPage);

  let skip = (page - 1) * amountPerPage;

  let query = {
    level: level
  };

  query = R.ifElse(R.isNil, R.always(query), R.assoc('environment', R.__, query))(env);

  var counterName = 'messages?env&level&page&amount!counter?env=' +
    R.toString(env) + 
    '&level=' + R.toString(level) +
    '&page=' + R.toString(page) +
    '&amount=' + R.toString(amountPerPage);

  let qParams = {
    limit: amountPerPage,
    skip: skip
  };

  Counts.publish(this, counterName, Messages.find(query), {
    noReady: true
  });

  console.log('-counter name:', counterName);

  return Messages.find(query, qParams);
});
