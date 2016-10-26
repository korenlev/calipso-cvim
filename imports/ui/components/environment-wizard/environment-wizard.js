/*
 * Template Component: EnvironmentWizard
 */

import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import * as R from 'ramda';

import { Environments } from '/imports/api/environments/environments';

import './environment-wizard.html';

import '/imports/ui/components/env-main-info/env-main-info';
import '/imports/ui/components/env-os-api-endpoint-info/env-os-api-endpoint-info';
import '/imports/ui/components/env-open-stack-db-credentials-info/env-open-stack-db-credentials-info';
import '/imports/ui/components/env-master-host-credentials-info/env-master-host-credentials-info';
import '/imports/ui/components/env-nfv-info/env-nfv-info';
import '/imports/ui/components/env-amqp-credentials-info/env-amqp-credentials-info';

import {
  insert,
  update
} from '/imports/api/environments/methods';

/*
 * Lifecycles
 */

Template.EnvironmentWizard.onCreated(function(){
  let instance = this;
  instance.state = new ReactiveDict();
  instance.state.setDefault({
    environment: null,
    action: null
  });



  instance.autorun(function () {

    //let controller = Iron.controller();
    //let params = controller.getParams();

    //let envName = params.env;
    let envName = Session.get('wizardEnv');
    if (envName) {
      instance.subscribe('environments?name', envName);
      instance.state.set('action', 'update');

    } else {
      instance.state.set('action', 'insert');
    }

    let action = instance.state.get('action');
    if (action === 'update') {
      Environments.find({'name': envName})
      .forEach(function (envItem) {
        instance.state.set('environment', R.clone(envItem));
      });
    } else if (action === 'insert') {
      instance.environmentModel = generateNewEnv();
    }
  });
});

Template.EnvironmentWizard.rendered = function(){

  // todo: refactor to use component - not jquery click
  $('.btnPrevious').click(function(){
    $('.nav-tabs > .active').prev('li').find('a').trigger('click');
  });

};

/*
 * Helpers
 */

Template.EnvironmentWizard.helpers({
  updateRecipeId : function () {
    return this._id;
  },

  user : function () {
    return Meteor.user().username;
  },

  tabs: function () {
    return [{
      label: 'Main Info',
      localLink: 'maininfo'
    }, {
      label: 'OS API Endpoint',
      localLink: 'endpoin-panel'
    }, {
      label: 'OS DB Credentials',
      localLink: 'db-credentials'
    }, {
      label: 'Master Host Credentials',
      localLink: 'master-host'
    }, {
      label: 'AMQP Credentials',
      localLink: 'amqp'
    }, {
      label: 'NFV Credentials',
      localLink: 'nfv'
    }];
  },

  environment: function () {
    let instance = Template.instance();
    return instance.state.get('environment');
  },

  createTabArgs: function (key, model, nextTabId) {
    let instance = Template.instance();

    return {
      key: key,
      model: model,
      setModel: function (subKey, value) {
        let mainModel = instance.state.get('environment');
        let calcKey = R.isEmpty(key) ? subKey : key;
        let newMainModel;

        if (R.isEmpty(calcKey)) {
          newMainModel = value;
        } else {
          newMainModel = setModelByKey(calcKey, value, mainModel);
        }
        instance.state.set('environment', newMainModel);
      },
      onNextRequested: function () {
        if (nextTabId) {
          instance.$('#link-' + nextTabId).tab('show');
        }
      },
      onSubmitRequested: function () {
        console.log('onSubmitRequested');
        console.log(model);

        let action = instance.state.get('action');
        let environment = instance.state.get('environment');

        switch (action) {
        case 'insert':
          insert.call({
            configuration: environment.configuration,
            distribution: environment.distribution,
            name: environment.name,
            network_plugins: environment.network_plugins,
          }, processActionResult);
          break;

        case 'update':
          update.call({
            itemId: environment._id,
            configuration: environment.configuration,
            distribution: environment.distribution,
            name: environment.name,
            network_plugins: environment.network_plugins,
          }, processActionResult);
          break;

        default:
          // todo
          break;
        }
      }
    };
  },

  getConfSection: function(sectionName, environment) {
    if (R.isNil(environment)) { return null; }
    let section = R.find(R.propEq('name', sectionName),
      environment.configuration);
    return section;
  }

  // todo: default active tab. 'class="active"'
});

/*
 * Events
 */

Template.EnvironmentWizard.events({
  'click .toast' : function () {
    toastr.success('Have fun storming the castle!', 'Open Stack server says');
  },
  // todo: research: seems not implemented
  'click .fa-trash' : function () {
    Meteor.call('deleteRecipe', this._id);
  }
});

function generateNewEnv() {
  return {
    user: '',
    name: ''
  };
}

function processActionResult(error) {
  if (error) {
    alert(error);
  }
}

function setModelByKey(key, value, model) {
  let newModel;

  if (typeof key !== 'string') {
    throw 'malformed key';
  }

  if (R.test(/^#configuration-/, key)) {
    let sectionName = (/^#configuration-(.*$)/.exec(key))[1];

    let sectionIndex = R.findIndex(R.propEq('name', sectionName),
      model.configuration);

    let configuration = R.update(sectionIndex, value, model.configuration);
    newModel = R.assoc('configuration', configuration, model);

  } else {
    newModel =R.assoc(key, value, model);
  }

  return newModel;
}
