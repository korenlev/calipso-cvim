//import * as R from 'ramda';

export const SET_ENV_NAME = 'SET_ENV_NAME';
export const UPDATE_ENV_TREE_NODE = 'UPDATE_ENV_TREE_NODE';
export const ADD_UPDATE_CHILDREN_ENV_TREE_NODE = 'ADD_UPDATE_CHILDREN_ENV_TREE_NODE';
export const RESET_ENV_TREE_NODE_CHILDREN = 'RESET_ENV_TREE_NODE_CHILDREN';
export const START_OPEN_ENV_TREE_NODE = 'START_OPEN_ENV_TREE_NODE';
export const END_OPEN_ENV_TREE_NODE = 'END_OPEN_ENV_TREE_NODE';
export const START_CLOSE_ENV_TREE_NODE = 'START_CLOSE_ENV_TREE_NODE';
export const END_CLOSE_ENV_TREE_NODE = 'END_CLOSE_ENV_TREE_NODE';
export const SET_ENV_CHILD_DETECTED_TREE_NODE = 'SET_ENV_CHILD_DETECTED_TREE_NODE';

export function setEnvName(envName) {
  return {
    type: SET_ENV_NAME,
    payload: {
      envName: envName
    }
  };
}

export function updateEnvTreeNode(nodeInfo) {
  return {
    type: UPDATE_ENV_TREE_NODE,
    payload: {
      nodeInfo: nodeInfo
    }
  };
}

export function addUpdateChildrenEnvTreeNode(nodePath, childrenInfo) {
  return {
    type: ADD_UPDATE_CHILDREN_ENV_TREE_NODE,
    payload: {
      nodePath: nodePath,
      childrenInfo: childrenInfo
    },
  };
}

export function resetEnvTreeNodeChildren(nodePath) {
  return {
    type: RESET_ENV_TREE_NODE_CHILDREN,
    payload: {
      nodePath: nodePath,
    }
  };
}

export function startOpenEnvTreeNode(nodePath) {
  return {
    type: START_OPEN_ENV_TREE_NODE,
    payload: {
      nodePath: nodePath,
    }
  };
}

export function endOpenEnvTreeNode(nodePath) {
  return {
    type: END_OPEN_ENV_TREE_NODE,
    payload: {
      nodePath: nodePath,
    }
  };
}

export function startCloseEnvTreeNode(nodePath) {
  return {
    type: START_CLOSE_ENV_TREE_NODE,
    payload: {
      nodePath: nodePath,
    }
  };
}

export function endCloseEnvTreeNode(nodePath) {
  return {
    type: END_CLOSE_ENV_TREE_NODE,
    payload: {
      nodePath: nodePath,
    }
  };
}

export function setEnvChildDetectedTreeNode(nodePath) {
  return {
    type: SET_ENV_CHILD_DETECTED_TREE_NODE,
    payload: {
      nodePath: nodePath
    }
  };
}
