/*
 * Template Component: EnvironmentDashboard 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import * as R from 'ramda';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { remove } from '/imports/api/environments/methods';
import { Icon } from '/imports/lib/icon';
import { store } from '/imports/ui/store/store';
import { Environments } from '/imports/api/environments/environments';
import { Inventory } from '/imports/api/inventories/inventories';
import { Messages } from '/imports/api/messages/messages';
import { Counts } from 'meteor/tmeasday:publish-counts';
        
import '/imports/ui/components/data-cubic/data-cubic';
import '/imports/ui/components/icon/icon';
import '/imports/ui/components/list-info-box/list-info-box';
import './environment-dashboard.html';     
    

let briefInfoList =  [{
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
}];

let listInfoBoxes = [{
  header: ['components', 'environment', 'listInfoBoxes', 'regions', 'header'],
  listName: 'regions',
  listItemFormat: { 
    getLabelFn: (item) => { return item.name; },
    getValueFn: (item) => { return item._id._str; },
  },
  icon: { type: 'material', name: 'public' },
}, {
  header: ['components', 'environment', 'listInfoBoxes', 'projects', 'header'],
  listName: 'projects',
  listItemFormat: { 
    getLabelFn: (item) => { return item.name; },
    getValueFn: (item) => { return item._id._str; },
  },
  icon: { type: 'material', name: 'folder' },
}];

/*  
 * Lifecycles
 */   
  
Template.EnvironmentDashboard.onCreated(function() {
  var instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    _id: null,
    envName: null,
  });

  instance.autorun(function () {
    let data = Template.currentData();
    new SimpleSchema({
      _id: { type: { _str: { type: String, regEx: SimpleSchema.RegEx.Id } } },
      onNodeSelected: { type: Function },
    }).validate(data);

    instance.state.set('_id', data._id);
  });

  instance.autorun(function () {
    let _id = instance.state.get('_id');

    instance.subscribe('environments?_id', _id);
    Environments.find({ _id: _id }).forEach((env) => {
      instance.state.set('envName', env.name);
      instance.state.set('infoLastScanning', env.last_scanned);

      instance.subscribe('inventory?env+type', env.name, 'instance');
      instance.subscribe('inventory?env+type', env.name, 'vservice');
      instance.subscribe('inventory?env+type', env.name, 'host');
      instance.subscribe('inventory?env+type', env.name, 'vconnector');
      instance.subscribe('inventory?env+type', env.name, 'project');
      instance.subscribe('inventory?env+type', env.name, 'region');
      instance.subscribe('messages?env+level', env.name, 'info');
      instance.subscribe('messages?env+level', env.name, 'warn');
      instance.subscribe('messages?env+level', env.name, 'error');

      let vConnectorCounterName = 'inventory?env+type!counter?env=' +
        env.name + '&type=' + 'vconnector';
      let infoVConnectorsCount = Counts.get(vConnectorCounterName);
      instance.state.set('infoVConnectorsCount', infoVConnectorsCount);

      let hostsCounterName = 'inventory?env+type!counter?env=' +
        env.name + '&type=' + 'host';
      let infoHostsCount = Counts.get(hostsCounterName);
      instance.state.set('infoHostsCount', infoHostsCount);

      let vServicesCounterName = 'inventory?env+type!counter?env=' +
        env.name + '&type=' + 'vservice';
      let infoVServicesCount =  Counts.get(vServicesCounterName);
      instance.state.set('infoVServicesCount', infoVServicesCount);

      let instancesCounterName = 'inventory?env+type!counter?env=' +
        env.name + '&type=' + 'instance';
      let infoInstancesCount = Counts.get(instancesCounterName);
      instance.state.set('infoInstancesCount', infoInstancesCount);

      let projectsCounterName = 'inventory?env+type!counter?env=' +
        env.name + '&type=' + 'project';
      let projectsCount = Counts.get(projectsCounterName);
      instance.state.set('projectsCount', projectsCount);

      let regionsCounterName = 'inventory?env+type!counter?env=' +
        env.name + '&type=' + 'region';
      let regionsCount = Counts.get(regionsCounterName);
      instance.state.set('regionsCount', regionsCount);
    });

  });
});  

/*
Template.EnvironmentDashboard.rendered = function() {
};  
*/

/*
 * Events
 */

Template.EnvironmentDashboard.events({
  'click .sm-edit-button': function (event, instance) {
    let envName = instance.state.get('envName');
    Router.go('/wizard/' + envName,{},{});
  },

  'click .sm-scan-button': function (event, instance) {
    let envName = instance.state.get('envName');
    Router.go('scanning-request',{},{ query: { env: envName, action: 'insert' } });
  },
});
   
/*  
 * Helpers
 */

Template.EnvironmentDashboard.helpers({    
  getState: function (key) {
    let instance = Template.instance();
    return instance.state.get(key);
  },

  getListInfoBoxes: function () {
    return listInfoBoxes;
  },
  
  getBriefInfoList: function () {
    return briefInfoList;
  },

  infoMessagesCount: function(){
    let instance = Template.instance();
    let envName = instance.state.get('envName');
    if (R.isNil(envName)) { return; }

    return Counts.get('messages?env+level!counter?env=' +
     envName + '&level=' + 'info');
  },

  warningsCount: function(){
    let instance = Template.instance();
    let envName = instance.state.get('envName');
    if (R.isNil(envName)) { return; }

    return Counts.get('messages?env+level!counter?env=' +
     envName + '&level=' + 'warn');
  },

  errorsCount: function(){
    let instance = Template.instance();
    let envName = instance.state.get('envName');
    if (R.isNil(envName)) { return; }

    return Counts.get('messages?env+level!counter?env=' +
       envName + '&level=' + 'error');
  },

  argsEnvDeleteModal: function () {
    let instance = Template.instance();
    return {
      onDeleteReq: function () {
        instance.$('#env-delete-modal').modal('hide'); 
        let _id = instance.state.get('_id');
        remove.call({ _id: _id }, function (error, _res) {
          if (R.isNil(error)) {
            setTimeout(() => {
              Router.go('/dashboard');
            }, 700);
          } else {
            alert('error removing environment. ' + error.message);
          }
        });
        console.log('delete req performed');
      }
    };
  },

  argsBriefInfo: function (briefInfo) {
    let instance = Template.instance();
    return {
      header: R.path(briefInfo.header, store.getState().api.i18n),
      dataInfo: R.toString(instance.state.get(briefInfo.dataSource)),
      icon: new Icon(briefInfo.icon)
    };
  },

  argsListInfoBox: function (listInfoBox) {
    let instance = Template.instance();
    let data = Template.currentData();
    let envName = instance.state.get('envName');

    //let lastScanned = calcLastScanned(listInfoBox.listName, envName);

    return {
      header: R.path(listInfoBox.header, store.getState().api.i18n),
      list: getList(listInfoBox.listName, envName),
      icon: new Icon(listInfoBox.icon),
      listItemFormat: listInfoBox.listItemFormat,
      //lastScanning: lastScanned,      
      onItemSelected: function (itemKey) {
        data.onNodeSelected(new Mongo.ObjectID(itemKey));
      }
    };
  },

  lastMessageTimestamp: function (level, envName) {
    if (R.any(R.isNil)([level, envName])) { return ''; }

    let message =  Messages.findOne({ environment: envName, level: level }, {
      sort: { timestamp: -1 } });

    return R.prop('timestamp', message);
  }
}); // end: helpers

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

/*
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
*/
