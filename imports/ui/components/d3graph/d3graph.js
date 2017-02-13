/*
 * Template Component: d3graph 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
        
import { d3Graph } from '/imports/lib/d3-graph';

import './d3graph.html';     
    
/*  
 * Lifecycles
 */   
  
Template.d3graph.onCreated(function() {
  let instance = this;

  instance.autorun(function () {
    instance.subscribe('attributes_for_hover_on_data');
  });
});  

Template.d3graph.rendered = function () {
  d3Graph.creategraphdata();
  //var graphData = getGraphData("node-25");
  //updateNetworkGraph(graphData);
  var initgraph = true;
  Tracker.autorun(function () {
    var nodeId = Session.get('currNodeId');
    if(nodeId){
      var graphData = d3Graph.getGraphDataByClique(nodeId);
      if(!initgraph){
        //d3Graph.start();
        d3Graph.updateNetworkGraph(graphData);
      }
    }
    initgraph = false;
  });
};

/*
 * Events
 */

Template.d3graph.events({
});
   
/*  
 * Helpers
 */

Template.d3graph.helpers({    
});


