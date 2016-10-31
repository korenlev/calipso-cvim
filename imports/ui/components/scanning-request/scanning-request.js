/*
 * Template Component: ScanningRequest 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import * as R from 'ramda';

//import { createInputArgs } from '/imports/ui/lib/input-model';
import { ScanningRequests } from '/imports/api/scanning_requests/scanning_requests';

import '/imports/ui/components/input-model/input-model';
        
import {
  insert,
} from '/imports/api/scanning_requests/methods';

import './scanning-request.html';     
    
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
  });

  instance.autorun(function () {
    let controller = Iron.controller();
    let params = controller.getParams();
    let query = params.query;

    instance.state.set('environmentName', query.env);
    instance.state.set('action', 'insert');
    instance.state.set('model', ScanningRequests.schema.clean({
      environment_name: instance.state.get('environmentName')
    }));
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
    console.log('submit click');

    submitItem(instance);
  }
});
   
/*  
 * Helpers
 */

Template.ScanningRequest.helpers({    
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
        console.log('setting model');
        console.log(value);

        let model = instance.state.get('model');
        let newModel = R.assoc(params.hash.key, value, model);
        instance.state.set('model', newModel);
      },
    };
  },

  getState: function (key) {
    let instance = Template.instance();
    return instance.state.get(key); 
  },

  getFieldDesc: function (key) {
    //let instance = Template.instance();
    return ScanningRequests.schemaRelated[key].description;
  },

  commandOptions: function () { 
    let array = [];

    R.mapObjIndexed((value, key) => {
      array = R.append({
        name: key,
        info: value
      }, array);
    }, ScanningRequests.schemaRelated);

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
      environment_name: model.environment_name,
      cgi: model.cgi,
      mongo_config: model.mongo_config,
      type: model.type,
      inventory: model.inventory,
      scan_self:  model.scan_self,
      id: model.id,
      parent_id: model.parent_id,
      parent_type: model.parent_type,
      id_field: model.id_field,
      loglevel: model.loglevel,
      inventory_only: model.inventory_only,
      links_only: model.links_only,
      cliques_only: model.cliques_only,
      clear: model.clear,
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
