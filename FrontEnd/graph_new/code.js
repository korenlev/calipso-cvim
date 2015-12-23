'use strict';

window.Graph = window.Graph || {};

window.Graph.GraphManager = new function () {
	var self = this;

	var selectors = {
		graphContainerSelector: "#sp-graph-container",
		btnExportImageSelector: "#btnExportImage"
	};

	var $cache = {};

	var dsNodes = {};
	var dsEdges = {};



	var options = {};

	// vis.js network object
	var network = null;
	
	this.init = function (settings) {

		$.extend(true, options, settings);

		$cache.graphContainer = $(selectors.graphContainerSelector);
		$cache.btnExportImage = $(selectors.btnExportImageSelector);

		$cache.btnExportImage.click(saveCanvasAsImage);

	};

	this.getGraphData = function () {
	
		// get data remotely (synchronous)
		// commented since local data is used
		// var params = /* get params */
		// var result = $.ajax({
			// type: "GET",
			// url: options.graphDataUrl,
			// data: params,
			// async: false,
			// cache: false
		// }).responseText;

		var result = Graph.DataManager.getData(false);
		
		// no need since test data already parsed 
		//var buf = JSON.parse(result);
		
		var data = mapData(result);

		dsNodes = new vis.DataSet(data.nodes);

		dsEdges = new vis.DataSet(data.edges);


		var nData = {
			nodes: dsNodes,
			edges: dsEdges
		};
		
		return nData;
	};

	// draw image
	this.drawGraph = function(data) {

		// if no network - init it and draw, 
		// otherwise update network data
		if (network == null) {
			initNetwork(data);
			network.physics.options.enabled = false;
		} else {
			network.physics.options.enabled = true;
			network.setData({ nodes: data.nodes, edges: data.edges });
			network.physics.options.enabled = false;
		}
	};

	function initNetwork(data) {

		network = new vis.Network($cache.graphContainer[0],	data, options.graphSettings);

		network.on("click", function (params) {
			console.log(JSON.stringify(params, undefined, 3)); // show the data in the div
/*
			if (params.nodes.length > 0) {
				alert("node id: " + params.nodes[0]);
			}
*/

			//console.log(JSON.stringify(json)); // show the data in the div
			if (params.nodes.length > 0) {
				//var data = findPurpose(params.nodes[0]);
				//console.log(JSON.stringify(data, undefined, 3));
				//alert(JSON.stringify(data, undefined, 3));
				var res = dsNodes.get(params.nodes[0]); // get the data from selected node
				var nodeContent = document.getElementById('nodeContent');
				nodeContent.innerHTML = JSON.stringify(res, undefined, 3); // show the data in the div
				//console.log(JSON.stringify(res, undefined, 3)); // show the data in the div
			}

			else if (params.edges.length > 0) {
				//var data = findPurpose(params.nodes[0]);
				//console.log(JSON.stringify(data, undefined, 3));
				//alert(JSON.stringify(data, undefined, 3));
				var res = dsEdges.get(params.edges[0]); // get the data from selected node
				var nodeContent = document.getElementById('nodeContent');
				nodeContent.innerHTML = JSON.stringify(res, undefined, 3); // show the data in the div
				//console.log(JSON.stringify(res, undefined, 3)); // show the data in the div
			}



		});
		network.on("hoverNode", function (params) {
			console.log('hoverNode Event:', params);
		});
		network.on("showPopup", function (params) {
			document.getElementById('nodeContent').innerHTML = '<h2>showPopup event: </h2>' + JSON.stringify(params, null, 4);
		});

	};
	
	// save graph as image
	function saveCanvasAsImage() {
		if (network == null) {
			return;
		}
		var dataUrl = network.canvas.frame.canvas.toDataURL();
		var imageName = "image.png";
		$cache.btnExportImage.attr('download', imageName);
		$cache.btnExportImage.attr('href', dataUrl);
	}

	// create proper edges and nodes out of received data
	function mapData(jsonData) {

		// map nodes
		for (var n in jsonData.Entities) {
			var node = jsonData.Entities[n];
			if (node.archived) {
				delete n.archived;
				node.group = "Archived";
			}
			node.title = JSON.stringify(node.attributes, null, 4);
			//node.title = "test";
		}

		 // map edges
		var edgeWidth = 1;
		var labelfont = {size:12, face:'arial'};

		for (var e in jsonData.Relations) {
			var edge = jsonData.Relations[e];
			edge.font = labelfont;
			if (!edge.approved) {
				delete edge.approved;
				edge.color = options.graphSettings.groups.RequireApprove.color.background;
			}
			else if (edge.archived) {
				delete edge.archived;
				edge.color = options.graphSettings.groups.Archived.color.background;
			}
			//edge.title = "test";
			edge.width = edge.rootLevel ? edgeWidth * 2 : edgeWidth;
		}

		var result = {
			nodes: jsonData.Entities,
			edges: jsonData.Relations
		};

		return result;
	}
};