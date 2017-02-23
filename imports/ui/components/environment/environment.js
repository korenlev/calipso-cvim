/*
 * Tempalte Component: Environment
 */

/*
 * Lifecycles methods
 */

import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { Counts } from 'meteor/tmeasday:publish-counts';
import * as R from 'ramda';

import { Inventory } from '/imports/api/inventories/inventories';
import { Environments } from '/imports/api/environments/environments';
//import { Messages } from '/imports/api/messages/messages';

import { store } from '/imports/ui/store/store';
import { setCurrentNode } from '/imports/ui/actions/navigation';
import { setEnvName } from '/imports/ui/actions/environment-panel.actions';
import { closeVedgeInfoWindow } from '/imports/ui/actions/vedge-info-window.actions';
import { Icon } from '/imports/lib/icon';

import '/imports/ui/components/accordionNavMenu/accordionNavMenu';
import '/imports/ui/components/data-cubic/data-cubic';
import '/imports/ui/components/icon/icon';
import '/imports/ui/components/graph-tooltip-window/graph-tooltip-window';
import '/imports/ui/components/vedge-info-window/vedge-info-window';

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
    searchTerm: null,
    briefInfoList: [{
      header: ['components', 'environment', 'briefInfos', 'instancesNum', 'header'],
      dataSource: 'infoInstancesCount',
      icon: new Icon({ type: 'fa', name: 'desktop' }),
    }, {
      header: ['components', 'environment', 'briefInfos', 'vServicesNum', 'header'],
      dataSource: 'infoVServicesCount',
      icon: new Icon({ type: 'fa', name: 'object-group' }),
    }, {
      header: ['components', 'environment', 'briefInfos', 'hostsNum', 'header'],
      dataSource: 'infoHostsCount',
      icon: new Icon({ type: 'fa', name: 'server' }),
    }, {
      header: ['components', 'environment', 'briefInfos', 'vConnectorsNum', 'header'],
      dataSource: 'infoVConnectorsCount',
      icon: new Icon({ type: 'fa', name: 'compress' }),
    }, {
      header: ['components', 'environment', 'briefInfos', 'lastScanning', 'header'],
      dataSource: 'infoLastScanning',
      icon: new Icon({ type: 'fa', name: 'search' }),
    }],
    infoLastScanning: null,
    listInfoBoxes: [{
      header: ['components', 'environment', 'listInfoBoxes', 'regions', 'header'],
      listName: 'regions',
      listItemFormat: { label: 'name', value: 'id_path' },
      icon: { type: 'material', name: 'public' },
    }, {
      header: ['components', 'environment', 'listInfoBoxes', 'projects', 'header'],
      listName: 'projects',
      listItemFormat: { label: 'name', value: 'id_path' },
      icon: { type: 'material', name: 'folder' },
    }],
    projectsCount: 0,
    regionsCount: 0,
    graphTooltipWindow: { label: '', title: '', left: 0, top: 0, show: false },
    vedgeInfoWindow: { node: null, left: 0, top: 0, show: false },
  });

  Session.set('currNodeId', null);

  instance.autorun(function () {
    var controller = Iron.controller();
    var params = controller.getParams();
    var query = params.query;

    var envName = controller.state.get('envName');
    if (envName !== instance.state.get('envName')) {
      instance.state.set('envName', envName);
      store.dispatch(setEnvName(envName));

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
    instance.subscribe('environments?name', envName);

    Environments.find({ name: envName }).forEach((env) => {
      instance.state.set('infoLastScanning', env.last_scanned);
    });

    let vConnectorCounterName = 'inventory?env+type!counter?env=' +
      envName + '&type=' + 'vconnector';
    let infoVConnectorsCount = Counts.get(vConnectorCounterName);
    instance.state.set('infoVConnectorsCount', infoVConnectorsCount);

    let hostsCounterName = 'inventory?env+type!counter?env=' +
      envName + '&type=' + 'host';
    let infoHostsCount = Counts.get(hostsCounterName);
    instance.state.set('infoHostsCount', infoHostsCount);

    let vServicesCounterName = 'inventory?env+type!counter?env=' +
      envName + '&type=' + 'vservice';
    let infoVServicesCount =  Counts.get(vServicesCounterName);
    instance.state.set('infoVServicesCount', infoVServicesCount);

    let instancesCounterName = 'inventory?env+type!counter?env=' +
      envName + '&type=' + 'instance';
    let infoInstancesCount = Counts.get(instancesCounterName);
    instance.state.set('infoInstancesCount', infoInstancesCount);

    let projectsCounterName = 'inventory?env+type!counter?env=' +
      envName + '&type=' + 'project';
    let projectsCount = Counts.get(projectsCounterName);
    instance.state.set('projectsCount', projectsCount);

    let regionsCounterName = 'inventory?env+type!counter?env=' +
      envName + '&type=' + 'region';
    let regionsCount = Counts.get(regionsCounterName);
    instance.state.set('regionsCount', regionsCount);
  });

  instance.storeUnsubscribe = store.subscribe(() => {
    let state = store.getState();

    let graphTooltipWindow = state.components.graphTooltipWindow;
    instance.state.set('graphTooltipWindow', graphTooltipWindow);

    let vedgeInfoWindow = state.components.vedgeInfoWindow;
    instance.state.set('vedgeInfoWindow', vedgeInfoWindow);
  });
});

Template.Environment.onDestroyed(function () {
  let instance = this;
  instance.storeUnsubscribe();
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
  },

  briefInfoList: function () {
    let instance = Template.instance();
    return instance.state.get('briefInfoList');
  },

  genArgsBriefInfo: function (briefInfo) {
    let instance = Template.instance();
    return {
      header: R.path(briefInfo.header, store.getState().api.i18n),
      dataInfo: R.toString(instance.state.get(briefInfo.dataSource)),
      icon: new Icon(briefInfo.icon)
    };
  },

  listInfoBoxes: function () {
    let instance = Template.instance();
    return instance.state.get('listInfoBoxes');
  },

  argsListInfoBox: function (listInfoBox) {
    let instance = Template.instance();
    let envName = instance.state.get('envName');

    let lastScanned = calcLastScanned(listInfoBox.listName, envName);

    return {
      header: R.path(listInfoBox.header, store.getState().api.i18n),
      list: getList(listInfoBox.listName, envName),
      icon: new Icon(listInfoBox.icon),
      listItemFormat: listInfoBox.listItemFormat,
      lastScanning: lastScanned,      
      onItemSelected: function (itemKey) {
        Router.go(buildRoute(listInfoBox.listName, itemKey));
      }
    };
  },
  
  graphTooltipWindow: function () {
    let instance = Template.instance();
    let graphTooltipWindow = instance.state.get('graphTooltipWindow');

    return graphTooltipWindow; 
  },

  vedgeInfoWindow: function () {
    let instance = Template.instance();
    let vedgeInfoWindow = instance.state.get('vedgeInfoWindow');

    return vedgeInfoWindow; 
  },

  argsGraphTooltipWindow: function (graphTooltipWindow) {
    return {
      label: R.path(['label'], graphTooltipWindow),
      title: R.path(['title'], graphTooltipWindow),
      left: R.path(['left'], graphTooltipWindow),
      top: R.path(['top'], graphTooltipWindow),
      show: R.path(['show'], graphTooltipWindow)
    };
  },

  argsVedgeInfoWindow: function (vedgeInfoWindow) {
    return {
      environment: R.path(['node', 'environment'], vedgeInfoWindow),
      object_id: R.path(['node', 'id'], vedgeInfoWindow),
      name: R.path(['node', 'name'], vedgeInfoWindow),
      left: R.path(['left'], vedgeInfoWindow),
      top: R.path(['top'], vedgeInfoWindow),
      show: R.path(['show'], vedgeInfoWindow),
      onCloseRequested: function () {
        store.dispatch(closeVedgeInfoWindow());
      }
    };
  },

  showVedgeInfoWindow: function () {
    let instance = Template.instance();
    let node = instance.state.get('vedgeInfoWindow').node;
    return ! R.isNil(node);
  }
});


Template.Environment.events({
  'click .sm-edit-button': function (event, instance) {
    let envName = instance.state.get('envName');
    Router.go('/wizard/' + envName,{},{});
  },

  'click .sm-scan-button': function (event, instance) {
    let envName = instance.state.get('envName');
    Router.go('scanning-request',{},{ query: { env: envName, action: 'insert' } });
  },
});

function getList(listName, envName) {
  switch (listName) {
  case 'regions':
    return Inventory.find({ 
      environment: envName,
      type: 'region'
    });   

  case 'projects':
    return Inventory.find({ 
      environment: envName,
      type: 'project'
    });   

  default:
    throw 'unknowned list type';
  }
}

function buildRoute(listName, itemKey) {
  switch (listName) {
  case 'regions':
    return buildRouteRegion(itemKey);
  case 'projects':
    return buildRouteProject(itemKey);
  default:
    throw 'unknowned list name';
  }
}

function buildRouteRegion(id_path) {
  return `/region?id_path=${id_path}`;
}

function buildRouteProject(id_path) {
  return `/project?id_path=${id_path}`;
}

function calcLastScanned(listName, envName) {
  switch (listName) {
  case 'regions':
    return R.path(['last_scanned'], Inventory.findOne({
      environment: envName, 
      type:'region'
    }));

  case 'projects':
    return R.path(['last_scanned'], Inventory.findOne({
      environment: envName, 
      type:'project'
    }));

  default:
    throw 'unknown';
  }
}
