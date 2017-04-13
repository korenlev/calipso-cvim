//import * as R from 'ramda';

export const ADD_UPDATE_TREE_NODE = 'ADD_UPDATE_TREE_NODE';
export const RESET_TREE_NODE_CHILDREN = 'RESET_TREE_NODE_CHILDREN';
export const START_OPEN_TREE_NODE = 'START_OPEN_TREE_NODE';
export const END_OPEN_TREE_NODE = 'END_OPEN_TREE_NODE';
export const START_CLOSE_TREE_NODE = 'START_CLOSE_TREE_NODE';
export const END_CLOSE_TREE_NODE = 'END_CLOSE_TREE_NODE';

export function addUpdateTreeNode(nodePath, nodeInfo) {
  return {
    type: ADD_UPDATE_TREE_NODE,
    payload: {
      nodePath: nodePath,
      nodeInfo: nodeInfo,
    }
  };
}

export function resetTreeNodeChildren(nodePath) {
  return {
    type: RESET_TREE_NODE_CHILDREN,
    payload: {
      nodePath: nodePath,
    }
  };
}

export function startOpenTreeNode(nodePath) {
  return {
    type: START_OPEN_TREE_NODE,
    payload: {
      nodePath: nodePath,
    }
  };
}

export function endOpenTreeNode(nodePath) {
  return {
    type: END_OPEN_TREE_NODE,
    payload: {
      nodePath: nodePath,
    }
  };
}

export function startCloseTreeNode(nodePath) {
  return {
    type: START_CLOSE_TREE_NODE,
    payload: {
      nodePath: nodePath,
    }
  };
}

export function endCloseTreeNode(nodePath) {
  return {
    type: END_CLOSE_TREE_NODE,
    payload: {
      nodePath: nodePath,
    }
  };
}
