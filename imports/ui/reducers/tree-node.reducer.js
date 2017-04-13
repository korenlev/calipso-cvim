//import { Mongo } from 'meteor/mongo';
import * as R from 'ramda';

import * as actions from '/imports/ui/actions/tree-node.actions';

const defaultState = {
  nodeInfo: {},
  openState: 'closed', // opened, start_close, closed, start_open
  children: [],
  childDetected: false,
  level: 1
};

export function reducer(state = defaultState, action) {
  let nodeId;
  let rest;
  let child;
  let index;

  if (R.isNil(action)) { return defaultState; }

  switch (action.type) {

  case actions.ADD_UPDATE_TREE_NODE:
    nodeId = R.head(action.payload.nodePath);
    rest = R.tail(action.payload.nodePath);

    if (R.isNil(nodeId)) {
      return R.merge(state, {
        nodeInfo: action.payload.nodeInfo,
        level: action.payload.level
      });
    }

    index = R.findIndex(R.propEq('id', nodeId), state.children);
    // todo: relie on below dispatch to update child after adition.  
    if (index < 0) {
      return R.merge(state, {
        children:
          R.append(
            R.merge(reducer(), { 
              id: nodeId, 
              nodeInfo: action.payload.nodeInfo,
              level: action.payload.level + 1
            }),
            state.children
          ),
        childDetected: true,
      });
    }

    child = state.children[index];
    return R.merge(state, {
      children:
        R.update(index,
          reducer(child, actions.addUpdateTreeNode(
            rest, action.payload.nodeInfo, action.payload.level + 1)),
          state.children),
      childDetected: true
    });

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
  let index = R.findIndex(R.propEq('id', nodeId), state.children);
  let child = state.children[index];

  return R.assoc('children',
    R.update(index,
      reducer(child, action),
      state.children),
  state);
}
