/*
 * Tempalte Component: Environment
 */

/*
 * Lifecycles methods
 */

import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { Counts } from 'meteor/tmeasday:publish-counts';
//import * as R from 'ramda';

import { Inventory } from '/imports/api/inventories/inventories';
//import { Messages } from '/imports/api/messages/messages';

import { store } from '/imports/ui/store/store';
import { setCurrentNode } from '/imports/ui/actions/navigation';
import { setEnvName } from '/imports/ui/actions/environment-panel.actions';
//import { addSearchInterestedParty } from '/imports/ui/actions/search-interested-parties';
//import { removeSearchInterestedParty } from '/imports/ui/actions/search-interested-parties';

import '/imports/ui/components/accordionNavMenu/accordionNavMenu';

import './environment.html';

/*
 * Lifecycles
 */

Template.Environment.onCreated(function () {
  var instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    childNodeRequested: null,
    envName: null,
    searchTerm: null
  });

  instance.autorun(function () {
    var controller = Iron.controller();
    var params = controller.getParams();
    var query = params.query;

    var envName = controller.state.get('envName');
    if (envName !== instance.state.get('envName')) {
      instance.state.set('envName', envName);
      store.dispatch(setEnvName(envName));

      /*
      let onSearchRequested = (searchTerm) => {
        console.log(`search requested for: ${searchTerm}`);
        instance.subscribe('inventory?env+name', envName, searchTerm);
        instance.state.set('searchTerm', null);
        instance.state.set('searchTerm', searchTerm);
      };
      */

      /*
      instance.onSearchRequested = onSearchRequested;
      store.dispatch(addSearchInterestedParty(onSearchRequested));
      */

      if (query.graph) {
        let node24IdPath =
          '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-aggregates/7/aggregate-WebEx-RTP-SSD-Aggregate-node-24';
        let node24NamePath =
          '/WebEX-Mirantis@Cisco/Regions/RegionOne/Aggregates/WebEx-RTP-SSD-Aggregate/node-24';

        store.dispatch(setCurrentNode({
          id_path: node24IdPath,
          name_path: node24NamePath
        }));
      } else {
        store.dispatch(setCurrentNode({
          id_path: '/' + envName,
          name_path: '/' + envName
        }));
      }

      instance.subscribe('inventory?env+type', envName, 'instance');
      instance.subscribe('inventory?env+type', envName, 'vservice');
      instance.subscribe('inventory?env+type', envName, 'host');
      instance.subscribe('inventory?env+type', envName, 'vconnector');
      instance.subscribe('inventory?env+type', envName, 'project');
      instance.subscribe('inventory?env+type', envName, 'region');
      instance.subscribe('messages?env+level', envName, 'notify');
      instance.subscribe('messages?env+level', envName, 'warn');
      instance.subscribe('messages?env+level', envName, 'error');
    }
  });

  /* Depracted: search is done in audo search box.
  instance.autorun(function () {
    var controller = Iron.controller();
    let envName = controller.state.get('envName');
    let searchTerm = instance.state.get('searchTerm');
    if (searchTerm) {
      Inventory.find({ environment: envName, name: searchTerm })
      .forEach(function (resultNode) { // todo: one result only ?
        store.dispatch(setCurrentNode(resultNode));
      });
    }
  });
  */

});

Template.Environment.onDestroyed(function () {
  //let instance = this;
  //store.dispatch(removeSearchInterestedParty(instance.onSearchRequested));
});

Template.Environment.rendered = function(){

  /*
  $.getScript('https://www.gstatic.com/charts/loader.js', function() {
    google.charts.load('current', {'packages':['gauge', 'line']});
    google.charts.setOnLoadCallback(drawLine);


    function drawLine() {
      var data = new google.visualization.DataTable();
      data.addColumn('number', 'Traffic Webex');
      data.addColumn('number', 'Traffic metapod');
      data.addColumn('number', 'Some other Traffic');
      data.addColumn('number', 'Some other Traffic');

      data.addRows([
        [1,  37.8, 80.8, 41.8],
        [2,  30.9, 69.5, 32.4],
        [3,  25.4,   57, 25.7],
        [4,  11.7, 18.8, 32.5],
        [5,  11.9, 25.6, 10.4],
        [6,   68.8, 13.6,  27.7],
        [7,   7.6, 42.3,  9.6],
        [8,  12.3, 29.2, 10.6],
        [9,  16.9, 42.9, 14.8]
      ]);

      var options = {
        chart: {
          title: 'Network traffic throughput',
          subtitle: 'in Mbps'
        }
      };

      var chart = new google.charts.Line(document.getElementById('curve_chart'));

      chart.draw(data, options);
    }
  });
  */

};

/*
 * Helpers
 */

Template.Environment.helpers({
  envName: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    return envName;
  },

  instancesCount: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    var counterName = 'inventory?env+type!counter?env=' +
      envName + '&type=' + 'instance';
    //return Inventory.find({environment: envName,type:'instance'}).count();
    return Counts.get(counterName);
  },

  vservicesCount: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    var counterName = 'inventory?env+type!counter?env=' +
      envName + '&type=' + 'vservice';
    //return Inventory.find({environment: envName,type:'vservice'}).count();
    return Counts.get(counterName);
  },

  hostsCount: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    var counterName = 'inventory?env+type!counter?env=' +
      envName + '&type=' + 'host';
    //return Inventory.find({environment: envName,type:'host'}).count();
    return Counts.get(counterName);
  },

  vconnectorsCount: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    var counterName = 'inventory?env+type!counter?env=' +
      envName + '&type=' + 'vconnector';
    //return Inventory.find({environment: envName,type: 'vconnector'}).count();
    return Counts.get(counterName);
  },

  projectsCount: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    var counterName = 'inventory?env+type!counter?env=' +
      envName + '&type=' + 'project';
    //return Inventory.find({environment: envName,type: 'project'}).count();
    return Counts.get(counterName);
  },

  regoinsCount: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    var counterName = 'inventory?env+type!counter?env=' +
      envName + '&type=' + 'region';
    //return Inventory.find({environment: envName,type: 'region'}).count();
    return Counts.get(counterName);
  },

  regoins: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    return Inventory.find({environment: envName,type:'region'});
  },

  projects: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    return Inventory.find({environment: envName,type:'project'});
  },

  regionItem: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    //return Inventory.findOne({environment: envName,type:'region'}).last_scanned;
    return Inventory.findOne({environment: envName,type:'region'});
  },

  projectItem: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    //return Inventory.findOne({environment: envName,type:'project'}).last_scanned;
    return Inventory.findOne({environment: envName,type:'project'});
  },

  notificationsCount: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    //return Messages.find({environment: envName,level:'notify'}).count();
    return Counts.get('messages?env+level!counter?env=' +
     envName + '&level=' + 'notify');
  },

  warningsCount: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    //return Messages.find({environment: envName,level:'warn'}).count();
    return Counts.get('messages?env+level!counter?env=' +
     envName + '&level=' + 'warn');
  },

  errorsCount: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    //return Messages.find({environment: envName,level:'error'}).count();
    return Counts.get('messages?env+level!counter?env=' +
       envName + '&level=' + 'error');
  },

  childNodeRequested: function () {
    let instance = Template.instance();
    return instance.state.get('childNodeRequested');
  },

  createNavMenuArgs: function (childNodeRequested) {
    return {
      childNodeRequested: childNodeRequested
    };
  }

});


Template.Environment.events({
  'click .sm-edit-button': function (event, instance) {
    let envName = instance.state.get('envName');
    Router.go('/wizard/' + envName,{},{});
  },

  'click .sm-scan-button': function (event, instance) {
    let envName = instance.state.get('envName');
    Router.go('scanning-request.insert',{},{ query: 'env=' + envName });
  },
});