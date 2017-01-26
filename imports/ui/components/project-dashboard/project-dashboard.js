/*
 * Template Component: ProjectDashboard 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import * as R from 'ramda';


import { Inventory } from '/imports/api/inventories/inventories';
import { store } from '/imports/ui/store/store';
import { Icon } from '/imports/lib/icon';
import { regexEscape } from '/imports/lib/regex-utils';
        
import '/imports/ui/components/accordionNavMenu/accordionNavMenu';
import '/imports/ui/components/network-info-box/network-info-box';

import './project-dashboard.html';     
    
/*  
 * Lifecycles
 */   
  
Template.ProjectDashboard.onCreated(function() {
  var instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    infoBoxes: [{
      header: ['components', 'projectDashboard', 'infoBoxes', 'networks', 'header'],
      dataSource: 'networksCount',
      icon: { type: 'material', name: 'device_hub' },
      theme: 'dark'
    }, {
      header: ['components', 'projectDashboard', 'infoBoxes', 'ports', 'header'],
      dataSource: 'portsCount',
      icon: { type: 'material', name: 'settings_input_hdmi' },
      theme: 'dark'
    }],
    project_id: null,
    networksCount: 0,
    portsCount: 0,
  });

  instance.autorun(function () {
    let controller = Iron.controller();
    let params = controller.getParams();
    let query = params.query;
    let project_id = query.id;

    instance.state.set('project_id', project_id);

    instance.subscribe('inventory?id', project_id);
    instance.subscribe('inventory?id_path_like&type', project_id, 'network');
    instance.subscribe('inventory?id_path_like&type', project_id, 'port');

    let idPathExp = new RegExp(regexEscape(project_id));
    instance.state.set('networksCount', Inventory.find({ 
      id_path: idPathExp,
      type: 'network'
    }).count());

    instance.state.set('portsCount', Inventory.find({ 
      id_path: idPathExp,
      type: 'port'
    }).count());
  });
});  

/*
Template.ProjectDashboard.rendered = function() {
};  
*/

/*
 * Events
 */

Template.ProjectDashboard.events({
});
   
/*  
 * Helpers
 */

Template.ProjectDashboard.helpers({    
  project: function () {
    let instance = Template.instance();
    let project_id = instance.state.get('project_id');

    return Inventory.findOne({ id: project_id });
  },

  infoBoxes: function () {
    let instance = Template.instance();
    return instance.state.get('infoBoxes');
  },

  networks: function () {
    let instance = Template.instance();
    let project_id = instance.state.get('project_id');
    let idPathExp = new RegExp(regexEscape(project_id));
    return Inventory.find({ 
      id_path: idPathExp,
      type: 'network'
    });
  },

  genArgsInfoBox: function (infoBox) {
    let instance = Template.instance();

    return {
      header: R.path(infoBox.header, store.getState().api.i18n),
      dataInfo: instance.state.get(infoBox.dataSource).toString(),
      icon: new Icon(infoBox.icon),
      theme: infoBox.theme
    };
  },

  argsNetworkInfoBox: function (network) {
    return {
      network: network
    };
  }
});
