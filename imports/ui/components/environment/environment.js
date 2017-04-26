/*
 * Tempalte Component: Environment
 */

/*
 * Lifecycles methods
 */

import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
//import { ReactiveVar } from 'meteor/reactive-var';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
import factory from 'reactive-redux';
import { _idFieldDef } from '/imports/lib/simple-schema-utils';
//import { idToStr } from '/imports/lib/utilities';

import { Environments } from '/imports/api/environments/environments';
import { Inventory } from '/imports/api/inventories/inventories';
//import { Messages } from '/imports/api/messages/messages';

import { store } from '/imports/ui/store/store';
//import { setCurrentNode } from '/imports/ui/actions/navigation';
import { 
  setEnvEnvId,
  setEnvName, 
  updateEnvTreeNode, 
  startOpenEnvTreeNode,
  setEnvSelectedNodeType,
  setEnvAsLoaded,
  setEnvAsNotLoaded,
  setEnvSelectedNodeAsEnv,
  toggleEnvShow,
//  setShowDashboard,
//  setShowGraph,
} from '/imports/ui/actions/environment-panel.actions';
//import { setMainAppSelectedEnvironment } from '/imports/ui/actions/main-app.actions';
import { closeVedgeInfoWindow } from '/imports/ui/actions/vedge-info-window.actions';
import { setEnvSelectedNode } 
  from '/imports/ui/actions/environment-panel.actions';

import '/imports/ui/components/accordion-nav-menu/accordion-nav-menu';
import '/imports/ui/components/graph-tooltip-window/graph-tooltip-window';
import '/imports/ui/components/vedge-info-window/vedge-info-window';
import '/imports/ui/components/env-delete-modal/env-delete-modal';
import '/imports/ui/components/environment-dashboard/environment-dashboard';

import './environment.html';

let maxOpenTreeNodeTrialCount = 3;

var nodeTypesForSelection = [
  'project', 
  'availability_zone',
  'host',
  'environment',
  'aggregate',
  'host',
  'region',
];

/*
 * Lifecycles
 */

Template.Environment.onCreated(function () {
  var instance = this;

  // reactive state
  instance.state = new ReactiveDict();
  instance.state.setDefault({
    graphTooltipWindow: { label: '', title: '', left: 0, top: 0, show: false },
    vedgeInfoWindow: { node: null, left: 0, top: 0, show: false },
    dashboardName: 'environment',
    clickedNode: null,
  });

  createAttachedFns(instance);

  const envIdSelector = (state) => (state.components.environmentPanel._id);
  instance.rdxEnvId = factory(envIdSelector, store);  

  const mainNodeSelector = (state) => (state.components.environmentPanel.treeNode);
  instance.rdxMainNode = factory(mainNodeSelector, store);

  const selectedNodeIdSelector = 
    (state) => (state.components.environmentPanel.selectedNode._id);
  instance.rdxSelectedNodeId = factory(selectedNodeIdSelector, store);

  const selectedNodeTypeSelector = 
    (state) => (state.components.environmentPanel.selectedNode.type);
  instance.rdxSelectedNodeType = factory(selectedNodeTypeSelector, store);

  const envNameSelector = (state) => (state.components.environmentPanel.envName);
  instance.rdxEnvName = factory(envNameSelector, store);

  const isLoadedSelector = (state) => (state.components.environmentPanel.isLoaded);
  instance.rdxIsLoaded = factory(isLoadedSelector, store);

  const showTypeSelector = (state) => (state.components.environmentPanel.showType);
  instance.rdxShowType = factory(showTypeSelector, store);

  // Autorun component input
  instance.autorun(function () {
    let data = Template.currentData();
    
    new SimpleSchema({
      _id: _idFieldDef, 
      selectedNodeId: R.assoc('optional', true, _idFieldDef),
    }).validate(data);

    store.dispatch(setEnvEnvId(data._id));
    if (R.isNil(data.selectedNodeId)) {
      store.dispatch(setEnvSelectedNodeAsEnv());
    } else {
      store.dispatch(setEnvSelectedNode(data.selectedNodeId));
    }
  });

  // Autorun object id
  instance.autorun(function () {
    let _id = instance.rdxEnvId.get();
    store.dispatch(setEnvAsNotLoaded());

    instance.subscribe('environments?_id', _id);
    Environments.find({ _id: _id }).forEach((env) => {
      store.dispatch(setEnvName(env.name));
      store.dispatch(updateEnvTreeNode(env));
      store.dispatch(setEnvAsLoaded());
      store.dispatch(startOpenEnvTreeNode([]));
    });
  });

  // Autorun selected node
  instance.autorun(function () {
    let selectedNodeId = instance.rdxSelectedNodeId.get(); 
    let selectedNodeType = instance.rdxSelectedNodeType.get();

    if (R.isNil(selectedNodeId)) { return; }
    if (selectedNodeType === 'environment') { return; }

    instance.subscribe('inventory?_id', selectedNodeId);
    Inventory.find({ _id: selectedNodeId }).forEach((selectedNode) => {
      store.dispatch(setEnvSelectedNodeType(selectedNode.type));

      let path = R.split('/', selectedNode.id_path);
      path = R.drop(2, path); // drop '' and 'envName'.
      openTreeNode([R.head(path)], R.tail(path), 0);
    });
  });

  /////////////////

  instance.storeUnsubscribe = store.subscribe(() => {
    let state = store.getState();

    let graphTooltipWindow = state.components.graphTooltipWindow;
    instance.state.set('graphTooltipWindow', graphTooltipWindow);

    let vedgeInfoWindow = state.components.vedgeInfoWindow;
    instance.state.set('vedgeInfoWindow', vedgeInfoWindow);
    
  });

    /*
    (() => {
      if (R.isNil(controller.params.query.selectedNodeId) &&
          R.isNil(selectedNodeId)) {
        return;
      }

      let srlSelectedNodeId = idToStr(selectedNodeId);
      if (R.equals(controller.params.query.selectedNodeId, srlSelectedNodeId)) {
        return;
      }

      setTimeout(() => {
        Router.go('environment', 
          { _id: controller.params._id }, 
          { query: { selectedNodeId: srlSelectedNodeId } });
      }, 1);

    })();
    */

});

Template.Environment.onDestroyed(function () {
  let instance = this;
  instance.storeUnsubscribe();
  instance.rdxMainNode.cancel();
  instance.rdxEnvId.cancel();
  instance.rdxSelectedNodeId.cancel();
  instance.rdxEnvName.cancel();
  instance.rdxIsLoaded.cancel();
  instance.rdxShowType.cancel();
});

Template.Environment.rendered = function(){
};

/*
 * Helpers
 */

Template.Environment.helpers({
  isLoaded: function () {
    let instance = Template.instance();
    return instance.rdxIsLoaded.get();
  },

  envName: function(){
    let instance = Template.instance();
    return instance.rdxEnvName.get();
  },

  mainNode: function () {
    let instance = Template.instance();
    return instance.rdxMainNode.get();
  },

  selectedNodeType: function () {
    let instance = Template.instance();
    return instance.rdxSelectedNodeType.get();
  },

  getState: function (key) {
    let instance = Template.instance();
    return instance.state.get(key);
  },

  argsNavMenu: function (envName, mainNode) {
    let instance = Template.instance();
    return {
      envName: envName,
      mainNode: mainNode,
      onNodeSelected: instance._fns.onNodeSelected,
      onToggleGraphReq: function () {
        store.dispatch(toggleEnvShow());
      },

      onResetSelectedNodeReq: function () {
        store.dispatch(setEnvSelectedNodeAsEnv());
      },
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

  argsD3Graph: function () {
    let instance = Template.instance();

    return {
      id_path: R.path(['id_path'], instance.state.get('clickedNode'))
    };
  },

  showVedgeInfoWindow: function () {
    let instance = Template.instance();
    let node = instance.state.get('vedgeInfoWindow').node;
    return ! R.isNil(node);
  },

  isClickedNodeAGraph: function () {
    let instance = Template.instance();
    let node = instance.state.get('clickedNode');

    return !R.isNil(node.clique);
  },

  dashboardTemplate: function () {
    let instance = Template.instance();
    let selectedNodeType = instance.rdxSelectedNodeType.get();
    let dashTemplate = 'EnvironmentDashboard';

    switch (selectedNodeType) {
    case 'project':
      dashTemplate = 'ProjectDashboard';
      break;

    case 'region':
      dashTemplate = 'RegionDashboard';
      break;

    case 'aggregate':
      dashTemplate = 'AggregateDashboard';
      break;

    case 'host':
      dashTemplate = 'HostDashboard';
      break;

    case 'availability_zone':
      dashTemplate = 'ZoneDashboard';
      break;

    case 'environment':
      dashTemplate = 'EnvironmentDashboard';
      break;

    default:
      dashTemplate = 'EmptyDashboard';
    }

    return dashTemplate;
  },

  rdxSelectedNodeId: function () {
    let instance = Template.instance();
    return instance.rdxSelectedNodeId.get();
  },

  argsDashboard: function (nodeId) {
    //let instance = Template.instance();

    return {
      _id: nodeId,
      onNodeSelected: function (selectedNodeId) {
        store.dispatch(setEnvSelectedNode(selectedNodeId, null));
      }
    };
  },

  argsBreadCrumb: function (selectedNodeId) {
    return {
      nodeId: selectedNodeId,
      onNodeSelected: function (node) {
        store.dispatch(setEnvSelectedNode(node._id, null));
      }
    };
  },

  getShow: function (qShowType) {
    let instance = Template.instance();
    let showType = instance.rdxShowType.get();

    return R.equals(showType, qShowType);
  },
}); // end: helpers


Template.Environment.events({
});

function openTreeNode(path, rest, trialCount) {
  if (trialCount > maxOpenTreeNodeTrialCount) {
    return;
  }

  let tree = store.getState().components.environmentPanel
    .treeNode;

  let node = getNodeInTree(path, tree);
  if (R.isNil(node)) { return; }
  
  if (node.openState === 'closed') {
    store.dispatch(startOpenEnvTreeNode(path)); 
    setTimeout(() => {
      openTreeNode(path, rest, trialCount + 1);
    }, 200);
    return;
  }

  if (R.length(rest) === 0) { return; } 

  let newPath = R.append(R.head(rest), path);
  let newRest = R.drop(1, rest);
  openTreeNode(newPath, newRest, 0);
}

function getNodeInTree(path, tree) {
  if (R.length(path) === 0) { return tree; }

  let first = R.head(path);
  let rest = R.tail(path);
  let child = R.find(R.pathEq(['nodeInfo', 'id'], first), 
    tree.children); 

  if (R.isNil(child)) { return null; }
 
  return getNodeInTree(rest, child);  
}

function createAttachedFns(instance) {
  instance._fns = {
    onNodeSelected: (nodeInfo) => {
      if (R.contains(nodeInfo.type, nodeTypesForSelection)) {
        store.dispatch(setEnvSelectedNode(nodeInfo._id, null));
      }
    },
  };
}
