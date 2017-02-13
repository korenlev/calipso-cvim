/*
 * Template Component: FlowGraph 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
// We import d3 v4 not into d3 because old code network visualization use globaly d3 v3.
import * as d3v4 from 'd3';
import * as R from 'ramda';
import { Statistics } from '/imports/api/statistics/statistics';
import { createGraphQuerySchema } from '/imports/api/statistics/helpers';
import * as BSON from 'bson';
        
import './flow-graph.html';     
    
/*  
 * Lifecycles
 */   
  
Template.FlowGraph.onCreated(function() {
  let instance = this;
  
  instance.state = new ReactiveDict();
  instance.state.setDefault({
    environment: instance.data.environment,
    object_id: instance.data.object_id,
    type: instance.data.type,
    flowType: instance.data.flowType,
    sourceMacAddress: instance.data.sourceMacAddress,
    destinationMacAddress: instance.data.destinationMacAddress,
    sourceIPv4Address: instance.data.sourceIPv4Address,
    destinationIPv4Address: instance.data.destinationIPv4Address,
    simulateGraph: instance.data.simulateGraph,
    timeDeltaNano: 0
  });

  instance.autorun(() => {
    new SimpleSchema({
      env: { type: String },
      object_id: { type: String },
      type: { type: String },
      flowType: { type: String },
      sourceMacAddress: { type: String, optional: true },
      destinationMacAddress: { type: String, optional: true },
      sourceIPv4Address: { type: String, optional: true },
      destinationIPv4Address: { type: String, optional: true },
      simulateGraph: { type: Boolean, optional: true },
      timeDeltaNano: { type: Number, optional: true }
    }).validate(Template.currentData());

    let data = Template.currentData();

    instance.state.set('environment', data.env);
    instance.state.set('object_id', data.object_id);
    instance.state.set('type', data.type);
    instance.state.set('flowType', data.flowType);
    instance.state.set('sourceMacAddress', data.sourceMacAddress);
    instance.state.set('destinationMacAddress', data.destinationMacAddress);
    instance.state.set('sourceIPv4Address', data.sourceIPv4Address);
    instance.state.set('destinationIPv4Address', data.destinationIPv4Address);
    instance.state.set('simulateGraph', data.simulateGraph);
    instance.state.set('timeDeltaNano', data.timeDeltaNano);

    //let timeStart = Date.now() * 1000000;
    let timeStart = 1486661783217004480; 

    instance.subscribe('statistics!graph-frames', {
      env: data.env, 
      object_id: data.object_id, 
      type: data.type,
      flowType: data.flowType, 
      timeStart: timeStart,
      sourceMacAddress: data.sourceMacAddress,
      destinationMacAddress: data.destinationMacAddress,
      sourceIPv4Address: data.sourceIPv4Address,
      destinationIPv4Address: data.destinationIPv4Address
    });
  });

});  

Template.FlowGraph.onDestroyed(function () {
  (function (d3) {
    let instance = Template.instance();
    let graphContainer = instance.$('.sm-graph');
    var svg = d3.select(graphContainer[0]);

    svg.interrupt();
    var lineSvg = svg.select('g g path.line');
    lineSvg.interrupt();
  })(d3v4);
});

Template.FlowGraph.rendered = function() {
  let instance = Template.instance();

  instance.autorun(() => {

    let environment = instance.state.get('environment');
    let object_id = instance.state.get('object_id');
    let type = instance.state.get('type');
    let flowType = instance.state.get('flowType');
    let sourceMacAddress = instance.state.get('sourceMacAddress');
    let destinationMacAddress = instance.state.get('destinationMacAddress');
    let sourceIPv4Address = instance.state.get('sourceIPv4Address');
    let destinationIPv4Address = instance.state.get('destinationIPv4Address');
    let simulateGraph = instance.state.get('simulateGraph');
    let timeDeltaNano = instance.state.get('timeDeltaNano');

    (function (d3) {
      let graphContainer = instance.$('.sm-graph');

      var n = 40;
      var random = d3.randomNormal(0, 2000000);
      //var data = d3.range(n).map(random);
      var data = d3.range(n).map(R.always(0));
    //var svg = d3.select('svg'),
      var svg = d3.select(graphContainer[0]),
        margin = {top: 20, right: 20, bottom: 20, left: 80},
        width = +svg.attr('width') - margin.left - margin.right,
        height = +svg.attr('height') - margin.top - margin.bottom;
        
      svg.select('g').remove();
      var g = svg.append('g').attr(
          'transform', 'translate(' + margin.left + ',' + margin.top + ')');

      var x = d3.scaleLinear()
        .domain([0, n - 1])
        .range([0, width]);

      var y = d3.scaleLinear()
        .domain([0, 5000000])
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

      //let timeStart = Date.now() * 1000000;
      //let timeStart = (Date.now() * 1000000) - timeDeltaNano;
      //let timeStart = 1486661783217004480; 
      let timeStart = 1486661034810432900;//  1486661034810432945;
      let delta = (Date.now() * 1000000) - timeStart; 
      debugger;
      let timeEnd;
      let serverData = [];
      let dataPoint;
      let lastDataPoint = 0;

      function tick() {
        // Push a new data point onto the back.
        
        timeEnd = (Date.now() * 1000000) - delta;
        //timeStart = timeEnd - (500 * 1000000);

        let timeStartBson = BSON.Long(timeStart);
        let timeEndBson = BSON.Long(timeEnd);

        // debug
        // timeStartBson = BSON.Long(0);
        //timeEndBson = BSON.Long(2486661034810432900);

        let query = createGraphQuerySchema(
          environment, 
          object_id,
          type,
          flowType, 
          timeStartBson,
          timeEndBson,
          sourceMacAddress,
          destinationMacAddress,
          sourceIPv4Address,
          destinationIPv4Address);

        let statItem = Statistics.findOne(query);
        if (!R.isNil(statItem)) {
          dataPoint = statItem.averageThroughput;
        } else {
          dataPoint = lastDataPoint;
        }

        data.push(dataPoint);

        timeStart = timeEnd - (4 * 1000000000);
        /*
        Meteor.call('statistics!graph-frames', { 
          env: environment,
          object_id: object_id,
          type: type,
          flowType: flowType,
          timeStart: timeStart,
          timeEnd: timeEnd,
          sourceMacAddress: sourceMacAddress,
          destinationMacAddress: destinationMacAddress,
          sourceIPv4Address: sourceIPv4Address,
          destinationIPv4Address: destinationIPv4Address 
        }, (err, res) => {
          timeStart = timeEnd;

          if (simulateGraph) {
            serverData = R.append(random(), serverData);
          } else if (! R.isNil(err)) {
            console.log(err);
          } else if (res.length === 0) {
            //serverData = R.append(0, serverData);
          } else {
            serverData = R.append(res[0].averageThroughput, serverData);
          }

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

        lastDataPoint = dataPoint;
      }
    })(d3v4);

  });
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


