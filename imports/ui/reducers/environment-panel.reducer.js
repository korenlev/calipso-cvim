import * as R from 'ramda';

import * as actions from '/imports/ui/actions/environment-panel.actions';
import { reducer as treeNode } from './tree-node.reducer';
import { 
  addUpdateTreeNode, 
  resetTreeNodeChildren, 
  startOpenTreeNode,
  endOpenTreeNode,
  startCloseTreeNode,
  endCloseTreeNode,
  setChildDetectedTreeNode,
} 
from '/imports/ui/actions/tree-node.actions';

const defaultState = {
  envName: null,
  treeNode: treeNode()
};

export function reducer(state = defaultState, action) {
  switch (action.type) {
  case actions.SET_ENV_NAME:
    return R.assoc('envName', action.payload.envName, state);

  case actions.ADD_UPDATE_ENV_TREE_NODE:
    return R.assoc('treeNode',
      treeNode(state.treeNode, 
        addUpdateTreeNode(action.payload.nodePath, action.payload.nodeInfo, 0)),
      state);

  case actions.RESET_ENV_TREE_NODE_CHILDREN:
    return R.assoc('treeNode',
      treeNode(state.treeNode, resetTreeNodeChildren(action.payload.nodePath)),
      state
    );

  case actions.START_OPEN_ENV_TREE_NODE:
    return R.assoc('treeNode',
      treeNode(state.treeNode, startOpenTreeNode(action.payload.nodePath)),
      state
    );

  case actions.END_OPEN_ENV_TREE_NODE:
    return R.assoc('treeNode',
      treeNode(state.treeNode, endOpenTreeNode(action.payload.nodePath)),
      state
    );

  case actions.START_CLOSE_ENV_TREE_NODE:
    return R.assoc('treeNode',
      treeNode(state.treeNode, startCloseTreeNode(action.payload.nodePath)),
      state
    );

  case actions.END_CLOSE_ENV_TREE_NODE:
    return R.assoc('treeNode',
      treeNode(state.treeNode, endCloseTreeNode(action.payload.nodePath)),
      state
    );

  case actions.SET_ENV_CHILD_DETECTED_TREE_NODE:
    return R.assoc('treeNode',
      treeNode(state.treeNode, setChildDetectedTreeNode(action.payload.nodePath)),
      state
    );

  default:
    return state;
  }
}
