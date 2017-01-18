/*
 * Template Component: ScanningRequest
 */

//import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
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
    environmentName: null,
    action: 'insert',
    isError: false,
    isSuccess: false,
    isMessage: false,
    message: null,
    disabled: false,
    notifications: {}
  });

  instance.autorun(function () {
    let controller = Iron.controller();
    let params = controller.getParams();
    let query = params.query;

    instance.subscribe('constants');
    instance.subscribe('scans?env', query.env);

    let envName = query.env;
    instance.state.set('environmentName', envName );
    instance.state.set('action', 'insert');
    instance.state.set('model', Scans.schema.clean({
      environment: instance.state.get('environmentName')
    }));

    let notifications = instance.state.get('notifications');
    if (Scans.find({ environment: envName, status: { $in: ['pending', 'running'] } }).count() > 0) {
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
        let model = instance.state.get('model');
        let newModel = R.assoc(params.hash.key, value, model);
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
    return instance.state.get('model')[key];
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
    } else if (action === 'update') {
      instance.state.set('message', 'Record had been updated successfully');
    }
  }
}
