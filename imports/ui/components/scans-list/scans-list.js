/*
 * Template Component: ScansList 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import * as R from 'ramda';
import { Counts } from 'meteor/tmeasday:publish-counts';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { Scans } from '/imports/api/scans/scans';
        
import '/imports/ui/components/pager/pager';

import './scans-list.html';     
    
/*  
 * Lifecycles
 */   
  
Template.ScansList.onCreated(function() {
  var instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    env: null,
    page: 1,
    amountPerPage: 10,
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

  });

  instance.autorun(function () {
    let env = instance.state.get('env');
    let amountPerPage = instance.state.get('amountPerPage');
    let page = instance.state.get('page');

    instance.subscribe('scans?env*&page&amount', env, page, amountPerPage);
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
    let instance = Template.instance();
    let page = instance.state.get('page');
    let amountPerPage = instance.state.get('amountPerPage');
    let skip = (page - 1) * amountPerPage;

    return Scans.find({}, {
      limit: amountPerPage,
      skip: skip,
    }); 
  },

  currentPage: function () {
    let instance = Template.instance();
    return instance.state.get('page');
  },

  amountPerPage: function () {
    let instance = Template.instance();
    return instance.state.get('amountPerPage');
  },

  totalItems: function () {
    return Counts.get('scans?env*&page&amount!count');
  },

  argsPager: function (currentPage, amountPerPage, totalItems) {
    let instance = Template.instance();
    let totalPages = Math.ceil(totalItems / amountPerPage);

    return {
      disableNext: currentPage * amountPerPage > totalItems,
      disablePrev: currentPage == 1,
      totalPages: totalPages,      
      currentPage: currentPage,
      onReqNext: function () {
        console.log('next');
        let page = (currentPage * amountPerPage > totalItems) ? currentPage : currentPage + 1;
        instance.state.set('page', page); 
      },
      onReqPrev: function () {
        console.log('prev');
        let page = (currentPage == 1) ? currentPage : currentPage - 1;
        instance.state.set('page', page); 
      },
      onReqFirst: function () {
        console.log('req first');
        instance.state.set('page', 1);
      },
      onReqLast: function () {
        console.log('req last');
        instance.state.set('page', totalPages);
      },
      onReqPage: function (pageNumber) {
        console.log('req page');
        let page;
        if (pageNumber <= 1) { 
          page = 1; 
        } else if (pageNumber > Math.ceil(totalItems / amountPerPage)) { 
          page = totalPages;
        } else {
          page = pageNumber;
        }

        instance.state.set('page', page);
      },
    };
  }
});

