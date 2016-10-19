/*
 * Template Component: accordionTreeNode
 */

import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';

import './environment-wizard.html';

Template.EnvironmentWizard.rendered = function(){
  
  // todo: refactor to use component - not jquery click
  $('.btnNext').click(function(){
    $('.nav-tabs > .active').next('li').find('a').trigger('click');
  });

  // todo: refactor to use component - not jquery click
  $('.btnPrevious').click(function(){
    $('.nav-tabs > .active').prev('li').find('a').trigger('click');
  });
  
};


Template.EnvironmentWizard.helpers({
  updateRecipeId : function () {
    return this._id;
  },
  user : function () {
    return Meteor.user().username;
  }
});

Template.EnvironmentWizard.events({
  'click .toast' : function () {
    toastr.success('Have fun storming the castle!', 'Open Stack server says');
  },
  // todo: research: seems not implemented 
  'click .fa-trash' : function () {
    Meteor.call('deleteRecipe', this._id);
  }
});
