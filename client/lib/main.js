d3Graph = {
    color:'',
    zoomer:function(){
        var width = "100%",
            height = "100%";
        var xScale = d3.scale.linear()
            .domain([0,width]).range([0,width]);
        var yScale = d3.scale.linear()
            .domain([0,height]).range([0, height]);
        return d3.behavior.zoom().
        scaleExtent([0.1,10]).
        x(xScale).
        y(yScale).
        on("zoomstart", d3Graph.zoomstart).
        on("zoom", d3Graph.redraw);
    },
    svg:'',
    force:'',
    link:'',
    node:'',
    linkText:'',
    graph:{
        nodes:[],
        links:[],
    },
    zoomstart:function () {
        var node = d3Graph.svg.selectAll(".node");
        node.each(function(d) {
            d.selected = false;
            d.previouslySelected = false;
        });
        node.classed("selected", false);
    },
    getGraphData:function(nodeId){

        var invNodes = Inventory.find({ "type": "instance", $and: [ { "host": nodeId } ] });

        var edges = [];
        var nodes = [];

        invNodes.forEach(function(n){
            nodes =  n["Entities"];
            edges =  n["Relations"];
        });

        nodes.forEach(function(n){
            n.name = n.object_name;
        });

        var edges_new = [];
        edges.forEach(function(e) {
            var sourceNode = nodes.filter(function(n) { return n.id === e.from; })[0],
                targetNode = nodes.filter(function(n) { return n.id === e.to; })[0];

            edges_new.push({source: sourceNode, target: targetNode, value: 1,label: e.label,attributes: e.attributes});
        });
//any links with duplicate source and target get an incremented 'linknum'
        for (var i=0; i<edges_new.length; i++) {
            if (i != 0 &&
                edges_new[i].source == edges_new[i-1].source &&
                edges_new[i].target == edges_new[i-1].target) {
                edges_new[i].linknum = edges_new[i-1].linknum + 1;
            }
            else {edges_new[i].linknum = 1;};
        };
        //var graph = {};
        this.graph.nodes = nodes;
        this.graph.links = edges_new;

    },
    getGraphDataByClique:function(nodeObjId){
        var cliques = Cliques.find({ focal_point: new Mongo.ObjectID(nodeObjId) }).fetch();
        var cliquesLinks = [];
        var nodes = [];
        var edges_new = [];
        //debugger;
        cliques[0].links.forEach(function(n){
            cliquesLinks.push(n);
        });
        var linksList = Links.find({ _id: {$in: cliquesLinks}}).fetch();
        //console.log(linksList);

        linksList.forEach(function(linkItem){
            nodes.push(linkItem["source"]);
            nodes.push(linkItem["target"]);
        });
        var nodesList = Inventory.find({ _id: {$in: nodes}}).fetch();
        linksList.forEach(function(linkItem){
            var sourceNode = nodesList.filter(function(n) { return n._id._str === linkItem.source._str; })[0],
                targetNode = nodesList.filter(function(n) { return n._id._str === linkItem.target._str; })[0];

            edges_new.push({source: sourceNode, target: targetNode, value: 1,label: linkItem.link_name,attributes: linkItem});

        });
        nodesList.forEach(function(nodeItem){
            nodeItem.attributes = [];
            var attrHoverFields = NodeHoverAttr.find({ "type": nodeItem["type"]}).fetch();
            if(attrHoverFields.length){
                attrHoverFields[0].attributes.forEach(function(field){
                    if(nodeItem[field]){
                        var object = {};
                        object[field] = nodeItem[field];
                        nodeItem.attributes.push(object);
                    }
                });
            }
        });

        this.graph.nodes = nodesList;
        this.graph.links = edges_new;

    },
    creategraphdata: function (){
        var self = this;
        var width = 500,
            height = 500;

        this.color = d3.scale.category20();
        /*
         this.svg = d3.select("#dgraphid").append("svg")
         .attr("width", "100%")
         .attr("height", "100%")
         .attr("pointer-events", "all")
         //.attr('transform', 'translate(250,250) scale(0.3)')
         .call(d3.behavior.zoom().on("zoom", this.redraw))
         .append('svg:g');

         //.append("g");

         this.force = cola.d3adaptor().convergenceThreshold(0.1)
         //.linkDistance(200)
         .size([width, height]);
         */
        var focused = null;

        this.force = cola.d3adaptor().convergenceThreshold(0.1)
        //.linkDistance(200)
            .size([width, height]);

        var outer = d3.select("#dgraphid")
            .append("svg")
            .attr({ width: "100%", height: "100%", "pointer-events": "all" });

        outer.append('rect')
            .attr({ class: 'background', width: "100%", height: "100%" })
            .call(this.zoomer());
            /*.call(d3.behavior.zoom()
                .on("zoom", function(d) {
                d3Graph.svg.attr("transform", "translate(" + d3.event.translate + ")" + " scale(" + d3.event.scale + ")");
            }))*/
            //.on("mouseover", function () { focused = this; });

        //d3.select("body").on("keydown", function () { d3.select(focused); /* then do something with it here */ });
        //d3.select("#dgraphid").on("keydown", d3Graph.keydown());

        this.svg = outer
            .append('g')
            .attr('transform', 'translate(250,250) scale(0.3)');

    },
    redraw: function(){
        //console.log("here", d3.event.translate, d3.event.scale);

        d3Graph.svg.attr("transform",
            "translate(" + d3.event.translate + ")"
            + " scale(" + d3.event.scale + ")");

    },

    updateNetworkGraph:function (){
        var self = this;

        this.svg.selectAll('g').remove();
        //this.svg.exit().remove();

        var div = d3.select("body").append("div")
            .attr("class", "tooltip")
            .style("opacity", 0);

        this.force
            .nodes(this.graph.nodes)
            .links(this.graph.links)
            .symmetricDiffLinkLengths(250)
            //.jaccardLinkLengths(300)
            //.jaccardLinkLengths(80,0.7)
            .handleDisconnected(true)
            .avoidOverlaps(true)
            .start(50, 100, 200);

        /*
         this.force
         .on("dragstart", function (d) { d3.event.sourceEvent.stopPropagation(); d3.select(this).classed("dragging", true); } )
         .on("drag", function (d) { d3.select(this).attr("cx", d.x = d3.event.x).attr("cy", d.y = d3.event.y); } )
         .on("dragend", function (d) { d3.select(this).classed("dragging", false); });
         */


        // Define the div for the tooltip

        //svg.exit().remove();
        //graph.constraints = [{"axis":"y", "left":0, "right":1, "gap":25},];

        //.start(10,15,20);
        /*var path = svg.append("svg:g")
         .selectAll("path")
         .data(force.links())
         .enter().append("svg:path")
         .attr("class", "link");;
         */
        var link = this.svg.selectAll(".link")
            .data(this.force.links())
            .enter()
            .append("g")
            .attr("class", "link-group")
            .append("line")
            .attr("class", "link")
            .style("stroke-width", function(d) { return 3; })
            //.style("stroke-width", function(d) { return Math.sqrt(d.stroke); })
            .attr('stroke', function (d) {
                if(d.attributes.state == 'error'){
                    self.blinkLink(d);
                    return "red";
                }
                else if(d.attributes.state == 'warn'){
                    self.blinkLink(d);
                    return "orange";
                }
                else if(d.source.level === d.target.level) {
                    return self.color(d.source.level);
                }
                else {
                    return self.color(d.level);
                    //d3.select(this).classed('different-groups', true);
                }
            });
        /*.style("stroke", function(d) {
         if(d.label == 'net-103'){
         self.blinkLink(d);
         return "red";
         }
         //return "red";
         //return self.color(d.level);
         })*/

        var linkText = this.svg.selectAll(".link-group")
            .append("text")
            .data(this.force.links())
            .text(function(d) { return d.label })
            .attr("x", function(d) { return (d.source.x + (d.target.x - d.source.x) * 0.5); })
            .attr("y", function(d) { return (d.source.y + (d.target.y - d.source.y) * 0.5); })
            .attr("dy", ".25em")
            .attr("text-anchor", "right")
            .on("mouseover", function(d) {
                div.transition()
                    .duration(200)
                    .style("opacity", .9);
                d.title = "";
                if(d.attributes != undefined){
                    d.title = JSON.stringify(d.attributes, null, 4).toString().replace(/\,/g,'<BR>').replace(/\[/g,'').replace(/\]/g,'').replace(/\{/g,'').replace(/\}/g,'').replace(/"/g,'');
                }
                div.html("<p><u>" + d.label + "</u><br/>"  + d.title + "<p/>")
                    .style("left", (d3.event.pageX) + "px")
                    .style("top", (d3.event.pageY - 28) + "px");
            })
            .on("mouseout", function(d) {
                div.transition()
                    .duration(500)
                    .style("opacity", 0);
            });



        var node = this.svg.selectAll(".node")
            .data(this.force.nodes())
            .enter().append("g")
            .attr("class", "node")
            .call(this.force.drag);

        // A map from group ID to image URL.
        var imageByGroup = {
            "instance": "ic_computer_black_48dp_2x.png",
            "pnic": "ic_dns_black_48dp_2x.png",
            "vconnector": "ic_settings_input_composite_black_48dp_2x.png",
            // "network": "ic_cloud_queue_black_48dp_2x.png",
            "network": "ic_cloud_queue_black_48dp_2x.png",
            "vedge": "ic_gamepad_black_48dp_2x.png",
            "vservice": "ic_storage_black_48dp_2x.png",
            "vnic": "ic_settings_input_hdmi_black_48dp_2x.png",
            "otep":"ic_keyboard_return_black_48dp_2x.png",
            "default":"ic_lens_black_48dp_2x.png"
        };

        node.append("image")
        //.attr("xlink:href", "https://github.com/favicon.ico")
            .attr("xlink:href", function(d) {
                if(imageByGroup[d.type]){
                    return imageByGroup[d.type];
                }
                else{
                    return imageByGroup["default"];
                }

            })
            .attr("x", -8)
            .attr("y", -8)
            .attr("width", 36)
            .attr("height", 36)
            //node.append("circle")
            .attr("class", "node")
            //.attr("r", function(d){return 13;})
            .on("mouseover", function(d) {
                div.transition()
                    .duration(200)
                    .style("opacity", .9);
                d.title = "";
                if(d.attributes != undefined){
                    d.title = JSON.stringify(d.attributes, null, 4).toString().replace(/\,/g,'<BR>').replace(/\[/g,'').replace(/\]/g,'').replace(/\{/g,'').replace(/\}/g,'').replace(/"/g,'');
                }

                div.html("<p><u>" + d.name + "</u><br/>"  + d.title + "<p/>")
                    .style("left", (d3.event.pageX) + "px")
                    .style("top", (d3.event.pageY - 28) + "px");
            })
            .on("mouseout", function(d) {
                div.transition()
                    .duration(500)
                    .style("opacity", 0);
            })
            .style("fill", function(d) {
                if(d.state == "error"){
                    self.blinkNode(d);
                    return "red";
                }
                return self.color(d.group);
            })
            .call(this.force.drag);


        /*
         .each(function() {
         var sel = d3.select(this);
         var state = false;
         sel.on('dblclick', function () {
         state = !state;
         if (state) {
         sel.style('fill', 'black');
         } else {
         sel.style('fill', function (d) {
         return d.colr;
         });
         }
         });
         });
         */

        node.append("text")
            .attr("dx", 0)
            .attr("dy", 40)
            .text(function(d) { return d.object_name});


        this.force.on("tick", function() {
            link.attr("x1", function(d) { return d.source.x; })
                .attr("y1", function(d) { return d.source.y; })
                .attr("x2", function(d) { return d.target.x; })
                .attr("y2", function(d) { return d.target.y; });
            /*
             .attr("dr1", function(d) { return 75/d.source.linknum; })
             .attr("dr2", function(d) { return 75/d.target.linknum; });
             */

            node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

            linkText
                .attr("x", function(d) { return (d.source.x + (d.target.x - d.source.x) * 0.5); })
                .attr("y", function(d) { return (d.source.y + (d.target.y - d.source.y) * 0.5); });

        });

    },
    centerview: function () {
        // Center the view on the molecule(s) and scale it so that everything
        // fits in the window
        var width = 500,
            height = 500;

        if (this.graph === null)
            return;

        var nodes = this.graph.nodes;

        //no molecules, nothing to do
        if (nodes.length === 0)
            return;

        // Get the bounding box
        min_x = d3.min(nodes.map(function(d) {return d.x;}));
        min_y = d3.min(nodes.map(function(d) {return d.y;}));

        max_x = d3.max(nodes.map(function(d) {return d.x;}));
        max_y = d3.max(nodes.map(function(d) {return d.y;}));


        // The width and the height of the graph
        mol_width = max_x - min_x;
        mol_height = max_y - min_y;

        // how much larger the drawing area is than the width and the height
        width_ratio = width / mol_width;
        height_ratio = height / mol_height;

        // we need to fit it in both directions, so we scale according to
        // the direction in which we need to shrink the most
        min_ratio = Math.min(width_ratio, height_ratio) * 0.8;

        // the new dimensions of the molecule
        new_mol_width = mol_width * min_ratio;
        new_mol_height = mol_height * min_ratio;

        // translate so that it's in the center of the window
        x_trans = -(min_x) * min_ratio + (width - new_mol_width) / 2;
        y_trans = -(min_y) * min_ratio + (height - new_mol_height) / 2;


        // do the actual moving
        d3Graph.svg.attr("transform",
            "translate(" + [x_trans, y_trans] + ")" + " scale(" + min_ratio + ")");

        // tell the zoomer what we did so that next we zoom, it uses the
        // transformation we entered here
        //d3Graph.zoomer.translate([x_trans, y_trans ]);
        //d3Graph.zoomer.scale(min_ratio);
    },
    keydown:function() {
/*
        shiftKey = d3.event.shiftKey || d3.event.metaKey;
        ctrlKey = d3.event.ctrlKey;
*/
        if(d3.event===null)
            return;

        console.log('d3.event', d3.event)

        if (d3.event.keyCode == 67) {   //the 'c' key
            this.centerview();
        }

    },
    blinkNode: function(node){
        var nodeList = this.svg.selectAll(".node");
        var selected = nodeList.filter(function (d, i) {
            return d.id == node.id;
            //return d.name != findFromParent;
        });
        selected.forEach(function(n){
                for (i = 0; i != 30; i++) {
                    $(n[1]).fadeTo('slow', 0.1).fadeTo('slow', 5.0)};
            }
        );
    },
    blinkLink: function(link){
        var linkList = this.svg.selectAll(".link");
        var selected = linkList.filter(function (d, i) {
            return d.label == link.label;
            //return d.id == link.id;
            //return d.name != findFromParent;
        });
        selected.forEach(function(n){
                for (i = 0; i != 30; i++) {
                    $(n[0]).fadeTo('slow', 0.1).fadeTo('slow', 5.0)};
            }
        );
    },
    tick:function(obj){

        obj.link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        obj.node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

        obj.linkText
            .attr("x", function(d) { return (d.source.x + (d.target.x - d.source.x) * 0.5); })
            .attr("y", function(d) { return (d.source.y + (d.target.y - d.source.y) * 0.5); });
    }
};
menuTree = {
    menu:{},
    init:function(){
        this.memu = $( '#menu' ).multilevelpushmenu({
            menuWidth: '20%',
            menuHeight: '94%',
            containersToPush: [$( '#pushobj' )],
            overlapWidth: 40,
            backItemIcon: 'fa fa-angle-left',
            groupIcon: 'fa fa-angle-right',
            onItemClick: function() {
                var event = arguments[0],
                    $menuLevelHolder = arguments[1],
                    $item = arguments[2],
                    options = arguments[3],
                    title = $menuLevelHolder.find( 'h2:first' ).text(),
                    itemName = $item.find( 'a:first' ).text();
                //console.log(arguments);
                //console.log($item[0]);
                if($item[0].type == "host_ref" && $item[0].title == 'node-24'){
                    if($item.level > 1){
                        var itemList = $('#menu').multilevelpushmenu('pathtoroot', $item);
                        $('.breadcrumb li').remove();
                        itemList.forEach(function(e){
                            if(e.firstChild.innerText != '' && e.firstChild.innerText != undefined)
                            {
                                $('.breadcrumb').append('<li><a href="#">'+e.firstChild.innerText+'</a></li>');
                            }
                        });
                        $('.breadcrumb').append('<li class="active">'+itemName+'</li>');
                    }

                    Session.set('currNodeId',$item[0].id);
                    var graphData = d3Graph.getGraphData($item[0].id);
                    d3Graph.updateNetworkGraph(graphData);
                    /*
                     myfunc = Template.multilevelorig.__helpers.get("getNodeItems");
                     myfunc($item[0].id);
                     */

                }
                else if($item.attr("clique") == "true"){
                    var graphData = d3Graph.getGraphDataByClique($item.attr("objId"));
                    //console.log($item[0].objId);
                }
                //console.log($item.find( 'a:first' ));
            },
            onGroupItemClick: function() {
                var event = arguments[0],
                    $menuLevelHolder = arguments[1],
                    $item = arguments[2],
                    options = arguments[3],
                    title = $menuLevelHolder.find('h2:first').text(),
                    itemName = $item.find('a:first').text();

                //console.log($item);
                if($item.attr("clique") == "true"){
                    var graphData = d3Graph.getGraphDataByClique($item.attr("objId"));
                    d3Graph.updateNetworkGraph(graphData);
                    //console.log($item.attr("objId"));
                }
            },
        });
    },
};
