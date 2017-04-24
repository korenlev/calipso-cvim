//import { Mongo } from 'meteor/mongo';
import * as R from 'ramda';

import * as actions from '/imports/ui/actions/tree-node.actions';

const defaultState = {
  _id: null,
  nodeInfo: {},
  openState: 'closed', // opened, start_close, closed, start_open
  children: [],
  childDetected: false,
  level: 1
};

export function reducer(state = defaultState, action) {
  let nodeId;
  let rest;
  //let child;
  //let index;

  if (R.isNil(action)) { return defaultState; }

  switch (action.type) {

  case actions.UPDATE_TREE_NODE_INFO:
    return R.merge(state, {
      _id: action.payload.nodeInfo._id._str,
      nodeInfo: action.payload.nodeInfo,
      openState: 'closed',
      children: [],
      childDetected: false,
      level: action.payload.level,
    });

  case actions.ADD_UPDATE_CHILDREN_TREE_NODE:
    nodeId = R.head(action.payload.nodePath);
    rest = R.tail(action.payload.nodePath);

    if (R.isNil(nodeId)) {
      let actionChildren = R.map((childInfo) => {
        let existingChild = R.find(
          R.pathEq(['nodeInfo', '_id', '_str'], childInfo._id._str), state.children);

        return reducer(existingChild,  
            actions.updateTreeNodeInfo(childInfo, action.payload.level + 1));
      }, action.payload.childrenInfo);

      let allChildren = R.unionWith(R.eqBy(R.path(['nodeInfo', '_id', '_str'])), 
        actionChildren, state.children);
      
      /*
      R.forEach((actionChild) => {
        let index = R.findIndex(R.pathEq(['nodeInfo', '_id', '_str'], actionChild._id._str),state.children);
        if (index < 0) {
          state.children.push(actionChild);
        } else {
          state.children[index] = actionChild;
        }
      }, actionChildren);
      let allChildren = state.children;
      */

      return R.merge(state, {
        children: allChildren,
        childDetected: R.length(allChildren) > 0
      });
      
      /*
      state.childDetected = R.length(allChildren) > 0;
      return state;
      */
    }

    return reduceActionOnChild(state, 
      actions.addUpdateChildrenTreeNode(
        rest, action.payload.childrenInfo, action.payload.level + 1), 
      nodeId);

  case actions.RESET_TREE_NODE_CHILDREN:
    nodeId = R.head(action.payload.nodePath);
    rest = R.tail(action.payload.nodePath);

    if (R.isNil(nodeId)) {
      return R.merge(state, { 
        children: [],
        childDetected: false
      });
    }

    return reduceActionOnChild(state, actions.resetTreeNodeChildren(rest), nodeId);

  case actions.START_OPEN_TREE_NODE:
    nodeId = R.head(action.payload.nodePath);
    rest = R.tail(action.payload.nodePath);

    if (R.isNil(nodeId)) {
      return R.assoc('openState', 'start_open', state);
    }

    return reduceActionOnChild(state, actions.startOpenTreeNode(rest), nodeId);

  case actions.END_OPEN_TREE_NODE:
    nodeId = R.head(action.payload.nodePath);
    rest = R.tail(action.payload.nodePath);

    if (R.isNil(nodeId)) {
      return R.assoc('openState', 'opened', state);
    }

    return reduceActionOnChild(state, actions.endOpenTreeNode(rest), nodeId);

  case actions.START_CLOSE_TREE_NODE:
    nodeId = R.head(action.payload.nodePath);
    rest = R.tail(action.payload.nodePath);

    if (R.isNil(nodeId)) {
      return R.assoc('openState', 'start_close', state);
    }

    return reduceActionOnChild(state, actions.startCloseTreeNode(rest), nodeId);

  case actions.END_CLOSE_TREE_NODE:
    nodeId = R.head(action.payload.nodePath);
    rest = R.tail(action.payload.nodePath);

    if (R.isNil(nodeId)) {
      return R.assoc('openState', 'closed', state);
    }

    return reduceActionOnChild(state, actions.endCloseTreeNode(rest), nodeId);

  case actions.SET_CHILD_DETECTED_TREE_NODE:
    nodeId = R.head(action.payload.nodePath);
    rest = R.tail(action.payload.nodePath);

    if (R.isNil(nodeId)) {
      return R.assoc('childDetected', true, state);
    }

    return reduceActionOnChild(state, actions.setChildDetectedTreeNode(rest), nodeId);

  default:
    return state;
  }
}

function reduceActionOnChild(state, action, nodeId) {
  let index = R.findIndex(R.pathEq(['nodeInfo', '_id', '_str'], nodeId), state.children);
  if (index < 0) throw 'error in reduce action on child';
  let child = state.children[index];

  return R.assoc('children',
    R.update(index,
      reducer(child, action),
      state.children),
  state);
}
