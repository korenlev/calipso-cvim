/*
 * Template Component: accordionTreeNode
 */

import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import * as R from 'ramda';

import { Environments } from '/imports/api/environments/environments';

import './environment-wizard.html';

import '/client/imports/env-main-info/env-main-info';
import '/client/imports/env-os-api-endpoint-info/env-os-api-endpoint-info';
import '/client/imports/env-open-stack-db-credentials-info/env-open-stack-db-credentials-info';
import '/client/imports/env-master-host-credentials-info/env-master-host-credentials-info';
import '/client/imports/env-nfv-info/env-nfv-info';

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
    let controller = Iron.controller();
    let params = controller.getParams();

    let envName = params.env;
    if (envName) {
      instance.subscribe('environments?name', envName);

      instance.state.set('action', 'edit');
      Environments.find({'name': envName})
      .forEach(function (envItem) {
        instance.state.set('environment', R.clone(envItem));
      });

    } else {
      instance.state.set('action', 'insert');
      instance.state.set('environment', generateNewEnv());
    }
  });
});

Template.EnvironmentWizard.rendered = function(){
  
  // todo: refactor to use component - not jquery click
  /*
  $('.btnNext').click(function(){
    $('.nav-tabs > .active').next('li').find('a').trigger('click');
  });
  */

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
      label: 'OpenStack DB Credentials',
      localLink: 'db-credentials'
    }, {
      label: 'Master Host Credentials',
      localLink: 'master-host'
    }, {
      label: 'NFV Credentials',
      localLink: 'nfv'
    }];
  },

  environment: function () {
    let instance = Template.instance();
    return instance.state.get('environment');
  },

  createTabArgs: function (environment, nextTabId) {
    let instance = Template.instance();

    return {
      environment: environment,
      onNextRequested: function () {
        if (nextTabId) {
          console.log('next requested to: ' + nextTabId);
          instance.$('#link-' + nextTabId).tab('show');
        }
      }
    };
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
