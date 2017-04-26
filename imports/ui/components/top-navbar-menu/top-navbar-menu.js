/*
 * Template Component: TopNavbarMenu 
 */
    
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
//import * as R from 'ramda';

import { store } from '/imports/ui/store/store';
//import { setSearchTerm } from '/imports/ui/actions/search-interested-parties';
import { setCurrentNode } from '/imports/ui/actions/navigation';
import { notifySearchAutoCompleteTermChanged } from '/imports/ui/actions/search-interested-parties';
import { idToStr } from '/imports/lib/utilities';

import '/imports/ui/components/search-auto-complete-list/search-auto-complete-list';
import '/imports/ui/components/get-started/get-started';
import '/imports/ui/components/env-form/env-form';
import '/imports/ui/components/event-modals/event-modals';
import '/imports/ui/components/alarm-icons/alarm-icons';

import './top-navbar-menu.html';

/*  
 * Lifecycles
 */   

Template.TopNavbarMenu.onCreated(function () {
  let instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    isAutoCompleteOpen: false,
    selectedEnvironment: null
  });

  instance.storeUnsubscribe = store.subscribe(() => {
    let state = store.getState();

    let selectedEnvironment = state.components.mainApp.selectedEnvironment;
    instance.state.set('selectedEnvironment', selectedEnvironment);
  });
});

Template.TopNavbarMenu.onDestroyed(function () {
  let instance = this;
  instance.storeUnsubscribe();
});

Template.TopNavbarMenu.events = {
  /*
  'keypress #search': function  (event) {
    if (event.which === 13) {
      var instance = Template.instance(),
        searchTerm =  instance.$(event.target).val();
      console.log('temp val is ' + searchTerm);

      store.dispatch(setSearchTerm(searchTerm));
      showNodeEffectInTree(searchTerm);
    }
  },
  */

  'keyup #search': function  (event) {
    let instance = Template.instance();
    let searchTerm =  instance.$(event.target).val();
    store.dispatch(notifySearchAutoCompleteTermChanged(searchTerm));
    instance.state.set('isAutoCompleteOpen', true);
  },

  'click .os-nav-link': function () {
    let instance = Template.instance();
    instance.state.set('isAutoCompleteOpen', false);
  },

  'click .sm-dashboard-link': function () {
    Router.go('Dashboard');
  },

  'click .sm-get-started-link': function () {
    Router.go('getstarted');
  }
};

Template.TopNavbarMenu.helpers({
  createSearchAutoCompleteListArgs: function () {
    let instance = Template.instance();

    return {
      isOpen: instance.state.get('isAutoCompleteOpen'),
      onResultSelected(node) {
        instance.state.set('isAutoCompleteOpen', false);

        let searchInput = instance.$('input#search');  
        searchInput.val(node.name_path);

        let envName = store.getState().components.environmentPanel.envName;
        Router.go(`/enviroment?env=${envName}`);

        // environment screen is opening with default selected node.
        // after that we need to set the current node.
        // todo: make env screen be aware of other state in redux (not only router) ?
        setTimeout(function () {
          store.dispatch(setCurrentNode(node));
        }, 0);
      }
    };
  },

  argsEnvForm: function () {
    let instance = Template.instance();
    let selectedEnvironment = instance.state.get('selectedEnvironment');

    return {
      selectedEnvironment: selectedEnvironment,
      onEnvSelected: function (env) {
        Router.go('environment', { _id: idToStr(env._id) }, { });
      }
    };
  }

}); // end: helpers
