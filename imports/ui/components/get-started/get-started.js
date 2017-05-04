/*
 * Template Component: getStarted
 */

import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';

//import { setCurrentNode } from '/imports/ui/actions/navigation';
import { store } from '/imports/ui/store/store';
import { setMainAppSelectedEnvironment } from '/imports/ui/actions/main-app.actions';

import '/imports/ui/components/accordion-wiki-menu/accordion-wiki-menu';

import './get-started.html';

Template.getstarted.onCreated(function () {
  store.dispatch(setMainAppSelectedEnvironment(null));
});

Template.getstarted.onDestroyed(function () {
});

Template.getstarted.helpers({
});
