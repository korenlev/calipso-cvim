/*
 * Template Component: ScanningRequest
 */

//import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';

import { Constants } from '/imports/api/constants/constants';
//import { createInputArgs } from '/imports/ui/lib/input-model';
import { createSelectArgs } from '/imports/ui/lib/select-model';
import { Scans } from '/imports/api/scans/scans';

import '/imports/ui/components/input-model/input-model';
import '/imports/ui/components/select-model/select-model';

import {
  insert,
} from '/imports/api/scans/methods';

import './scanning-request.html';

const noteTypeScanExists = {
  type: 'scanExists',
  message: 'There is already a scan in progess in the system. Please wait until it ends.'
};

/*
 * Lifecycles
 */

Template.ScanningRequest.onCreated(function() {
  let instance = this;
  instance.state = new ReactiveDict();
  instance.state.setDefault({
    env: null,
    action: 'insert',
    isError: false,
    isSuccess: false,
    isMessage: false,
    message: null,
    disabled: false,
    notifications: {},
    model: {},
    beforeInsert: true
  });

  instance.autorun(function () {
    let controller = Iron.controller();
    let params = controller.getParams();
    let query = params.query;

    new SimpleSchema({
      action: { type: String, allowedValues: ['insert', 'view', 'update'] },
      env: { type: String, optional: true },
      id: { type: String, optional: true }
    }).validate(query);

    switch (query.action) {
    case 'insert':
      initInsertView(instance, query); 
      break;

    case 'view':
      initViewView(instance, query);
      break;

    default:
      throw 'unimplemented action';
    }
  });
});

/*
Template.ScanningRequest.rendered = function() {
};
*/

/*
 * Events
 */

Template.ScanningRequest.events({
  'click .js-submit-button': function(event, instance) {
    submitItem(instance);
  }
});

/*
 * Helpers
 */

Template.ScanningRequest.helpers({
  getState: function (key) {
    let instance = Template.instance();
    return instance.state.get(key);
  },

  notifications: function () {
    let instance = Template.instance();
    let notifications = instance.state.get('notifications');
    let notesExpaned = R.pipe(
      R.map((noteType) => {
        switch(noteType) {
        case noteTypeScanExists.type:
          return noteTypeScanExists.message;
        default:
          return '';
        }
      }),
      R.values()
    )(notifications);

    return notesExpaned;
  },

  notificationsExists: function () {
    let instance = Template.instance();
    return R.keys(instance.state.get('notifications')).length > 0;
  },

  model: function () {
    let instance = Template.instance();
    return instance.state.get('model');
  },

  createInputArgs: function (params) {
    let instance = Template.instance();

    return {
      value: params.hash.value,
      type: params.hash.type,
      classes: params.hash.classes,
      placeholder: params.hash.placeholder,
      disabled: params.hash.disabled,
      setModel: function (value) {
        let key = params.hash.key;
        let model = instance.state.get('model');
        let newModel = model;

        if(R.indexOf(key, Scans.scansOnlyFields) >= 0) {
          newModel = setRadioValues(Scans.scansOnlyFields, key, value, model)
        }else {
          newModel = R.assoc(key, value, newModel);
        }

        instance.state.set('model', newModel);
      },
    };
  },

  createSelectArgs: createSelectArgs,

  calcSetModelFn: function (key) {
    let instance = Template.instance();
    let intf =  {
      fn: (values) => {
        let model = instance.state.get('model');
        let newModel = R.assoc(key, values, model);
        instance.state.set('model', newModel);
      },
      sample: 'text'
    };

    return intf;
  },

  getState: function (key) {
    let instance = Template.instance();
    return instance.state.get(key);
  },

  getFieldDesc: function (key) {
    //let instance = Template.instance();
    return Scans.schemaRelated[key].description;
  },

  commandOptions: function () {
    let array = [];

    R.mapObjIndexed((value, key) => {
      array = R.append({
        name: key,
        info: value
      }, array);
    }, Scans.schemaRelated);

    return array;
  },

  getModelKeyValue: function (key) {
    let instance = Template.instance();
    return R.path([key], instance.state.get('model'));
  },

  calcInputType: function(fieldInfo) {
    if (fieldInfo.type == Boolean) {
      return 'checkbox';
    }

    if (fieldInfo.type == String) {
      return 'textbox';
    }

    return 'textbox';
  },

  isCommandOptionSelectType(commandOption) {
    return (R.path(['info', 'subtype'], commandOption) === 'select');
  },

  calcCommandSelectOptions(commandOption) {
    let item = Constants.findOne({ name: R.path(['info', 'options'], commandOption) });
    if (R.isNil(item)) { return []; }
    return item.data;
  },

  pageHeader() {
    let instance = Template.instance();
    let action = instance.state.get('action');
    
    switch (action) {
    case 'insert': 
      return 'New Scanning Reuqest';

    case 'view':
      return 'Scan Information';

    default:
      return '';
    }
  },

  isUpdateableAction() {
    let instance = Template.instance();
    let action = instance.state.get('action');

    return R.contains(action, ['insert', 'update']);
  },

  isCommandDisabled(isSpecificCommandDisabled) {
    let instance = Template.instance();
    let action = instance.state.get('action');

    return isSpecificCommandDisabled || (action === 'view');
  }
});

function submitItem(instance) {
  let action = instance.state.get('action');
  let model = instance.state.get('model');

  instance.state.set('isError', false);
  instance.state.set('isSuccess', false);
  instance.state.set('isMessage', false);
  instance.state.set('message', null);

  switch (action) {
  case 'insert':
    insert.call({
      environment: model.environment,
      inventory: model.inventory,
      object_id: model.object_id,
      log_level: model.log_level,
      clear: model.clear,
      scan_only_inventory: model.scan_only_inventory,
      scan_only_links: model.scan_only_links,
      scan_only_cliques: model.scan_only_cliques,
    }, processActionResult.bind(null, instance));
    break;
  default:
      // todo
    break;
  }
}

function setRadioValues(radioFields, key, value, modal) {
  let newModal = modal;
  let currentRadioFields = R.filter(f => modal[f], radioFields);

  for(let field of currentRadioFields) {
    newModal = R.assoc(field, false, newModal)
  }

  newModal = R.assoc(key, value, newModal);
  return newModal;
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

    if (action === 'insert') {
      instance.state.set('message', 'Record had been added successfully');
      instance.state.set('disabled', true);
      instance.state.set('beforeInsert', false);
    } else if (action === 'update') {
      instance.state.set('message', 'Record had been updated successfully');
    }
  }
}

function initInsertView(instance, query) {
  instance.state.set('action', query.action);
  instance.state.set('env', query.env);
  instance.state.set('model', Scans.schema.clean({
    environment: instance.state.get('env')
  }));

  instance.subscribe('constants');
  instance.subscribe('scans?env', query.env);

  updateNotificationSameScanExistsForInsert(instance, query.env);

  // todo
}

function updateNotificationSameScanExistsForInsert(instance, env) {
  let notifications = instance.state.get('notifications');
  if (Scans.find({ 
    environment: env, 
    status: { 
      $in: ['pending', 'running'] 
    } }).count() > 0) {

    instance.state.set('notifications', R.assoc(
      noteTypeScanExists.type,
      noteTypeScanExists.type,
      notifications
    ));
  } else {
    instance.state.set('notifications', R.dissoc(
      noteTypeScanExists.type,
      notifications
    ));
  }
}

function initViewView(instance, query) {
  instance.state.set('action', query.action);
  instance.state.set('env', query.env);
  instance.state.set('id', query.id);

  instance.subscribe('constants');
  instance.subscribe('scans?id', query.id);

  let model = Scans.findOne({ _id: query.id }); 
  instance.state.set('model', model);
  // todo
}
