/*
 * Tempalte Component: Environment
 */

/*
 * Lifecycles methods
 */

import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import * as R from 'ramda';

import { Environments } from '/imports/api/environments/environments';
//import { Messages } from '/imports/api/messages/messages';

import { store } from '/imports/ui/store/store';
import { setCurrentNode } from '/imports/ui/actions/navigation';
import { setEnvName } from '/imports/ui/actions/environment-panel.actions';
import { closeVedgeInfoWindow } from '/imports/ui/actions/vedge-info-window.actions';

import '/imports/ui/components/accordionNavMenu/accordionNavMenu';
import '/imports/ui/components/graph-tooltip-window/graph-tooltip-window';
import '/imports/ui/components/vedge-info-window/vedge-info-window';
import '/imports/ui/components/event-modals/event-modals';
import '/imports/ui/components/env-delete-modal/env-delete-modal';
import '/imports/ui/components/environment-dashboard/environment-dashboard';

import './environment.html';

/*
 * Lifecycles
 */

Template.Environment.onCreated(function () {
  var instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    childNodeRequested: null,
    _id: null,
    envName: null,
    graphTooltipWindow: { label: '', title: '', left: 0, top: 0, show: false },
    vedgeInfoWindow: { node: null, left: 0, top: 0, show: false },
    dashboardName: 'environment',
    clickedNode: null
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

    if (query.resetDashboard === 'true') {
      $('.mainContentData').show();
      $('#dgraphid').hide();

      store.dispatch(setCurrentNode({
        id_path: '/' + envName,
        name_path: '/' + envName
      }));

      instance.state.set('dashboardName', 'environment');

      let newRoute = Router.current().route.path({}, { 
        query: R.dissoc('resetDashboard', query) 
      });
      Router.go(newRoute);
    }

    instance.subscribe('environments?name', envName);

    Environments.find({ name: envName }).forEach((env) => {
      instance.state.set('_id', env._id);
    });
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

  childNodeRequested: function () {
    let instance = Template.instance();
    return instance.state.get('childNodeRequested');
  },

  createNavMenuArgs: function (childNodeRequested) {
    let instance = Template.instance();
    return {
      childNodeRequested: childNodeRequested,
      onNodeClick: function (node) {
        if (R.contains(node.type, ['project', 'aggregate', 'region', 'host', 
          'availability_zone'])) {
          instance.state.set('dashboardName', node.type);
          instance.state.set('clickedNode', node);  
        }
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
  },

  argsEnvDashboard: function () {
    let instance = Template.instance();

    return {
      _id: instance.state.get('_id'),
    };
  },

  argsInventoryNodeDashboard: function () {
    let instance = Template.instance();
    let node = instance.state.get('clickedNode');

    return {
      id_path: node.id_path
    };
  },

  isShowDashboard: function (dashboardName) {
    let instance = Template.instance();
    if (R.isNil(instance.state.get('_id'))) { return false; }

    return instance.state.get('dashboardName') === dashboardName;
  },

});


Template.Environment.events({
});
