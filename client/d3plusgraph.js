/*
 * Template Component: d3plusgraph
 */

(function () {

/*
 * Lifecycle methods
 */

Template.d3plusgraph.rendered = function () {
    var sample_data = [
        {"name": "alpha", "size": 10},
        {"name": "beta", "size": 12},
        {"name": "gamma", "size": 30},
        {"name": "delta", "size": 26},
        {"name": "epsilon", "size": 12},
        {"name": "zeta", "size": 26},
        {"name": "theta", "size": 11},
        {"name": "eta", "size": 24}
    ];
    var connections = [
        {"source": "alpha", "target": "beta"},
        {"source": "alpha", "target": "gamma"},
        {"source": "beta", "target": "delta"},
        {"source": "beta", "target": "epsilon"},
        {"source": "zeta", "target": "gamma"},
        {"source": "theta", "target": "gamma"},
        {"source": "eta", "target": "gamma"}
    ];
    var invNodes = Inventory.find({ "type": "instance", $and: [ { "host": 'node-25' } ] }).fetch();

    var edges = [];
    var nodes = [];

    invNodes.forEach(function(n){
        nodes =  n["Entities"];
        edges =  n["Relations"];
    });
    nodes.forEach(function(n){
        n.name = n.label;
    });
    var edges_new = [];
    edges.forEach(function(e) {
        var sourceNode = nodes.filter(function(n) { return n.id === e.from; })[0],
            targetNode = nodes.filter(function(n) { return n.id === e.to; })[0];

        edges_new.push({source: sourceNode, target: targetNode, value: 1,label: e.label});
    });

    var visualization = d3plus.viz()
        .container("#viz")
        .type("network")
        .data(nodes)
        .edges(edges_new)
        .size("level")
        .id("id")
        .draw();
};

})();  
