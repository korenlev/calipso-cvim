/////////////////////////////////////////////////////////////////////////////////////////
// Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems) and others /
//                                                                                      /
// All rights reserved. This program and the accompanying materials                     /
// are made available under the terms of the Apache License, Version 2.0                /
// which accompanies this distribution, and is available at                             /
// http://www.apache.org/licenses/LICENSE-2.0                                           /
/////////////////////////////////////////////////////////////////////////////////////////
/*
 * Template Component: TopNavbarMenu 
 */

import * as R from 'ramda';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
//import * as R from 'ramda';

import { store } from '/imports/ui/store/store';
//import { setSearchTerm } from '/imports/ui/actions/search-interested-parties';
//import { notifySearchAutoCompleteTermChanged } from '/imports/ui/actions/search-interested-parties';
import { idToStr } from '/imports/lib/utilities';
import factory from 'reactive-redux';

import '/imports/ui/components/search-auto-complete-list/search-auto-complete-list';
import '/imports/ui/components/get-started/get-started';
import '/imports/ui/components/env-form/env-form';
import '/imports/ui/components/alarm-icons/alarm-icons';
import '/imports/ui/components/settings-list/settings-list';

import './top-navbar-menu.html';
import { getParentTemplateInstance } from "../../../lib/utilities";

/*  
 * Lifecycles
 */

Template.TopNavbarMenu.onCreated(function () {
  let instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    isAutoCompleteOpen: false,
    searchTerm: null,
    loginButtonsOpen: false,
  });

  const mainEnvIdSelector = (state) => (state.components.mainApp.selectedEnvironment._id);
  instance.rdxMainEnvId = factory(mainEnvIdSelector, store);

  instance.tempSearchTerm = null;
  instance.searchDebounced = _.debounce(function () {
    instance.state.set('searchTerm', instance.tempSearchTerm);
    instance.state.set('isAutoCompleteOpen', true);
  }, 250);
});

Template.TopNavbarMenu.events = {
  'keyup #search': function (event) {
    let instance = Template.instance();

    instance.tempSearchTerm = instance.$(event.target).val();
    instance.searchDebounced();
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

let parentInstance = null;
let loginButtonsSession = null;

Template.loginButtons.onCreated(function () {
  parentInstance = getParentTemplateInstance(Template.instance());
  loginButtonsSession = Accounts._loginButtonsSession;
});

Template.body.events({
  'click': function (ev, instance) {

    if (parentInstance == null || parentInstance.state == null)
      return;

    //if user clicked on the following elements
    if (R.contains(ev.target.id, ["login-name-link"]))
      return;

    let isOpen = parentInstance.state.get('loginButtonsOpen');
    if (isOpen === false) {
      if (ev.target.id === "login-main-container" || ev.target.id === "login-user-container") {
        openLoginMenu();
      }
    }
    else {
      closeLoginMenu();
    }
  }
});

Template.settingsList.events({
  'click': function (ev, instance) {

    if (parentInstance == null || parentInstance.state == null)
      return;

    let isOpen = parentInstance.state.get('loginButtonsOpen');
    if (isOpen === true) {
      closeLoginMenu();
    }
  }
});

Template.envForm.events({
  'click': function (ev, instance) {

    if (parentInstance == null || parentInstance.state == null)
      return;

    let isOpen = parentInstance.state.get('loginButtonsOpen');
    if (isOpen === true) {
      closeLoginMenu();
    }
  }
});

function openLoginMenu() {
  parentInstance.state.set('loginButtonsOpen', true);
  loginButtonsSession.set('dropdownVisible', true);
}

function closeLoginMenu() {
  loginButtonsSession.closeDropdown();
  parentInstance.state.set('loginButtonsOpen', false);
}

Template.loginButtons.events({
  'click #login-name-link, click #login-sign-in-link': function () {

    let isOpen = parentInstance.state.get('loginButtonsOpen');

    if (isOpen === false) {
      openLoginMenu();
    }
    else {
      closeLoginMenu();
    }
  },
});

Template.TopNavbarMenu.helpers({
  envId: function () {
    let instance = Template.instance();
    return instance.rdxMainEnvId.get();
  },

  searchTerm: function () {
    let instance = Template.instance();
    return instance.state.get('searchTerm');
  },

  argsSearch: function (envId, searchTerm) {
    let instance = Template.instance();

    return {
      isOpen: instance.state.get('isAutoCompleteOpen'),
      envId: envId,
      searchTerm: searchTerm,
      onResultSelected(node) {
        instance.state.set('isAutoCompleteOpen', false);

        let searchInput = instance.$('input#search');
        searchInput.val(node.name_path);

        Router.go('environment', { _id: idToStr(node._envId) }, {
          query: { selectedNodeId: idToStr(node._id) }
        });
      },
      onCloseReq() {
        instance.state.set('isAutoCompleteOpen', false);

        let searchInput = instance.$('input#search');
        searchInput.val(null);
      },
    };
  },

  argsEnvForm: function () {
    let instance = Template.instance();
    let selectedEnvironment = instance.state.get('selectedEnvironment');

    return {
      selectedEnvironment: selectedEnvironment,
      onEnvSelected: function (env) {
        Router.go('environment', { _id: idToStr(env._id) }, { query: `r=${Date.now()}` });
      }
    };
  }

}); // end: helpers
