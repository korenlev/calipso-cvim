/*
 * Template Component: EnvMainInfo
 */

//import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';

import '/imports/ui/components/input-model/input-model';
import '/imports/ui/components/select-model/select-model';
import { createInputArgs } from '/imports/ui/lib/input-model';
import { createSelectArgs } from '/imports/ui/lib/select-model';
import { Distributions } from '/imports/api/environments/environments';
import { NetworkPlugins } from '/imports/api/environments/environments';

import './env-main-info.html';

/*
 * Lifecycles
 */

Template.EnvMainInfo.onCreated(function () {

});

/*
Template.EnvironmentWizard.rendered = function(){
};
*/
 
/*
 * Helpers
 */

Template.EnvMainInfo.helpers({
  /*
  createInputArgs: function (params) {
    let instance = Template.instance();
    return {
      context: params.hash.context,
      key: params.hash.key,
      type: params.hash.type,
      placeholder: params.hash.placeholder,
      setModel: instance.data.setModel 
    };
  }*/
  createInputArgs: createInputArgs,

  createSelectArgs: createSelectArgs,

  distributionOptions: function () {
    return Distributions;
  },

  networkOptions: function () {
    return NetworkPlugins;
  },
 
});

/*
 * Events
 */

Template.EnvMainInfo.events({
  'click .sm-next-button': function () {
    let instance = Template.instance();
    instance.data.onNextRequested(); 
  }
});
