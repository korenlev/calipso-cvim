/*
 * Template Component: HostDashboard 
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

import './host-dashboard.html';     
    
/*  
 * Lifecycles
 */   
  
Template.HostDashboard.onCreated(function() {
  var instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    infoBoxes: [{
      header: ['components', 'hostDashboard', 'infoBoxes', 'instances', 'header'],
      dataSource: 'instancesCount',
      icon: { type: 'fa', name: 'desktop' },
      theme: 'dark'
    }, {
      header: ['components', 'hostDashboard', 'infoBoxes', 'vServices', 'header'],
      dataSource: 'vServicesCount',
      icon: { type: 'fa', name: 'object-group' },
      theme: 'dark'
    }, {
      header: ['components', 'hostDashboard', 'infoBoxes', 'vConnectors', 'header'],
      dataSource: 'vConnectorsCount',
      icon: { type: 'fa', name: 'compress' },
      theme: 'dark'
    }, {
      header: ['components', 'hostDashboard', 'infoBoxes', 'ports', 'header'],
      dataSource: 'portsCount',
      icon: { type: 'fa', name: 'compress' },
      theme: 'dark'
    }, {
      header: ['components', 'hostDashboard', 'infoBoxes', 'networkAgents', 'header'],
      dataSource: 'networkAgentsCount',
      icon: { type: 'fa', name: 'compress' }, // todo: icon
      theme: 'dark'
    }, {
      header: ['components', 'hostDashboard', 'infoBoxes', 'pnics', 'header'],
      dataSource: 'pnicsCount',
      icon: { type: 'fa', name: 'compress' }, // todo: icon
      theme: 'dark'
    }, {
      header: ['components', 'hostDashboard', 'infoBoxes', 'vEdges', 'header'],
      dataSource: 'vEdgesCount',
      icon: { type: 'fa', name: 'external-link' },
      theme: 'dark'
    }], 
    host_id_path: null,
    instancesCount: 0,
    vServicesCount: 0,
    vConnectors: 0,
    portsCount: 0, 
    networkAgentsCount: 0,
    pnicsCount: 0,
    vEdgesCount: 0,
  });

  instance.autorun(function () {
    let data = Template.currentData();

    new SimpleSchema({
      id_path: { type: String },
    }).validate(data);

    let host_id_path = data.id_path;
    instance.state.set('host_id_path', host_id_path);

    instance.subscribe('inventory?id_path', host_id_path);
    instance.subscribe('inventory?id_path_start&type', host_id_path, 'instance');
    instance.subscribe('inventory?id_path_start&type', host_id_path, 'vservice');
    instance.subscribe('inventory?id_path_start&type', host_id_path, 'vconnector');
    instance.subscribe('inventory?id_path_start&type', host_id_path, 'network_agent');
    instance.subscribe('inventory?id_path_start&type', host_id_path, 'pnic');
    instance.subscribe('inventory?id_path_start&type', host_id_path, 'vedge');

    Inventory.find({ id_path: host_id_path }).forEach((host) => {
      instance.subscribe('inventory?env&binding:host_id&type', 
        host.environment, host.id, 'port');

      instance.state.set('portsCount', Inventory.find({
        environment: host.environment,
        'binding:host_id': host.id,
        type: 'port'
      }).count());
    });

    let idPathExp = new RegExp(`^${regexEscape(host_id_path)}`);

    instance.state.set('instancesCount', Inventory.find({ 
      id_path: idPathExp,
      type: 'instance'
    }).count());

    instance.state.set('vServicesCount', Inventory.find({ 
      id_path: idPathExp,
      type: 'vservice'
    }).count());

    instance.state.set('vConnectorsCount', Inventory.find({ 
      id_path: idPathExp,
      type: 'vconnector'
    }).count());

    instance.state.set('networkHostsCount', Inventory.find({ 
      id_path: idPathExp,
      type: 'network_host'
    }).count());

    instance.state.set('pnicsCount', Inventory.find({ 
      id_path: idPathExp,
      type: 'pnic'
    }).count());

    instance.state.set('vEdgesCount', Inventory.find({ 
      id_path: idPathExp,
      type: 'vedge'
    }).count());


  });
});  

/*
Template.HostDashboard.rendered = function() {
};  
*/

/*
 * Events
 */

Template.HostDashboard.events({
});
   
/*  
 * Helpers
 */

Template.HostDashboard.helpers({    
  host: function () {
    let instance = Template.instance();
    let host_id_path = instance.state.get('host_id_path');

    return Inventory.findOne({ id_path: host_id_path });
  },

  infoBoxes: function () {
    let instance = Template.instance();
    return instance.state.get('infoBoxes');
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
});


