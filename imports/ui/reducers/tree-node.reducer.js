//import { Mongo } from 'meteor/mongo';
import * as R from 'ramda';

import * as actions from '/imports/ui/actions/tree-node.actions';

const defaultState = {
  nodeInfo: {},
  openState: 'closed', // opened, start_close, closed, start_open
  children: []
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
      return R.assoc('nodeInfo', action.payload.nodeInfo, state);
    }

    index = R.findIndex(R.propEq('id', nodeId), state.children);
    if (index < 0) {
      return R.assoc('children',
        R.append(
          R.merge(reducer(), { id: nodeId, nodeInfo: action.payload.nodeInfo }),
          state.children
        ),
        state);
    }

    child = state.children[index];
    return R.assoc('children',
      R.update(index,
        reducer(child, actions.addUpdateTreeNode(rest, action.payload.nodeInfo)),
        state.children),
    state);

  case actions.RESET_TREE_NODE_CHILDREN:
    nodeId = R.head(action.payload.nodePath);
    rest = R.tail(action.payload.nodePath);

    if (R.isNil(nodeId)) {
      return R.assoc('children', [], state);
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
