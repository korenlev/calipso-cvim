/*
 * Template Component: FlowGraph 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
// We import d3 v4 not into d3 because old code network visualization use globaly d3 v3.
import * as d3v4 from 'd3';
        
import './flow-graph.html';     
    
/*  
 * Lifecycles
 */   
  
Template.FlowGraph.onCreated(function() {
  let instance = this;
  
  instance.state = new ReactiveDict();
  instance.state.setDefault({
  });

  instance.autorun(() => {
    new SimpleSchema({
      env: { type: String },
      object_id: { type: String },
      flowType: { type: String },
      sourceMacAddress: { type: String, optional: true },
      destinationMacAddress: { type: String, optional: true },
      sourceIPv4Address: { type: String, optional: true },
      destinationIPv4Address: { type: String, optional: true },
    }).validate(Template.currentData());

  });

});  

Template.FlowGraph.rendered = function() {
  let instance = Template.instance();

  (function (d3) {
    let graphContainer = instance.$('.sm-graph');

    var n = 40,
      random = d3.randomNormal(0, .2),
      data = d3.range(n).map(random);
  //var svg = d3.select('svg'),
    var svg = d3.select(graphContainer[0]),
      margin = {top: 20, right: 20, bottom: 20, left: 40},
      width = +svg.attr('width') - margin.left - margin.right,
      height = +svg.attr('height') - margin.top - margin.bottom,
      g = svg.append('g').attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
    var x = d3.scaleLinear()
      .domain([0, n - 1])
      .range([0, width]);

    var y = d3.scaleLinear()
      .domain([-1, 1])
      .range([height, 0]);

    var line = d3.line()
      .x(function(d, i) { return x(i); })
      .y(function(d, _i) { return y(d); });

    g.append('defs').append('clipPath')
      .attr('id', 'clip')
    .append('rect')
      .attr('width', width)
      .attr('height', height);

    g.append('g')
      .attr('class', 'axis axis--x')
      .attr('transform', 'translate(0,' + y(0) + ')')
      .call(d3.axisBottom(x));

    g.append('g')
      .attr('class', 'axis axis--y')
      .call(d3.axisLeft(y));

    g.append('g')
      .attr('clip-path', 'url(#clip)')
    .append('path')
      .datum(data)
      .attr('class', 'line')
    .transition()
      .duration(500)
      .ease(d3.easeLinear)
      .on('start', tick);

    function tick() {
      // Push a new data point onto the back.
      data.push(random());

/*
      Meteor.call('vedge_flows!graph-frames', { 
        // todo: remove debug constants
        env: 'Devstack-VPP', 
        hostIp: '192.168.2.1'
      }, (_err, res) => {
        // todo: error
        debugger;
        let flowTypes = R.pipe(
          R.map(R.prop('flow_type')),
          R.map((name) => { return { name: name }; })
        )(res);
        instance.state.set('flowTypes', flowTypes);
      });
*/

      // Redraw the line.
      d3.select(this)
          .attr('d', line)
          .attr('transform', null);

      // Slide it to the left.
      d3.active(this)
          .attr('transform', 'translate(' + x(-1) + ',0)')
        .transition()
          .on('start', tick);

      // Pop the old data point off the front.
      data.shift();
    }
  })(d3v4);

};  

/*
 * Events
 */

Template.FlowGraph.events({
});
   
/*  
 * Helpers
 */

Template.FlowGraph.helpers({    
});


