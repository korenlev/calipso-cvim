/*
 * Template Component: NetworkGraph 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
import * as cola from 'webcola';
import { imagesForNodeType, defaultNodeTypeImage } from '/imports/lib/images-for-node-type';
        
import './network-graph.html';     
    
/*  
 * Lifecycles
 */   
  
Template.NetworkGraph.onCreated(function() {
  let instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault({
    graphDataChanged: null,
  });
  instance.simpleState = {
    graphData: null
  };

  instance.autorun(function () {
    let data = Template.currentData();

    new SimpleSchema({
      graphData: { type: Object, blackbox: true },
      onNodeOver: { type: Function, optional: true },
      onNodeOut: { type: Function, optional: true },
      onNodeClick: { type: Function, optional: true },
      onDragStart: { type: Function, optional: true },
      onDragEnd: { type: Function, optional: true },
    }).validate(data);

    instance.simpleState.graphData = data.graphData;
    instance.state.set('graphDataChanged', Date.now());
    instance.onNodeOver = R.defaultTo(() => {}, data.onNodeOver);
    instance.onNodeOut = R.defaultTo(() => {}, data.onNodeOut);
    instance.onNodeClick = R.defaultTo(() => {}, data.onNodeClick);
    instance.onDragStart = R.defaultTo(() => {}, data.onDragStart);
    instance.onDragEnd = R.defaultTo(() => {}, data.onDragEnd);
  });
});  

Template.NetworkGraph.rendered = function() {
  let instance = Template.instance();

  instance.autorun(function () {
    //let _graphDataChanged = 
    instance.state.get('graphDataChanged');
    let graphEl = instance.$('.sm-graph')[0];

    renderGraph(graphEl, 
      graphEl.clientWidth, 
      graphEl.clientHeight,
      instance.simpleState.graphData,
      genConfig(),
      instance.onNodeOver,
      instance.onNodeOut, 
      instance.onNodeClick,
      instance.onDragStart,
      instance.onDragEnd
    );
  });
};  

/*
 * Events
 */

Template.NetworkGraph.events({
});
   
/*  
 * Helpers
 */

Template.NetworkGraph.helpers({    
}); // end: helpers


function genConfig() {
  let outline = false;
  let tocolor = 'fill';
  let towhite = 'stroke';
  if (outline) {
    tocolor = 'stroke';
    towhite = 'fill';
  }

  return {
    tocolor: tocolor,
    towhite: towhite,
    text_center: false,
    outline: outline,
    min_score: 0,
    max_score: 1,
    highlight_color: 'blue',
    highlight_trans: 0.1,
    default_node_color: '#ccc',
    //var default_node_color: 'rgb(3,190,100)',
    default_link_color: '#888',
    nominal_base_node_size: 8,
    nominal_text_size: 10,
    max_text_size: 24,
    nominal_stroke: 1.5,
    max_stroke: 4.5,
    max_base_node_size: 36,
    min_zoom: 0.3,
    max_zoom: 5,
  };
}

function renderGraph(
  mainElement, 
  w, 
  h, 
  graph, 
  config, 
  onNodeOver, 
  onNodeOut, 
  onNodeClick,
  onDragStart,
  onDragEnd
) {

  let force = genForceCola(cola, d3, w, h);
  let drag = force.drag()
    .on('start', function (_d) {
      onDragStart();
    })
    .on('end', function (_d) {
      onDragEnd();
    })
  ;

  let svg = d3.select(mainElement).select('svg');
  svg.remove();
  svg = genSvg(d3, mainElement);

  /*
  let background = svg.append('rect')
    .attr('class', 'background')
    .attr('width', '100%')
    .attr('height', '100%');
  */
  let zoom = genZoomBehavior(d3, config);

  let g = svg.append('g');
  
  activateForce(force, graph.nodes, graph.links, graph.groups);

  let groups = genSvgGroups(g, graph.groups, drag);
  let {svgLinkLines, svgLinkLabels} = genSvgLinks(
    g, graph.links, config.nominal_stroke, config.default_link_color);
  let [nodes] = genSvgNodes(g, graph.nodes, drag, onNodeOver, onNodeOut, onNodeClick); 

  zoom.on('zoom', function () {
    //g.attr('transform', 'translate(' + d3.event.translate + ')scale(' + d3.event.scale + ')');
    g.attr('transform', d3.event.transform);
  });

  svg.call(zoom);
  //background.call(zoom);

  //force.on('tick', forceTick.bind(null, nodes, links, groups));
  force.on('tick', tickFn);
  
  function tickFn() {
    nodes.attr('transform', function(d) {
      return 'translate(' + d.x + ',' + d.y + ')';
    });

    nodes.attr('cx', function(d) { return d.x; })
    .attr('cy', function(d) { return d.y; });

    /*
    nodes.attr('x', function (d) {
      return d.x;
      //return d.x - d.width / 2 + 3; 
    })
    .attr('y', function (d) {
      return d.y;
      //return d.y - d.height / 2 + 3;
    });
    */

    svgLinkLines
      .attr('x1', function(d) { return d.source.x; })
      .attr('y1', function(d) { return d.source.y; })
      .attr('x2', function(d) { return d.target.x; })
      .attr('y2', function(d) { return d.target.y; });

    svgLinkLabels
      .attr('x', function(d) { 
        return (d.source.x + (d.target.x - d.source.x) * 0.5); 
      })
      .attr('y', function(d) { 
        return (d.source.y + (d.target.y - d.source.y) * 0.5); 
      });

    groups
      .attr('x', function (d) { 
        return R.path(['bounds', 'x'], d); 
      })
      .attr('y', function (d) { 
        return R.path(['bounds', 'y'], d);
      })
      .attr('width', function (d) { 
        if (d.bounds) { return d.bounds.width(); } 
      })
      .attr('height', function (d) { 
        if (d.bounds) { return d.bounds.height(); } 
      });
  }
}

 // d3.select(window).on('resize', resize);

/*
function isNumber(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}	
*/

function genSvg(d3, mainElement) {
  let svg = d3.select(mainElement).append('svg');

  svg.style('cursor', 'move')
    .attr('width', '100%')
    .attr('height', '100%')
    .attr('pointer-events', 'all');

  return svg;
}

function genSvgLinks(g, links, nominal_stroke, default_link_color) {
  let svgLinks = g.selectAll('.link')
    .data(links)
    .enter()
    .append('g')
    .attr('class', 'link-group');


  let svgLinkLines = svgLinks
    .append('line')
    .attr('class', 'link')
    .style('stroke-width', nominal_stroke)
    .style('stroke', 
    function(_d) { 
      return default_link_color;
    });

  let svgLinkLabels = svgLinks
    .append('text')
    .text(function(d) { 
      return d.label; 
    })
    .attr('x', function(d) { return (d.source.x + (d.target.x - d.source.x) * 0.5); })
    .attr('y', function(d) { return (d.source.y + (d.target.y - d.source.y) * 0.5); })
    .attr('dy', '.25em')
    .attr('text-anchor', 'right');

  return {svgLinks, svgLinkLines, svgLinkLabels};
}

function genSvgNodes(g, nodes, drag, onNodeOver, onNodeOut, onNodeClick) {
  let svgNodes = g.selectAll('.node')
    .data(nodes)
    .enter()
    .append('g')
      .attr('class', 'node')
      .call(drag)

  ;
  
  let imageLength = 36;
  let images = svgNodes.append('image')
    .attr('xlink:href', function(d) {
      return `/${calcImageForNodeType(d._osmeta.type)}`;
    })
    .attr('x', -(Math.floor(imageLength / 2)))
    .attr('y', -(Math.floor(imageLength / 2)))
    .attr('width', imageLength)
    .attr('height', imageLength)
    .on('mouseover', function (d) {
      onNodeOver(d._osmeta.nodeId, d3.event.pageX, d3.event.pageY);
    })
    .on('mouseout', function (d) {
      onNodeOut(d._osmeta.nodeId);
    })
    .on('click', function (d) {
      onNodeClick(d._osmeta.nodeId);
    })
  ;

  return [svgNodes, images];
  //return [svgNodes];
}

function calcImageForNodeType(nodeType) {
  return R.defaultTo(defaultNodeTypeImage, R.prop(nodeType, imagesForNodeType));
}

function genZoomBehavior(d3, config) {
  let zoom = d3.zoom().scaleExtent([config.min_zoom, config.max_zoom]);

  return zoom;
}

/*
function genForceD3(d3, w, h) {
  let force = d3.layout.force()
    .linkDistance(60)
    .charge(-300)
    .size([w,h]);

  return force;
}
*/

function genForceCola(cola, d3, w, h) {
  let force = cola.d3adaptor(d3)
    .convergenceThreshold(0.1)
  //  .convergenceThreshold(1e-9)
    .linkDistance(100)
    .size([w,h]);

  return force;
}

function activateForce(force, nodes, links, groups) {
  force
    .nodes(nodes)
    .links(links) 
    .groups(groups)
    //.symmetricDiffLinkLengths(25)
    .handleDisconnected(true)
    .avoidOverlaps(true)
    .start(50, 100, 200);
    //.start();
}

/*
function resize() {
  let width = mainElement.clientWidth;
  let height = mainElement.clientHeight;

  svg.attr('width', '100%') //width)
    .attr('height', '100%'); //height);

  force.size([
    force.size()[0] + (width - w) / zoom.scale(), 
    force.size()[1] + (height - h) / zoom.scale()
  ]).resume();

  w = width;
  h = height;
}
*/

function genSvgGroups(g, groups, drag) {
  return g.selectAll('.group')
      .data(groups)
    .enter().append('rect')
      .attr('rx', 8)
      .attr('ry', 8)
      .attr('class', 'group')
      .style('fill', function (_d, _i) { return 'lightblue'; })
      .call(drag);
}
