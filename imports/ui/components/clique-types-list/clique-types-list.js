/*
 * Template Component: CliqueTypesList 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { CliqueTypes } from '/imports/api/clique-types/clique-types';
        
import './clique-types-list.html';     
    
/*  
 * Lifecycles
 */   
  
Template.CliqueTypesList.onCreated(function() {
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
    instance.state.set('env', env);

    instance.subscribe('clique_types?env*', env);
  });
});  

/*
Template.CliqueTypesList.rendered = function() {
};  
*/

/*
 * Events
 */

Template.CliqueTypesList.events({
});
   
/*  
 * Helpers
 */

Template.CliqueTypesList.helpers({    
  cliqueTypes: function () {
    //let instance = Template.instance();

    //var env = instance.state.get('env');
    //return Scans.find({ environment: env });
    return CliqueTypes.find({}); 
  },
});


