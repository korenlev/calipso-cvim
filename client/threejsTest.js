/////////////////////////////////////////////////////////////////////////////////////////
// Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems) and others /
//                                                                                      /
// All rights reserved. This program and the accompanying materials                     /
// are made available under the terms of the Apache License, Version 2.0                /
// which accompanies this distribution, and is available at                             /
// http://www.apache.org/licenses/LICENSE-2.0                                           /
/////////////////////////////////////////////////////////////////////////////////////////
/*(function() {
// D3.layout.force3d.js
// (C) 2012 ziggy.jonsson.nyc@gmail.com
// BSD license (http://opensource.org/licenses/BSD-3-Clause)

    d3.layout.force3d = function() {
        var  forceXY = d3.layout.force()
            ,forceZ = d3.layout.force()
            ,zNodes = {}
            ,zLinks = {}
            ,nodeID = 1
            ,linkID = 1
            ,tickFunction = Object

        var force3d = {}

        Object.keys(forceXY).forEach(function(d) {
            force3d[d] = function() {
                var result = forceXY[d].apply(this,arguments)
                if (d !="nodes" && d!="links")  forceZ[d].apply(this,arguments)
                return (result == forceXY) ? force3d : result
            }
        })


        force3d.on = function(name,fn) {
            tickFunction = fn
            return force3d
        }


        forceXY.on("tick",function() {

            // Refresh zNodes add new, delete removed
            var _zNodes = {}
            forceXY.nodes().forEach(function(d,i) {
                if (!d.id) d.id = nodeID++
                _zNodes[d.id] = zNodes[d.id] ||  {x:d.z,px:d.z,py:d.z,y:d.z,id:d.id}
                d.z =  _zNodes[d.id].x
            })
            zNodes = _zNodes

            // Refresh zLinks add new, delete removed
            var _zLinks = {}
            forceXY.links().forEach(function(d) {
                var nytt = false
                if (!d.linkID) { d.linkID = linkID++;nytt=true}
                _zLinks[d.linkID] = zLinks[d.linkID]  || {target:zNodes[d.target.id],source:zNodes[d.source.id]}

            })
            zLinks = _zLinks

            // Update the nodes/links in forceZ
            forceZ.nodes(d3.values(zNodes))
            forceZ.links(d3.values(zLinks))
            forceZ.start() // Need to kick forceZ so we don't lose the update mechanism

            // And run the user defined function, if defined
            tickFunction()
        })

        // Expose the sub-forces for debugging purposes
        force3d.xy = forceXY
        force3d.z = forceZ

        return force3d
    }
})()*/
Template.threeTest.rendered = function () {
    function getGraphData(){
        nodeId = 'node-24';
        //d3.json("miserables.json", function(error, graph) {

        //var invNodes = Inventory.find({ "type": "instance", $and: [ { "id": nodeId } ] });
        var invNodes = Inventory.find({ "type": "instance", $and: [ { "host": nodeId } ] });

        var edges = [];
        var nodes = [];

        invNodes.forEach(function(n){
            nodes =  n["Entities"];
            edges =  n["Relations"];
        });
        //console.log(testNodes);
        //var invEdges = Inventory.find({ "type": "instance", $and: [ { "id": nodeId } ] }["Edges"]);

        //var invEdges = EdgesList.find(nodeId).fetch();
        //var invNodes = NodesList.find(nodeId).fetch();
        //console.log(invEdges);


        /*
         var edges = Edges.find().fetch();
         var nodes = Nodes.find().fetch();
         */

        nodes.forEach(function(n){
            n.name = n.label;
            n.x = Math.random();
            n.y = Math.random();
        });
        var edges_new = [];
        edges.forEach(function(e) {
            var sourceNode = nodes.filter(function(n) { return n.id === e.from; })[0],
                targetNode = nodes.filter(function(n) { return n.id === e.to; })[0];

            edges_new.push({source: sourceNode, target: targetNode, value: 1,label: e.label,attributes: e.attributes});
        });

        var graph = {};
        graph.nodes = nodes;
        graph.links = edges_new;

        //console.log(graph);

        return graph;
    }


    var graph = getGraphData();

    var color = d3.scale.category20();


    var WIDTH = 700, HEIGHT = 700;

    var COLOR = "#0f608b";
    var LINK_COLOR = "#999999";

    var scene = new THREE.Scene();

// set some camera attributes
    var VIEW_ANGLE = 45,
        ASPECT = WIDTH / HEIGHT,
        NEAR = 0.1,
        FAR = 10000;

// get the DOM element to attach to
// - assume we've got jQuery to hand
    var $container = $('#threeGraph');

// create a WebGL renderer, camera
// and a scene
    var renderer = new THREE.WebGLRenderer({alpha: true,
        antialiasing: true});

    renderer.setClearColor( 0x000000, 0 );

    var camera =
        new THREE.PerspectiveCamera(
            VIEW_ANGLE,
            ASPECT,
            NEAR,
            FAR);

    var scene = new THREE.Scene();

// add the camera to the scene
    scene.add(camera);

// the camera starts at 0,0,0
// so pull it back
    camera.position.z = 300;

// start the renderer
    renderer.setSize(WIDTH, HEIGHT);

// attach the render-supplied DOM element
    $container.append(renderer.domElement);

    var spheres = [], three_links = [];

// Define the 3d force
    var force = d3.layout.force3d()
        .nodes(sort_data=[])
        .links(links=[])
        .size([50, 50])
        .gravity(0.3)
        .charge(-400)

    var DISTANCE = 1
//    var data = graph;
    var data = {
        "nodes": [
            {
                "x": 469,
                "y": 410
            },
            {
                "x": 493,
                "y": 364
            },
            {
                "x": 442,
                "y": 365
            },
            {
                "x": 467,
                "y": 314
            },
            {
                "x": 477,
                "y": 248
            },
            {
                "x": 425,
                "y": 207
            },
            {
                "x": 402,
                "y": 155
            },
            {
                "x": 369,
                "y": 196
            },
            {
                "x": 350,
                "y": 148
            },
            {
                "x": 539,
                "y": 222
            },
            {
                "x": 594,
                "y": 235
            },
            {
                "x": 582,
                "y": 185
            },
            {
                "x": 633,
                "y": 200
            }
        ],
        "links": [
            {
                "source": 0,
                "target": 1
            },
            {
                "source": 1,
                "target": 2
            },
            {
                "source": 2,
                "target": 0
            },
            {
                "source": 1,
                "target": 3
            },
            {
                "source": 3,
                "target": 2
            },
            {
                "source": 3,
                "target": 4
            },
            {
                "source": 4,
                "target": 5
            },
            {
                "source": 5,
                "target": 6
            },
            {
                "source": 5,
                "target": 7
            },
            {
                "source": 6,
                "target": 7
            },
            {
                "source": 6,
                "target": 8
            },
            {
                "source": 7,
                "target": 8
            },
            {
                "source": 9,
                "target": 4
            },
            {
                "source": 9,
                "target": 11
            },
            {
                "source": 9,
                "target": 10
            },
            {
                "source": 10,
                "target": 11
            },
            {
                "source": 11,
                "target": 12
            },
            {
                "source": 12,
                "target": 10
            }
        ]
    };

    for (var i = 0; i < data.nodes.length; i++) {
        sort_data.push({x:data.nodes.x + DISTANCE,y:data.nodes.y + DISTANCE,z:0})

        // set up the sphere vars
        var radius = 5,
            segments = 16,
            rings = 16;

        // create the sphere's material
        var sphereMaterial = new THREE.MeshLambertMaterial(
            {
                color: COLOR
            });

        var sphere = new THREE.Mesh(
            new THREE.SphereGeometry(
                radius,
                segments,
                rings),
            sphereMaterial);

        spheres.push(sphere);

        // add the sphere to the scene
        scene.add(sphere);
    }

    for (var i = 0; i < data.links.length; i++) {
        links.push({target:data.links[i].target,source:data.links[i].source});

        var material = new THREE.LineBasicMaterial({ color: LINK_COLOR,
            linewidth: 2});
        var geometry = new THREE.Geometry();

        geometry.vertices.push( new THREE.Vector3( 0, 0, 0 ) );
        geometry.vertices.push( new THREE.Vector3( 0, 0, 0 ) );
        var line = new THREE.Line( geometry, material );
        line.userData = { source: data.links[i].source,
            target: data.links[i].target };
        three_links.push(line);
        scene.add(line);

        force.start();
    }

// set up the axes
    var x = d3.scale.linear().domain([0, 350]).range([0, 10]),
        y = d3.scale.linear().domain([0, 350]).range([0, 10]),
        z = d3.scale.linear().domain([0, 350]).range([0, 10]);

    force.on("tick", function(e) {
        for (var i = 0; i < sort_data.length; i++) {
            spheres[i].position.set(x(sort_data[i].x) * 40 - 40, y(sort_data[i].y) * 40 - 40,0);

            for (var j = 0; j < three_links.length; j++) {
                var line = three_links[j];
                var vi = -1;
                if (line.userData.source === i) {
                    vi = 0;
                }
                if (line.userData.target === i) {
                    vi = 1;
                }

                if (vi >= 0) {
                    line.geometry.vertices[vi].x = x(sort_data[i].x) * 40 - 40;
                    line.geometry.vertices[vi].y = y(sort_data[i].y) * 40 - 40;
                    line.geometry.verticesNeedUpdate = true;
                }
            }
        }

        renderer.render(scene, camera);
    });

// create a point light
    var pointLight = new THREE.PointLight( 0xFFFFFF );

// set its position
    pointLight.position.x = 10;
    pointLight.position.y = 50;
    pointLight.position.z = 130;

// add to the scene
    scene.add(pointLight);

    var rotSpeed = 0.01;
    function checkRotation(){

        var x = camera.position.x,
            y = camera.position.y,
            z = camera.position.z;

        camera.position.x = x * Math.cos(rotSpeed) - z * Math.sin(rotSpeed);
        camera.position.z = z * Math.cos(rotSpeed) + x * Math.sin(rotSpeed);

        camera.lookAt(scene.position);

    }

    function animate() {
        requestAnimationFrame(animate);

        checkRotation();

        renderer.render(scene, camera);
    }

    animate();
 /*   var data = [4, 8, 15, 16, 23, 42];

// these are, as before, to make D3's .append() and .selectAll() work
    THREE.Object3D.prototype.appendChild = function (c) { this.add(c); return c; };
    THREE.Object3D.prototype.querySelectorAll = function () { return []; };

// this one is to use D3's .attr() on THREE's objects
    THREE.Object3D.prototype.setAttribute = function (name, value) {
        var chain = name.split('.');
        var object = this;
        for (var i = 0; i < chain.length - 1; i++) {
            object = object[chain[i]];
        }
        object[chain[chain.length - 1]] = value;
    }

    var camera, scene, renderer, chart3d;

    init();
    animate();

    function init () {
        // standard THREE stuff, straight from examples
        renderer = new THREE.WebGLRenderer();
        renderer.setSize( window.innerWidth, window.innerHeight );
        document.body.appendChild( renderer.domElement );

        camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 1000 );
        camera.position.z = 400;

        scene = new THREE.Scene();

        var light = new THREE.DirectionalLight( 0xffffff );
        light.position.set( 0, 0, 1 );
        scene.add( light );

        var geometry = new THREE.CubeGeometry( 20, 20, 20 );
        var material = new THREE.MeshLambertMaterial( {
            color: 0x4682B4, shading: THREE.FlatShading, vertexColors: THREE.VertexColors } );

        // create container for our 3D chart
        chart3d = new THREE.Object3D();
        chart3d.rotation.x = 0.6;
        scene.add( chart3d );

        // use D3 to set up 3D bars
        d3.select( chart3d )
            .selectAll()
            .data(data)
            .enter().append( function() { return new THREE.Mesh( geometry, material ); } )
            .attr("position.x", function(d, i) { return 30 * i; })
            .attr("position.y", function(d, i) { return d; })
            .attr("scale.y", function(d, i) { return d / 10; })

        // continue with THREE stuff
        window.addEventListener( 'resize', onWindowResize, false );
    }

    function onWindowResize() {

        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();

        renderer.setSize( window.innerWidth, window.innerHeight );

    }

    function animate() {

        requestAnimationFrame( animate );

        chart3d.rotation.y += 0.01;

        renderer.render( scene, camera );

    }
*/


/*

    var d3obj = d3.select("#threeGraph").append("svg")
        .attr("width", "100%")
        .attr("height", "100%");

    var force = d3.layout.force()
        .charge(-120)
        .linkDistance(30)
        .size([700, 700]);

    force
        .nodes(graph.nodes)
        .links(graph.links)
        .start(10,15,20);
*/


    /*
        var d3obj = d3.select( chart )
            .selectAll()
            //.data(graph.nodes)
            //.enter()
            .append( createDiv )
            .style("width", function(d) { return d * 10 + "px"; })
            .text(function(d) { return d; });
    */
/*

    var link = d3obj.selectAll(".link")
        .data(graph.links)
        .enter()
        .append("g")
        .attr("class", "link-group")
        .append("line")
        .attr("class", "link")
        .style("stroke-width", function(d) { return Math.sqrt(d.stroke); });

    var node = d3obj.selectAll(".node")
        .data(graph.nodes)
        .enter().append("g")
        .attr("class", "node")
        .call(force.drag);
    
    
    node.append("circle")
        .attr("class", "node")
        .attr("r", function(d){return 13;})
        .on("mouseover", function(d) {
            d3obj.transition()
                .duration(200)
                .style("opacity", .9);
            d.title = "";
            if(d.attributes != undefined){
                d.title = JSON.stringify(d.attributes, null, 4).toString().replace(/\,/g,'<BR>').replace(/\[/g,'').replace(/\]/g,'').replace(/\{/g,'').replace(/\}/g,'').replace(/"/g,'');
            }

            d3obj.html("<p><u>" + d.name + "</u><br/>"  + d.title + "<p/>")
                .style("left", (d3.event.pageX) + "px")
                .style("top", (d3.event.pageY - 28) + "px");
        })
        .on("mouseout", function(d) {
            d3obj.transition()
                .duration(500)
                .style("opacity", 0);
        })
        .style("fill", function(d) { return color(d.level); })
        .call(force.drag);

    node.append("text")
        .attr("dx", 14)
        .attr("dy", ".35em")
        .text(function(d) { return d.label});


    force.on("tick", function() {
        link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

    });
*/



    /*
    $(document).ready(function() {
        var container, stats, valid;
        var camera, scene, renderer, group, particle;
        var mouseX = 0, mouseY = 0;
        var force, nodes = [], links = [];

        var part = new Image();
        part.src = "/particle.png";
        part.onload = function () {
            init();
            animate();
        };

        var w2 = document.body.clientWidth / 2;
        var h2 = document.body.clientHeight / 2;

        function colorize(img, r, g, b, a) {
            if (!img)
                return img;

            var tempFileCanvas = document.createElement("canvas");
            tempFileCanvas.width = img.width;
            tempFileCanvas.height = img.height;

            var imgCtx = tempFileCanvas.getContext("2d"), imgdata, i;
            imgCtx.clearRect(0, 0, img.width, img.height);
            imgCtx.save();
            imgCtx.drawImage(img, 0, 0);

            imgdata = imgCtx.getImageData(0, 0, img.width, img.height);

            i = imgdata.data.length;
            while ((i -= 4) > -1) {
                imgdata.data[i + 3] = imgdata.data[i] * a;
                if (imgdata.data[i + 3]) {
                    imgdata.data[i] = r;
                    imgdata.data[i + 1] = g;
                    imgdata.data[i + 2] = b;
                }
            }

            imgCtx.putImageData(imgdata, 0, 0);
            imgCtx.restore();
            return tempFileCanvas;
        }

        function init() {

            //container = document.createElement('div');
            container = $("#threeGraph");
            //document.body.appendChild(container);

            camera = new THREE.PerspectiveCamera(h2 * 2, w2 / h2, 99, 101);
            camera.position.z = 100;

            scene = new THREE.Scene();

            var group = new THREE.Object3D();

            var PI2 = Math.PI * 2;
            var program = function (ctx, color) {
                color = d3.rgb(ctx.fillStyle);
                ctx.drawImage(part, 0.5, 0.5, 1, 1);
            };

            var lineMaterial = new THREE.LineBasicMaterial({
                color: 0xff0000,
                opacity: .1
            });

            var particleMaterial = new THREE.PointsMaterial({
                size: 0.1,
                blending: THREE.AdditiveBlending, // required
                depthTest: false, // required
                transparent: true,
                opacity: 0.7,
                vertexColors: true // optional
            });

            /!*new THREE.ParticleCanvasMaterial( {
             color: Math.random() * 0x808008 + 0x808080,
             program: program
             } )*!/

            for (var i = 0, j; i < 500; i++) {

                var pm = particleMaterial.clone();

                pm.color = new THREE.Color();
                //pm.color.setHSV(Math.random(), 1, 1);

                var c = d3.rgb(pm.color.getStyle());
                pm.map = new THREE.Texture(colorize(part, c.r, c.g, c.b, 1));

                particle = new THREE.Particle(pm);
                particle.position.x = (Math.random() * w2 * 4 - w2 * 2);
                particle.position.y = (Math.random() * h2 * 4 - h2 * 2);
                particle.position.z = 0;
                particle.scale.x = particle.scale.y = Math.random();

                j = nodes.push(particle.position);

                j = links.push({source: j % 10, target: j - 1});
                j = links[j - 1];
                stats = new THREE.Geometry();
                stats.vertices.push(new THREE.Vector3(nodes[j.source]));
                stats.vertices.push(new THREE.Vector3(nodes[j.target]));

                group.add(new THREE.Line(stats, lineMaterial));

                group.add(particle);
            }
            scene.add(group);

            renderer = new THREE.CanvasRenderer();
            renderer.setSize(w2 * 2, h2 * 2);
            //container.appendChild(renderer.domElement);
            container.append(renderer.domElement);

            d3.select(renderer.domElement)
                .call(d3.behavior.zoom()
                    .scaleExtent([0.01, 8])
                    .scale(1)
                    .translate([group.position.x, group.position.y])
                    .on("zoom", function () {
                        group.scale.x = group.scale.y = d3.event.scale;
                        //camera.position.z = d3.event.scale;
                        group.position.x = -d3.event.translate[0];
                        group.position.y = d3.event.translate[1];

                        valid = false;
                    }));

            window.addEventListener('resize', onWindowResize, false);

            force = d3.layout.force()
                .nodes(nodes)
                .links(links)
                .on("tick", function () {
                    valid = false;
                })
                .start();
        }

        function onWindowResize() {

            w2 = window.innerWidth / 2;
            h2 = window.innerHeight / 2;

            camera.aspect = w2 / h2;
            camera.updateProjectionMatrix();

            renderer.setSize(w2 * 2, h2 * 2);

            valid = false;
        }

        function animate() {

            requestAnimationFrame(animate);

            if (!valid) {
                valid = true;
                render();
            }

        }

        function render() {

            camera.lookAt(scene.position);

            renderer.render(scene, camera);

        }
    });
*/
};
