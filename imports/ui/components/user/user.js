/*
 * Template Component: User 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { parseReqId } from '/imports/lib/utilities';
import * as R from 'ramda';
import { remove, insert, update } from '/imports/api/accounts/methods';
        
import './user.html';     
    
/*  
 * Lifecycles
 */   
  
Template.User.onCreated(function() {
  let instance = this;
  instance.state = new ReactiveDict();
  instance.state.setDefault({
    id: null,
    //env: null,
    action: 'insert',
    isError: false,
    isSuccess: false,
    isMessage: false,
    message: null,
    disabled: false,
    notifications: {},
    model: {},
    pageHeader: 'User'
  });

  instance.autorun(function () {
    let controller = Iron.controller();
    let params = controller.getParams();
    let query = params.query;

    new SimpleSchema({
      action: { type: String, allowedValues: ['insert', 'view', 'remove', 'update'] },
      //env: { type: String, optional: true },
      id: { type: String, optional: true }
    }).validate(query);

    switch (query.action) {
    case 'insert':
      initInsertView(instance, query); 
      break;

    case 'view':
      initViewView(instance, query);
      break;

    case 'update':
      initUpdateView(instance, query);
      break;

    case 'remove':
      initRemoveView(instance, query);
      break;

    default:
      throw 'unimplemented action';
    }
  });
});  

/*
Template.User.rendered = function() {
};  
*/

/*
 * Events
 */

Template.User.events({
  'submit .sm-item-form': function(event, instance) {
    event.preventDefault(); 

    let _id = instance.state.get('id');
    let username = instance.$('.sm-input-username')[0].value;
    let password = instance.$('.sm-input-password')[0].value; 

    submitItem(instance,
      _id,
      username,
      password
    ); 
  }
});
   
/*  
 * Helpers
 */

Template.User.helpers({    
  isUpdateableAction() {
    let instance = Template.instance();
    let action = instance.state.get('action');

    return R.contains(action, ['insert', 'update', 'remove']);
  },

  getState: function (key) {
    let instance = Template.instance();
    return instance.state.get(key);
  },

  getAttrDisabled: function () {
    let instance = Template.instance();
    let result = {};
    let action = instance.state.get('action');

    if (R.contains(action, ['view', 'remove'])) {
      result = R.assoc('disabled', true, result);
    }

    return result;
  },

  getModelField: function (fieldName) {
    let instance = Template.instance();
    return R.path([fieldName], instance.state.get('model'));
  },

  actionLabel: function () {
    let instance = Template.instance();
    let action = instance.state.get('action');
    return calcActionLabel(action);
  }
});


function initInsertView(instance, query) {
  instance.state.set('action', query.action);
  //instance.state.set('env', query.env);
  
  instance.state.set('model', 
    {
      username: '',
      password: ''
    }
    /*.schema.clean({
    //environment: instance.state.get('env')
    })
    */
  );

  subscribeToOptionsData(instance);
  //instance.subscribe('constants');
  //instance.subscribe('link_types?env', query.env);
}

function initViewView(instance, query) {
  let reqId = parseReqId(query.id);

  instance.state.set('action', query.action);
  //instance.state.set('env', query.env);
  instance.state.set('id', reqId);

  //subscribeToOptionsData(instance);
  //instance.subscribe('constants');
  //instance.subscribe('link_types?_id', reqId.id);

  Meteor.users.find({ _id: reqId.id }).forEach((model) => {
    instance.state.set('model', {
      username: model.username,
      password: ''
    });
  }); 
}

function initUpdateView(instance, query) {
  let reqId = parseReqId(query.id);

  instance.state.set('action', query.action);
  //instance.state.set('env', query.env);
  instance.state.set('id', reqId);

  //subscribeToOptionsData(instance);
  //instance.subscribe('constants');
  //instance.subscribe('link_types?_id', reqId.id);

  Meteor.users.find({ _id: reqId.id }).forEach((model) => {
    instance.state.set('model', {
      username: model.username,
      password: ''
    });
  }); 
}

function initRemoveView(instance, query) {
  initViewView(instance, query);
}

function subscribeToOptionsData(_instance) {
  //instance.subscribe('environments_config');
}

function submitItem(
  instance, 
  id, 
  username,
  password
  ){

  let action = instance.state.get('action');

  instance.state.set('isError', false);
  instance.state.set('isSuccess', false);
  instance.state.set('isMessage', false);
  instance.state.set('message', null);

  switch (action) {
  case 'insert':
    insert.call({
      username: username,
      password: password,
    }, processActionResult.bind(null, instance));
    break;

  case 'update': 
    update.call({
      _id: id.id,
      password: password,
    }, processActionResult.bind(null, instance));
    break;

  case 'remove':
    remove.call({
      _id: id.id
    }, processActionResult.bind(null, instance));
    break;

  default:
      // todo
    break;
  }
}

function processActionResult(instance, error) {
  let action = instance.state.get('action');

  if (error) {
    instance.state.set('isError', true);
    instance.state.set('isSuccess', false);
    instance.state.set('isMessage', true);

    if (typeof error === 'string') {
      instance.state.set('message', error);
    } else {
      instance.state.set('message', error.message);
    }

  } else {
    instance.state.set('isError', false);
    instance.state.set('isSuccess', true);
    instance.state.set('isMessage', true);

    switch (action) {
    case 'insert':
      instance.state.set('message', 'Record had been added successfully');
      instance.state.set('disabled', true);
      break;  

    case 'remove':
      instance.state.set('message', 'Record had been removed successfully');
      instance.state.set('disabled', true);
      break;

    case 'update':  
      instance.state.set('message', 'Record had been updated successfully');
      break;
    }
  }
}

function calcActionLabel(action) {
  switch (action) {
  case 'insert':
    return 'Add';
  case 'remove':
    return 'Remove';
  default:
    return 'Submit';
  }
}
