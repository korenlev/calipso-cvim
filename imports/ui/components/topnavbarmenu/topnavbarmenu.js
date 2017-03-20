/*
 * Template Component: topnavbarmenu 
 */
    
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
//import * as R from 'ramda';

import { store } from '/imports/ui/store/store';
//import { setSearchTerm } from '/imports/ui/actions/search-interested-parties';
import { setCurrentNode } from '/imports/ui/actions/navigation';
import { notifySearchAutoCompleteTermChanged } from '/imports/ui/actions/search-interested-parties';


import '/imports/ui/components/search-auto-complete-list/search-auto-complete-list';
import '/imports/ui/components/get-started/get-started';
import '/imports/ui/components/env-form/env-form';
import '/imports/ui/components/event-modals/event-modals';

import './topnavbarmenu.html';

/*  
 * Lifecycles
 */   

Template.topnavbarmenu.onCreated(function () {
  let instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    isAutoCompleteOpen: false
  });
});

Template.topnavbarmenu.events = {
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
    Router.go('dashboard');
  },

  'click .sm-get-started-link': function () {
    Router.go('getstarted');
  }
};

Template.topnavbarmenu.helpers({
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
  }
});

/*
function showNodeEffectInTree(searchValue) {
  //var selectedVal = $('#search').val();
  var node = d3Graph.svg.selectAll('.node');
  if (searchValue == 'none') {
    node.style('stroke', 'white').style('stroke-width', '1');
  } else {
    var selected = node.filter(function (d) {
      return d.object_name.indexOf(searchValue)<0;
      //return d.name != searchValue;
    });
    selected.style('opacity', '0');
    var link = d3Graph.svg.selectAll('.link');
    link.style('opacity', '0');
    d3.selectAll('.node, .link').transition()
        .duration(5000)
        .style('opacity', 1);
  }
}
*/
