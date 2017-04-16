//import * as R from 'ramda';

export const UPDATE_TREE_NODE_INFO = 'UPDATE_TREE_NODE_INFO';
export const ADD_UPDATE_CHILDREN_TREE_NODE = 'ADD_UPDATE_CHILDREN_TREE_NODE';
export const RESET_TREE_NODE_CHILDREN = 'RESET_TREE_NODE_CHILDREN';
export const START_OPEN_TREE_NODE = 'START_OPEN_TREE_NODE';
export const END_OPEN_TREE_NODE = 'END_OPEN_TREE_NODE';
export const START_CLOSE_TREE_NODE = 'START_CLOSE_TREE_NODE';
export const END_CLOSE_TREE_NODE = 'END_CLOSE_TREE_NODE';
export const SET_CHILD_DETECTED_TREE_NODE = 'SET_CHILD_DETECTED_TREE_NODE';

export function updateTreeNodeInfo(nodeInfo, level) {
  return {
    type: UPDATE_TREE_NODE_INFO,
    payload: {
      nodeInfo: nodeInfo,
      level: level
    }
  };
}

export function addUpdateChildrenTreeNode(nodePath, childrenInfo, level) {
  return {
    type: ADD_UPDATE_CHILDREN_TREE_NODE,
    payload: {
      nodePath: nodePath,
      childrenInfo: childrenInfo,
      level: level
    },
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

export function setChildDetectedTreeNode(nodePath) {
  return {
    type: SET_CHILD_DETECTED_TREE_NODE,
    payload: {
      nodePath: nodePath
    }
  };
}
