import * as R from 'ramda';

const SET_CURRENT_NODE = 'SET_CURRENT_NODE';
const SET_CURRENT_NODE_FROM_TREE_CONTROL = 'SET_CURRENT_NODE_FROM_TREE_CONTROL';

function setCurrentNode(idPath, namePath) {
  let nodeChain = convertToNodeChain(idPath, namePath);

  return {
    type: SET_CURRENT_NODE,
    payload: {
      nodeChain: nodeChain
    }
  };
}

function setCurrentNodeFromTreeControl (idPath, namePath) {
  let nodeChain = convertToNodeChain(idPath, namePath);

  return {
    type: SET_CURRENT_NODE_FROM_TREE_CONTROL,
    payload: {
      nodeChain: nodeChain
    }
  };
}

function convertToNodeChain(idPath, namePath) {
  let convert = R.pipe(R.split(), R.slice(1, Infinity));
  let paths = convert('/', idPath);
  let names = convert('/', namePath);
  let nodesData = R.zip(paths, names);
  let nodeChain = R.map((nodeData) => {
    return { 
      id: nodeData[0],
      name: nodeData[1]
    };
  }, nodesData); 

  let parent = null;

  for (let i = 0; i < nodeChain.length; i++) {
    let node = nodeChain[i];
    node.parent = parent;
    node.fullIdPath = calcFullIdPath(node); 
    node.fullNamePath = calcFullNamePath(node);
    parent = node;
  }

  return nodeChain; 
}

function calcFullIdPath (node) {
  if (R.isNil(node)) { return null; }
  if (R.isNil(node.parent)) { return '/' + node.id; }

  let parentFullPath = calcFullIdPath(node.parent);
  return parentFullPath + '/' + node.id; 
} 

function calcFullNamePath (node) {
  if (R.isNil(node)) { return null; }
  if (R.isNil(node.parent)) { return '/' + node.name; }

  let parentFullPath = calcFullNamePath(node.parent);
  return parentFullPath + '/' + node.name; 
}

export {
  SET_CURRENT_NODE,
  SET_CURRENT_NODE_FROM_TREE_CONTROL,
  setCurrentNode,
  setCurrentNodeFromTreeControl
};
