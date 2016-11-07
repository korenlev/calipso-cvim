//import * as R from 'ramda';

const ADD_SEARCH_INTERESTED_PARTY = 'ADD_SEARCH_INTERESTED_PARTY';
const REMOVE_SEARCH_INTERESTED_PARTY = 'REMOVE_SEARCH_INTERESTED_PARTY';
const SET_SEARCH_TERM = 'SET_SEARCH_TERM';

function addSearchInterestedParty(listener) {
  return {
    type: ADD_SEARCH_INTERESTED_PARTY,
    payload: {
      listener: listener
    }
  };
}

function removeSearchInterestedParty(listener) {
  return {
    type: REMOVE_SEARCH_INTERESTED_PARTY,
    payload: {
      listener: listener
    }
  };
}

function setSearchTerm(searchTerm) {
  return {
    type: SET_SEARCH_TERM,
    payload: {
      searchTerm: searchTerm
    }
  };
}

export {
  ADD_SEARCH_INTERESTED_PARTY,
  REMOVE_SEARCH_INTERESTED_PARTY,
  SET_SEARCH_TERM,
  addSearchInterestedParty,
  removeSearchInterestedParty,
  setSearchTerm,
};
