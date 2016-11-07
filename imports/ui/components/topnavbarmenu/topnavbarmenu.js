/*
 * Template Component: topnavbarmenu 
 */
    
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
//import * as R from 'ramda';

import { store } from '/imports/ui/store/store';
import { setSearchTerm } from '/imports/ui/actions/search-interested-parties';

import './topnavbarmenu.html';

/*  
 * Lifecycles
 */   

Template.topnavbarmenu.onCreated(function () {
});

Template.topnavbarmenu.events = {
  'keypress #search': function  (event) {
    if (event.which === 13) {
      var instance = Template.instance(),
        searchTerm =  instance.$(event.target).val();
      console.log('temp val is ' + searchTerm);

      store.dispatch(setSearchTerm(searchTerm));
      showNodeEffectInTree(searchTerm);
    }
  },
};

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
