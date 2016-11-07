import * as R from 'ramda';

import * as actions from '/imports/ui/actions/search-interested-parties';

const defaultState = { listeners: [], searchTerm: null };

function reducer(state = defaultState, action) {
  let newListeners;

  switch (action.type) {
  case actions.ADD_SEARCH_INTERESTED_PARTY: 
    newListeners = R.unionWith(
        R.eqBy(R.prop('action')),
        state.listeners, 
        [{ action: action.payload.listener }]);
    return R.assoc('listeners', newListeners, state);

  case actions.REMOVE_SEARCH_INTERESTED_PARTY: 
    newListeners = R.differenceWith(
      R.eqBy(R.prop('action')),
      state.listeners, 
      [{ action:action.payload.listener }]);
    return R.assoc('listeners', newListeners, state);

  case actions.SET_SEARCH_TERM:
    asyncCall(() => { 
      notifyListeners(action.payload.searchTerm, state.listeners); 
    });  
    return R.assoc('searchTerm', action.payload.searchTerm, state);

  default:
    return state;
  }
}

function asyncCall(fnObject) {
  setTimeout(() => {
    fnObject.call(null);
  }, 0);
}

function notifyListeners(searchTerm, listeners) {
  R.forEach((listenerItem) => {
    listenerItem.action.call(null, searchTerm);
  }, listeners);
}

export const searchInterestedParties = reducer;
