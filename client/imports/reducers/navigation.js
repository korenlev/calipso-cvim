import * as R from 'ramda';

import * as actions from '/client/imports/actions/navigation';

function navigation(state = [], action) {
  switch (action.type) {
  case actions.SET_CURRENT_NODE:
    console.log(action.payload.nodeChain);
    return action.payload.nodeChain; 

  case actions.SET_CURRENT_NODE_FROM_TREE_CONTROL:
    if (contains(action.payload.nodeChain, state)) {
      let equalLastIndex = findEqualLastIndex(action.payload.nodeChain, state);
      return R.slice(0, equalLastIndex, action.payload.nodeChain);  
    } else {
      return action.payload.nodeChain;
    }

  default:
    return state;
  }
}

function contains(subArray, array) {
  let equalLastIndex = findEqualLastIndex(subArray, array);

  if (subArray.length <= array.length &&
      equalLastIndex >= 0 &&
      subArray.length === equalLastIndex + 1) {

    return true;
  }

  return false;
}

function findEqualLastIndex (arrayA, arrayB) {
  let indexResult = -1;

  for (let i = 0; i < arrayA.length; i++) {
    if (R.equals(arrayA[i], arrayB[i])) {
      indexResult = i;
    } else {
      break;
    }
  }

  return indexResult;
}

export default navigation;
