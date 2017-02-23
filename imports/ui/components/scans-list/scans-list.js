/*
 * Template Component: ScansList 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import * as R from 'ramda';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { Scans } from '/imports/api/scans/scans';
        
import './scans-list.html';     
    
/*  
 * Lifecycles
 */   
  
Template.ScansList.onCreated(function() {
  var instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    env: null
  });

  instance.autorun(function () {


    //let data = Template.currentData();
    
    var controller = Iron.controller();
    var params = controller.getParams();
    var query = params.query;

    new SimpleSchema({
      env: { type: String, optional: true },
    }).validate(query);

    let env = query.env;
    if (R.isNil(env)) {
      instance.state.set('env', null);
    } else {
      instance.state.set('env', env);
    }

    instance.subscribe('scans?env*', env);
  });
});  

/*
Template.ScansList.rendered = function() {
};  
*/

/*
 * Events
 */

Template.ScansList.events({
});
   
/*  
 * Helpers
 */

Template.ScansList.helpers({    
  scans: function () {
    //let instance = Template.instance();

    //var env = instance.state.get('env');
    //return Scans.find({ environment: env });
    return Scans.find({}); 
  },

  toObj: function (params) {
    return R.clone(params.hash);
  }
});
