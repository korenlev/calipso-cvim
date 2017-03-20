/*
 * Template Component: CliqueConstraintsList 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { CliqueConstraints } from '/imports/api/clique-constraints/clique-constraints';
        
import './clique-constraints-list.html';     
    
/*  
 * Lifecycles
 */   
  
Template.CliqueConstraintsList.onCreated(function() {
  var instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
  });

  instance.autorun(function () {
    //let data = Template.currentData();
    
    var controller = Iron.controller();
    var params = controller.getParams();
    var query = params.query;

    new SimpleSchema({
    }).validate(query);

    instance.subscribe('clique_constraints');
  });
});  

/*
Template.CliqueConstraintsList.rendered = function() {
};  
*/

/*
 * Events
 */

Template.CliqueConstraintsList.events({
});
   
/*  
 * Helpers
 */

Template.CliqueConstraintsList.helpers({    
  cliqueConstraints: function () {
    //let instance = Template.instance();

    //var env = instance.state.get('env');
    //return Scans.find({ environment: env });
    return CliqueConstraints.find({}); 
  },
});

