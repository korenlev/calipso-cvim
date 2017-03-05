/*
 * Template Component: RegionDashboard 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import * as R from 'ramda';
import { Inventory } from '/imports/api/inventories/inventories';
import { store } from '/imports/ui/store/store';
import { Icon } from '/imports/lib/icon';
import { regexEscape } from '/imports/lib/regex-utils';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
//import { setCurrentNode } from '/imports/ui/actions/navigation';

import '/imports/ui/components/accordionNavMenu/accordionNavMenu';
import '/imports/ui/components/data-cubic/data-cubic';
import '/imports/ui/components/list-info-box/list-info-box';
import '/imports/ui/components/event-modals/event-modals';
        
import './region-dashboard.html';     
    
/*  
 * Lifecycles
 */   
  
Template.RegionDashboard.onCreated(function() {
  var instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    infoBoxes: [{
      header: ['components', 'regionDashboard', 'infoBoxes', 'instances', 'header'],
      dataSource: 'instancesCount',
      icon: { type: 'fa', name: 'desktop' },
      theme: 'dark'
    }, {
      header: ['components', 'regionDashboard', 'infoBoxes', 'vServices', 'header'],
      dataSource: 'vServicesCount',
      icon: { type: 'fa', name: 'object-group' },
      theme: 'dark'
    }, {
      header: ['components', 'regionDashboard', 'infoBoxes', 'hosts', 'header'],
      dataSource: 'hostsCount',
      icon: { type: 'fa', name: 'server' },
      theme: 'dark'
    }, {
      header: ['components', 'regionDashboard', 'infoBoxes', 'vConnectors', 'header'],
      dataSource: 'vConnectorsCount',
      icon: { type: 'fa', name: 'compress' },
      theme: 'dark'
    }, 
    ],
    region_id_path: null,
    instancesCount: 0,
    vServicesCount: 0,
    hostsCount: 0,
    vConnectors: 0,
    listInfoBoxes: [{
      header: ['components', 'regionDashboard', 'listInfoBoxes', 'availabilityZones', 'header'],
      listName: 'availabilityZones',
      listItemFormat: { label: 'name', value: 'id_path' },
      icon: { type: 'material', name: 'developer_board' },
    }, {
      header: ['components', 'regionDashboard', 'listInfoBoxes', 'aggregates', 'header'],
      listName: 'aggregates',
      listItemFormat: { label: 'name', value: 'id_path' },
      icon: { type: 'material', name: 'storage' },
    }]
  });

  instance.autorun(function () {
    let controller = Iron.controller();
    let params = controller.getParams();
    let query = params.query;
    let region_id_path = query.id_path;

    new SimpleSchema({
      region_id_path: { type: String },
    }).validate({ region_id_path });

    instance.state.set('region_id_path', region_id_path);

    instance.subscribe('inventory?id_path', region_id_path);
    instance.subscribe('inventory?id_path_start&type', region_id_path, 'instance');
    instance.subscribe('inventory?id_path_start&type', region_id_path, 'vservice');
    instance.subscribe('inventory?id_path_start&type', region_id_path, 'host');
    instance.subscribe('inventory?id_path_start&type', region_id_path, 'vconnector');
    instance.subscribe('inventory?id_path_start&type', region_id_path, 'availability_zone');
    instance.subscribe('inventory?id_path_start&type', region_id_path, 'aggregate');

    let idPathExp = new RegExp(`^${regexEscape(region_id_path)}`);

    instance.state.set('instancesCount', Inventory.find({ 
      id_path: idPathExp,
      type: 'instance'
    }).count());

    instance.state.set('vServicesCount', Inventory.find({ 
      id_path: idPathExp,
      type: 'vservice'
    }).count());

    instance.state.set('hostsCount', Inventory.find({ 
      id_path: idPathExp,
      type: 'host'
    }).count());

    instance.state.set('vConnectorsCount', Inventory.find({ 
      id_path: idPathExp,
      type: 'vconnector'
    }).count());
  });

});  

/*
Template.RegionDashboard.rendered = function() {
};  
*/

/*
 * Events
 */

Template.RegionDashboard.events({
});
   
/*  
 * Helpers
 */

Template.RegionDashboard.helpers({    
  region: function () {
    let instance = Template.instance();
    let region_id_path = instance.state.get('region_id_path');

    return Inventory.findOne({ id_path: region_id_path });
  },

  infoBoxes: function () {
    let instance = Template.instance();
    return instance.state.get('infoBoxes');
  },

  listInfoBoxes: function () {
    let instance = Template.instance();
    return instance.state.get('listInfoBoxes');
  },
  
  argsInfoBox: function (infoBox) {
    let instance = Template.instance();

    return {
      header: R.path(infoBox.header, store.getState().api.i18n),
      dataInfo: instance.state.get(infoBox.dataSource).toString(),
      icon: new Icon(infoBox.icon),
      theme: infoBox.theme
    };
  },

  argsListInfoBox: function (listInfoBox) {
    let instance = Template.instance();
    let region_id_path = instance.state.get('region_id_path');

    return {
      header: R.path(listInfoBox.header, store.getState().api.i18n),
      list: getList(listInfoBox.listName, region_id_path),
      //dataInfo: instance.state.get(infoBox.dataSource).toString(),
      icon: new Icon(listInfoBox.icon),
      //theme: infoBox.theme
      listItemFormat: listInfoBox.listItemFormat,
      onItemSelected: function (itemKey) {
        Router.go(buildRoute(itemKey, listInfoBox.listName));
      }
    };
  },
});

function getList(listName, parentIdPath) {
  let idPathExp = new RegExp(`^${regexEscape(parentIdPath)}`);

  switch (listName) {
  case 'availabilityZones':
    return Inventory.find({ 
      id_path: idPathExp,
      type: 'availability_zone'
    });   

  case 'aggregates':
    return Inventory.find({ 
      id_path: idPathExp,
      type: 'aggregate'
    });   

  default:
    throw 'unknowned list type';
  }
}

function buildRoute(itemKey, listName) {
  switch (listName) {
  case 'availabilityZones':
    return buildRouteZone(itemKey);
  case 'aggregates':
    return buildRouteAggregate(itemKey);
  default:
    throw 'unknowned list name';
  }
}

function buildRouteZone(id_path) {
  return `/zone?id_path=${id_path}`;
}

function buildRouteAggregate(id_path) {
  return `/aggregate?id_path=${id_path}`;
}
