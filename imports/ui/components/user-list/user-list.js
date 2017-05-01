/*
 * Template Component: UserList 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
//import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
        
import './user-list.html';     
    
/*  
 * Lifecycles
 */   
  
Template.UserList.onCreated(function() {
  var instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
  });

  instance.autorun(function () {
    //let data = Template.currentData();
    
    /*
    var controller = Iron.controller();
    var params = controller.getParams();
    var query = params.query;

    new SimpleSchema({
    }).validate(query);
    */

    instance.subscribe('users');
  });
});  

/*
Template.UserList.rendered = function() {
};  
*/

/*
 * Events
 */

Template.UserList.events({
});
   
/*  
 * Helpers
 */

Template.UserList.helpers({    
  userList: function () {
    return Meteor.users.find({});
  },

  toString: function (val) {
    return R.toString(val);
  }
});


