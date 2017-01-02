/*
 * Template Component: SearchAutoCompleteList 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import * as R from 'ramda';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
        
import { store } from '/imports/ui/store/store';

import '../auto-search-result-line/auto-search-result-line';

import './search-auto-complete-list.html';     
    
/*  
 * Lifecycles
 */   
  
Template.SearchAutoCompleteList.onCreated(function() {
  let instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    results: [],
    invocationCounter: 0,
    lastSearchTerm: null
  });

  instance.storeUnsubscribe = store.subscribe(() => {
    let state = store.getState();
    let searchTerm = state.api.searchInterestedParties.searchAutoCompleteTerm;
    if (searchTerm !== instance.state.get('lastSearchTerm')) {
      if (R.isNil(searchTerm) || R.isEmpty(searchTerm)) {
        instance.state.set('results', []); 
        instance.state.set('lastSearchTerm', searchTerm);
        incInvocationCounter(instance.state);
      } else {
        // do query and set result in the state
        performSearch(searchTerm, 
          state.components.environmentPanel.envName, instance.state);
      }
    }
  });
});  

/*
Template.SearchAutoCompleteList.rendered = function() {
};  
*/

Template.SearchAutoCompleteList.onDestroyed(() => {
  let instance = this;
  instance.storeUnsubscribe();
});

/*
 * Events
 */

Template.SearchAutoCompleteList.events({
});
   
/*  
 * Helpers
 */

Template.SearchAutoCompleteList.helpers({    
  searchResults: function () {
    let instance = Template.instance();
    return instance.state.get('results');
  },

  createAutoSearchResultLineArgs: function (resultItem) {
    let instance = Template.instance();
    return {
      namePath: resultItem.name_path,
      onClick() {
        instance.data.onResultSelected(resultItem); 
      }
    };
  }
});

function performSearch(searchTerm, envName, state) {
  let results = [];
  incInvocationCounter(state);
  let invocationId = state.get('invocationCounter');
  Meteor.apply('inventorySearch', [ searchTerm, envName ], { wait: false }, function (err, res) {
    if (invocationId < state.get('invocationCounter')) {
      return;
    }

    if (err) {
      console.error(err);
      return;
    }

    state.set('lastSearchTerm', searchTerm);
   
    R.forEach((resultItem) => {
      results = R.append(resultItem, results);
    }, res);

    state.set('results', results);
  });
}

function incInvocationCounter(state) {
  let invocationCounter = state.get('invocationCounter');
  state.set('invocationCounter',  invocationCounter + 1);
}

