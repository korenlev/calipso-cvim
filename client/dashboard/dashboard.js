/*
 * Template Component: dashboard
 */

import { Environments } from '/imports/api/environments/environments';
import { Inventory } from '/imports/api/inventories/inventories';

(function () {

/* 
 * Lifecycle methods
 */

Template.dashboard.onCreated(function () {
  var instance = this;

  instance.autorun(function () {
    instance.subscribe('environments_config');

    Environments.find({}).forEach(function (envItem) {
      instance.subscribe('inventory?env+type', envItem.name, 'instance');
      instance.subscribe('inventory?env+type', envItem.name, 'vservice');
      instance.subscribe('inventory?env+type', envItem.name, 'host');
      instance.subscribe('inventory?env+type', envItem.name, 'vconnector');
      instance.subscribe('inventory?env+type', envItem.name, 'project');
      instance.subscribe('inventory?env+type', envItem.name, 'region');
    });

    instance.subscribe('messages?level', 'notify');
    instance.subscribe('messages?level', 'warn');
    instance.subscribe('messages?level', 'error');
  });
});

Template.dashboard.rendered = function(){

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

}
/*
 * Helpers
 */

Template.dashboard.helpers({

    envList:function(){
        //return Environments.find({type:'environment'});
        return Environments.find({});
    },

    instancesCount: function (envName){
        //return Inventory.find({environment: envName, type:'instance'}).count();
        return Counts.get('inventory?env+type!counter?env=' +
          envName + '&type=' + 'instance'); 
    },

    vservicesCount: function (envName) {
        //return Inventory.find({environment: envName, type:'vservice'}).count();
        return Counts.get('inventory?env+type!counter?env=' +
          envName + '&type=' + 'vservice'); 
    },

    hostsCount: function (envName) {
        //return Inventory.find({environment: envName, type:'host'}).count();
        return Counts.get('inventory?env+type!counter?env=' +
          envName + '&type=' + 'host'); 
    },

    vconnectorsCount: function(envName){
        //return Inventory.find({environment: envName, type:'vconnector'}).count();
        return Counts.get('inventory?env+type!counter?env=' +
          envName + '&type=' + 'vconnector'); 
    },

    projectsCount: function (envName){
        //return Inventory.find({environment: envName, type:'project'}).count();
        return Counts.get('inventory?env+type!counter?env=' +
          envName + '&type=' + 'project'); 
    },

    regoinsCount: function (envName){
        //return Inventory.find({environment: envName, type:'region'}).count();
        return Counts.get('inventory?env+type!counter?env=' +
          envName + '&type=' + 'region'); 
    },

    regoins: function (envName) {
        return Inventory.find({environment: envName, type:'region'});
    },

    projects: function (envName){
        return Inventory.find({environment: envName, type:'project'});
    },

    notificationsCount: function(){
        //return Messages.find({level:'notify'}).count();
        return Counts.get('messages?level!counter?' +
          'level=' + 'notify');
    },

    warningsCount: function(){
        //return Messages.find({level:'warn'}).count();
        return Counts.get('messages?level!counter?' +
          'level=' + 'warn');
    },

    errorsCount: function(){
        //return Messages.find({level:'error'}).count();
        return Counts.get('messages?level!counter?' +
          'level=' + 'error');
    },

/*
    notificationsTimestamp: function(){
        var msgTimestamp = Messages.findOne({state:'added'},{fields: {'timestamp': 1} });
        return msgTimestamp.timestamp;
    },
    warnings: function(){
        return Messages.findOne({state:'warn'});
    },
    errors: function(){
        return Messages.findOne({state:'down'});
    },
*/

});

})();  
