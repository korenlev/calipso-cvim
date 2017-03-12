/*
 * Template Component: AggregateDashboard 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { Inventory } from '/imports/api/inventories/inventories';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { regexEscape } from '/imports/lib/regex-utils';
import * as R from 'ramda';
import { store } from '/imports/ui/store/store';
import { Icon } from '/imports/lib/icon';
        
import '/imports/ui/components/accordionNavMenu/accordionNavMenu';
import '/imports/ui/components/data-cubic/data-cubic';
import '/imports/ui/components/list-info-box/list-info-box';
import '/imports/ui/components/event-modals/event-modals';

import './aggregate-dashboard.html';     
    
/*  
 * Lifecycles
 */   
  
Template.AggregateDashboard.onCreated(function() {
  var instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    infoBoxes: [{
      header: ['components', 'aggregateDashboard', 'infoBoxes', 'instances', 'header'],
      dataSource: 'instancesCount',
      icon: { type: 'fa', name: 'desktop' },
      theme: 'dark'
    }, {
      header: ['components', 'aggregateDashboard', 'infoBoxes', 'vServices', 'header'],
      dataSource: 'vServicesCount',
      icon: { type: 'fa', name: 'object-group' },
      theme: 'dark'
    }, {
      header: ['components', 'aggregateDashboard', 'infoBoxes', 'hosts', 'header'],
      dataSource: 'hostsCount',
      icon: { type: 'fa', name: 'server' },
      theme: 'dark'
    }, {
      header: ['components', 'aggregateDashboard', 'infoBoxes', 'vConnectors', 'header'],
      dataSource: 'vConnectorsCount',
      icon: { type: 'fa', name: 'compress' },
      theme: 'dark'
    }, {
      header: ['components', 'aggregateDashboard', 'infoBoxes', 'vEdges', 'header'],
      dataSource: 'vEdgesCount',
      icon: { type: 'fa', name: 'external-link' },
      theme: 'dark'
    }], 

    listInfoBoxes: [{
      header: ['components', 'aggregateDashboard', 'listInfoBoxes', 'hosts', 'header'],
      listName: 'hosts',
      listItemFormat: { label: 'name', value: 'id_path' },
      icon: { type: 'material', name: 'developer_board' },
    }
    ],
    aggregate_id_path: null,
    instancesCount: 0,
    vServicesCount: 0,
    hostsCount: 0,
    vConnectors: 0,
    vEdges: 0,
  });

  instance.autorun(function () {
    let data = Template.currentData();

    new SimpleSchema({
      id_path: { type: String },
    }).validate(data);

    let aggregate_id_path = data.id_path;

    instance.state.set('aggregate_id_path', aggregate_id_path);

    instance.subscribe('inventory?id_path', aggregate_id_path);
    instance.subscribe('inventory?id_path_start&type', aggregate_id_path, 'instance');
    instance.subscribe('inventory?id_path_start&type', aggregate_id_path, 'vservice');
    instance.subscribe('inventory?id_path_start&type', aggregate_id_path, 'host');
    instance.subscribe('inventory?id_path_start&type', aggregate_id_path, 'vconnector');
    instance.subscribe('inventory?id_path_start&type', aggregate_id_path, 'vedge');

    let idPathExp = new RegExp(`^${regexEscape(aggregate_id_path)}`);

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

    instance.state.set('vEdgesCount', Inventory.find({ 
      id_path: idPathExp,
      type: 'vedge'
    }).count());
  });
});  

/*
Template.AggregateDashboard.rendered = function() {
};  
*/

/*
 * Events
 */

Template.AggregateDashboard.events({
});
   
/*  
 * Helpers
 */

Template.AggregateDashboard.helpers({    
  aggregate: function () {
    let instance = Template.instance();
    let aggregate_id_path = instance.state.get('aggregate_id_path');

    return Inventory.findOne({ id_path: aggregate_id_path });
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
    let aggregate_id_path = instance.state.get('aggregate_id_path');

    return {
      header: R.path(listInfoBox.header, store.getState().api.i18n),
      list: getList(listInfoBox.listName, aggregate_id_path),
      //dataInfo: instance.state.get(infoBox.dataSource).toString(),
      icon: new Icon(listInfoBox.icon),
      //theme: infoBox.theme
      listItemFormat: listInfoBox.listItemFormat,
      onItemSelected: function (itemKey) {
        Router.go(`/host?id_path=${itemKey}`);
      }
    };
  }
});


function getList(listName, parentIdPath) {
  let idPathExp = new RegExp(`^${regexEscape(parentIdPath)}`);

  switch (listName) {
  case 'hosts':
    return Inventory.find({ 
      id_path: idPathExp,
      type: 'host'
    });   

  default:
    throw 'unknowned list type';
  }
}
