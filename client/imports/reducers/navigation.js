import * as R from 'ramda';

import * as actions from '/client/imports/actions/navigation';

function navigation(state = { current: [], lastActionable: [] }, action) {
  switch (action.type) {
  case actions.SET_CURRENT_NODE:
    return R.assoc('current', action.payload.nodeChain, state); 

  case actions.SET_CURRENT_NODE_FROM_TREE_CONTROL:
    if (contains(action.payload.nodeChain, state)) {
      let equalLastIndex = findEqualLastIndex(action.payload.nodeChain, state.current);
      return R.assoc('current', 
        R.slice(0, equalLastIndex, action.payload.nodeChain),
        state);  
    } else {
      return R.assoc('current', action.payload.nodeChain, state);
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
