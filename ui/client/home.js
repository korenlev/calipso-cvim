/*
Template.home.rendered = function () {
    console.log("Home Render");
    //Router.current().render().data();
};
Template.topnavbarmenu.helpers({
});
Template.topnavbarmenu.rendered = function(){
    
};
Template.topnavbarmenu.events = {
/!*
    "autocompleteselect input": function(event, template, doc) {
        console.log("selected ", doc);
    },
*!/
/!*
    'keyup input#search': function () {
        
        /!*AutoCompletion.autocomplete({
            element: 'input#search',       // DOM identifier for the element
            collection: Inventory,// MeteorJS collection object
            field: 'Entities',                    // Document field name to search for
            limit: 10,                         // Max number of elements to show
            sort: { id: 1 },              // Sort object to filter results with
            filter: { "host": "node-25","type": "instance" }});
        //filter: { 'gender': 'female' }}); // Additional filtering*!/
    },
*!/
    "keypress #search": function  (event,template) {
        if (event.which === 13) {
            var instance = Template.instance(),
                findFromParent =  instance.$(event.target).val();
            console.log("temp val is " + findFromParent);

            //var selectedVal = $('#search').val();
            var node = svg.selectAll(".node");
            if (findFromParent == "none") {
                node.style("stroke", "white").style("stroke-width", "1");
            } else {
                var selected = node.filter(function (d, i) {
                    return d.label.indexOf(findFromParent)<0;
                    //return d.name != findFromParent;
                });
                selected.style("opacity", "0");
                var link = svg.selectAll(".link")
                link.style("opacity", "0");
                d3.selectAll(".node, .link").transition()
                    .duration(5000)
                    .style("opacity", 1);


            }

        }

        //return Inventory.find({ "type": "instance", $and: [ { "host": Session.get('currNodeId')} ] }).fetch().map(function(it){ return it.name; });
    },
};

Template.d3graph.rendered = function () {
    d3Graph.creategraphdata();
    //var graphData = getGraphData("node-25");
    //updateNetworkGraph(graphData);
    var initgraph = true;
    Tracker.autorun(function () {
        var nodeId = Session.get('currNodeId');
        var nodesXY = [];
        if(nodeId){
            d3Graph.getGraphData(nodeId);
/!*
            d3Graph.force.nodes().forEach(function(e){
                nodesXY.push({id:e.id,x:e.x,y:e.y});
                //graphData.nodes[e] = e.x;
                //graphData.nodes[] = e.y;
            });
            var i=0;
            graphData.nodes.forEach(function(e){
                if(e.id==nodesXY[i].id){
                    e.x = nodesXY[i].x;
                    e.y = nodesXY[i].y;
                }
                i++;
            });
            var j=0;
            graphData.links.forEach(function(e){
                if(e.source.id==nodesXY[j].id){
                    e.source.x = nodesXY[j].x;
                    e.source.y = nodesXY[j].y;
                }
                else if(e.target.id==nodesXY[j].id){
                    e.target.x = nodesXY[j].x;
                    e.target.y = nodesXY[j].y;
                }
                j++;
            });
            console.log(graphData.nodes);
*!/
            //d3Graph.updateNetworkGraph(graphData);
            if(!initgraph){
                //d3Graph.start();
                d3Graph.updateNetworkGraph();
            }


        }
        initgraph = false;
    });

};
Template.multilevelorig.events = {
     "click a": function(event,template){
     //console.log(event.target.innerText);
        $( '#menu' ).multilevelpushmenu( 'expand' , event.target.innerText );
     },
};


Template.multilevelorig.rendered = function(){
    console.log("multilevelorig Render");

    //Router.current().render().data();
    //Session.set("currEnv","WebEX-Mirantis@Cisco");
    menuTree.init();

    //Session.set("currEnv","WebEX-Mirantis@Cisco");

    /!*$('#menu').multilevelpushmenu('option', 'menuHeight', $(document).height());
    $('#menu').multilevelpushmenu('redraw');
    $(window).resize(function () {
        $('#menu').multilevelpushmenu('option', 'menuHeight', $(document).height());
        $('#menu').multilevelpushmenu('redraw');
    });
*!/
    /!*
        Meteor.setTimeout( function(){
        },1000);
    *!/

    $(document).ready(function(){
        // HTML markup implementation, overlap mode
/!*
        var nodesList = getGraphData("node-25").nodes;
        var nodesNames = [];
        nodesList.forEach(function(n){
            nodesNames.push(n.label);
        });
        nodesNames = nodesNames.sort();
        console.log(nodesNames);
        $('#search').autocomplete({
            minLength: 0,
            source: nodesNames
        });
*!/

    });

};

Template.multilevelorig.helpers({
    treeItems: function(){
        //console.log(Inventory.find({parent_id: "WebEX-Mirantis@Cisco"}));
        //return Inventory.find({parent_id: "WebEX-Mirantis@Cisco"});
/!*
        var currEnv = Router.current().route.getName();
        console.log("*****"+currEnv+"*****");
*!/
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Inventory.find({environment: envName,parent_id: envName});
    },
    getNodeItems: function(nodeId){
        //console.log(nodeId);
        //console.log(Inventory.find({parent_id: nodeId}));
        return Inventory.find({parent_id: nodeId});
    },
});

Template.multilevelorigNodeTemplate.helpers({
    hasClique: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        if(Inventory.find({parent_id: this.id, parent_type:this.type,environment: envName,clique:true,show_in_tree:true}).count() > 0){
            console.log("clique=True");
            return "true";
        }
        else{
            return "false";
        }

    },
    hasChildren: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Inventory.find({parent_id: this.id, parent_type:this.type,environment: envName,show_in_tree:true}).count() > 0;
    },
    children: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Inventory.find({parent_id: this.id ,parent_type:this.type,environment: envName,show_in_tree:true});
    }
});

*/
