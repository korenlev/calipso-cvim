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
    return [{
      label: 'Mirantis-6.0',
    }, {
      label: 'Mirantis-7.0',
    }, {
      label: 'Mirantis-8.0',
    }, {
      label: 'Mirantis-9.0',
    }, { 
      label: 'RDO-Mitaka',
    }, {
      label: 'RDO-Liberty',
    }, {
      label: 'RDO-Juno',
    }, {
      label: 'RDO-kilo',
    }, {
      label: 'devstack-liberty',
    }, {
      label: 'Canonical-icehouse', 
    }, {
      label: 'Canonical-juno',
    }, {
      label: 'Canonical-liberty',
    }, {
      label: 'Canonical-mitaka',
    }, {
      label: 'Apex-Mitaka',
    }, {
      label: 'Devstack-Mitaka',
    }, {
      label: 'packstack-7.0.0-0.10.dev1682'
    }
    ];
  },

  networkOptions: function () {
    return [{
      label: 'OSV',
    }, {
      label: 'VPP',
    }];
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
