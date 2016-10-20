/*
 * Tempalte Component: environment
 */

/*
 * Lifecycles methods
 */

import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { Counts } from 'meteor/tmeasday:publish-counts';

import { store } from '/client/imports/store';
import { setCurrentNode } from '/client/imports/actions/navigation';

import './enviroment.html';

Template.enviroment.onCreated(function () {
  var instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    childNodeRequested: null
  });

  instance.autorun(function () {
    var controller = Iron.controller();
    var params = controller.getParams();
    var query = params.query;

    var envName = controller.state.get('envName');

    if (query.graph) {
      let node24IdPath = 
        '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-aggregates/7/aggregate-WebEx-RTP-SSD-Aggregate-node-24';
      let node24NamePath = 
        '/WebEX-Mirantis@Cisco/Regions/RegionOne/Aggregates/WebEx-RTP-SSD-Aggregate/node-24';

      store.dispatch(setCurrentNode(node24IdPath, node24NamePath));
    } else {
      store.dispatch(setCurrentNode('/' + envName, '/' + envName));
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
  });

});

Template.enviroment.onDestroyed(function () {
  let instance = this;
  instance.storeUnsubscribe();
});

Template.enviroment.rendered = function(){

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

};

/*
 * Helpers
 */

Template.enviroment.helpers({
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
