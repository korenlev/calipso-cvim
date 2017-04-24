import * as R from 'ramda';

import * as actions from '/imports/ui/actions/environment-panel.actions';
import { reducer as treeNode } from './tree-node.reducer';
import { 
  updateTreeNodeInfo,
  addUpdateChildrenTreeNode, 
  resetTreeNodeChildren, 
  startOpenTreeNode,
  endOpenTreeNode,
  startCloseTreeNode,
  endCloseTreeNode,
  setChildDetectedTreeNode,
} 
  from '/imports/ui/actions/tree-node.actions';

const defaultState = {
  _id: null,
  envName: null,
  isLoaded: false,
  treeNode: treeNode(),
  selectedNode: {
    _id: null,
    type: null
  }
};

export function reducer(state = defaultState, action) {
  switch (action.type) {
  case actions.SET_ENV_NAME:
    return R.assoc('envName', action.payload.envName, state);

  case actions.UPDATE_ENV_TREE_NODE:
    return R.assoc('treeNode',
      treeNode(state.treeNode, 
        updateTreeNodeInfo(action.payload.nodeInfo, 0)),
      state);

  case actions.ADD_UPDATE_CHILDREN_ENV_TREE_NODE:
    return R.assoc('treeNode',
      treeNode(state.treeNode, 
        addUpdateChildrenTreeNode(action.payload.nodePath, action.payload.childrenInfo, 0)),
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

  case actions.SET_ENV_SELECTED_NODE:
    return R.merge(state, {
      selectedNode: { 
        _id: action.payload.nodeId,
        type: action.payload.nodeType
      }
    });

  case actions.SET_ENV_SELECTED_NODE_TYPE:
    return R.merge(state, {
      selectedNode: R.merge(state.selectedNode, {
        type: action.payload.type
      })
    });

  case actions.SET_ENV_SELECTED_NODE_AS_ENV:
    return R.merge(state, {
      selectedNode: {
        _id: state._id,
        type: 'environment'
      }
    });

  case actions.SET_ENV_ENV_ID:
    return R.assoc('_id', action.payload._id, state);

  case actions.SET_ENV_AS_LOADED:
    return R.assoc('isLoaded', true, state);

  case actions.SET_ENV_AS_NOT_LOADED:
    return R.assoc('isLoaded', false, state);

  default:
    return state;
  }
}
