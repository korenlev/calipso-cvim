/*
 * Template Component: EnvMonitoringInfo 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
import * as R from 'ramda';
        
import { createInputArgs } from '/imports/ui/lib/input-model';
import { createSelectArgs } from '/imports/ui/lib/select-model';
import { Constants } from '/imports/api/constants/constants';

import './env-monitoring-info.html';     
    
/*  
 * Lifecycles
 */   
  
Template.EnvMonitoringInfo.onCreated(function() {
  let instance = this;

  instance.autorun(function () {
    instance.subscribe('constants');
  });
});  

/*
Template.EnvMonitoringInfo.rendered = function() {
};  
*/

/*
 * Events
 */

Template.EnvMonitoringInfo.events({
});
   
/*  
 * Helpers
 */

Template.EnvMonitoringInfo.helpers({    
  createInputArgs: createInputArgs,

  createSelectArgs: createSelectArgs,

  envTypeOptions: function () {
    let item = Constants.findOne({ name: 'env_types' });
    if (R.isNil(item)) { return []; }
    return item.data;
  },
});


