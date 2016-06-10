//////////////////////////////////////////////////////////////////////////
//                                                                      //
// This is a generated file. You can view the original                  //
// source in your browser if your browser supports source maps.         //
// Source maps are supported by all recent versions of Chrome, Safari,  //
// and Firefox, and by Internet Explorer 11.                            //
//                                                                      //
//////////////////////////////////////////////////////////////////////////


(function () {

/* Imports */
var Meteor = Package.meteor.Meteor;
var global = Package.meteor.global;
var meteorEnv = Package.meteor.meteorEnv;
var _ = Package.underscore._;
var meteorInstall = Package['modules-runtime'].meteorInstall;

/* Package-scope variables */
var Buffer, process;

var require = meteorInstall({"node_modules":{"meteor":{"modules":{"client.js":["./install-packages.js","./stubs.js","./buffer.js","./process.js","./css",function(require,exports){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// packages/modules/client.js                                                                                          //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
require("./install-packages.js");                                                                                      // 1
require("./stubs.js");                                                                                                 // 2
require("./buffer.js");                                                                                                // 3
require("./process.js");                                                                                               // 4
                                                                                                                       // 5
exports.addStyles = require("./css").addStyles;                                                                        // 6
                                                                                                                       // 7
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}],"buffer.js":["buffer",function(require){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// packages/modules/buffer.js                                                                                          //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
try {                                                                                                                  // 1
  Buffer = global.Buffer || require("buffer").Buffer;                                                                  // 2
} catch (noBuffer) {}                                                                                                  // 3
                                                                                                                       // 4
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}],"css.js":function(require,exports){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// packages/modules/css.js                                                                                             //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
var doc = document;                                                                                                    // 1
var head = doc.getElementsByTagName("head").item(0);                                                                   // 2
                                                                                                                       // 3
exports.addStyles = function (css) {                                                                                   // 4
  var style = doc.createElement("style");                                                                              // 5
                                                                                                                       // 6
  style.setAttribute("type", "text/css");                                                                              // 7
                                                                                                                       // 8
  // https://msdn.microsoft.com/en-us/library/ms535871(v=vs.85).aspx                                                   // 9
  var internetExplorerSheetObject =                                                                                    // 10
    style.sheet || // Edge/IE11.                                                                                       // 11
    style.styleSheet; // Older IEs.                                                                                    // 12
                                                                                                                       // 13
  if (internetExplorerSheetObject) {                                                                                   // 14
    internetExplorerSheetObject.cssText = css;                                                                         // 15
  } else {                                                                                                             // 16
    style.appendChild(doc.createTextNode(css));                                                                        // 17
  }                                                                                                                    // 18
                                                                                                                       // 19
  return head.appendChild(style);                                                                                      // 20
};                                                                                                                     // 21
                                                                                                                       // 22
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"install-packages.js":function(require,exports,module){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// packages/modules/install-packages.js                                                                                //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
function install(name) {                                                                                               // 1
  var meteorDir = {};                                                                                                  // 2
                                                                                                                       // 3
  // Given a package name <name>, install a stub module in the                                                         // 4
  // /node_modules/meteor directory called <name>.js, so that                                                          // 5
  // require.resolve("meteor/<name>") will always return                                                               // 6
  // /node_modules/meteor/<name>.js instead of something like                                                          // 7
  // /node_modules/meteor/<name>/index.js, in the rare but possible event                                              // 8
  // that the package contains a file called index.js (#6590).                                                         // 9
  meteorDir[name + ".js"] = function (r, e, module) {                                                                  // 10
    module.exports = Package[name];                                                                                    // 11
  };                                                                                                                   // 12
                                                                                                                       // 13
  meteorInstall({                                                                                                      // 14
    node_modules: {                                                                                                    // 15
      meteor: meteorDir                                                                                                // 16
    }                                                                                                                  // 17
  });                                                                                                                  // 18
}                                                                                                                      // 19
                                                                                                                       // 20
// This file will be modified during computeJsOutputFilesMap to include                                                // 21
// install(<name>) calls for every Meteor package.                                                                     // 22
                                                                                                                       // 23
install("underscore");                                                                                                 // 24
install("meteor");                                                                                                     // 25
install("meteor-base");                                                                                                // 26
install("mobile-experience");                                                                                          // 27
install("babel-compiler");                                                                                             // 28
install("ecmascript");                                                                                                 // 29
install("base64");                                                                                                     // 30
install("ejson");                                                                                                      // 31
install("id-map");                                                                                                     // 32
install("ordered-dict");                                                                                               // 33
install("tracker");                                                                                                    // 34
install("modules-runtime");                                                                                            // 35
install("modules");                                                                                                    // 36
install("es5-shim");                                                                                                   // 37
install("promise");                                                                                                    // 38
install("ecmascript-runtime");                                                                                         // 39
install("babel-runtime");                                                                                              // 40
install("random");                                                                                                     // 41
install("mongo-id");                                                                                                   // 42
install("diff-sequence");                                                                                              // 43
install("geojson-utils");                                                                                              // 44
install("minimongo");                                                                                                  // 45
install("check");                                                                                                      // 46
install("retry");                                                                                                      // 47
install("ddp-common");                                                                                                 // 48
install("reload");                                                                                                     // 49
install("ddp-client");                                                                                                 // 50
install("ddp");                                                                                                        // 51
install("ddp-server");                                                                                                 // 52
install("allow-deny");                                                                                                 // 53
install("mongo");                                                                                                      // 54
install("blaze-html-templates");                                                                                       // 55
install("reactive-dict");                                                                                              // 56
install("session");                                                                                                    // 57
install("jquery");                                                                                                     // 58
install("url");                                                                                                        // 59
install("http");                                                                                                       // 60
install("deps");                                                                                                       // 61
install("htmljs");                                                                                                     // 62
install("observe-sequence");                                                                                           // 63
install("reactive-var");                                                                                               // 64
install("blaze");                                                                                                      // 65
install("ui");                                                                                                         // 66
install("spacebars");                                                                                                  // 67
install("templating");                                                                                                 // 68
install("iron:core");                                                                                                  // 69
install("iron:dynamic-template");                                                                                      // 70
install("iron:layout");                                                                                                // 71
install("iron:url");                                                                                                   // 72
install("iron:middleware-stack");                                                                                      // 73
install("iron:location");                                                                                              // 74
install("iron:controller");                                                                                            // 75
install("iron:router");                                                                                                // 76
install("twbs:bootstrap");                                                                                             // 77
install("d3js:d3");                                                                                                    // 78
install("standard-minifier-css");                                                                                      // 79
install("standard-minifier-js");                                                                                       // 80
install("limemakers:three");                                                                                           // 81
install("pcel:loading");                                                                                               // 82
install("spectrum:material-design-lite");                                                                              // 83
install("timmyg:wow");                                                                                                 // 84
install("ddp-rate-limiter");                                                                                           // 85
install("localstorage");                                                                                               // 86
install("callback-hook");                                                                                              // 87
install("accounts-base");                                                                                              // 88
install("service-configuration");                                                                                      // 89
install("npm-bcrypt");                                                                                                 // 90
install("sha");                                                                                                        // 91
install("srp");                                                                                                        // 92
install("accounts-password");                                                                                          // 93
install("less");                                                                                                       // 94
install("accounts-ui-unstyled");                                                                                       // 95
install("accounts-ui");                                                                                                // 96
install("webapp");                                                                                                     // 97
install("livedata");                                                                                                   // 98
install("hot-code-push");                                                                                              // 99
install("launch-screen");                                                                                              // 100
install("autoupdate");                                                                                                 // 101
                                                                                                                       // 102
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"process.js":["process",function(require,exports,module){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// packages/modules/process.js                                                                                         //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
try {                                                                                                                  // 1
  // The application can run `npm install process` to provide its own                                                  // 2
  // process stub; otherwise this module will provide a partial stub.                                                  // 3
  process = global.process || require("process");                                                                      // 4
} catch (noProcess) {                                                                                                  // 5
  process = {};                                                                                                        // 6
}                                                                                                                      // 7
                                                                                                                       // 8
if (Meteor.isServer) {                                                                                                 // 9
  // Make require("process") work on the server in all versions of Node.                                               // 10
  meteorInstall({                                                                                                      // 11
    node_modules: {                                                                                                    // 12
      "process.js": function (r, e, module) {                                                                          // 13
        module.exports = process;                                                                                      // 14
      }                                                                                                                // 15
    }                                                                                                                  // 16
  });                                                                                                                  // 17
} else {                                                                                                               // 18
  process.platform = "browser";                                                                                        // 19
  process.nextTick = process.nextTick || Meteor._setImmediate;                                                         // 20
}                                                                                                                      // 21
                                                                                                                       // 22
if (typeof process.env !== "object") {                                                                                 // 23
  process.env = {};                                                                                                    // 24
}                                                                                                                      // 25
                                                                                                                       // 26
_.extend(process.env, meteorEnv);                                                                                      // 27
                                                                                                                       // 28
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}],"stubs.js":["meteor-node-stubs",function(require){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// packages/modules/stubs.js                                                                                           //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
try {                                                                                                                  // 1
  // When meteor-node-stubs is installed in the application's root                                                     // 2
  // node_modules directory, requiring it here installs aliases for stubs                                              // 3
  // for all Node built-in modules, such as fs, util, and http.                                                        // 4
  require("meteor-node-stubs");                                                                                        // 5
} catch (noStubs) {}                                                                                                   // 6
                                                                                                                       // 7
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}]}},"webcola":{"package.json":function(require,exports){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/webcola/package.json                                                                                   //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
exports.name = "webcola";                                                                                              // 1
exports.version = "3.1.3";                                                                                             // 2
exports.main = "WebCola/index.js";                                                                                     // 3
                                                                                                                       // 4
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"WebCola":{"index.js":function(require,exports,module){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/webcola/WebCola/index.js                                                                               //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
var cola;                                                                                                              // 1
(function (cola) {                                                                                                     // 2
    var packingOptions = {                                                                                             // 3
        PADDING: 10,                                                                                                   // 4
        GOLDEN_SECTION: (1 + Math.sqrt(5)) / 2,                                                                        // 5
        FLOAT_EPSILON: 0.0001,                                                                                         // 6
        MAX_INERATIONS: 100                                                                                            // 7
    };                                                                                                                 // 8
    // assign x, y to nodes while using box packing algorithm for disconnected graphs                                  // 9
    function applyPacking(graphs, w, h, node_size, desired_ratio) {                                                    // 10
        if (desired_ratio === void 0) { desired_ratio = 1; }                                                           // 11
        var init_x = 0, init_y = 0, svg_width = w, svg_height = h, desired_ratio = typeof desired_ratio !== 'undefined' ? desired_ratio : 1, node_size = typeof node_size !== 'undefined' ? node_size : 0, real_width = 0, real_height = 0, min_width = 0, global_bottom = 0, line = [];
        if (graphs.length == 0)                                                                                        // 13
            return;                                                                                                    // 14
        /// that would take care of single nodes problem                                                               // 15
        // graphs.forEach(function (g) {                                                                               // 16
        //     if (g.array.length == 1) {                                                                              // 17
        //         g.array[0].x = 0;                                                                                   // 18
        //         g.array[0].y = 0;                                                                                   // 19
        //     }                                                                                                       // 20
        // });                                                                                                         // 21
        calculate_bb(graphs);                                                                                          // 22
        apply(graphs, desired_ratio);                                                                                  // 23
        put_nodes_to_right_positions(graphs);                                                                          // 24
        // get bounding boxes for all separate graphs                                                                  // 25
        function calculate_bb(graphs) {                                                                                // 26
            graphs.forEach(function (g) {                                                                              // 27
                calculate_single_bb(g);                                                                                // 28
            });                                                                                                        // 29
            function calculate_single_bb(graph) {                                                                      // 30
                var min_x = Number.MAX_VALUE, min_y = Number.MAX_VALUE, max_x = 0, max_y = 0;                          // 31
                graph.array.forEach(function (v) {                                                                     // 32
                    var w = typeof v.width !== 'undefined' ? v.width : node_size;                                      // 33
                    var h = typeof v.height !== 'undefined' ? v.height : node_size;                                    // 34
                    w /= 2;                                                                                            // 35
                    h /= 2;                                                                                            // 36
                    max_x = Math.max(v.x + w, max_x);                                                                  // 37
                    min_x = Math.min(v.x - w, min_x);                                                                  // 38
                    max_y = Math.max(v.y + h, max_y);                                                                  // 39
                    min_y = Math.min(v.y - h, min_y);                                                                  // 40
                });                                                                                                    // 41
                graph.width = max_x - min_x;                                                                           // 42
                graph.height = max_y - min_y;                                                                          // 43
            }                                                                                                          // 44
        }                                                                                                              // 45
        //function plot(data, left, right, opt_x, opt_y) {                                                             // 46
        //    // plot the cost function                                                                                // 47
        //    var plot_svg = d3.select("body").append("svg")                                                           // 48
        //        .attr("width", function () { return 2 * (right - left); })                                           // 49
        //        .attr("height", 200);                                                                                // 50
        //    var x = d3.time.scale().range([0, 2 * (right - left)]);                                                  // 51
        //    var xAxis = d3.svg.axis().scale(x).orient("bottom");                                                     // 52
        //    plot_svg.append("g").attr("class", "x axis")                                                             // 53
        //        .attr("transform", "translate(0, 199)")                                                              // 54
        //        .call(xAxis);                                                                                        // 55
        //    var lastX = 0;                                                                                           // 56
        //    var lastY = 0;                                                                                           // 57
        //    var value = 0;                                                                                           // 58
        //    for (var r = left; r < right; r += 1) {                                                                  // 59
        //        value = step(data, r);                                                                               // 60
        //        // value = 1;                                                                                        // 61
        //        plot_svg.append("line").attr("x1", 2 * (lastX - left))                                               // 62
        //            .attr("y1", 200 - 30 * lastY)                                                                    // 63
        //            .attr("x2", 2 * r - 2 * left)                                                                    // 64
        //            .attr("y2", 200 - 30 * value)                                                                    // 65
        //            .style("stroke", "rgb(6,120,155)");                                                              // 66
        //        lastX = r;                                                                                           // 67
        //        lastY = value;                                                                                       // 68
        //    }                                                                                                        // 69
        //    plot_svg.append("circle").attr("cx", 2 * opt_x - 2 * left).attr("cy", 200 - 30 * opt_y)                  // 70
        //        .attr("r", 5).style('fill', "rgba(0,0,0,0.5)");                                                      // 71
        //}                                                                                                            // 72
        // actual assigning of position to nodes                                                                       // 73
        function put_nodes_to_right_positions(graphs) {                                                                // 74
            graphs.forEach(function (g) {                                                                              // 75
                // calculate current graph center:                                                                     // 76
                var center = { x: 0, y: 0 };                                                                           // 77
                g.array.forEach(function (node) {                                                                      // 78
                    center.x += node.x;                                                                                // 79
                    center.y += node.y;                                                                                // 80
                });                                                                                                    // 81
                center.x /= g.array.length;                                                                            // 82
                center.y /= g.array.length;                                                                            // 83
                // calculate current top left corner:                                                                  // 84
                var corner = { x: center.x - g.width / 2, y: center.y - g.height / 2 };                                // 85
                var offset = { x: g.x - corner.x + svg_width / 2 - real_width / 2, y: g.y - corner.y + svg_height / 2 - real_height / 2 };
                // put nodes:                                                                                          // 87
                g.array.forEach(function (node) {                                                                      // 88
                    node.x += offset.x;                                                                                // 89
                    node.y += offset.y;                                                                                // 90
                });                                                                                                    // 91
            });                                                                                                        // 92
        }                                                                                                              // 93
        // starts box packing algorithm                                                                                // 94
        // desired ratio is 1 by default                                                                               // 95
        function apply(data, desired_ratio) {                                                                          // 96
            var curr_best_f = Number.POSITIVE_INFINITY;                                                                // 97
            var curr_best = 0;                                                                                         // 98
            data.sort(function (a, b) { return b.height - a.height; });                                                // 99
            min_width = data.reduce(function (a, b) {                                                                  // 100
                return a.width < b.width ? a.width : b.width;                                                          // 101
            });                                                                                                        // 102
            var left = x1 = min_width;                                                                                 // 103
            var right = x2 = get_entire_width(data);                                                                   // 104
            var iterationCounter = 0;                                                                                  // 105
            var f_x1 = Number.MAX_VALUE;                                                                               // 106
            var f_x2 = Number.MAX_VALUE;                                                                               // 107
            var flag = -1; // determines which among f_x1 and f_x2 to recompute                                        // 108
            var dx = Number.MAX_VALUE;                                                                                 // 109
            var df = Number.MAX_VALUE;                                                                                 // 110
            while ((dx > min_width) || df > packingOptions.FLOAT_EPSILON) {                                            // 111
                if (flag != 1) {                                                                                       // 112
                    var x1 = right - (right - left) / packingOptions.GOLDEN_SECTION;                                   // 113
                    var f_x1 = step(data, x1);                                                                         // 114
                }                                                                                                      // 115
                if (flag != 0) {                                                                                       // 116
                    var x2 = left + (right - left) / packingOptions.GOLDEN_SECTION;                                    // 117
                    var f_x2 = step(data, x2);                                                                         // 118
                }                                                                                                      // 119
                dx = Math.abs(x1 - x2);                                                                                // 120
                df = Math.abs(f_x1 - f_x2);                                                                            // 121
                if (f_x1 < curr_best_f) {                                                                              // 122
                    curr_best_f = f_x1;                                                                                // 123
                    curr_best = x1;                                                                                    // 124
                }                                                                                                      // 125
                if (f_x2 < curr_best_f) {                                                                              // 126
                    curr_best_f = f_x2;                                                                                // 127
                    curr_best = x2;                                                                                    // 128
                }                                                                                                      // 129
                if (f_x1 > f_x2) {                                                                                     // 130
                    left = x1;                                                                                         // 131
                    x1 = x2;                                                                                           // 132
                    f_x1 = f_x2;                                                                                       // 133
                    flag = 1;                                                                                          // 134
                }                                                                                                      // 135
                else {                                                                                                 // 136
                    right = x2;                                                                                        // 137
                    x2 = x1;                                                                                           // 138
                    f_x2 = f_x1;                                                                                       // 139
                    flag = 0;                                                                                          // 140
                }                                                                                                      // 141
                if (iterationCounter++ > 100) {                                                                        // 142
                    break;                                                                                             // 143
                }                                                                                                      // 144
            }                                                                                                          // 145
            // plot(data, min_width, get_entire_width(data), curr_best, curr_best_f);                                  // 146
            step(data, curr_best);                                                                                     // 147
        }                                                                                                              // 148
        // one iteration of the optimization method                                                                    // 149
        // (gives a proper, but not necessarily optimal packing)                                                       // 150
        function step(data, max_width) {                                                                               // 151
            line = [];                                                                                                 // 152
            real_width = 0;                                                                                            // 153
            real_height = 0;                                                                                           // 154
            global_bottom = init_y;                                                                                    // 155
            for (var i = 0; i < data.length; i++) {                                                                    // 156
                var o = data[i];                                                                                       // 157
                put_rect(o, max_width);                                                                                // 158
            }                                                                                                          // 159
            return Math.abs(get_real_ratio() - desired_ratio);                                                         // 160
        }                                                                                                              // 161
        // looking for a position to one box                                                                           // 162
        function put_rect(rect, max_width) {                                                                           // 163
            var parent = undefined;                                                                                    // 164
            for (var i = 0; i < line.length; i++) {                                                                    // 165
                if ((line[i].space_left >= rect.height) && (line[i].x + line[i].width + rect.width + packingOptions.PADDING - max_width) <= packingOptions.FLOAT_EPSILON) {
                    parent = line[i];                                                                                  // 167
                    break;                                                                                             // 168
                }                                                                                                      // 169
            }                                                                                                          // 170
            line.push(rect);                                                                                           // 171
            if (parent !== undefined) {                                                                                // 172
                rect.x = parent.x + parent.width + packingOptions.PADDING;                                             // 173
                rect.y = parent.bottom;                                                                                // 174
                rect.space_left = rect.height;                                                                         // 175
                rect.bottom = rect.y;                                                                                  // 176
                parent.space_left -= rect.height + packingOptions.PADDING;                                             // 177
                parent.bottom += rect.height + packingOptions.PADDING;                                                 // 178
            }                                                                                                          // 179
            else {                                                                                                     // 180
                rect.y = global_bottom;                                                                                // 181
                global_bottom += rect.height + packingOptions.PADDING;                                                 // 182
                rect.x = init_x;                                                                                       // 183
                rect.bottom = rect.y;                                                                                  // 184
                rect.space_left = rect.height;                                                                         // 185
            }                                                                                                          // 186
            if (rect.y + rect.height - real_height > -packingOptions.FLOAT_EPSILON)                                    // 187
                real_height = rect.y + rect.height - init_y;                                                           // 188
            if (rect.x + rect.width - real_width > -packingOptions.FLOAT_EPSILON)                                      // 189
                real_width = rect.x + rect.width - init_x;                                                             // 190
        }                                                                                                              // 191
        ;                                                                                                              // 192
        function get_entire_width(data) {                                                                              // 193
            var width = 0;                                                                                             // 194
            data.forEach(function (d) { return width += d.width + packingOptions.PADDING; });                          // 195
            return width;                                                                                              // 196
        }                                                                                                              // 197
        function get_real_ratio() {                                                                                    // 198
            return (real_width / real_height);                                                                         // 199
        }                                                                                                              // 200
    }                                                                                                                  // 201
    cola.applyPacking = applyPacking;                                                                                  // 202
    /**                                                                                                                // 203
     * connected components of graph                                                                                   // 204
     * returns an array of {}                                                                                          // 205
     */                                                                                                                // 206
    function separateGraphs(nodes, links) {                                                                            // 207
        var marks = {};                                                                                                // 208
        var ways = {};                                                                                                 // 209
        var graphs = [];                                                                                               // 210
        var clusters = 0;                                                                                              // 211
        for (var i = 0; i < links.length; i++) {                                                                       // 212
            var link = links[i];                                                                                       // 213
            var n1 = link.source;                                                                                      // 214
            var n2 = link.target;                                                                                      // 215
            if (ways[n1.index])                                                                                        // 216
                ways[n1.index].push(n2);                                                                               // 217
            else                                                                                                       // 218
                ways[n1.index] = [n2];                                                                                 // 219
            if (ways[n2.index])                                                                                        // 220
                ways[n2.index].push(n1);                                                                               // 221
            else                                                                                                       // 222
                ways[n2.index] = [n1];                                                                                 // 223
        }                                                                                                              // 224
        for (var i = 0; i < nodes.length; i++) {                                                                       // 225
            var node = nodes[i];                                                                                       // 226
            if (marks[node.index])                                                                                     // 227
                continue;                                                                                              // 228
            explore_node(node, true);                                                                                  // 229
        }                                                                                                              // 230
        function explore_node(n, is_new) {                                                                             // 231
            if (marks[n.index] !== undefined)                                                                          // 232
                return;                                                                                                // 233
            if (is_new) {                                                                                              // 234
                clusters++;                                                                                            // 235
                graphs.push({ array: [] });                                                                            // 236
            }                                                                                                          // 237
            marks[n.index] = clusters;                                                                                 // 238
            graphs[clusters - 1].array.push(n);                                                                        // 239
            var adjacent = ways[n.index];                                                                              // 240
            if (!adjacent)                                                                                             // 241
                return;                                                                                                // 242
            for (var j = 0; j < adjacent.length; j++) {                                                                // 243
                explore_node(adjacent[j], false);                                                                      // 244
            }                                                                                                          // 245
        }                                                                                                              // 246
        return graphs;                                                                                                 // 247
    }                                                                                                                  // 248
    cola.separateGraphs = separateGraphs;                                                                              // 249
})(cola || (cola = {}));                                                                                               // 250
var cola;                                                                                                              // 251
(function (cola) {                                                                                                     // 252
    var vpsc;                                                                                                          // 253
    (function (vpsc) {                                                                                                 // 254
        var PositionStats = (function () {                                                                             // 255
            function PositionStats(scale) {                                                                            // 256
                this.scale = scale;                                                                                    // 257
                this.AB = 0;                                                                                           // 258
                this.AD = 0;                                                                                           // 259
                this.A2 = 0;                                                                                           // 260
            }                                                                                                          // 261
            PositionStats.prototype.addVariable = function (v) {                                                       // 262
                var ai = this.scale / v.scale;                                                                         // 263
                var bi = v.offset / v.scale;                                                                           // 264
                var wi = v.weight;                                                                                     // 265
                this.AB += wi * ai * bi;                                                                               // 266
                this.AD += wi * ai * v.desiredPosition;                                                                // 267
                this.A2 += wi * ai * ai;                                                                               // 268
            };                                                                                                         // 269
            PositionStats.prototype.getPosn = function () {                                                            // 270
                return (this.AD - this.AB) / this.A2;                                                                  // 271
            };                                                                                                         // 272
            return PositionStats;                                                                                      // 273
        })();                                                                                                          // 274
        vpsc.PositionStats = PositionStats;                                                                            // 275
        var Constraint = (function () {                                                                                // 276
            function Constraint(left, right, gap, equality) {                                                          // 277
                if (equality === void 0) { equality = false; }                                                         // 278
                this.left = left;                                                                                      // 279
                this.right = right;                                                                                    // 280
                this.gap = gap;                                                                                        // 281
                this.equality = equality;                                                                              // 282
                this.active = false;                                                                                   // 283
                this.unsatisfiable = false;                                                                            // 284
                this.left = left;                                                                                      // 285
                this.right = right;                                                                                    // 286
                this.gap = gap;                                                                                        // 287
                this.equality = equality;                                                                              // 288
            }                                                                                                          // 289
            Constraint.prototype.slack = function () {                                                                 // 290
                return this.unsatisfiable ? Number.MAX_VALUE                                                           // 291
                    : this.right.scale * this.right.position() - this.gap                                              // 292
                        - this.left.scale * this.left.position();                                                      // 293
            };                                                                                                         // 294
            return Constraint;                                                                                         // 295
        })();                                                                                                          // 296
        vpsc.Constraint = Constraint;                                                                                  // 297
        var Variable = (function () {                                                                                  // 298
            function Variable(desiredPosition, weight, scale) {                                                        // 299
                if (weight === void 0) { weight = 1; }                                                                 // 300
                if (scale === void 0) { scale = 1; }                                                                   // 301
                this.desiredPosition = desiredPosition;                                                                // 302
                this.weight = weight;                                                                                  // 303
                this.scale = scale;                                                                                    // 304
                this.offset = 0;                                                                                       // 305
            }                                                                                                          // 306
            Variable.prototype.dfdv = function () {                                                                    // 307
                return 2.0 * this.weight * (this.position() - this.desiredPosition);                                   // 308
            };                                                                                                         // 309
            Variable.prototype.position = function () {                                                                // 310
                return (this.block.ps.scale * this.block.posn + this.offset) / this.scale;                             // 311
            };                                                                                                         // 312
            // visit neighbours by active constraints within the same block                                            // 313
            Variable.prototype.visitNeighbours = function (prev, f) {                                                  // 314
                var ff = function (c, next) { return c.active && prev !== next && f(c, next); };                       // 315
                this.cOut.forEach(function (c) { return ff(c, c.right); });                                            // 316
                this.cIn.forEach(function (c) { return ff(c, c.left); });                                              // 317
            };                                                                                                         // 318
            return Variable;                                                                                           // 319
        })();                                                                                                          // 320
        vpsc.Variable = Variable;                                                                                      // 321
        var Block = (function () {                                                                                     // 322
            function Block(v) {                                                                                        // 323
                this.vars = [];                                                                                        // 324
                v.offset = 0;                                                                                          // 325
                this.ps = new PositionStats(v.scale);                                                                  // 326
                this.addVariable(v);                                                                                   // 327
            }                                                                                                          // 328
            Block.prototype.addVariable = function (v) {                                                               // 329
                v.block = this;                                                                                        // 330
                this.vars.push(v);                                                                                     // 331
                this.ps.addVariable(v);                                                                                // 332
                this.posn = this.ps.getPosn();                                                                         // 333
            };                                                                                                         // 334
            // move the block where it needs to be to minimize cost                                                    // 335
            Block.prototype.updateWeightedPosition = function () {                                                     // 336
                this.ps.AB = this.ps.AD = this.ps.A2 = 0;                                                              // 337
                for (var i = 0, n = this.vars.length; i < n; ++i)                                                      // 338
                    this.ps.addVariable(this.vars[i]);                                                                 // 339
                this.posn = this.ps.getPosn();                                                                         // 340
            };                                                                                                         // 341
            Block.prototype.compute_lm = function (v, u, postAction) {                                                 // 342
                var _this = this;                                                                                      // 343
                var dfdv = v.dfdv();                                                                                   // 344
                v.visitNeighbours(u, function (c, next) {                                                              // 345
                    var _dfdv = _this.compute_lm(next, v, postAction);                                                 // 346
                    if (next === c.right) {                                                                            // 347
                        dfdv += _dfdv * c.left.scale;                                                                  // 348
                        c.lm = _dfdv;                                                                                  // 349
                    }                                                                                                  // 350
                    else {                                                                                             // 351
                        dfdv += _dfdv * c.right.scale;                                                                 // 352
                        c.lm = -_dfdv;                                                                                 // 353
                    }                                                                                                  // 354
                    postAction(c);                                                                                     // 355
                });                                                                                                    // 356
                return dfdv / v.scale;                                                                                 // 357
            };                                                                                                         // 358
            Block.prototype.populateSplitBlock = function (v, prev) {                                                  // 359
                var _this = this;                                                                                      // 360
                v.visitNeighbours(prev, function (c, next) {                                                           // 361
                    next.offset = v.offset + (next === c.right ? c.gap : -c.gap);                                      // 362
                    _this.addVariable(next);                                                                           // 363
                    _this.populateSplitBlock(next, v);                                                                 // 364
                });                                                                                                    // 365
            };                                                                                                         // 366
            // traverse the active constraint tree applying visit to each active constraint                            // 367
            Block.prototype.traverse = function (visit, acc, v, prev) {                                                // 368
                var _this = this;                                                                                      // 369
                if (v === void 0) { v = this.vars[0]; }                                                                // 370
                if (prev === void 0) { prev = null; }                                                                  // 371
                v.visitNeighbours(prev, function (c, next) {                                                           // 372
                    acc.push(visit(c));                                                                                // 373
                    _this.traverse(visit, acc, next, v);                                                               // 374
                });                                                                                                    // 375
            };                                                                                                         // 376
            // calculate lagrangian multipliers on constraints and                                                     // 377
            // find the active constraint in this block with the smallest lagrangian.                                  // 378
            // if the lagrangian is negative, then the constraint is a split candidate.                                // 379
            Block.prototype.findMinLM = function () {                                                                  // 380
                var m = null;                                                                                          // 381
                this.compute_lm(this.vars[0], null, function (c) {                                                     // 382
                    if (!c.equality && (m === null || c.lm < m.lm))                                                    // 383
                        m = c;                                                                                         // 384
                });                                                                                                    // 385
                return m;                                                                                              // 386
            };                                                                                                         // 387
            Block.prototype.findMinLMBetween = function (lv, rv) {                                                     // 388
                this.compute_lm(lv, null, function () { });                                                            // 389
                var m = null;                                                                                          // 390
                this.findPath(lv, null, rv, function (c, next) {                                                       // 391
                    if (!c.equality && c.right === next && (m === null || c.lm < m.lm))                                // 392
                        m = c;                                                                                         // 393
                });                                                                                                    // 394
                return m;                                                                                              // 395
            };                                                                                                         // 396
            Block.prototype.findPath = function (v, prev, to, visit) {                                                 // 397
                var _this = this;                                                                                      // 398
                var endFound = false;                                                                                  // 399
                v.visitNeighbours(prev, function (c, next) {                                                           // 400
                    if (!endFound && (next === to || _this.findPath(next, v, to, visit))) {                            // 401
                        endFound = true;                                                                               // 402
                        visit(c, next);                                                                                // 403
                    }                                                                                                  // 404
                });                                                                                                    // 405
                return endFound;                                                                                       // 406
            };                                                                                                         // 407
            // Search active constraint tree from u to see if there is a directed path to v.                           // 408
            // Returns true if path is found.                                                                          // 409
            Block.prototype.isActiveDirectedPathBetween = function (u, v) {                                            // 410
                if (u === v)                                                                                           // 411
                    return true;                                                                                       // 412
                var i = u.cOut.length;                                                                                 // 413
                while (i--) {                                                                                          // 414
                    var c = u.cOut[i];                                                                                 // 415
                    if (c.active && this.isActiveDirectedPathBetween(c.right, v))                                      // 416
                        return true;                                                                                   // 417
                }                                                                                                      // 418
                return false;                                                                                          // 419
            };                                                                                                         // 420
            // split the block into two by deactivating the specified constraint                                       // 421
            Block.split = function (c) {                                                                               // 422
                /* DEBUG                                                                                               // 423
                            console.log("split on " + c);                                                              // 424
                            console.assert(c.active, "attempt to split on inactive constraint");                       // 425
                DEBUG */                                                                                               // 426
                c.active = false;                                                                                      // 427
                return [Block.createSplitBlock(c.left), Block.createSplitBlock(c.right)];                              // 428
            };                                                                                                         // 429
            Block.createSplitBlock = function (startVar) {                                                             // 430
                var b = new Block(startVar);                                                                           // 431
                b.populateSplitBlock(startVar, null);                                                                  // 432
                return b;                                                                                              // 433
            };                                                                                                         // 434
            // find a split point somewhere between the specified variables                                            // 435
            Block.prototype.splitBetween = function (vl, vr) {                                                         // 436
                /* DEBUG                                                                                               // 437
                            console.assert(vl.block === this);                                                         // 438
                            console.assert(vr.block === this);                                                         // 439
                DEBUG */                                                                                               // 440
                var c = this.findMinLMBetween(vl, vr);                                                                 // 441
                if (c !== null) {                                                                                      // 442
                    var bs = Block.split(c);                                                                           // 443
                    return { constraint: c, lb: bs[0], rb: bs[1] };                                                    // 444
                }                                                                                                      // 445
                // couldn't find a split point - for example the active path is all equality constraints               // 446
                return null;                                                                                           // 447
            };                                                                                                         // 448
            Block.prototype.mergeAcross = function (b, c, dist) {                                                      // 449
                c.active = true;                                                                                       // 450
                for (var i = 0, n = b.vars.length; i < n; ++i) {                                                       // 451
                    var v = b.vars[i];                                                                                 // 452
                    v.offset += dist;                                                                                  // 453
                    this.addVariable(v);                                                                               // 454
                }                                                                                                      // 455
                this.posn = this.ps.getPosn();                                                                         // 456
            };                                                                                                         // 457
            Block.prototype.cost = function () {                                                                       // 458
                var sum = 0, i = this.vars.length;                                                                     // 459
                while (i--) {                                                                                          // 460
                    var v = this.vars[i], d = v.position() - v.desiredPosition;                                        // 461
                    sum += d * d * v.weight;                                                                           // 462
                }                                                                                                      // 463
                return sum;                                                                                            // 464
            };                                                                                                         // 465
            return Block;                                                                                              // 466
        })();                                                                                                          // 467
        vpsc.Block = Block;                                                                                            // 468
        var Blocks = (function () {                                                                                    // 469
            function Blocks(vs) {                                                                                      // 470
                this.vs = vs;                                                                                          // 471
                var n = vs.length;                                                                                     // 472
                this.list = new Array(n);                                                                              // 473
                while (n--) {                                                                                          // 474
                    var b = new Block(vs[n]);                                                                          // 475
                    this.list[n] = b;                                                                                  // 476
                    b.blockInd = n;                                                                                    // 477
                }                                                                                                      // 478
            }                                                                                                          // 479
            Blocks.prototype.cost = function () {                                                                      // 480
                var sum = 0, i = this.list.length;                                                                     // 481
                while (i--)                                                                                            // 482
                    sum += this.list[i].cost();                                                                        // 483
                return sum;                                                                                            // 484
            };                                                                                                         // 485
            Blocks.prototype.insert = function (b) {                                                                   // 486
                /* DEBUG                                                                                               // 487
                            console.assert(!this.contains(b), "blocks error: tried to reinsert block " + b.blockInd)   // 488
                DEBUG */                                                                                               // 489
                b.blockInd = this.list.length;                                                                         // 490
                this.list.push(b);                                                                                     // 491
                /* DEBUG                                                                                               // 492
                            console.log("insert block: " + b.blockInd);                                                // 493
                            this.contains(b);                                                                          // 494
                DEBUG */                                                                                               // 495
            };                                                                                                         // 496
            Blocks.prototype.remove = function (b) {                                                                   // 497
                /* DEBUG                                                                                               // 498
                            console.log("remove block: " + b.blockInd);                                                // 499
                            console.assert(this.contains(b));                                                          // 500
                DEBUG */                                                                                               // 501
                var last = this.list.length - 1;                                                                       // 502
                var swapBlock = this.list[last];                                                                       // 503
                this.list.length = last;                                                                               // 504
                if (b !== swapBlock) {                                                                                 // 505
                    this.list[b.blockInd] = swapBlock;                                                                 // 506
                    swapBlock.blockInd = b.blockInd;                                                                   // 507
                }                                                                                                      // 508
            };                                                                                                         // 509
            // merge the blocks on either side of the specified constraint, by copying the smaller block into the larger
            // and deleting the smaller.                                                                               // 511
            Blocks.prototype.merge = function (c) {                                                                    // 512
                var l = c.left.block, r = c.right.block;                                                               // 513
                /* DEBUG                                                                                               // 514
                            console.assert(l!==r, "attempt to merge within the same block");                           // 515
                DEBUG */                                                                                               // 516
                var dist = c.right.offset - c.left.offset - c.gap;                                                     // 517
                if (l.vars.length < r.vars.length) {                                                                   // 518
                    r.mergeAcross(l, c, dist);                                                                         // 519
                    this.remove(l);                                                                                    // 520
                }                                                                                                      // 521
                else {                                                                                                 // 522
                    l.mergeAcross(r, c, -dist);                                                                        // 523
                    this.remove(r);                                                                                    // 524
                }                                                                                                      // 525
                /* DEBUG                                                                                               // 526
                            console.assert(Math.abs(c.slack()) < 1e-6, "Error: Constraint should be at equality after merge!");
                            console.log("merged on " + c);                                                             // 528
                DEBUG */                                                                                               // 529
            };                                                                                                         // 530
            Blocks.prototype.forEach = function (f) {                                                                  // 531
                this.list.forEach(f);                                                                                  // 532
            };                                                                                                         // 533
            // useful, for example, after variable desired positions change.                                           // 534
            Blocks.prototype.updateBlockPositions = function () {                                                      // 535
                this.list.forEach(function (b) { return b.updateWeightedPosition(); });                                // 536
            };                                                                                                         // 537
            // split each block across its constraint with the minimum lagrangian                                      // 538
            Blocks.prototype.split = function (inactive) {                                                             // 539
                var _this = this;                                                                                      // 540
                this.updateBlockPositions();                                                                           // 541
                this.list.forEach(function (b) {                                                                       // 542
                    var v = b.findMinLM();                                                                             // 543
                    if (v !== null && v.lm < Solver.LAGRANGIAN_TOLERANCE) {                                            // 544
                        b = v.left.block;                                                                              // 545
                        Block.split(v).forEach(function (nb) { return _this.insert(nb); });                            // 546
                        _this.remove(b);                                                                               // 547
                        inactive.push(v);                                                                              // 548
                    }                                                                                                  // 549
                });                                                                                                    // 550
            };                                                                                                         // 551
            return Blocks;                                                                                             // 552
        })();                                                                                                          // 553
        vpsc.Blocks = Blocks;                                                                                          // 554
        var Solver = (function () {                                                                                    // 555
            function Solver(vs, cs) {                                                                                  // 556
                this.vs = vs;                                                                                          // 557
                this.cs = cs;                                                                                          // 558
                this.vs = vs;                                                                                          // 559
                vs.forEach(function (v) {                                                                              // 560
                    v.cIn = [], v.cOut = [];                                                                           // 561
                    /* DEBUG                                                                                           // 562
                                    v.toString = () => "v" + vs.indexOf(v);                                            // 563
                    DEBUG */                                                                                           // 564
                });                                                                                                    // 565
                this.cs = cs;                                                                                          // 566
                cs.forEach(function (c) {                                                                              // 567
                    c.left.cOut.push(c);                                                                               // 568
                    c.right.cIn.push(c);                                                                               // 569
                    /* DEBUG                                                                                           // 570
                                    c.toString = () => c.left + "+" + c.gap + "<=" + c.right + " slack=" + c.slack() + " active=" + c.active;
                    DEBUG */                                                                                           // 572
                });                                                                                                    // 573
                this.inactive = cs.map(function (c) { c.active = false; return c; });                                  // 574
                this.bs = null;                                                                                        // 575
            }                                                                                                          // 576
            Solver.prototype.cost = function () {                                                                      // 577
                return this.bs.cost();                                                                                 // 578
            };                                                                                                         // 579
            // set starting positions without changing desired positions.                                              // 580
            // Note: it throws away any previous block structure.                                                      // 581
            Solver.prototype.setStartingPositions = function (ps) {                                                    // 582
                this.inactive = this.cs.map(function (c) { c.active = false; return c; });                             // 583
                this.bs = new Blocks(this.vs);                                                                         // 584
                this.bs.forEach(function (b, i) { return b.posn = ps[i]; });                                           // 585
            };                                                                                                         // 586
            Solver.prototype.setDesiredPositions = function (ps) {                                                     // 587
                this.vs.forEach(function (v, i) { return v.desiredPosition = ps[i]; });                                // 588
            };                                                                                                         // 589
            /* DEBUG                                                                                                   // 590
                    private getId(v: Variable): number {                                                               // 591
                        return this.vs.indexOf(v);                                                                     // 592
                    }                                                                                                  // 593
                                                                                                                       // 594
                    // sanity check of the index integrity of the inactive list                                        // 595
                    checkInactive(): void {                                                                            // 596
                        var inactiveCount = 0;                                                                         // 597
                        this.cs.forEach(c=> {                                                                          // 598
                            var i = this.inactive.indexOf(c);                                                          // 599
                            console.assert(!c.active && i >= 0 || c.active && i < 0, "constraint should be in the inactive list if it is not active: " + c);
                            if (i >= 0) {                                                                              // 601
                                inactiveCount++;                                                                       // 602
                            } else {                                                                                   // 603
                                console.assert(c.active, "inactive constraint not found in inactive list: " + c);      // 604
                            }                                                                                          // 605
                        });                                                                                            // 606
                        console.assert(inactiveCount === this.inactive.length, inactiveCount + " inactive constraints found, " + this.inactive.length + "in inactive list");
                    }                                                                                                  // 608
                    // after every call to satisfy the following should check should pass                              // 609
                    checkSatisfied(): void {                                                                           // 610
                        this.cs.forEach(c=>console.assert(c.slack() >= vpsc.Solver.ZERO_UPPERBOUND, "Error: Unsatisfied constraint! "+c));
                    }                                                                                                  // 612
            DEBUG */                                                                                                   // 613
            Solver.prototype.mostViolated = function () {                                                              // 614
                var minSlack = Number.MAX_VALUE, v = null, l = this.inactive, n = l.length, deletePoint = n;           // 615
                for (var i = 0; i < n; ++i) {                                                                          // 616
                    var c = l[i];                                                                                      // 617
                    if (c.unsatisfiable)                                                                               // 618
                        continue;                                                                                      // 619
                    var slack = c.slack();                                                                             // 620
                    if (c.equality || slack < minSlack) {                                                              // 621
                        minSlack = slack;                                                                              // 622
                        v = c;                                                                                         // 623
                        deletePoint = i;                                                                               // 624
                        if (c.equality)                                                                                // 625
                            break;                                                                                     // 626
                    }                                                                                                  // 627
                }                                                                                                      // 628
                if (deletePoint !== n &&                                                                               // 629
                    (minSlack < Solver.ZERO_UPPERBOUND && !v.active || v.equality)) {                                  // 630
                    l[deletePoint] = l[n - 1];                                                                         // 631
                    l.length = n - 1;                                                                                  // 632
                }                                                                                                      // 633
                return v;                                                                                              // 634
            };                                                                                                         // 635
            // satisfy constraints by building block structure over violated constraints                               // 636
            // and moving the blocks to their desired positions                                                        // 637
            Solver.prototype.satisfy = function () {                                                                   // 638
                if (this.bs == null) {                                                                                 // 639
                    this.bs = new Blocks(this.vs);                                                                     // 640
                }                                                                                                      // 641
                /* DEBUG                                                                                               // 642
                            console.log("satisfy: " + this.bs);                                                        // 643
                DEBUG */                                                                                               // 644
                this.bs.split(this.inactive);                                                                          // 645
                var v = null;                                                                                          // 646
                while ((v = this.mostViolated()) && (v.equality || v.slack() < Solver.ZERO_UPPERBOUND && !v.active)) {
                    var lb = v.left.block, rb = v.right.block;                                                         // 648
                    /* DEBUG                                                                                           // 649
                                    console.log("most violated is: " + v);                                             // 650
                                    this.bs.contains(lb);                                                              // 651
                                    this.bs.contains(rb);                                                              // 652
                    DEBUG */                                                                                           // 653
                    if (lb !== rb) {                                                                                   // 654
                        this.bs.merge(v);                                                                              // 655
                    }                                                                                                  // 656
                    else {                                                                                             // 657
                        if (lb.isActiveDirectedPathBetween(v.right, v.left)) {                                         // 658
                            // cycle found!                                                                            // 659
                            v.unsatisfiable = true;                                                                    // 660
                            continue;                                                                                  // 661
                        }                                                                                              // 662
                        // constraint is within block, need to split first                                             // 663
                        var split = lb.splitBetween(v.left, v.right);                                                  // 664
                        if (split !== null) {                                                                          // 665
                            this.bs.insert(split.lb);                                                                  // 666
                            this.bs.insert(split.rb);                                                                  // 667
                            this.bs.remove(lb);                                                                        // 668
                            this.inactive.push(split.constraint);                                                      // 669
                        }                                                                                              // 670
                        else {                                                                                         // 671
                            /* DEBUG                                                                                   // 672
                                                    console.log("unsatisfiable constraint found");                     // 673
                            DEBUG */                                                                                   // 674
                            v.unsatisfiable = true;                                                                    // 675
                            continue;                                                                                  // 676
                        }                                                                                              // 677
                        if (v.slack() >= 0) {                                                                          // 678
                            /* DEBUG                                                                                   // 679
                                                    console.log("violated constraint indirectly satisfied: " + v);     // 680
                            DEBUG */                                                                                   // 681
                            // v was satisfied by the above split!                                                     // 682
                            this.inactive.push(v);                                                                     // 683
                        }                                                                                              // 684
                        else {                                                                                         // 685
                            /* DEBUG                                                                                   // 686
                                                    console.log("merge after split:");                                 // 687
                            DEBUG */                                                                                   // 688
                            this.bs.merge(v);                                                                          // 689
                        }                                                                                              // 690
                    }                                                                                                  // 691
                }                                                                                                      // 692
                /* DEBUG                                                                                               // 693
                            this.checkSatisfied();                                                                     // 694
                DEBUG */                                                                                               // 695
            };                                                                                                         // 696
            // repeatedly build and split block structure until we converge to an optimal solution                     // 697
            Solver.prototype.solve = function () {                                                                     // 698
                this.satisfy();                                                                                        // 699
                var lastcost = Number.MAX_VALUE, cost = this.bs.cost();                                                // 700
                while (Math.abs(lastcost - cost) > 0.0001) {                                                           // 701
                    this.satisfy();                                                                                    // 702
                    lastcost = cost;                                                                                   // 703
                    cost = this.bs.cost();                                                                             // 704
                }                                                                                                      // 705
                return cost;                                                                                           // 706
            };                                                                                                         // 707
            Solver.LAGRANGIAN_TOLERANCE = -1e-4;                                                                       // 708
            Solver.ZERO_UPPERBOUND = -1e-10;                                                                           // 709
            return Solver;                                                                                             // 710
        })();                                                                                                          // 711
        vpsc.Solver = Solver;                                                                                          // 712
    })(vpsc = cola.vpsc || (cola.vpsc = {}));                                                                          // 713
})(cola || (cola = {}));                                                                                               // 714
var __extends = (this && this.__extends) || function (d, b) {                                                          // 715
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];                                                             // 716
    function __() { this.constructor = d; }                                                                            // 717
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());                              // 718
};                                                                                                                     // 719
var cola;                                                                                                              // 720
(function (cola) {                                                                                                     // 721
    var vpsc;                                                                                                          // 722
    (function (vpsc) {                                                                                                 // 723
        //Based on js_es:                                                                                              // 724
        //                                                                                                             // 725
        //https://github.com/vadimg/js_bintrees                                                                        // 726
        //                                                                                                             // 727
        //Copyright (C) 2011 by Vadim Graboys                                                                          // 728
        //                                                                                                             // 729
        //Permission is hereby granted, free of charge, to any person obtaining a copy                                 // 730
        //of this software and associated documentation files (the "Software"), to deal                                // 731
        //in the Software without restriction, including without limitation the rights                                 // 732
        //to use, copy, modify, merge, publish, distribute, sublicense, and/or sell                                    // 733
        //copies of the Software, and to permit persons to whom the Software is                                        // 734
        //furnished to do so, subject to the following conditions:                                                     // 735
        //                                                                                                             // 736
        //The above copyright notice and this permission notice shall be included in                                   // 737
        //all copies or substantial portions of the Software.                                                          // 738
        //                                                                                                             // 739
        //THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR                                   // 740
        //IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                                     // 741
        //FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE                                  // 742
        //AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                                       // 743
        //LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,                                // 744
        //OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN                                    // 745
        //THE SOFTWARE.                                                                                                // 746
        var TreeBase = (function () {                                                                                  // 747
            function TreeBase() {                                                                                      // 748
                // returns iterator to node if found, null otherwise                                                   // 749
                this.findIter = function (data) {                                                                      // 750
                    var res = this._root;                                                                              // 751
                    var iter = this.iterator();                                                                        // 752
                    while (res !== null) {                                                                             // 753
                        var c = this._comparator(data, res.data);                                                      // 754
                        if (c === 0) {                                                                                 // 755
                            iter._cursor = res;                                                                        // 756
                            return iter;                                                                               // 757
                        }                                                                                              // 758
                        else {                                                                                         // 759
                            iter._ancestors.push(res);                                                                 // 760
                            res = res.get_child(c > 0);                                                                // 761
                        }                                                                                              // 762
                    }                                                                                                  // 763
                    return null;                                                                                       // 764
                };                                                                                                     // 765
            }                                                                                                          // 766
            // removes all nodes from the tree                                                                         // 767
            TreeBase.prototype.clear = function () {                                                                   // 768
                this._root = null;                                                                                     // 769
                this.size = 0;                                                                                         // 770
            };                                                                                                         // 771
            ;                                                                                                          // 772
            // returns node data if found, null otherwise                                                              // 773
            TreeBase.prototype.find = function (data) {                                                                // 774
                var res = this._root;                                                                                  // 775
                while (res !== null) {                                                                                 // 776
                    var c = this._comparator(data, res.data);                                                          // 777
                    if (c === 0) {                                                                                     // 778
                        return res.data;                                                                               // 779
                    }                                                                                                  // 780
                    else {                                                                                             // 781
                        res = res.get_child(c > 0);                                                                    // 782
                    }                                                                                                  // 783
                }                                                                                                      // 784
                return null;                                                                                           // 785
            };                                                                                                         // 786
            ;                                                                                                          // 787
            // Returns an interator to the tree node immediately before (or at) the element                            // 788
            TreeBase.prototype.lowerBound = function (data) {                                                          // 789
                return this._bound(data, this._comparator);                                                            // 790
            };                                                                                                         // 791
            ;                                                                                                          // 792
            // Returns an interator to the tree node immediately after (or at) the element                             // 793
            TreeBase.prototype.upperBound = function (data) {                                                          // 794
                var cmp = this._comparator;                                                                            // 795
                function reverse_cmp(a, b) {                                                                           // 796
                    return cmp(b, a);                                                                                  // 797
                }                                                                                                      // 798
                return this._bound(data, reverse_cmp);                                                                 // 799
            };                                                                                                         // 800
            ;                                                                                                          // 801
            // returns null if tree is empty                                                                           // 802
            TreeBase.prototype.min = function () {                                                                     // 803
                var res = this._root;                                                                                  // 804
                if (res === null) {                                                                                    // 805
                    return null;                                                                                       // 806
                }                                                                                                      // 807
                while (res.left !== null) {                                                                            // 808
                    res = res.left;                                                                                    // 809
                }                                                                                                      // 810
                return res.data;                                                                                       // 811
            };                                                                                                         // 812
            ;                                                                                                          // 813
            // returns null if tree is empty                                                                           // 814
            TreeBase.prototype.max = function () {                                                                     // 815
                var res = this._root;                                                                                  // 816
                if (res === null) {                                                                                    // 817
                    return null;                                                                                       // 818
                }                                                                                                      // 819
                while (res.right !== null) {                                                                           // 820
                    res = res.right;                                                                                   // 821
                }                                                                                                      // 822
                return res.data;                                                                                       // 823
            };                                                                                                         // 824
            ;                                                                                                          // 825
            // returns a null iterator                                                                                 // 826
            // call next() or prev() to point to an element                                                            // 827
            TreeBase.prototype.iterator = function () {                                                                // 828
                return new Iterator(this);                                                                             // 829
            };                                                                                                         // 830
            ;                                                                                                          // 831
            // calls cb on each node's data, in order                                                                  // 832
            TreeBase.prototype.each = function (cb) {                                                                  // 833
                var it = this.iterator(), data;                                                                        // 834
                while ((data = it.next()) !== null) {                                                                  // 835
                    cb(data);                                                                                          // 836
                }                                                                                                      // 837
            };                                                                                                         // 838
            ;                                                                                                          // 839
            // calls cb on each node's data, in reverse order                                                          // 840
            TreeBase.prototype.reach = function (cb) {                                                                 // 841
                var it = this.iterator(), data;                                                                        // 842
                while ((data = it.prev()) !== null) {                                                                  // 843
                    cb(data);                                                                                          // 844
                }                                                                                                      // 845
            };                                                                                                         // 846
            ;                                                                                                          // 847
            // used for lowerBound and upperBound                                                                      // 848
            TreeBase.prototype._bound = function (data, cmp) {                                                         // 849
                var cur = this._root;                                                                                  // 850
                var iter = this.iterator();                                                                            // 851
                while (cur !== null) {                                                                                 // 852
                    var c = this._comparator(data, cur.data);                                                          // 853
                    if (c === 0) {                                                                                     // 854
                        iter._cursor = cur;                                                                            // 855
                        return iter;                                                                                   // 856
                    }                                                                                                  // 857
                    iter._ancestors.push(cur);                                                                         // 858
                    cur = cur.get_child(c > 0);                                                                        // 859
                }                                                                                                      // 860
                for (var i = iter._ancestors.length - 1; i >= 0; --i) {                                                // 861
                    cur = iter._ancestors[i];                                                                          // 862
                    if (cmp(data, cur.data) > 0) {                                                                     // 863
                        iter._cursor = cur;                                                                            // 864
                        iter._ancestors.length = i;                                                                    // 865
                        return iter;                                                                                   // 866
                    }                                                                                                  // 867
                }                                                                                                      // 868
                iter._ancestors.length = 0;                                                                            // 869
                return iter;                                                                                           // 870
            };                                                                                                         // 871
            ;                                                                                                          // 872
            return TreeBase;                                                                                           // 873
        })();                                                                                                          // 874
        vpsc.TreeBase = TreeBase;                                                                                      // 875
        var Iterator = (function () {                                                                                  // 876
            function Iterator(tree) {                                                                                  // 877
                this._tree = tree;                                                                                     // 878
                this._ancestors = [];                                                                                  // 879
                this._cursor = null;                                                                                   // 880
            }                                                                                                          // 881
            Iterator.prototype.data = function () {                                                                    // 882
                return this._cursor !== null ? this._cursor.data : null;                                               // 883
            };                                                                                                         // 884
            ;                                                                                                          // 885
            // if null-iterator, returns first node                                                                    // 886
            // otherwise, returns next node                                                                            // 887
            Iterator.prototype.next = function () {                                                                    // 888
                if (this._cursor === null) {                                                                           // 889
                    var root = this._tree._root;                                                                       // 890
                    if (root !== null) {                                                                               // 891
                        this._minNode(root);                                                                           // 892
                    }                                                                                                  // 893
                }                                                                                                      // 894
                else {                                                                                                 // 895
                    if (this._cursor.right === null) {                                                                 // 896
                        // no greater node in subtree, go up to parent                                                 // 897
                        // if coming from a right child, continue up the stack                                         // 898
                        var save;                                                                                      // 899
                        do {                                                                                           // 900
                            save = this._cursor;                                                                       // 901
                            if (this._ancestors.length) {                                                              // 902
                                this._cursor = this._ancestors.pop();                                                  // 903
                            }                                                                                          // 904
                            else {                                                                                     // 905
                                this._cursor = null;                                                                   // 906
                                break;                                                                                 // 907
                            }                                                                                          // 908
                        } while (this._cursor.right === save);                                                         // 909
                    }                                                                                                  // 910
                    else {                                                                                             // 911
                        // get the next node from the subtree                                                          // 912
                        this._ancestors.push(this._cursor);                                                            // 913
                        this._minNode(this._cursor.right);                                                             // 914
                    }                                                                                                  // 915
                }                                                                                                      // 916
                return this._cursor !== null ? this._cursor.data : null;                                               // 917
            };                                                                                                         // 918
            ;                                                                                                          // 919
            // if null-iterator, returns last node                                                                     // 920
            // otherwise, returns previous node                                                                        // 921
            Iterator.prototype.prev = function () {                                                                    // 922
                if (this._cursor === null) {                                                                           // 923
                    var root = this._tree._root;                                                                       // 924
                    if (root !== null) {                                                                               // 925
                        this._maxNode(root);                                                                           // 926
                    }                                                                                                  // 927
                }                                                                                                      // 928
                else {                                                                                                 // 929
                    if (this._cursor.left === null) {                                                                  // 930
                        var save;                                                                                      // 931
                        do {                                                                                           // 932
                            save = this._cursor;                                                                       // 933
                            if (this._ancestors.length) {                                                              // 934
                                this._cursor = this._ancestors.pop();                                                  // 935
                            }                                                                                          // 936
                            else {                                                                                     // 937
                                this._cursor = null;                                                                   // 938
                                break;                                                                                 // 939
                            }                                                                                          // 940
                        } while (this._cursor.left === save);                                                          // 941
                    }                                                                                                  // 942
                    else {                                                                                             // 943
                        this._ancestors.push(this._cursor);                                                            // 944
                        this._maxNode(this._cursor.left);                                                              // 945
                    }                                                                                                  // 946
                }                                                                                                      // 947
                return this._cursor !== null ? this._cursor.data : null;                                               // 948
            };                                                                                                         // 949
            ;                                                                                                          // 950
            Iterator.prototype._minNode = function (start) {                                                           // 951
                while (start.left !== null) {                                                                          // 952
                    this._ancestors.push(start);                                                                       // 953
                    start = start.left;                                                                                // 954
                }                                                                                                      // 955
                this._cursor = start;                                                                                  // 956
            };                                                                                                         // 957
            ;                                                                                                          // 958
            Iterator.prototype._maxNode = function (start) {                                                           // 959
                while (start.right !== null) {                                                                         // 960
                    this._ancestors.push(start);                                                                       // 961
                    start = start.right;                                                                               // 962
                }                                                                                                      // 963
                this._cursor = start;                                                                                  // 964
            };                                                                                                         // 965
            ;                                                                                                          // 966
            return Iterator;                                                                                           // 967
        })();                                                                                                          // 968
        vpsc.Iterator = Iterator;                                                                                      // 969
        var Node = (function () {                                                                                      // 970
            function Node(data) {                                                                                      // 971
                this.data = data;                                                                                      // 972
                this.left = null;                                                                                      // 973
                this.right = null;                                                                                     // 974
                this.red = true;                                                                                       // 975
            }                                                                                                          // 976
            Node.prototype.get_child = function (dir) {                                                                // 977
                return dir ? this.right : this.left;                                                                   // 978
            };                                                                                                         // 979
            ;                                                                                                          // 980
            Node.prototype.set_child = function (dir, val) {                                                           // 981
                if (dir) {                                                                                             // 982
                    this.right = val;                                                                                  // 983
                }                                                                                                      // 984
                else {                                                                                                 // 985
                    this.left = val;                                                                                   // 986
                }                                                                                                      // 987
            };                                                                                                         // 988
            ;                                                                                                          // 989
            return Node;                                                                                               // 990
        })();                                                                                                          // 991
        var RBTree = (function (_super) {                                                                              // 992
            __extends(RBTree, _super);                                                                                 // 993
            function RBTree(comparator) {                                                                              // 994
                _super.call(this);                                                                                     // 995
                this._root = null;                                                                                     // 996
                this._comparator = comparator;                                                                         // 997
                this.size = 0;                                                                                         // 998
            }                                                                                                          // 999
            // returns true if inserted, false if duplicate                                                            // 1000
            RBTree.prototype.insert = function (data) {                                                                // 1001
                var ret = false;                                                                                       // 1002
                if (this._root === null) {                                                                             // 1003
                    // empty tree                                                                                      // 1004
                    this._root = new Node(data);                                                                       // 1005
                    ret = true;                                                                                        // 1006
                    this.size++;                                                                                       // 1007
                }                                                                                                      // 1008
                else {                                                                                                 // 1009
                    var head = new Node(undefined); // fake tree root                                                  // 1010
                    var dir = false;                                                                                   // 1011
                    var last = false;                                                                                  // 1012
                    // setup                                                                                           // 1013
                    var gp = null; // grandparent                                                                      // 1014
                    var ggp = head; // grand-grand-parent                                                              // 1015
                    var p = null; // parent                                                                            // 1016
                    var node = this._root;                                                                             // 1017
                    ggp.right = this._root;                                                                            // 1018
                    // search down                                                                                     // 1019
                    while (true) {                                                                                     // 1020
                        if (node === null) {                                                                           // 1021
                            // insert new node at the bottom                                                           // 1022
                            node = new Node(data);                                                                     // 1023
                            p.set_child(dir, node);                                                                    // 1024
                            ret = true;                                                                                // 1025
                            this.size++;                                                                               // 1026
                        }                                                                                              // 1027
                        else if (RBTree.is_red(node.left) && RBTree.is_red(node.right)) {                              // 1028
                            // color flip                                                                              // 1029
                            node.red = true;                                                                           // 1030
                            node.left.red = false;                                                                     // 1031
                            node.right.red = false;                                                                    // 1032
                        }                                                                                              // 1033
                        // fix red violation                                                                           // 1034
                        if (RBTree.is_red(node) && RBTree.is_red(p)) {                                                 // 1035
                            var dir2 = ggp.right === gp;                                                               // 1036
                            if (node === p.get_child(last)) {                                                          // 1037
                                ggp.set_child(dir2, RBTree.single_rotate(gp, !last));                                  // 1038
                            }                                                                                          // 1039
                            else {                                                                                     // 1040
                                ggp.set_child(dir2, RBTree.double_rotate(gp, !last));                                  // 1041
                            }                                                                                          // 1042
                        }                                                                                              // 1043
                        var cmp = this._comparator(node.data, data);                                                   // 1044
                        // stop if found                                                                               // 1045
                        if (cmp === 0) {                                                                               // 1046
                            break;                                                                                     // 1047
                        }                                                                                              // 1048
                        last = dir;                                                                                    // 1049
                        dir = cmp < 0;                                                                                 // 1050
                        // update helpers                                                                              // 1051
                        if (gp !== null) {                                                                             // 1052
                            ggp = gp;                                                                                  // 1053
                        }                                                                                              // 1054
                        gp = p;                                                                                        // 1055
                        p = node;                                                                                      // 1056
                        node = node.get_child(dir);                                                                    // 1057
                    }                                                                                                  // 1058
                    // update root                                                                                     // 1059
                    this._root = head.right;                                                                           // 1060
                }                                                                                                      // 1061
                // make root black                                                                                     // 1062
                this._root.red = false;                                                                                // 1063
                return ret;                                                                                            // 1064
            };                                                                                                         // 1065
            ;                                                                                                          // 1066
            // returns true if removed, false if not found                                                             // 1067
            RBTree.prototype.remove = function (data) {                                                                // 1068
                if (this._root === null) {                                                                             // 1069
                    return false;                                                                                      // 1070
                }                                                                                                      // 1071
                var head = new Node(undefined); // fake tree root                                                      // 1072
                var node = head;                                                                                       // 1073
                node.right = this._root;                                                                               // 1074
                var p = null; // parent                                                                                // 1075
                var gp = null; // grand parent                                                                         // 1076
                var found = null; // found item                                                                        // 1077
                var dir = true;                                                                                        // 1078
                while (node.get_child(dir) !== null) {                                                                 // 1079
                    var last = dir;                                                                                    // 1080
                    // update helpers                                                                                  // 1081
                    gp = p;                                                                                            // 1082
                    p = node;                                                                                          // 1083
                    node = node.get_child(dir);                                                                        // 1084
                    var cmp = this._comparator(data, node.data);                                                       // 1085
                    dir = cmp > 0;                                                                                     // 1086
                    // save found node                                                                                 // 1087
                    if (cmp === 0) {                                                                                   // 1088
                        found = node;                                                                                  // 1089
                    }                                                                                                  // 1090
                    // push the red node down                                                                          // 1091
                    if (!RBTree.is_red(node) && !RBTree.is_red(node.get_child(dir))) {                                 // 1092
                        if (RBTree.is_red(node.get_child(!dir))) {                                                     // 1093
                            var sr = RBTree.single_rotate(node, dir);                                                  // 1094
                            p.set_child(last, sr);                                                                     // 1095
                            p = sr;                                                                                    // 1096
                        }                                                                                              // 1097
                        else if (!RBTree.is_red(node.get_child(!dir))) {                                               // 1098
                            var sibling = p.get_child(!last);                                                          // 1099
                            if (sibling !== null) {                                                                    // 1100
                                if (!RBTree.is_red(sibling.get_child(!last)) && !RBTree.is_red(sibling.get_child(last))) {
                                    // color flip                                                                      // 1102
                                    p.red = false;                                                                     // 1103
                                    sibling.red = true;                                                                // 1104
                                    node.red = true;                                                                   // 1105
                                }                                                                                      // 1106
                                else {                                                                                 // 1107
                                    var dir2 = gp.right === p;                                                         // 1108
                                    if (RBTree.is_red(sibling.get_child(last))) {                                      // 1109
                                        gp.set_child(dir2, RBTree.double_rotate(p, last));                             // 1110
                                    }                                                                                  // 1111
                                    else if (RBTree.is_red(sibling.get_child(!last))) {                                // 1112
                                        gp.set_child(dir2, RBTree.single_rotate(p, last));                             // 1113
                                    }                                                                                  // 1114
                                    // ensure correct coloring                                                         // 1115
                                    var gpc = gp.get_child(dir2);                                                      // 1116
                                    gpc.red = true;                                                                    // 1117
                                    node.red = true;                                                                   // 1118
                                    gpc.left.red = false;                                                              // 1119
                                    gpc.right.red = false;                                                             // 1120
                                }                                                                                      // 1121
                            }                                                                                          // 1122
                        }                                                                                              // 1123
                    }                                                                                                  // 1124
                }                                                                                                      // 1125
                // replace and remove if found                                                                         // 1126
                if (found !== null) {                                                                                  // 1127
                    found.data = node.data;                                                                            // 1128
                    p.set_child(p.right === node, node.get_child(node.left === null));                                 // 1129
                    this.size--;                                                                                       // 1130
                }                                                                                                      // 1131
                // update root and make it black                                                                       // 1132
                this._root = head.right;                                                                               // 1133
                if (this._root !== null) {                                                                             // 1134
                    this._root.red = false;                                                                            // 1135
                }                                                                                                      // 1136
                return found !== null;                                                                                 // 1137
            };                                                                                                         // 1138
            ;                                                                                                          // 1139
            RBTree.is_red = function (node) {                                                                          // 1140
                return node !== null && node.red;                                                                      // 1141
            };                                                                                                         // 1142
            RBTree.single_rotate = function (root, dir) {                                                              // 1143
                var save = root.get_child(!dir);                                                                       // 1144
                root.set_child(!dir, save.get_child(dir));                                                             // 1145
                save.set_child(dir, root);                                                                             // 1146
                root.red = true;                                                                                       // 1147
                save.red = false;                                                                                      // 1148
                return save;                                                                                           // 1149
            };                                                                                                         // 1150
            RBTree.double_rotate = function (root, dir) {                                                              // 1151
                root.set_child(!dir, RBTree.single_rotate(root.get_child(!dir), !dir));                                // 1152
                return RBTree.single_rotate(root, dir);                                                                // 1153
            };                                                                                                         // 1154
            return RBTree;                                                                                             // 1155
        })(TreeBase);                                                                                                  // 1156
        vpsc.RBTree = RBTree;                                                                                          // 1157
    })(vpsc = cola.vpsc || (cola.vpsc = {}));                                                                          // 1158
})(cola || (cola = {}));                                                                                               // 1159
///<reference path="vpsc.ts"/>                                                                                         // 1160
///<reference path="rbtree.ts"/>                                                                                       // 1161
var cola;                                                                                                              // 1162
(function (cola) {                                                                                                     // 1163
    var vpsc;                                                                                                          // 1164
    (function (vpsc) {                                                                                                 // 1165
        function computeGroupBounds(g) {                                                                               // 1166
            g.bounds = typeof g.leaves !== "undefined" ?                                                               // 1167
                g.leaves.reduce(function (r, c) { return c.bounds.union(r); }, Rectangle.empty()) :                    // 1168
                Rectangle.empty();                                                                                     // 1169
            if (typeof g.groups !== "undefined")                                                                       // 1170
                g.bounds = g.groups.reduce(function (r, c) { return computeGroupBounds(c).union(r); }, g.bounds);      // 1171
            g.bounds = g.bounds.inflate(g.padding);                                                                    // 1172
            return g.bounds;                                                                                           // 1173
        }                                                                                                              // 1174
        vpsc.computeGroupBounds = computeGroupBounds;                                                                  // 1175
        var Rectangle = (function () {                                                                                 // 1176
            function Rectangle(x, X, y, Y) {                                                                           // 1177
                this.x = x;                                                                                            // 1178
                this.X = X;                                                                                            // 1179
                this.y = y;                                                                                            // 1180
                this.Y = Y;                                                                                            // 1181
            }                                                                                                          // 1182
            Rectangle.empty = function () { return new Rectangle(Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY); };
            Rectangle.prototype.cx = function () { return (this.x + this.X) / 2; };                                    // 1184
            Rectangle.prototype.cy = function () { return (this.y + this.Y) / 2; };                                    // 1185
            Rectangle.prototype.overlapX = function (r) {                                                              // 1186
                var ux = this.cx(), vx = r.cx();                                                                       // 1187
                if (ux <= vx && r.x < this.X)                                                                          // 1188
                    return this.X - r.x;                                                                               // 1189
                if (vx <= ux && this.x < r.X)                                                                          // 1190
                    return r.X - this.x;                                                                               // 1191
                return 0;                                                                                              // 1192
            };                                                                                                         // 1193
            Rectangle.prototype.overlapY = function (r) {                                                              // 1194
                var uy = this.cy(), vy = r.cy();                                                                       // 1195
                if (uy <= vy && r.y < this.Y)                                                                          // 1196
                    return this.Y - r.y;                                                                               // 1197
                if (vy <= uy && this.y < r.Y)                                                                          // 1198
                    return r.Y - this.y;                                                                               // 1199
                return 0;                                                                                              // 1200
            };                                                                                                         // 1201
            Rectangle.prototype.setXCentre = function (cx) {                                                           // 1202
                var dx = cx - this.cx();                                                                               // 1203
                this.x += dx;                                                                                          // 1204
                this.X += dx;                                                                                          // 1205
            };                                                                                                         // 1206
            Rectangle.prototype.setYCentre = function (cy) {                                                           // 1207
                var dy = cy - this.cy();                                                                               // 1208
                this.y += dy;                                                                                          // 1209
                this.Y += dy;                                                                                          // 1210
            };                                                                                                         // 1211
            Rectangle.prototype.width = function () {                                                                  // 1212
                return this.X - this.x;                                                                                // 1213
            };                                                                                                         // 1214
            Rectangle.prototype.height = function () {                                                                 // 1215
                return this.Y - this.y;                                                                                // 1216
            };                                                                                                         // 1217
            Rectangle.prototype.union = function (r) {                                                                 // 1218
                return new Rectangle(Math.min(this.x, r.x), Math.max(this.X, r.X), Math.min(this.y, r.y), Math.max(this.Y, r.Y));
            };                                                                                                         // 1220
            /**                                                                                                        // 1221
             * return any intersection points between the given line and the sides of this rectangle                   // 1222
             * @method lineIntersection                                                                                // 1223
             * @param x1 number first x coord of line                                                                  // 1224
             * @param y1 number first y coord of line                                                                  // 1225
             * @param x2 number second x coord of line                                                                 // 1226
             * @param y2 number second y coord of line                                                                 // 1227
             * @return any intersection points found                                                                   // 1228
             */                                                                                                        // 1229
            Rectangle.prototype.lineIntersections = function (x1, y1, x2, y2) {                                        // 1230
                var sides = [[this.x, this.y, this.X, this.y],                                                         // 1231
                    [this.X, this.y, this.X, this.Y],                                                                  // 1232
                    [this.X, this.Y, this.x, this.Y],                                                                  // 1233
                    [this.x, this.Y, this.x, this.y]];                                                                 // 1234
                var intersections = [];                                                                                // 1235
                for (var i = 0; i < 4; ++i) {                                                                          // 1236
                    var r = Rectangle.lineIntersection(x1, y1, x2, y2, sides[i][0], sides[i][1], sides[i][2], sides[i][3]);
                    if (r !== null)                                                                                    // 1238
                        intersections.push({ x: r.x, y: r.y });                                                        // 1239
                }                                                                                                      // 1240
                return intersections;                                                                                  // 1241
            };                                                                                                         // 1242
            /**                                                                                                        // 1243
             * return any intersection points between a line extending from the centre of this rectangle to the given point,
             *  and the sides of this rectangle                                                                        // 1245
             * @method lineIntersection                                                                                // 1246
             * @param x2 number second x coord of line                                                                 // 1247
             * @param y2 number second y coord of line                                                                 // 1248
             * @return any intersection points found                                                                   // 1249
             */                                                                                                        // 1250
            Rectangle.prototype.rayIntersection = function (x2, y2) {                                                  // 1251
                var ints = this.lineIntersections(this.cx(), this.cy(), x2, y2);                                       // 1252
                return ints.length > 0 ? ints[0] : null;                                                               // 1253
            };                                                                                                         // 1254
            Rectangle.prototype.vertices = function () {                                                               // 1255
                return [                                                                                               // 1256
                    { x: this.x, y: this.y },                                                                          // 1257
                    { x: this.X, y: this.y },                                                                          // 1258
                    { x: this.X, y: this.Y },                                                                          // 1259
                    { x: this.x, y: this.Y },                                                                          // 1260
                    { x: this.x, y: this.y }];                                                                         // 1261
            };                                                                                                         // 1262
            Rectangle.lineIntersection = function (x1, y1, x2, y2, x3, y3, x4, y4) {                                   // 1263
                var dx12 = x2 - x1, dx34 = x4 - x3, dy12 = y2 - y1, dy34 = y4 - y3, denominator = dy34 * dx12 - dx34 * dy12;
                if (denominator == 0)                                                                                  // 1265
                    return null;                                                                                       // 1266
                var dx31 = x1 - x3, dy31 = y1 - y3, numa = dx34 * dy31 - dy34 * dx31, a = numa / denominator, numb = dx12 * dy31 - dy12 * dx31, b = numb / denominator;
                if (a >= 0 && a <= 1 && b >= 0 && b <= 1) {                                                            // 1268
                    return {                                                                                           // 1269
                        x: x1 + a * dx12,                                                                              // 1270
                        y: y1 + a * dy12                                                                               // 1271
                    };                                                                                                 // 1272
                }                                                                                                      // 1273
                return null;                                                                                           // 1274
            };                                                                                                         // 1275
            Rectangle.prototype.inflate = function (pad) {                                                             // 1276
                return new Rectangle(this.x - pad, this.X + pad, this.y - pad, this.Y + pad);                          // 1277
            };                                                                                                         // 1278
            return Rectangle;                                                                                          // 1279
        })();                                                                                                          // 1280
        vpsc.Rectangle = Rectangle;                                                                                    // 1281
        function makeEdgeBetween(source, target, ah) {                                                                 // 1282
            var si = source.rayIntersection(target.cx(), target.cy()) || { x: source.cx(), y: source.cy() }, ti = target.rayIntersection(source.cx(), source.cy()) || { x: target.cx(), y: target.cy() }, dx = ti.x - si.x, dy = ti.y - si.y, l = Math.sqrt(dx * dx + dy * dy), al = l - ah;
            return {                                                                                                   // 1284
                sourceIntersection: si,                                                                                // 1285
                targetIntersection: ti,                                                                                // 1286
                arrowStart: { x: si.x + al * dx / l, y: si.y + al * dy / l }                                           // 1287
            };                                                                                                         // 1288
        }                                                                                                              // 1289
        vpsc.makeEdgeBetween = makeEdgeBetween;                                                                        // 1290
        function makeEdgeTo(s, target, ah) {                                                                           // 1291
            var ti = target.rayIntersection(s.x, s.y);                                                                 // 1292
            if (!ti)                                                                                                   // 1293
                ti = { x: target.cx(), y: target.cy() };                                                               // 1294
            var dx = ti.x - s.x, dy = ti.y - s.y, l = Math.sqrt(dx * dx + dy * dy);                                    // 1295
            return { x: ti.x - ah * dx / l, y: ti.y - ah * dy / l };                                                   // 1296
        }                                                                                                              // 1297
        vpsc.makeEdgeTo = makeEdgeTo;                                                                                  // 1298
        var Node = (function () {                                                                                      // 1299
            function Node(v, r, pos) {                                                                                 // 1300
                this.v = v;                                                                                            // 1301
                this.r = r;                                                                                            // 1302
                this.pos = pos;                                                                                        // 1303
                this.prev = makeRBTree();                                                                              // 1304
                this.next = makeRBTree();                                                                              // 1305
            }                                                                                                          // 1306
            return Node;                                                                                               // 1307
        })();                                                                                                          // 1308
        var Event = (function () {                                                                                     // 1309
            function Event(isOpen, v, pos) {                                                                           // 1310
                this.isOpen = isOpen;                                                                                  // 1311
                this.v = v;                                                                                            // 1312
                this.pos = pos;                                                                                        // 1313
            }                                                                                                          // 1314
            return Event;                                                                                              // 1315
        })();                                                                                                          // 1316
        function compareEvents(a, b) {                                                                                 // 1317
            if (a.pos > b.pos) {                                                                                       // 1318
                return 1;                                                                                              // 1319
            }                                                                                                          // 1320
            if (a.pos < b.pos) {                                                                                       // 1321
                return -1;                                                                                             // 1322
            }                                                                                                          // 1323
            if (a.isOpen) {                                                                                            // 1324
                // open must come before close                                                                         // 1325
                return -1;                                                                                             // 1326
            }                                                                                                          // 1327
            if (b.isOpen) {                                                                                            // 1328
                // open must come before close                                                                         // 1329
                return 1;                                                                                              // 1330
            }                                                                                                          // 1331
            return 0;                                                                                                  // 1332
        }                                                                                                              // 1333
        function makeRBTree() {                                                                                        // 1334
            return new vpsc.RBTree(function (a, b) { return a.pos - b.pos; });                                         // 1335
        }                                                                                                              // 1336
        var xRect = {                                                                                                  // 1337
            getCentre: function (r) { return r.cx(); },                                                                // 1338
            getOpen: function (r) { return r.y; },                                                                     // 1339
            getClose: function (r) { return r.Y; },                                                                    // 1340
            getSize: function (r) { return r.width(); },                                                               // 1341
            makeRect: function (open, close, center, size) { return new Rectangle(center - size / 2, center + size / 2, open, close); },
            findNeighbours: findXNeighbours                                                                            // 1343
        };                                                                                                             // 1344
        var yRect = {                                                                                                  // 1345
            getCentre: function (r) { return r.cy(); },                                                                // 1346
            getOpen: function (r) { return r.x; },                                                                     // 1347
            getClose: function (r) { return r.X; },                                                                    // 1348
            getSize: function (r) { return r.height(); },                                                              // 1349
            makeRect: function (open, close, center, size) { return new Rectangle(open, close, center - size / 2, center + size / 2); },
            findNeighbours: findYNeighbours                                                                            // 1351
        };                                                                                                             // 1352
        function generateGroupConstraints(root, f, minSep, isContained) {                                              // 1353
            if (isContained === void 0) { isContained = false; }                                                       // 1354
            var padding = root.padding, gn = typeof root.groups !== 'undefined' ? root.groups.length : 0, ln = typeof root.leaves !== 'undefined' ? root.leaves.length : 0, childConstraints = !gn ? []
                : root.groups.reduce(function (ccs, g) { return ccs.concat(generateGroupConstraints(g, f, minSep, true)); }, []), n = (isContained ? 2 : 0) + ln + gn, vs = new Array(n), rs = new Array(n), i = 0, add = function (r, v) { rs[i] = r; vs[i++] = v; };
            if (isContained) {                                                                                         // 1357
                // if this group is contained by another, then we add two dummy vars and rectangles for the borders    // 1358
                var b = root.bounds, c = f.getCentre(b), s = f.getSize(b) / 2, open = f.getOpen(b), close = f.getClose(b), min = c - s + padding / 2, max = c + s - padding / 2;
                root.minVar.desiredPosition = min;                                                                     // 1360
                add(f.makeRect(open, close, min, padding), root.minVar);                                               // 1361
                root.maxVar.desiredPosition = max;                                                                     // 1362
                add(f.makeRect(open, close, max, padding), root.maxVar);                                               // 1363
            }                                                                                                          // 1364
            if (ln)                                                                                                    // 1365
                root.leaves.forEach(function (l) { return add(l.bounds, l.variable); });                               // 1366
            if (gn)                                                                                                    // 1367
                root.groups.forEach(function (g) {                                                                     // 1368
                    var b = g.bounds;                                                                                  // 1369
                    add(f.makeRect(f.getOpen(b), f.getClose(b), f.getCentre(b), f.getSize(b)), g.minVar);              // 1370
                });                                                                                                    // 1371
            var cs = generateConstraints(rs, vs, f, minSep);                                                           // 1372
            if (gn) {                                                                                                  // 1373
                vs.forEach(function (v) { v.cOut = [], v.cIn = []; });                                                 // 1374
                cs.forEach(function (c) { c.left.cOut.push(c), c.right.cIn.push(c); });                                // 1375
                root.groups.forEach(function (g) {                                                                     // 1376
                    var gapAdjustment = (g.padding - f.getSize(g.bounds)) / 2;                                         // 1377
                    g.minVar.cIn.forEach(function (c) { return c.gap += gapAdjustment; });                             // 1378
                    g.minVar.cOut.forEach(function (c) { c.left = g.maxVar; c.gap += gapAdjustment; });                // 1379
                });                                                                                                    // 1380
            }                                                                                                          // 1381
            return childConstraints.concat(cs);                                                                        // 1382
        }                                                                                                              // 1383
        function generateConstraints(rs, vars, rect, minSep) {                                                         // 1384
            var i, n = rs.length;                                                                                      // 1385
            var N = 2 * n;                                                                                             // 1386
            console.assert(vars.length >= n);                                                                          // 1387
            var events = new Array(N);                                                                                 // 1388
            for (i = 0; i < n; ++i) {                                                                                  // 1389
                var r = rs[i];                                                                                         // 1390
                var v = new Node(vars[i], r, rect.getCentre(r));                                                       // 1391
                events[i] = new Event(true, v, rect.getOpen(r));                                                       // 1392
                events[i + n] = new Event(false, v, rect.getClose(r));                                                 // 1393
            }                                                                                                          // 1394
            events.sort(compareEvents);                                                                                // 1395
            var cs = new Array();                                                                                      // 1396
            var scanline = makeRBTree();                                                                               // 1397
            for (i = 0; i < N; ++i) {                                                                                  // 1398
                var e = events[i];                                                                                     // 1399
                var v = e.v;                                                                                           // 1400
                if (e.isOpen) {                                                                                        // 1401
                    scanline.insert(v);                                                                                // 1402
                    rect.findNeighbours(v, scanline);                                                                  // 1403
                }                                                                                                      // 1404
                else {                                                                                                 // 1405
                    // close event                                                                                     // 1406
                    scanline.remove(v);                                                                                // 1407
                    var makeConstraint = function (l, r) {                                                             // 1408
                        var sep = (rect.getSize(l.r) + rect.getSize(r.r)) / 2 + minSep;                                // 1409
                        cs.push(new vpsc.Constraint(l.v, r.v, sep));                                                   // 1410
                    };                                                                                                 // 1411
                    var visitNeighbours = function (forward, reverse, mkcon) {                                         // 1412
                        var u, it = v[forward].iterator();                                                             // 1413
                        while ((u = it[forward]()) !== null) {                                                         // 1414
                            mkcon(u, v);                                                                               // 1415
                            u[reverse].remove(v);                                                                      // 1416
                        }                                                                                              // 1417
                    };                                                                                                 // 1418
                    visitNeighbours("prev", "next", function (u, v) { return makeConstraint(u, v); });                 // 1419
                    visitNeighbours("next", "prev", function (u, v) { return makeConstraint(v, u); });                 // 1420
                }                                                                                                      // 1421
            }                                                                                                          // 1422
            console.assert(scanline.size === 0);                                                                       // 1423
            return cs;                                                                                                 // 1424
        }                                                                                                              // 1425
        function findXNeighbours(v, scanline) {                                                                        // 1426
            var f = function (forward, reverse) {                                                                      // 1427
                var it = scanline.findIter(v);                                                                         // 1428
                var u;                                                                                                 // 1429
                while ((u = it[forward]()) !== null) {                                                                 // 1430
                    var uovervX = u.r.overlapX(v.r);                                                                   // 1431
                    if (uovervX <= 0 || uovervX <= u.r.overlapY(v.r)) {                                                // 1432
                        v[forward].insert(u);                                                                          // 1433
                        u[reverse].insert(v);                                                                          // 1434
                    }                                                                                                  // 1435
                    if (uovervX <= 0) {                                                                                // 1436
                        break;                                                                                         // 1437
                    }                                                                                                  // 1438
                }                                                                                                      // 1439
            };                                                                                                         // 1440
            f("next", "prev");                                                                                         // 1441
            f("prev", "next");                                                                                         // 1442
        }                                                                                                              // 1443
        function findYNeighbours(v, scanline) {                                                                        // 1444
            var f = function (forward, reverse) {                                                                      // 1445
                var u = scanline.findIter(v)[forward]();                                                               // 1446
                if (u !== null && u.r.overlapX(v.r) > 0) {                                                             // 1447
                    v[forward].insert(u);                                                                              // 1448
                    u[reverse].insert(v);                                                                              // 1449
                }                                                                                                      // 1450
            };                                                                                                         // 1451
            f("next", "prev");                                                                                         // 1452
            f("prev", "next");                                                                                         // 1453
        }                                                                                                              // 1454
        function generateXConstraints(rs, vars) {                                                                      // 1455
            return generateConstraints(rs, vars, xRect, 1e-6);                                                         // 1456
        }                                                                                                              // 1457
        vpsc.generateXConstraints = generateXConstraints;                                                              // 1458
        function generateYConstraints(rs, vars) {                                                                      // 1459
            return generateConstraints(rs, vars, yRect, 1e-6);                                                         // 1460
        }                                                                                                              // 1461
        vpsc.generateYConstraints = generateYConstraints;                                                              // 1462
        function generateXGroupConstraints(root) {                                                                     // 1463
            return generateGroupConstraints(root, xRect, 1e-6);                                                        // 1464
        }                                                                                                              // 1465
        vpsc.generateXGroupConstraints = generateXGroupConstraints;                                                    // 1466
        function generateYGroupConstraints(root) {                                                                     // 1467
            return generateGroupConstraints(root, yRect, 1e-6);                                                        // 1468
        }                                                                                                              // 1469
        vpsc.generateYGroupConstraints = generateYGroupConstraints;                                                    // 1470
        function removeOverlaps(rs) {                                                                                  // 1471
            var vs = rs.map(function (r) { return new vpsc.Variable(r.cx()); });                                       // 1472
            var cs = vpsc.generateXConstraints(rs, vs);                                                                // 1473
            var solver = new vpsc.Solver(vs, cs);                                                                      // 1474
            solver.solve();                                                                                            // 1475
            vs.forEach(function (v, i) { return rs[i].setXCentre(v.position()); });                                    // 1476
            vs = rs.map(function (r) { return new vpsc.Variable(r.cy()); });                                           // 1477
            cs = vpsc.generateYConstraints(rs, vs);                                                                    // 1478
            solver = new vpsc.Solver(vs, cs);                                                                          // 1479
            solver.solve();                                                                                            // 1480
            vs.forEach(function (v, i) { return rs[i].setYCentre(v.position()); });                                    // 1481
        }                                                                                                              // 1482
        vpsc.removeOverlaps = removeOverlaps;                                                                          // 1483
        var IndexedVariable = (function (_super) {                                                                     // 1484
            __extends(IndexedVariable, _super);                                                                        // 1485
            function IndexedVariable(index, w) {                                                                       // 1486
                _super.call(this, 0, w);                                                                               // 1487
                this.index = index;                                                                                    // 1488
            }                                                                                                          // 1489
            return IndexedVariable;                                                                                    // 1490
        })(vpsc.Variable);                                                                                             // 1491
        vpsc.IndexedVariable = IndexedVariable;                                                                        // 1492
        var Projection = (function () {                                                                                // 1493
            function Projection(nodes, groups, rootGroup, constraints, avoidOverlaps) {                                // 1494
                var _this = this;                                                                                      // 1495
                if (rootGroup === void 0) { rootGroup = null; }                                                        // 1496
                if (constraints === void 0) { constraints = null; }                                                    // 1497
                if (avoidOverlaps === void 0) { avoidOverlaps = false; }                                               // 1498
                this.nodes = nodes;                                                                                    // 1499
                this.groups = groups;                                                                                  // 1500
                this.rootGroup = rootGroup;                                                                            // 1501
                this.avoidOverlaps = avoidOverlaps;                                                                    // 1502
                this.variables = nodes.map(function (v, i) {                                                           // 1503
                    return v.variable = new IndexedVariable(i, 1);                                                     // 1504
                });                                                                                                    // 1505
                if (constraints)                                                                                       // 1506
                    this.createConstraints(constraints);                                                               // 1507
                if (avoidOverlaps && rootGroup && typeof rootGroup.groups !== 'undefined') {                           // 1508
                    nodes.forEach(function (v) {                                                                       // 1509
                        if (!v.width || !v.height) {                                                                   // 1510
                            //If undefined, default to nothing                                                         // 1511
                            v.bounds = new vpsc.Rectangle(v.x, v.x, v.y, v.y);                                         // 1512
                            return;                                                                                    // 1513
                        }                                                                                              // 1514
                        var w2 = v.width / 2, h2 = v.height / 2;                                                       // 1515
                        v.bounds = new vpsc.Rectangle(v.x - w2, v.x + w2, v.y - h2, v.y + h2);                         // 1516
                    });                                                                                                // 1517
                    computeGroupBounds(rootGroup);                                                                     // 1518
                    var i = nodes.length;                                                                              // 1519
                    groups.forEach(function (g) {                                                                      // 1520
                        _this.variables[i] = g.minVar = new IndexedVariable(i++, typeof g.stiffness !== "undefined" ? g.stiffness : 0.01);
                        _this.variables[i] = g.maxVar = new IndexedVariable(i++, typeof g.stiffness !== "undefined" ? g.stiffness : 0.01);
                    });                                                                                                // 1523
                }                                                                                                      // 1524
            }                                                                                                          // 1525
            Projection.prototype.createSeparation = function (c) {                                                     // 1526
                return new vpsc.Constraint(this.nodes[c.left].variable, this.nodes[c.right].variable, c.gap, typeof c.equality !== "undefined" ? c.equality : false);
            };                                                                                                         // 1528
            Projection.prototype.makeFeasible = function (c) {                                                         // 1529
                var _this = this;                                                                                      // 1530
                if (!this.avoidOverlaps)                                                                               // 1531
                    return;                                                                                            // 1532
                var axis = 'x', dim = 'width';                                                                         // 1533
                if (c.axis === 'x')                                                                                    // 1534
                    axis = 'y', dim = 'height';                                                                        // 1535
                var vs = c.offsets.map(function (o) { return _this.nodes[o.node]; }).sort(function (a, b) { return a[axis] - b[axis]; });
                var p = null;                                                                                          // 1537
                vs.forEach(function (v) {                                                                              // 1538
                    if (p)                                                                                             // 1539
                        v[axis] = p[axis] + p[dim] + 1;                                                                // 1540
                    p = v;                                                                                             // 1541
                });                                                                                                    // 1542
            };                                                                                                         // 1543
            Projection.prototype.createAlignment = function (c) {                                                      // 1544
                var _this = this;                                                                                      // 1545
                var u = this.nodes[c.offsets[0].node].variable;                                                        // 1546
                this.makeFeasible(c);                                                                                  // 1547
                var cs = c.axis === 'x' ? this.xConstraints : this.yConstraints;                                       // 1548
                c.offsets.slice(1).forEach(function (o) {                                                              // 1549
                    var v = _this.nodes[o.node].variable;                                                              // 1550
                    cs.push(new vpsc.Constraint(u, v, o.offset, true));                                                // 1551
                });                                                                                                    // 1552
            };                                                                                                         // 1553
            Projection.prototype.createConstraints = function (constraints) {                                          // 1554
                var _this = this;                                                                                      // 1555
                var isSep = function (c) { return typeof c.type === 'undefined' || c.type === 'separation'; };         // 1556
                this.xConstraints = constraints                                                                        // 1557
                    .filter(function (c) { return c.axis === "x" && isSep(c); })                                       // 1558
                    .map(function (c) { return _this.createSeparation(c); });                                          // 1559
                this.yConstraints = constraints                                                                        // 1560
                    .filter(function (c) { return c.axis === "y" && isSep(c); })                                       // 1561
                    .map(function (c) { return _this.createSeparation(c); });                                          // 1562
                constraints                                                                                            // 1563
                    .filter(function (c) { return c.type === 'alignment'; })                                           // 1564
                    .forEach(function (c) { return _this.createAlignment(c); });                                       // 1565
            };                                                                                                         // 1566
            Projection.prototype.setupVariablesAndBounds = function (x0, y0, desired, getDesired) {                    // 1567
                this.nodes.forEach(function (v, i) {                                                                   // 1568
                    if (v.fixed) {                                                                                     // 1569
                        v.variable.weight = v.fixedWeight ? v.fixedWeight : 1000;                                      // 1570
                        desired[i] = getDesired(v);                                                                    // 1571
                    }                                                                                                  // 1572
                    else {                                                                                             // 1573
                        v.variable.weight = 1;                                                                         // 1574
                    }                                                                                                  // 1575
                    var w = (v.width || 0) / 2, h = (v.height || 0) / 2;                                               // 1576
                    var ix = x0[i], iy = y0[i];                                                                        // 1577
                    v.bounds = new Rectangle(ix - w, ix + w, iy - h, iy + h);                                          // 1578
                });                                                                                                    // 1579
            };                                                                                                         // 1580
            Projection.prototype.xProject = function (x0, y0, x) {                                                     // 1581
                if (!this.rootGroup && !(this.avoidOverlaps || this.xConstraints))                                     // 1582
                    return;                                                                                            // 1583
                this.project(x0, y0, x0, x, function (v) { return v.px; }, this.xConstraints, generateXGroupConstraints, function (v) { return v.bounds.setXCentre(x[v.variable.index] = v.variable.position()); }, function (g) {
                    var xmin = x[g.minVar.index] = g.minVar.position();                                                // 1585
                    var xmax = x[g.maxVar.index] = g.maxVar.position();                                                // 1586
                    var p2 = g.padding / 2;                                                                            // 1587
                    g.bounds.x = xmin - p2;                                                                            // 1588
                    g.bounds.X = xmax + p2;                                                                            // 1589
                });                                                                                                    // 1590
            };                                                                                                         // 1591
            Projection.prototype.yProject = function (x0, y0, y) {                                                     // 1592
                if (!this.rootGroup && !this.yConstraints)                                                             // 1593
                    return;                                                                                            // 1594
                this.project(x0, y0, y0, y, function (v) { return v.py; }, this.yConstraints, generateYGroupConstraints, function (v) { return v.bounds.setYCentre(y[v.variable.index] = v.variable.position()); }, function (g) {
                    var ymin = y[g.minVar.index] = g.minVar.position();                                                // 1596
                    var ymax = y[g.maxVar.index] = g.maxVar.position();                                                // 1597
                    var p2 = g.padding / 2;                                                                            // 1598
                    g.bounds.y = ymin - p2;                                                                            // 1599
                    ;                                                                                                  // 1600
                    g.bounds.Y = ymax + p2;                                                                            // 1601
                });                                                                                                    // 1602
            };                                                                                                         // 1603
            Projection.prototype.projectFunctions = function () {                                                      // 1604
                var _this = this;                                                                                      // 1605
                return [                                                                                               // 1606
                    function (x0, y0, x) { return _this.xProject(x0, y0, x); },                                        // 1607
                    function (x0, y0, y) { return _this.yProject(x0, y0, y); }                                         // 1608
                ];                                                                                                     // 1609
            };                                                                                                         // 1610
            Projection.prototype.project = function (x0, y0, start, desired, getDesired, cs, generateConstraints, updateNodeBounds, updateGroupBounds) {
                this.setupVariablesAndBounds(x0, y0, desired, getDesired);                                             // 1612
                if (this.rootGroup && this.avoidOverlaps) {                                                            // 1613
                    computeGroupBounds(this.rootGroup);                                                                // 1614
                    cs = cs.concat(generateConstraints(this.rootGroup));                                               // 1615
                }                                                                                                      // 1616
                this.solve(this.variables, cs, start, desired);                                                        // 1617
                this.nodes.forEach(updateNodeBounds);                                                                  // 1618
                if (this.rootGroup && this.avoidOverlaps) {                                                            // 1619
                    this.groups.forEach(updateGroupBounds);                                                            // 1620
                    computeGroupBounds(this.rootGroup);                                                                // 1621
                }                                                                                                      // 1622
            };                                                                                                         // 1623
            Projection.prototype.solve = function (vs, cs, starting, desired) {                                        // 1624
                var solver = new vpsc.Solver(vs, cs);                                                                  // 1625
                solver.setStartingPositions(starting);                                                                 // 1626
                solver.setDesiredPositions(desired);                                                                   // 1627
                solver.solve();                                                                                        // 1628
            };                                                                                                         // 1629
            return Projection;                                                                                         // 1630
        })();                                                                                                          // 1631
        vpsc.Projection = Projection;                                                                                  // 1632
    })(vpsc = cola.vpsc || (cola.vpsc = {}));                                                                          // 1633
})(cola || (cola = {}));                                                                                               // 1634
///<reference path="vpsc.ts"/>                                                                                         // 1635
///<reference path="rectangle.ts"/>                                                                                    // 1636
var cola;                                                                                                              // 1637
(function (cola) {                                                                                                     // 1638
    var geom;                                                                                                          // 1639
    (function (geom) {                                                                                                 // 1640
        var Point = (function () {                                                                                     // 1641
            function Point() {                                                                                         // 1642
            }                                                                                                          // 1643
            return Point;                                                                                              // 1644
        })();                                                                                                          // 1645
        geom.Point = Point;                                                                                            // 1646
        var LineSegment = (function () {                                                                               // 1647
            function LineSegment(x1, y1, x2, y2) {                                                                     // 1648
                this.x1 = x1;                                                                                          // 1649
                this.y1 = y1;                                                                                          // 1650
                this.x2 = x2;                                                                                          // 1651
                this.y2 = y2;                                                                                          // 1652
            }                                                                                                          // 1653
            return LineSegment;                                                                                        // 1654
        })();                                                                                                          // 1655
        geom.LineSegment = LineSegment;                                                                                // 1656
        var PolyPoint = (function (_super) {                                                                           // 1657
            __extends(PolyPoint, _super);                                                                              // 1658
            function PolyPoint() {                                                                                     // 1659
                _super.apply(this, arguments);                                                                         // 1660
            }                                                                                                          // 1661
            return PolyPoint;                                                                                          // 1662
        })(Point);                                                                                                     // 1663
        geom.PolyPoint = PolyPoint;                                                                                    // 1664
        /** tests if a point is Left|On|Right of an infinite line.                                                     // 1665
         * @param points P0, P1, and P2                                                                                // 1666
         * @return >0 for P2 left of the line through P0 and P1                                                        // 1667
         *            =0 for P2 on the line                                                                            // 1668
         *            <0 for P2 right of the line                                                                      // 1669
         */                                                                                                            // 1670
        function isLeft(P0, P1, P2) {                                                                                  // 1671
            return (P1.x - P0.x) * (P2.y - P0.y) - (P2.x - P0.x) * (P1.y - P0.y);                                      // 1672
        }                                                                                                              // 1673
        geom.isLeft = isLeft;                                                                                          // 1674
        function above(p, vi, vj) {                                                                                    // 1675
            return isLeft(p, vi, vj) > 0;                                                                              // 1676
        }                                                                                                              // 1677
        function below(p, vi, vj) {                                                                                    // 1678
            return isLeft(p, vi, vj) < 0;                                                                              // 1679
        }                                                                                                              // 1680
        /**                                                                                                            // 1681
         * returns the convex hull of a set of points using Andrew's monotone chain algorithm                          // 1682
         * see: http://geomalgorithms.com/a10-_hull-1.html#Monotone%20Chain                                            // 1683
         * @param S array of points                                                                                    // 1684
         * @return the convex hull as an array of points                                                               // 1685
         */                                                                                                            // 1686
        function ConvexHull(S) {                                                                                       // 1687
            var P = S.slice(0).sort(function (a, b) { return a.x !== b.x ? b.x - a.x : b.y - a.y; });                  // 1688
            var n = S.length, i;                                                                                       // 1689
            var minmin = 0;                                                                                            // 1690
            var xmin = P[0].x;                                                                                         // 1691
            for (i = 1; i < n; ++i) {                                                                                  // 1692
                if (P[i].x !== xmin)                                                                                   // 1693
                    break;                                                                                             // 1694
            }                                                                                                          // 1695
            var minmax = i - 1;                                                                                        // 1696
            var H = [];                                                                                                // 1697
            H.push(P[minmin]); // push minmin point onto stack                                                         // 1698
            if (minmax === n - 1) {                                                                                    // 1699
                if (P[minmax].y !== P[minmin].y)                                                                       // 1700
                    H.push(P[minmax]);                                                                                 // 1701
            }                                                                                                          // 1702
            else {                                                                                                     // 1703
                // Get the indices of points with max x-coord and min|max y-coord                                      // 1704
                var maxmin, maxmax = n - 1;                                                                            // 1705
                var xmax = P[n - 1].x;                                                                                 // 1706
                for (i = n - 2; i >= 0; i--)                                                                           // 1707
                    if (P[i].x !== xmax)                                                                               // 1708
                        break;                                                                                         // 1709
                maxmin = i + 1;                                                                                        // 1710
                // Compute the lower hull on the stack H                                                               // 1711
                i = minmax;                                                                                            // 1712
                while (++i <= maxmin) {                                                                                // 1713
                    // the lower line joins P[minmin]  with P[maxmin]                                                  // 1714
                    if (isLeft(P[minmin], P[maxmin], P[i]) >= 0 && i < maxmin)                                         // 1715
                        continue; // ignore P[i] above or on the lower line                                            // 1716
                    while (H.length > 1) {                                                                             // 1717
                        // test if  P[i] is left of the line at the stack top                                          // 1718
                        if (isLeft(H[H.length - 2], H[H.length - 1], P[i]) > 0)                                        // 1719
                            break; // P[i] is a new hull  vertex                                                       // 1720
                        else                                                                                           // 1721
                            H.length -= 1; // pop top point off  stack                                                 // 1722
                    }                                                                                                  // 1723
                    if (i != minmin)                                                                                   // 1724
                        H.push(P[i]);                                                                                  // 1725
                }                                                                                                      // 1726
                // Next, compute the upper hull on the stack H above the bottom hull                                   // 1727
                if (maxmax != maxmin)                                                                                  // 1728
                    H.push(P[maxmax]); // push maxmax point onto stack                                                 // 1729
                var bot = H.length; // the bottom point of the upper hull stack                                        // 1730
                i = maxmin;                                                                                            // 1731
                while (--i >= minmax) {                                                                                // 1732
                    // the upper line joins P[maxmax]  with P[minmax]                                                  // 1733
                    if (isLeft(P[maxmax], P[minmax], P[i]) >= 0 && i > minmax)                                         // 1734
                        continue; // ignore P[i] below or on the upper line                                            // 1735
                    while (H.length > bot) {                                                                           // 1736
                        // test if  P[i] is left of the line at the stack top                                          // 1737
                        if (isLeft(H[H.length - 2], H[H.length - 1], P[i]) > 0)                                        // 1738
                            break; // P[i] is a new hull  vertex                                                       // 1739
                        else                                                                                           // 1740
                            H.length -= 1; // pop top point off  stack                                                 // 1741
                    }                                                                                                  // 1742
                    if (i != minmin)                                                                                   // 1743
                        H.push(P[i]); // push P[i] onto stack                                                          // 1744
                }                                                                                                      // 1745
            }                                                                                                          // 1746
            return H;                                                                                                  // 1747
        }                                                                                                              // 1748
        geom.ConvexHull = ConvexHull;                                                                                  // 1749
        // apply f to the points in P in clockwise order around the point p                                            // 1750
        function clockwiseRadialSweep(p, P, f) {                                                                       // 1751
            P.slice(0).sort(function (a, b) { return Math.atan2(a.y - p.y, a.x - p.x) - Math.atan2(b.y - p.y, b.x - p.x); }).forEach(f);
        }                                                                                                              // 1753
        geom.clockwiseRadialSweep = clockwiseRadialSweep;                                                              // 1754
        function nextPolyPoint(p, ps) {                                                                                // 1755
            if (p.polyIndex === ps.length - 1)                                                                         // 1756
                return ps[0];                                                                                          // 1757
            return ps[p.polyIndex + 1];                                                                                // 1758
        }                                                                                                              // 1759
        function prevPolyPoint(p, ps) {                                                                                // 1760
            if (p.polyIndex === 0)                                                                                     // 1761
                return ps[ps.length - 1];                                                                              // 1762
            return ps[p.polyIndex - 1];                                                                                // 1763
        }                                                                                                              // 1764
        // tangent_PointPolyC(): fast binary search for tangents to a convex polygon                                   // 1765
        //    Input:  P = a 2D point (exterior to the polygon)                                                         // 1766
        //            n = number of polygon vertices                                                                   // 1767
        //            V = array of vertices for a 2D convex polygon with V[n] = V[0]                                   // 1768
        //    Output: rtan = index of rightmost tangent point V[rtan]                                                  // 1769
        //            ltan = index of leftmost tangent point V[ltan]                                                   // 1770
        function tangent_PointPolyC(P, V) {                                                                            // 1771
            return { rtan: Rtangent_PointPolyC(P, V), ltan: Ltangent_PointPolyC(P, V) };                               // 1772
        }                                                                                                              // 1773
        // Rtangent_PointPolyC(): binary search for convex polygon right tangent                                       // 1774
        //    Input:  P = a 2D point (exterior to the polygon)                                                         // 1775
        //            n = number of polygon vertices                                                                   // 1776
        //            V = array of vertices for a 2D convex polygon with V[n] = V[0]                                   // 1777
        //    Return: index "i" of rightmost tangent point V[i]                                                        // 1778
        function Rtangent_PointPolyC(P, V) {                                                                           // 1779
            var n = V.length - 1;                                                                                      // 1780
            // use binary search for large convex polygons                                                             // 1781
            var a, b, c; // indices for edge chain endpoints                                                           // 1782
            var upA, dnC; // test for up direction of edges a and c                                                    // 1783
            // rightmost tangent = maximum for the isLeft() ordering                                                   // 1784
            // test if V[0] is a local maximum                                                                         // 1785
            if (below(P, V[1], V[0]) && !above(P, V[n - 1], V[0]))                                                     // 1786
                return 0; // V[0] is the maximum tangent point                                                         // 1787
            for (a = 0, b = n;;) {                                                                                     // 1788
                if (b - a === 1)                                                                                       // 1789
                    if (above(P, V[a], V[b]))                                                                          // 1790
                        return a;                                                                                      // 1791
                    else                                                                                               // 1792
                        return b;                                                                                      // 1793
                c = Math.floor((a + b) / 2); // midpoint of [a,b], and 0<c<n                                           // 1794
                dnC = below(P, V[c + 1], V[c]);                                                                        // 1795
                if (dnC && !above(P, V[c - 1], V[c]))                                                                  // 1796
                    return c; // V[c] is the maximum tangent point                                                     // 1797
                // no max yet, so continue with the binary search                                                      // 1798
                // pick one of the two subchains [a,c] or [c,b]                                                        // 1799
                upA = above(P, V[a + 1], V[a]);                                                                        // 1800
                if (upA) {                                                                                             // 1801
                    if (dnC)                                                                                           // 1802
                        b = c; // select [a,c]                                                                         // 1803
                    else {                                                                                             // 1804
                        if (above(P, V[a], V[c]))                                                                      // 1805
                            b = c; // select [a,c]                                                                     // 1806
                        else                                                                                           // 1807
                            a = c; // select [c,b]                                                                     // 1808
                    }                                                                                                  // 1809
                }                                                                                                      // 1810
                else {                                                                                                 // 1811
                    if (!dnC)                                                                                          // 1812
                        a = c; // select [c,b]                                                                         // 1813
                    else {                                                                                             // 1814
                        if (below(P, V[a], V[c]))                                                                      // 1815
                            b = c; // select [a,c]                                                                     // 1816
                        else                                                                                           // 1817
                            a = c; // select [c,b]                                                                     // 1818
                    }                                                                                                  // 1819
                }                                                                                                      // 1820
            }                                                                                                          // 1821
        }                                                                                                              // 1822
        // Ltangent_PointPolyC(): binary search for convex polygon left tangent                                        // 1823
        //    Input:  P = a 2D point (exterior to the polygon)                                                         // 1824
        //            n = number of polygon vertices                                                                   // 1825
        //            V = array of vertices for a 2D convex polygon with V[n]=V[0]                                     // 1826
        //    Return: index "i" of leftmost tangent point V[i]                                                         // 1827
        function Ltangent_PointPolyC(P, V) {                                                                           // 1828
            var n = V.length - 1;                                                                                      // 1829
            // use binary search for large convex polygons                                                             // 1830
            var a, b, c; // indices for edge chain endpoints                                                           // 1831
            var dnA, dnC; // test for down direction of edges a and c                                                  // 1832
            // leftmost tangent = minimum for the isLeft() ordering                                                    // 1833
            // test if V[0] is a local minimum                                                                         // 1834
            if (above(P, V[n - 1], V[0]) && !below(P, V[1], V[0]))                                                     // 1835
                return 0; // V[0] is the minimum tangent point                                                         // 1836
            for (a = 0, b = n;;) {                                                                                     // 1837
                if (b - a === 1)                                                                                       // 1838
                    if (below(P, V[a], V[b]))                                                                          // 1839
                        return a;                                                                                      // 1840
                    else                                                                                               // 1841
                        return b;                                                                                      // 1842
                c = Math.floor((a + b) / 2); // midpoint of [a,b], and 0<c<n                                           // 1843
                dnC = below(P, V[c + 1], V[c]);                                                                        // 1844
                if (above(P, V[c - 1], V[c]) && !dnC)                                                                  // 1845
                    return c; // V[c] is the minimum tangent point                                                     // 1846
                // no min yet, so continue with the binary search                                                      // 1847
                // pick one of the two subchains [a,c] or [c,b]                                                        // 1848
                dnA = below(P, V[a + 1], V[a]);                                                                        // 1849
                if (dnA) {                                                                                             // 1850
                    if (!dnC)                                                                                          // 1851
                        b = c; // select [a,c]                                                                         // 1852
                    else {                                                                                             // 1853
                        if (below(P, V[a], V[c]))                                                                      // 1854
                            b = c; // select [a,c]                                                                     // 1855
                        else                                                                                           // 1856
                            a = c; // select [c,b]                                                                     // 1857
                    }                                                                                                  // 1858
                }                                                                                                      // 1859
                else {                                                                                                 // 1860
                    if (dnC)                                                                                           // 1861
                        a = c; // select [c,b]                                                                         // 1862
                    else {                                                                                             // 1863
                        if (above(P, V[a], V[c]))                                                                      // 1864
                            b = c; // select [a,c]                                                                     // 1865
                        else                                                                                           // 1866
                            a = c; // select [c,b]                                                                     // 1867
                    }                                                                                                  // 1868
                }                                                                                                      // 1869
            }                                                                                                          // 1870
        }                                                                                                              // 1871
        // RLtangent_PolyPolyC(): get the RL tangent between two convex polygons                                       // 1872
        //    Input:  m = number of vertices in polygon 1                                                              // 1873
        //            V = array of vertices for convex polygon 1 with V[m]=V[0]                                        // 1874
        //            n = number of vertices in polygon 2                                                              // 1875
        //            W = array of vertices for convex polygon 2 with W[n]=W[0]                                        // 1876
        //    Output: *t1 = index of tangent point V[t1] for polygon 1                                                 // 1877
        //            *t2 = index of tangent point W[t2] for polygon 2                                                 // 1878
        function tangent_PolyPolyC(V, W, t1, t2, cmp1, cmp2) {                                                         // 1879
            var ix1, ix2; // search indices for polygons 1 and 2                                                       // 1880
            // first get the initial vertex on each polygon                                                            // 1881
            ix1 = t1(W[0], V); // right tangent from W[0] to V                                                         // 1882
            ix2 = t2(V[ix1], W); // left tangent from V[ix1] to W                                                      // 1883
            // ping-pong linear search until it stabilizes                                                             // 1884
            var done = false; // flag when done                                                                        // 1885
            while (!done) {                                                                                            // 1886
                done = true; // assume done until...                                                                   // 1887
                while (true) {                                                                                         // 1888
                    if (ix1 === V.length - 1)                                                                          // 1889
                        ix1 = 0;                                                                                       // 1890
                    if (cmp1(W[ix2], V[ix1], V[ix1 + 1]))                                                              // 1891
                        break;                                                                                         // 1892
                    ++ix1; // get Rtangent from W[ix2] to V                                                            // 1893
                }                                                                                                      // 1894
                while (true) {                                                                                         // 1895
                    if (ix2 === 0)                                                                                     // 1896
                        ix2 = W.length - 1;                                                                            // 1897
                    if (cmp2(V[ix1], W[ix2], W[ix2 - 1]))                                                              // 1898
                        break;                                                                                         // 1899
                    --ix2; // get Ltangent from V[ix1] to W                                                            // 1900
                    done = false; // not done if had to adjust this                                                    // 1901
                }                                                                                                      // 1902
            }                                                                                                          // 1903
            return { t1: ix1, t2: ix2 };                                                                               // 1904
        }                                                                                                              // 1905
        geom.tangent_PolyPolyC = tangent_PolyPolyC;                                                                    // 1906
        function LRtangent_PolyPolyC(V, W) {                                                                           // 1907
            var rl = RLtangent_PolyPolyC(W, V);                                                                        // 1908
            return { t1: rl.t2, t2: rl.t1 };                                                                           // 1909
        }                                                                                                              // 1910
        geom.LRtangent_PolyPolyC = LRtangent_PolyPolyC;                                                                // 1911
        function RLtangent_PolyPolyC(V, W) {                                                                           // 1912
            return tangent_PolyPolyC(V, W, Rtangent_PointPolyC, Ltangent_PointPolyC, above, below);                    // 1913
        }                                                                                                              // 1914
        geom.RLtangent_PolyPolyC = RLtangent_PolyPolyC;                                                                // 1915
        function LLtangent_PolyPolyC(V, W) {                                                                           // 1916
            return tangent_PolyPolyC(V, W, Ltangent_PointPolyC, Ltangent_PointPolyC, below, below);                    // 1917
        }                                                                                                              // 1918
        geom.LLtangent_PolyPolyC = LLtangent_PolyPolyC;                                                                // 1919
        function RRtangent_PolyPolyC(V, W) {                                                                           // 1920
            return tangent_PolyPolyC(V, W, Rtangent_PointPolyC, Rtangent_PointPolyC, above, above);                    // 1921
        }                                                                                                              // 1922
        geom.RRtangent_PolyPolyC = RRtangent_PolyPolyC;                                                                // 1923
        var BiTangent = (function () {                                                                                 // 1924
            function BiTangent(t1, t2) {                                                                               // 1925
                this.t1 = t1;                                                                                          // 1926
                this.t2 = t2;                                                                                          // 1927
            }                                                                                                          // 1928
            return BiTangent;                                                                                          // 1929
        })();                                                                                                          // 1930
        geom.BiTangent = BiTangent;                                                                                    // 1931
        var BiTangents = (function () {                                                                                // 1932
            function BiTangents() {                                                                                    // 1933
            }                                                                                                          // 1934
            return BiTangents;                                                                                         // 1935
        })();                                                                                                          // 1936
        geom.BiTangents = BiTangents;                                                                                  // 1937
        var TVGPoint = (function (_super) {                                                                            // 1938
            __extends(TVGPoint, _super);                                                                               // 1939
            function TVGPoint() {                                                                                      // 1940
                _super.apply(this, arguments);                                                                         // 1941
            }                                                                                                          // 1942
            return TVGPoint;                                                                                           // 1943
        })(Point);                                                                                                     // 1944
        geom.TVGPoint = TVGPoint;                                                                                      // 1945
        var VisibilityVertex = (function () {                                                                          // 1946
            function VisibilityVertex(id, polyid, polyvertid, p) {                                                     // 1947
                this.id = id;                                                                                          // 1948
                this.polyid = polyid;                                                                                  // 1949
                this.polyvertid = polyvertid;                                                                          // 1950
                this.p = p;                                                                                            // 1951
                p.vv = this;                                                                                           // 1952
            }                                                                                                          // 1953
            return VisibilityVertex;                                                                                   // 1954
        })();                                                                                                          // 1955
        geom.VisibilityVertex = VisibilityVertex;                                                                      // 1956
        var VisibilityEdge = (function () {                                                                            // 1957
            function VisibilityEdge(source, target) {                                                                  // 1958
                this.source = source;                                                                                  // 1959
                this.target = target;                                                                                  // 1960
            }                                                                                                          // 1961
            VisibilityEdge.prototype.length = function () {                                                            // 1962
                var dx = this.source.p.x - this.target.p.x;                                                            // 1963
                var dy = this.source.p.y - this.target.p.y;                                                            // 1964
                return Math.sqrt(dx * dx + dy * dy);                                                                   // 1965
            };                                                                                                         // 1966
            return VisibilityEdge;                                                                                     // 1967
        })();                                                                                                          // 1968
        geom.VisibilityEdge = VisibilityEdge;                                                                          // 1969
        var TangentVisibilityGraph = (function () {                                                                    // 1970
            function TangentVisibilityGraph(P, g0) {                                                                   // 1971
                this.P = P;                                                                                            // 1972
                this.V = [];                                                                                           // 1973
                this.E = [];                                                                                           // 1974
                if (!g0) {                                                                                             // 1975
                    var n = P.length;                                                                                  // 1976
                    for (var i = 0; i < n; i++) {                                                                      // 1977
                        var p = P[i];                                                                                  // 1978
                        for (var j = 0; j < p.length; ++j) {                                                           // 1979
                            var pj = p[j], vv = new VisibilityVertex(this.V.length, i, j, pj);                         // 1980
                            this.V.push(vv);                                                                           // 1981
                            if (j > 0)                                                                                 // 1982
                                this.E.push(new VisibilityEdge(p[j - 1].vv, vv));                                      // 1983
                        }                                                                                              // 1984
                    }                                                                                                  // 1985
                    for (var i = 0; i < n - 1; i++) {                                                                  // 1986
                        var Pi = P[i];                                                                                 // 1987
                        for (var j = i + 1; j < n; j++) {                                                              // 1988
                            var Pj = P[j], t = geom.tangents(Pi, Pj);                                                  // 1989
                            for (var q in t) {                                                                         // 1990
                                var c = t[q], source = Pi[c.t1], target = Pj[c.t2];                                    // 1991
                                this.addEdgeIfVisible(source, target, i, j);                                           // 1992
                            }                                                                                          // 1993
                        }                                                                                              // 1994
                    }                                                                                                  // 1995
                }                                                                                                      // 1996
                else {                                                                                                 // 1997
                    this.V = g0.V.slice(0);                                                                            // 1998
                    this.E = g0.E.slice(0);                                                                            // 1999
                }                                                                                                      // 2000
            }                                                                                                          // 2001
            TangentVisibilityGraph.prototype.addEdgeIfVisible = function (u, v, i1, i2) {                              // 2002
                if (!this.intersectsPolys(new LineSegment(u.x, u.y, v.x, v.y), i1, i2)) {                              // 2003
                    this.E.push(new VisibilityEdge(u.vv, v.vv));                                                       // 2004
                }                                                                                                      // 2005
            };                                                                                                         // 2006
            TangentVisibilityGraph.prototype.addPoint = function (p, i1) {                                             // 2007
                var n = this.P.length;                                                                                 // 2008
                this.V.push(new VisibilityVertex(this.V.length, n, 0, p));                                             // 2009
                for (var i = 0; i < n; ++i) {                                                                          // 2010
                    if (i === i1)                                                                                      // 2011
                        continue;                                                                                      // 2012
                    var poly = this.P[i], t = tangent_PointPolyC(p, poly);                                             // 2013
                    this.addEdgeIfVisible(p, poly[t.ltan], i1, i);                                                     // 2014
                    this.addEdgeIfVisible(p, poly[t.rtan], i1, i);                                                     // 2015
                }                                                                                                      // 2016
                return p.vv;                                                                                           // 2017
            };                                                                                                         // 2018
            TangentVisibilityGraph.prototype.intersectsPolys = function (l, i1, i2) {                                  // 2019
                for (var i = 0, n = this.P.length; i < n; ++i) {                                                       // 2020
                    if (i != i1 && i != i2 && intersects(l, this.P[i]).length > 0) {                                   // 2021
                        return true;                                                                                   // 2022
                    }                                                                                                  // 2023
                }                                                                                                      // 2024
                return false;                                                                                          // 2025
            };                                                                                                         // 2026
            return TangentVisibilityGraph;                                                                             // 2027
        })();                                                                                                          // 2028
        geom.TangentVisibilityGraph = TangentVisibilityGraph;                                                          // 2029
        function intersects(l, P) {                                                                                    // 2030
            var ints = [];                                                                                             // 2031
            for (var i = 1, n = P.length; i < n; ++i) {                                                                // 2032
                var int = cola.vpsc.Rectangle.lineIntersection(l.x1, l.y1, l.x2, l.y2, P[i - 1].x, P[i - 1].y, P[i].x, P[i].y);
                if (int)                                                                                               // 2034
                    ints.push(int);                                                                                    // 2035
            }                                                                                                          // 2036
            return ints;                                                                                               // 2037
        }                                                                                                              // 2038
        function tangents(V, W) {                                                                                      // 2039
            var m = V.length - 1, n = W.length - 1;                                                                    // 2040
            var bt = new BiTangents();                                                                                 // 2041
            for (var i = 0; i < m; ++i) {                                                                              // 2042
                for (var j = 0; j < n; ++j) {                                                                          // 2043
                    var v1 = V[i == 0 ? m - 1 : i - 1];                                                                // 2044
                    var v2 = V[i];                                                                                     // 2045
                    var v3 = V[i + 1];                                                                                 // 2046
                    var w1 = W[j == 0 ? n - 1 : j - 1];                                                                // 2047
                    var w2 = W[j];                                                                                     // 2048
                    var w3 = W[j + 1];                                                                                 // 2049
                    var v1v2w2 = isLeft(v1, v2, w2);                                                                   // 2050
                    var v2w1w2 = isLeft(v2, w1, w2);                                                                   // 2051
                    var v2w2w3 = isLeft(v2, w2, w3);                                                                   // 2052
                    var w1w2v2 = isLeft(w1, w2, v2);                                                                   // 2053
                    var w2v1v2 = isLeft(w2, v1, v2);                                                                   // 2054
                    var w2v2v3 = isLeft(w2, v2, v3);                                                                   // 2055
                    if (v1v2w2 >= 0 && v2w1w2 >= 0 && v2w2w3 < 0                                                       // 2056
                        && w1w2v2 >= 0 && w2v1v2 >= 0 && w2v2v3 < 0) {                                                 // 2057
                        bt.ll = new BiTangent(i, j);                                                                   // 2058
                    }                                                                                                  // 2059
                    else if (v1v2w2 <= 0 && v2w1w2 <= 0 && v2w2w3 > 0                                                  // 2060
                        && w1w2v2 <= 0 && w2v1v2 <= 0 && w2v2v3 > 0) {                                                 // 2061
                        bt.rr = new BiTangent(i, j);                                                                   // 2062
                    }                                                                                                  // 2063
                    else if (v1v2w2 <= 0 && v2w1w2 > 0 && v2w2w3 <= 0                                                  // 2064
                        && w1w2v2 >= 0 && w2v1v2 < 0 && w2v2v3 >= 0) {                                                 // 2065
                        bt.rl = new BiTangent(i, j);                                                                   // 2066
                    }                                                                                                  // 2067
                    else if (v1v2w2 >= 0 && v2w1w2 < 0 && v2w2w3 >= 0                                                  // 2068
                        && w1w2v2 <= 0 && w2v1v2 > 0 && w2v2v3 <= 0) {                                                 // 2069
                        bt.lr = new BiTangent(i, j);                                                                   // 2070
                    }                                                                                                  // 2071
                }                                                                                                      // 2072
            }                                                                                                          // 2073
            return bt;                                                                                                 // 2074
        }                                                                                                              // 2075
        geom.tangents = tangents;                                                                                      // 2076
        function isPointInsidePoly(p, poly) {                                                                          // 2077
            for (var i = 1, n = poly.length; i < n; ++i)                                                               // 2078
                if (below(poly[i - 1], poly[i], p))                                                                    // 2079
                    return false;                                                                                      // 2080
            return true;                                                                                               // 2081
        }                                                                                                              // 2082
        function isAnyPInQ(p, q) {                                                                                     // 2083
            return !p.every(function (v) { return !isPointInsidePoly(v, q); });                                        // 2084
        }                                                                                                              // 2085
        function polysOverlap(p, q) {                                                                                  // 2086
            if (isAnyPInQ(p, q))                                                                                       // 2087
                return true;                                                                                           // 2088
            if (isAnyPInQ(q, p))                                                                                       // 2089
                return true;                                                                                           // 2090
            for (var i = 1, n = p.length; i < n; ++i) {                                                                // 2091
                var v = p[i], u = p[i - 1];                                                                            // 2092
                if (intersects(new LineSegment(u.x, u.y, v.x, v.y), q).length > 0)                                     // 2093
                    return true;                                                                                       // 2094
            }                                                                                                          // 2095
            return false;                                                                                              // 2096
        }                                                                                                              // 2097
        geom.polysOverlap = polysOverlap;                                                                              // 2098
    })(geom = cola.geom || (cola.geom = {}));                                                                          // 2099
})(cola || (cola = {}));                                                                                               // 2100
/**                                                                                                                    // 2101
 * @module cola                                                                                                        // 2102
 */                                                                                                                    // 2103
var cola;                                                                                                              // 2104
(function (cola) {                                                                                                     // 2105
    /**                                                                                                                // 2106
     * Descent respects a collection of locks over nodes that should not move                                          // 2107
     * @class Locks                                                                                                    // 2108
     */                                                                                                                // 2109
    var Locks = (function () {                                                                                         // 2110
        function Locks() {                                                                                             // 2111
            this.locks = {};                                                                                           // 2112
        }                                                                                                              // 2113
        /**                                                                                                            // 2114
         * add a lock on the node at index id                                                                          // 2115
         * @method add                                                                                                 // 2116
         * @param id index of node to be locked                                                                        // 2117
         * @param x required position for node                                                                         // 2118
         */                                                                                                            // 2119
        Locks.prototype.add = function (id, x) {                                                                       // 2120
            /* DEBUG                                                                                                   // 2121
                        if (isNaN(x[0]) || isNaN(x[1])) debugger;                                                      // 2122
            DEBUG */                                                                                                   // 2123
            this.locks[id] = x;                                                                                        // 2124
        };                                                                                                             // 2125
        /**                                                                                                            // 2126
         * @method clear clear all locks                                                                               // 2127
         */                                                                                                            // 2128
        Locks.prototype.clear = function () {                                                                          // 2129
            this.locks = {};                                                                                           // 2130
        };                                                                                                             // 2131
        /**                                                                                                            // 2132
         * @isEmpty                                                                                                    // 2133
         * @returns false if no locks exist                                                                            // 2134
         */                                                                                                            // 2135
        Locks.prototype.isEmpty = function () {                                                                        // 2136
            for (var l in this.locks)                                                                                  // 2137
                return false;                                                                                          // 2138
            return true;                                                                                               // 2139
        };                                                                                                             // 2140
        /**                                                                                                            // 2141
         * perform an operation on each lock                                                                           // 2142
         * @apply                                                                                                      // 2143
         */                                                                                                            // 2144
        Locks.prototype.apply = function (f) {                                                                         // 2145
            for (var l in this.locks) {                                                                                // 2146
                f(l, this.locks[l]);                                                                                   // 2147
            }                                                                                                          // 2148
        };                                                                                                             // 2149
        return Locks;                                                                                                  // 2150
    })();                                                                                                              // 2151
    cola.Locks = Locks;                                                                                                // 2152
    /**                                                                                                                // 2153
     * Uses a gradient descent approach to reduce a stress or p-stress goal function over a graph with specified ideal edge lengths or a square matrix of dissimilarities.
     * The standard stress function over a graph nodes with position vectors x,y,z is (mathematica input):             // 2155
     *   stress[x_,y_,z_,D_,w_]:=Sum[w[[i,j]] (length[x[[i]],y[[i]],z[[i]],x[[j]],y[[j]],z[[j]]]-d[[i,j]])^2,{i,Length[x]-1},{j,i+1,Length[x]}]
     * where: D is a square matrix of ideal separations between nodes, w is matrix of weights for those separations    // 2157
     *        length[x1_, y1_, z1_, x2_, y2_, z2_] = Sqrt[(x1 - x2)^2 + (y1 - y2)^2 + (z1 - z2)^2]                     // 2158
     * below, we use wij = 1/(Dij^2)                                                                                   // 2159
     *                                                                                                                 // 2160
     * @class Descent                                                                                                  // 2161
     */                                                                                                                // 2162
    var Descent = (function () {                                                                                       // 2163
        /**                                                                                                            // 2164
         * @method constructor                                                                                         // 2165
         * @param x {number[][]} initial coordinates for nodes                                                         // 2166
         * @param D {number[][]} matrix of desired distances between pairs of nodes                                    // 2167
         * @param G {number[][]} [default=null] if specified, G is a matrix of weights for goal terms between pairs of nodes.
         * If G[i][j] > 1 and the separation between nodes i and j is greater than their ideal distance, then there is no contribution for this pair to the goal
         * If G[i][j] <= 1 then it is used as a weighting on the contribution of the variance between ideal and actual separation between i and j to the goal function
         */                                                                                                            // 2171
        function Descent(x, D, G) {                                                                                    // 2172
            if (G === void 0) { G = null; }                                                                            // 2173
            this.D = D;                                                                                                // 2174
            this.G = G;                                                                                                // 2175
            this.threshold = 0.0001;                                                                                   // 2176
            // Parameters for grid snap stress.                                                                        // 2177
            // TODO: Make a pluggable "StressTerm" class instead of this                                               // 2178
            // mess.                                                                                                   // 2179
            this.numGridSnapNodes = 0;                                                                                 // 2180
            this.snapGridSize = 100;                                                                                   // 2181
            this.snapStrength = 1000;                                                                                  // 2182
            this.scaleSnapByMaxH = false;                                                                              // 2183
            this.random = new PseudoRandom();                                                                          // 2184
            this.project = null;                                                                                       // 2185
            this.x = x;                                                                                                // 2186
            this.k = x.length; // dimensionality                                                                       // 2187
            var n = this.n = x[0].length; // number of nodes                                                           // 2188
            this.H = new Array(this.k);                                                                                // 2189
            this.g = new Array(this.k);                                                                                // 2190
            this.Hd = new Array(this.k);                                                                               // 2191
            this.a = new Array(this.k);                                                                                // 2192
            this.b = new Array(this.k);                                                                                // 2193
            this.c = new Array(this.k);                                                                                // 2194
            this.d = new Array(this.k);                                                                                // 2195
            this.e = new Array(this.k);                                                                                // 2196
            this.ia = new Array(this.k);                                                                               // 2197
            this.ib = new Array(this.k);                                                                               // 2198
            this.xtmp = new Array(this.k);                                                                             // 2199
            this.locks = new Locks();                                                                                  // 2200
            this.minD = Number.MAX_VALUE;                                                                              // 2201
            var i = n, j;                                                                                              // 2202
            while (i--) {                                                                                              // 2203
                j = n;                                                                                                 // 2204
                while (--j > i) {                                                                                      // 2205
                    var d = D[i][j];                                                                                   // 2206
                    if (d > 0 && d < this.minD) {                                                                      // 2207
                        this.minD = d;                                                                                 // 2208
                    }                                                                                                  // 2209
                }                                                                                                      // 2210
            }                                                                                                          // 2211
            if (this.minD === Number.MAX_VALUE)                                                                        // 2212
                this.minD = 1;                                                                                         // 2213
            i = this.k;                                                                                                // 2214
            while (i--) {                                                                                              // 2215
                this.g[i] = new Array(n);                                                                              // 2216
                this.H[i] = new Array(n);                                                                              // 2217
                j = n;                                                                                                 // 2218
                while (j--) {                                                                                          // 2219
                    this.H[i][j] = new Array(n);                                                                       // 2220
                }                                                                                                      // 2221
                this.Hd[i] = new Array(n);                                                                             // 2222
                this.a[i] = new Array(n);                                                                              // 2223
                this.b[i] = new Array(n);                                                                              // 2224
                this.c[i] = new Array(n);                                                                              // 2225
                this.d[i] = new Array(n);                                                                              // 2226
                this.e[i] = new Array(n);                                                                              // 2227
                this.ia[i] = new Array(n);                                                                             // 2228
                this.ib[i] = new Array(n);                                                                             // 2229
                this.xtmp[i] = new Array(n);                                                                           // 2230
            }                                                                                                          // 2231
        }                                                                                                              // 2232
        Descent.createSquareMatrix = function (n, f) {                                                                 // 2233
            var M = new Array(n);                                                                                      // 2234
            for (var i = 0; i < n; ++i) {                                                                              // 2235
                M[i] = new Array(n);                                                                                   // 2236
                for (var j = 0; j < n; ++j) {                                                                          // 2237
                    M[i][j] = f(i, j);                                                                                 // 2238
                }                                                                                                      // 2239
            }                                                                                                          // 2240
            return M;                                                                                                  // 2241
        };                                                                                                             // 2242
        Descent.prototype.offsetDir = function () {                                                                    // 2243
            var _this = this;                                                                                          // 2244
            var u = new Array(this.k);                                                                                 // 2245
            var l = 0;                                                                                                 // 2246
            for (var i = 0; i < this.k; ++i) {                                                                         // 2247
                var x = u[i] = this.random.getNextBetween(0.01, 1) - 0.5;                                              // 2248
                l += x * x;                                                                                            // 2249
            }                                                                                                          // 2250
            l = Math.sqrt(l);                                                                                          // 2251
            return u.map(function (x) { return x *= _this.minD / l; });                                                // 2252
        };                                                                                                             // 2253
        // compute first and second derivative information storing results in this.g and this.H                        // 2254
        Descent.prototype.computeDerivatives = function (x) {                                                          // 2255
            var _this = this;                                                                                          // 2256
            var n = this.n;                                                                                            // 2257
            if (n < 1)                                                                                                 // 2258
                return;                                                                                                // 2259
            var i;                                                                                                     // 2260
            /* DEBUG                                                                                                   // 2261
                        for (var u: number = 0; u < n; ++u)                                                            // 2262
                            for (i = 0; i < this.k; ++i)                                                               // 2263
                                if (isNaN(x[i][u])) debugger;                                                          // 2264
            DEBUG */                                                                                                   // 2265
            var d = new Array(this.k);                                                                                 // 2266
            var d2 = new Array(this.k);                                                                                // 2267
            var Huu = new Array(this.k);                                                                               // 2268
            var maxH = 0;                                                                                              // 2269
            for (var u = 0; u < n; ++u) {                                                                              // 2270
                for (i = 0; i < this.k; ++i)                                                                           // 2271
                    Huu[i] = this.g[i][u] = 0;                                                                         // 2272
                for (var v = 0; v < n; ++v) {                                                                          // 2273
                    if (u === v)                                                                                       // 2274
                        continue;                                                                                      // 2275
                    // The following loop randomly displaces nodes that are at identical positions                     // 2276
                    var maxDisplaces = n; // avoid infinite loop in the case of numerical issues, such as huge values  // 2277
                    while (maxDisplaces--) {                                                                           // 2278
                        var sd2 = 0;                                                                                   // 2279
                        for (i = 0; i < this.k; ++i) {                                                                 // 2280
                            var dx = d[i] = x[i][u] - x[i][v];                                                         // 2281
                            sd2 += d2[i] = dx * dx;                                                                    // 2282
                        }                                                                                              // 2283
                        if (sd2 > 1e-9)                                                                                // 2284
                            break;                                                                                     // 2285
                        var rd = this.offsetDir();                                                                     // 2286
                        for (i = 0; i < this.k; ++i)                                                                   // 2287
                            x[i][v] += rd[i];                                                                          // 2288
                    }                                                                                                  // 2289
                    var l = Math.sqrt(sd2);                                                                            // 2290
                    var D = this.D[u][v];                                                                              // 2291
                    var weight = this.G != null ? this.G[u][v] : 1;                                                    // 2292
                    if (weight > 1 && l > D || !isFinite(D)) {                                                         // 2293
                        for (i = 0; i < this.k; ++i)                                                                   // 2294
                            this.H[i][u][v] = 0;                                                                       // 2295
                        continue;                                                                                      // 2296
                    }                                                                                                  // 2297
                    if (weight > 1) {                                                                                  // 2298
                        weight = 1;                                                                                    // 2299
                    }                                                                                                  // 2300
                    var D2 = D * D;                                                                                    // 2301
                    var gs = 2 * weight * (l - D) / (D2 * l);                                                          // 2302
                    var l3 = l * l * l;                                                                                // 2303
                    var hs = 2 * -weight / (D2 * l3);                                                                  // 2304
                    if (!isFinite(gs))                                                                                 // 2305
                        console.log(gs);                                                                               // 2306
                    for (i = 0; i < this.k; ++i) {                                                                     // 2307
                        this.g[i][u] += d[i] * gs;                                                                     // 2308
                        Huu[i] -= this.H[i][u][v] = hs * (l3 + D * (d2[i] - sd2) + l * sd2);                           // 2309
                    }                                                                                                  // 2310
                }                                                                                                      // 2311
                for (i = 0; i < this.k; ++i)                                                                           // 2312
                    maxH = Math.max(maxH, this.H[i][u][u] = Huu[i]);                                                   // 2313
            }                                                                                                          // 2314
            // Grid snap forces                                                                                        // 2315
            var r = this.snapGridSize / 2;                                                                             // 2316
            var g = this.snapGridSize;                                                                                 // 2317
            var w = this.snapStrength;                                                                                 // 2318
            var k = w / (r * r);                                                                                       // 2319
            var numNodes = this.numGridSnapNodes;                                                                      // 2320
            //var numNodes = n;                                                                                        // 2321
            for (var u = 0; u < numNodes; ++u) {                                                                       // 2322
                for (i = 0; i < this.k; ++i) {                                                                         // 2323
                    var xiu = this.x[i][u];                                                                            // 2324
                    var m = xiu / g;                                                                                   // 2325
                    var f = m % 1;                                                                                     // 2326
                    var q = m - f;                                                                                     // 2327
                    var a = Math.abs(f);                                                                               // 2328
                    var dx = (a <= 0.5) ? xiu - q * g :                                                                // 2329
                        (xiu > 0) ? xiu - (q + 1) * g : xiu - (q - 1) * g;                                             // 2330
                    if (-r < dx && dx <= r) {                                                                          // 2331
                        if (this.scaleSnapByMaxH) {                                                                    // 2332
                            this.g[i][u] += maxH * k * dx;                                                             // 2333
                            this.H[i][u][u] += maxH * k;                                                               // 2334
                        }                                                                                              // 2335
                        else {                                                                                         // 2336
                            this.g[i][u] += k * dx;                                                                    // 2337
                            this.H[i][u][u] += k;                                                                      // 2338
                        }                                                                                              // 2339
                    }                                                                                                  // 2340
                }                                                                                                      // 2341
            }                                                                                                          // 2342
            if (!this.locks.isEmpty()) {                                                                               // 2343
                this.locks.apply(function (u, p) {                                                                     // 2344
                    for (i = 0; i < _this.k; ++i) {                                                                    // 2345
                        _this.H[i][u][u] += maxH;                                                                      // 2346
                        _this.g[i][u] -= maxH * (p[i] - x[i][u]);                                                      // 2347
                    }                                                                                                  // 2348
                });                                                                                                    // 2349
            }                                                                                                          // 2350
            /* DEBUG                                                                                                   // 2351
                        for (var u: number = 0; u < n; ++u)                                                            // 2352
                            for (i = 0; i < this.k; ++i) {                                                             // 2353
                                if (isNaN(this.g[i][u])) debugger;                                                     // 2354
                                for (var v: number = 0; v < n; ++v)                                                    // 2355
                                    if (isNaN(this.H[i][u][v])) debugger;                                              // 2356
                            }                                                                                          // 2357
            DEBUG */                                                                                                   // 2358
        };                                                                                                             // 2359
        Descent.dotProd = function (a, b) {                                                                            // 2360
            var x = 0, i = a.length;                                                                                   // 2361
            while (i--)                                                                                                // 2362
                x += a[i] * b[i];                                                                                      // 2363
            return x;                                                                                                  // 2364
        };                                                                                                             // 2365
        // result r = matrix m * vector v                                                                              // 2366
        Descent.rightMultiply = function (m, v, r) {                                                                   // 2367
            var i = m.length;                                                                                          // 2368
            while (i--)                                                                                                // 2369
                r[i] = Descent.dotProd(m[i], v);                                                                       // 2370
        };                                                                                                             // 2371
        // computes the optimal step size to take in direction d using the                                             // 2372
        // derivative information in this.g and this.H                                                                 // 2373
        // returns the scalar multiplier to apply to d to get the optimal step                                         // 2374
        Descent.prototype.computeStepSize = function (d) {                                                             // 2375
            var numerator = 0, denominator = 0;                                                                        // 2376
            for (var i = 0; i < this.k; ++i) {                                                                         // 2377
                numerator += Descent.dotProd(this.g[i], d[i]);                                                         // 2378
                Descent.rightMultiply(this.H[i], d[i], this.Hd[i]);                                                    // 2379
                denominator += Descent.dotProd(d[i], this.Hd[i]);                                                      // 2380
            }                                                                                                          // 2381
            if (denominator === 0 || !isFinite(denominator))                                                           // 2382
                return 0;                                                                                              // 2383
            return 1 * numerator / denominator;                                                                        // 2384
        };                                                                                                             // 2385
        Descent.prototype.reduceStress = function () {                                                                 // 2386
            this.computeDerivatives(this.x);                                                                           // 2387
            var alpha = this.computeStepSize(this.g);                                                                  // 2388
            for (var i = 0; i < this.k; ++i) {                                                                         // 2389
                this.takeDescentStep(this.x[i], this.g[i], alpha);                                                     // 2390
            }                                                                                                          // 2391
            return this.computeStress();                                                                               // 2392
        };                                                                                                             // 2393
        Descent.copy = function (a, b) {                                                                               // 2394
            var m = a.length, n = b[0].length;                                                                         // 2395
            for (var i = 0; i < m; ++i) {                                                                              // 2396
                for (var j = 0; j < n; ++j) {                                                                          // 2397
                    b[i][j] = a[i][j];                                                                                 // 2398
                }                                                                                                      // 2399
            }                                                                                                          // 2400
        };                                                                                                             // 2401
        // takes a step of stepSize * d from x0, and then project against any constraints.                             // 2402
        // result is returned in r.                                                                                    // 2403
        // x0: starting positions                                                                                      // 2404
        // r: result positions will be returned here                                                                   // 2405
        // d: unconstrained descent vector                                                                             // 2406
        // stepSize: amount to step along d                                                                            // 2407
        Descent.prototype.stepAndProject = function (x0, r, d, stepSize) {                                             // 2408
            Descent.copy(x0, r);                                                                                       // 2409
            this.takeDescentStep(r[0], d[0], stepSize);                                                                // 2410
            if (this.project)                                                                                          // 2411
                this.project[0](x0[0], x0[1], r[0]);                                                                   // 2412
            this.takeDescentStep(r[1], d[1], stepSize);                                                                // 2413
            if (this.project)                                                                                          // 2414
                this.project[1](r[0], x0[1], r[1]);                                                                    // 2415
            // todo: allow projection against constraints in higher dimensions                                         // 2416
            for (var i = 2; i < this.k; i++)                                                                           // 2417
                this.takeDescentStep(r[i], d[i], stepSize);                                                            // 2418
            // the following makes locks extra sticky... but hides the result of the projection from the consumer      // 2419
            //if (!this.locks.isEmpty()) {                                                                             // 2420
            //    this.locks.apply((u, p) => {                                                                         // 2421
            //        for (var i = 0; i < this.k; i++) {                                                               // 2422
            //            r[i][u] = p[i];                                                                              // 2423
            //        }                                                                                                // 2424
            //    });                                                                                                  // 2425
            //}                                                                                                        // 2426
        };                                                                                                             // 2427
        Descent.mApply = function (m, n, f) {                                                                          // 2428
            var i = m;                                                                                                 // 2429
            while (i-- > 0) {                                                                                          // 2430
                var j = n;                                                                                             // 2431
                while (j-- > 0)                                                                                        // 2432
                    f(i, j);                                                                                           // 2433
            }                                                                                                          // 2434
        };                                                                                                             // 2435
        Descent.prototype.matrixApply = function (f) {                                                                 // 2436
            Descent.mApply(this.k, this.n, f);                                                                         // 2437
        };                                                                                                             // 2438
        Descent.prototype.computeNextPosition = function (x0, r) {                                                     // 2439
            var _this = this;                                                                                          // 2440
            this.computeDerivatives(x0);                                                                               // 2441
            var alpha = this.computeStepSize(this.g);                                                                  // 2442
            this.stepAndProject(x0, r, this.g, alpha);                                                                 // 2443
            /* DEBUG                                                                                                   // 2444
                        for (var u: number = 0; u < this.n; ++u)                                                       // 2445
                            for (var i = 0; i < this.k; ++i)                                                           // 2446
                                if (isNaN(r[i][u])) debugger;                                                          // 2447
            DEBUG */                                                                                                   // 2448
            if (this.project) {                                                                                        // 2449
                this.matrixApply(function (i, j) { return _this.e[i][j] = x0[i][j] - r[i][j]; });                      // 2450
                var beta = this.computeStepSize(this.e);                                                               // 2451
                beta = Math.max(0.2, Math.min(beta, 1));                                                               // 2452
                this.stepAndProject(x0, r, this.e, beta);                                                              // 2453
            }                                                                                                          // 2454
        };                                                                                                             // 2455
        Descent.prototype.run = function (iterations) {                                                                // 2456
            var stress = Number.MAX_VALUE, converged = false;                                                          // 2457
            while (!converged && iterations-- > 0) {                                                                   // 2458
                var s = this.rungeKutta();                                                                             // 2459
                converged = Math.abs(stress / s - 1) < this.threshold;                                                 // 2460
                stress = s;                                                                                            // 2461
            }                                                                                                          // 2462
            return stress;                                                                                             // 2463
        };                                                                                                             // 2464
        Descent.prototype.rungeKutta = function () {                                                                   // 2465
            var _this = this;                                                                                          // 2466
            this.computeNextPosition(this.x, this.a);                                                                  // 2467
            Descent.mid(this.x, this.a, this.ia);                                                                      // 2468
            this.computeNextPosition(this.ia, this.b);                                                                 // 2469
            Descent.mid(this.x, this.b, this.ib);                                                                      // 2470
            this.computeNextPosition(this.ib, this.c);                                                                 // 2471
            this.computeNextPosition(this.c, this.d);                                                                  // 2472
            var disp = 0;                                                                                              // 2473
            this.matrixApply(function (i, j) {                                                                         // 2474
                var x = (_this.a[i][j] + 2.0 * _this.b[i][j] + 2.0 * _this.c[i][j] + _this.d[i][j]) / 6.0, d = _this.x[i][j] - x;
                disp += d * d;                                                                                         // 2476
                _this.x[i][j] = x;                                                                                     // 2477
            });                                                                                                        // 2478
            return disp;                                                                                               // 2479
        };                                                                                                             // 2480
        Descent.mid = function (a, b, m) {                                                                             // 2481
            Descent.mApply(a.length, a[0].length, function (i, j) {                                                    // 2482
                return m[i][j] = a[i][j] + (b[i][j] - a[i][j]) / 2.0;                                                  // 2483
            });                                                                                                        // 2484
        };                                                                                                             // 2485
        Descent.prototype.takeDescentStep = function (x, d, stepSize) {                                                // 2486
            for (var i = 0; i < this.n; ++i) {                                                                         // 2487
                x[i] = x[i] - stepSize * d[i];                                                                         // 2488
            }                                                                                                          // 2489
        };                                                                                                             // 2490
        Descent.prototype.computeStress = function () {                                                                // 2491
            var stress = 0;                                                                                            // 2492
            for (var u = 0, nMinus1 = this.n - 1; u < nMinus1; ++u) {                                                  // 2493
                for (var v = u + 1, n = this.n; v < n; ++v) {                                                          // 2494
                    var l = 0;                                                                                         // 2495
                    for (var i = 0; i < this.k; ++i) {                                                                 // 2496
                        var dx = this.x[i][u] - this.x[i][v];                                                          // 2497
                        l += dx * dx;                                                                                  // 2498
                    }                                                                                                  // 2499
                    l = Math.sqrt(l);                                                                                  // 2500
                    var d = this.D[u][v];                                                                              // 2501
                    if (!isFinite(d))                                                                                  // 2502
                        continue;                                                                                      // 2503
                    var rl = d - l;                                                                                    // 2504
                    var d2 = d * d;                                                                                    // 2505
                    stress += rl * rl / d2;                                                                            // 2506
                }                                                                                                      // 2507
            }                                                                                                          // 2508
            return stress;                                                                                             // 2509
        };                                                                                                             // 2510
        Descent.zeroDistance = 1e-10;                                                                                  // 2511
        return Descent;                                                                                                // 2512
    })();                                                                                                              // 2513
    cola.Descent = Descent;                                                                                            // 2514
    // Linear congruential pseudo random number generator                                                              // 2515
    var PseudoRandom = (function () {                                                                                  // 2516
        function PseudoRandom(seed) {                                                                                  // 2517
            if (seed === void 0) { seed = 1; }                                                                         // 2518
            this.seed = seed;                                                                                          // 2519
            this.a = 214013;                                                                                           // 2520
            this.c = 2531011;                                                                                          // 2521
            this.m = 2147483648;                                                                                       // 2522
            this.range = 32767;                                                                                        // 2523
        }                                                                                                              // 2524
        // random real between 0 and 1                                                                                 // 2525
        PseudoRandom.prototype.getNext = function () {                                                                 // 2526
            this.seed = (this.seed * this.a + this.c) % this.m;                                                        // 2527
            return (this.seed >> 16) / this.range;                                                                     // 2528
        };                                                                                                             // 2529
        // random real between min and max                                                                             // 2530
        PseudoRandom.prototype.getNextBetween = function (min, max) {                                                  // 2531
            return min + this.getNext() * (max - min);                                                                 // 2532
        };                                                                                                             // 2533
        return PseudoRandom;                                                                                           // 2534
    })();                                                                                                              // 2535
    cola.PseudoRandom = PseudoRandom;                                                                                  // 2536
})(cola || (cola = {}));                                                                                               // 2537
var cola;                                                                                                              // 2538
(function (cola) {                                                                                                     // 2539
    var powergraph;                                                                                                    // 2540
    (function (powergraph) {                                                                                           // 2541
        var PowerEdge = (function () {                                                                                 // 2542
            function PowerEdge(source, target, type) {                                                                 // 2543
                this.source = source;                                                                                  // 2544
                this.target = target;                                                                                  // 2545
                this.type = type;                                                                                      // 2546
            }                                                                                                          // 2547
            return PowerEdge;                                                                                          // 2548
        })();                                                                                                          // 2549
        powergraph.PowerEdge = PowerEdge;                                                                              // 2550
        var Configuration = (function () {                                                                             // 2551
            function Configuration(n, edges, linkAccessor, rootGroup) {                                                // 2552
                var _this = this;                                                                                      // 2553
                this.linkAccessor = linkAccessor;                                                                      // 2554
                this.modules = new Array(n);                                                                           // 2555
                this.roots = [];                                                                                       // 2556
                if (rootGroup) {                                                                                       // 2557
                    this.initModulesFromGroup(rootGroup);                                                              // 2558
                }                                                                                                      // 2559
                else {                                                                                                 // 2560
                    this.roots.push(new ModuleSet());                                                                  // 2561
                    for (var i = 0; i < n; ++i)                                                                        // 2562
                        this.roots[0].add(this.modules[i] = new Module(i));                                            // 2563
                }                                                                                                      // 2564
                this.R = edges.length;                                                                                 // 2565
                edges.forEach(function (e) {                                                                           // 2566
                    var s = _this.modules[linkAccessor.getSourceIndex(e)], t = _this.modules[linkAccessor.getTargetIndex(e)], type = linkAccessor.getType(e);
                    s.outgoing.add(type, t);                                                                           // 2568
                    t.incoming.add(type, s);                                                                           // 2569
                });                                                                                                    // 2570
            }                                                                                                          // 2571
            Configuration.prototype.initModulesFromGroup = function (group) {                                          // 2572
                var moduleSet = new ModuleSet();                                                                       // 2573
                this.roots.push(moduleSet);                                                                            // 2574
                for (var i = 0; i < group.leaves.length; ++i) {                                                        // 2575
                    var node = group.leaves[i];                                                                        // 2576
                    var module = new Module(node.id);                                                                  // 2577
                    this.modules[node.id] = module;                                                                    // 2578
                    moduleSet.add(module);                                                                             // 2579
                }                                                                                                      // 2580
                if (group.groups) {                                                                                    // 2581
                    for (var j = 0; j < group.groups.length; ++j) {                                                    // 2582
                        var child = group.groups[j];                                                                   // 2583
                        // Propagate group properties (like padding, stiffness, ...) as module definition so that the generated power graph group will inherit it
                        var definition = {};                                                                           // 2585
                        for (var prop in child)                                                                        // 2586
                            if (prop !== "leaves" && prop !== "groups" && child.hasOwnProperty(prop))                  // 2587
                                definition[prop] = child[prop];                                                        // 2588
                        // Use negative module id to avoid clashes between predefined and generated modules            // 2589
                        moduleSet.add(new Module(-1 - j, new LinkSets(), new LinkSets(), this.initModulesFromGroup(child), definition));
                    }                                                                                                  // 2591
                }                                                                                                      // 2592
                return moduleSet;                                                                                      // 2593
            };                                                                                                         // 2594
            // merge modules a and b keeping track of their power edges and removing the from roots                    // 2595
            Configuration.prototype.merge = function (a, b, k) {                                                       // 2596
                if (k === void 0) { k = 0; }                                                                           // 2597
                var inInt = a.incoming.intersection(b.incoming), outInt = a.outgoing.intersection(b.outgoing);         // 2598
                var children = new ModuleSet();                                                                        // 2599
                children.add(a);                                                                                       // 2600
                children.add(b);                                                                                       // 2601
                var m = new Module(this.modules.length, outInt, inInt, children);                                      // 2602
                this.modules.push(m);                                                                                  // 2603
                var update = function (s, i, o) {                                                                      // 2604
                    s.forAll(function (ms, linktype) {                                                                 // 2605
                        ms.forAll(function (n) {                                                                       // 2606
                            var nls = n[i];                                                                            // 2607
                            nls.add(linktype, m);                                                                      // 2608
                            nls.remove(linktype, a);                                                                   // 2609
                            nls.remove(linktype, b);                                                                   // 2610
                            a[o].remove(linktype, n);                                                                  // 2611
                            b[o].remove(linktype, n);                                                                  // 2612
                        });                                                                                            // 2613
                    });                                                                                                // 2614
                };                                                                                                     // 2615
                update(outInt, "incoming", "outgoing");                                                                // 2616
                update(inInt, "outgoing", "incoming");                                                                 // 2617
                this.R -= inInt.count() + outInt.count();                                                              // 2618
                this.roots[k].remove(a);                                                                               // 2619
                this.roots[k].remove(b);                                                                               // 2620
                this.roots[k].add(m);                                                                                  // 2621
                return m;                                                                                              // 2622
            };                                                                                                         // 2623
            Configuration.prototype.rootMerges = function (k) {                                                        // 2624
                if (k === void 0) { k = 0; }                                                                           // 2625
                var rs = this.roots[k].modules();                                                                      // 2626
                var n = rs.length;                                                                                     // 2627
                var merges = new Array(n * (n - 1));                                                                   // 2628
                var ctr = 0;                                                                                           // 2629
                for (var i = 0, i_ = n - 1; i < i_; ++i) {                                                             // 2630
                    for (var j = i + 1; j < n; ++j) {                                                                  // 2631
                        var a = rs[i], b = rs[j];                                                                      // 2632
                        merges[ctr] = { id: ctr, nEdges: this.nEdges(a, b), a: a, b: b };                              // 2633
                        ctr++;                                                                                         // 2634
                    }                                                                                                  // 2635
                }                                                                                                      // 2636
                return merges;                                                                                         // 2637
            };                                                                                                         // 2638
            Configuration.prototype.greedyMerge = function () {                                                        // 2639
                for (var i = 0; i < this.roots.length; ++i) {                                                          // 2640
                    // Handle single nested module case                                                                // 2641
                    if (this.roots[i].modules().length < 2)                                                            // 2642
                        continue;                                                                                      // 2643
                    // find the merge that allows for the most edges to be removed.  secondary ordering based on arbitrary id (for predictability)
                    var ms = this.rootMerges(i).sort(function (a, b) { return a.nEdges == b.nEdges ? a.id - b.id : a.nEdges - b.nEdges; });
                    var m = ms[0];                                                                                     // 2646
                    if (m.nEdges >= this.R)                                                                            // 2647
                        continue;                                                                                      // 2648
                    this.merge(m.a, m.b, i);                                                                           // 2649
                    return true;                                                                                       // 2650
                }                                                                                                      // 2651
            };                                                                                                         // 2652
            Configuration.prototype.nEdges = function (a, b) {                                                         // 2653
                var inInt = a.incoming.intersection(b.incoming), outInt = a.outgoing.intersection(b.outgoing);         // 2654
                return this.R - inInt.count() - outInt.count();                                                        // 2655
            };                                                                                                         // 2656
            Configuration.prototype.getGroupHierarchy = function (retargetedEdges) {                                   // 2657
                var _this = this;                                                                                      // 2658
                var groups = [];                                                                                       // 2659
                var root = {};                                                                                         // 2660
                toGroups(this.roots[0], root, groups);                                                                 // 2661
                var es = this.allEdges();                                                                              // 2662
                es.forEach(function (e) {                                                                              // 2663
                    var a = _this.modules[e.source];                                                                   // 2664
                    var b = _this.modules[e.target];                                                                   // 2665
                    retargetedEdges.push(new PowerEdge(typeof a.gid === "undefined" ? e.source : groups[a.gid], typeof b.gid === "undefined" ? e.target : groups[b.gid], e.type));
                });                                                                                                    // 2667
                return groups;                                                                                         // 2668
            };                                                                                                         // 2669
            Configuration.prototype.allEdges = function () {                                                           // 2670
                var es = [];                                                                                           // 2671
                Configuration.getEdges(this.roots[0], es);                                                             // 2672
                return es;                                                                                             // 2673
            };                                                                                                         // 2674
            Configuration.getEdges = function (modules, es) {                                                          // 2675
                modules.forAll(function (m) {                                                                          // 2676
                    m.getEdges(es);                                                                                    // 2677
                    Configuration.getEdges(m.children, es);                                                            // 2678
                });                                                                                                    // 2679
            };                                                                                                         // 2680
            return Configuration;                                                                                      // 2681
        })();                                                                                                          // 2682
        powergraph.Configuration = Configuration;                                                                      // 2683
        function toGroups(modules, group, groups) {                                                                    // 2684
            modules.forAll(function (m) {                                                                              // 2685
                if (m.isLeaf()) {                                                                                      // 2686
                    if (!group.leaves)                                                                                 // 2687
                        group.leaves = [];                                                                             // 2688
                    group.leaves.push(m.id);                                                                           // 2689
                }                                                                                                      // 2690
                else {                                                                                                 // 2691
                    var g = group;                                                                                     // 2692
                    m.gid = groups.length;                                                                             // 2693
                    if (!m.isIsland() || m.isPredefined()) {                                                           // 2694
                        g = { id: m.gid };                                                                             // 2695
                        if (m.isPredefined())                                                                          // 2696
                            // Apply original group properties                                                         // 2697
                            for (var prop in m.definition)                                                             // 2698
                                g[prop] = m.definition[prop];                                                          // 2699
                        if (!group.groups)                                                                             // 2700
                            group.groups = [];                                                                         // 2701
                        group.groups.push(m.gid);                                                                      // 2702
                        groups.push(g);                                                                                // 2703
                    }                                                                                                  // 2704
                    toGroups(m.children, g, groups);                                                                   // 2705
                }                                                                                                      // 2706
            });                                                                                                        // 2707
        }                                                                                                              // 2708
        var Module = (function () {                                                                                    // 2709
            function Module(id, outgoing, incoming, children, definition) {                                            // 2710
                if (outgoing === void 0) { outgoing = new LinkSets(); }                                                // 2711
                if (incoming === void 0) { incoming = new LinkSets(); }                                                // 2712
                if (children === void 0) { children = new ModuleSet(); }                                               // 2713
                this.id = id;                                                                                          // 2714
                this.outgoing = outgoing;                                                                              // 2715
                this.incoming = incoming;                                                                              // 2716
                this.children = children;                                                                              // 2717
                this.definition = definition;                                                                          // 2718
            }                                                                                                          // 2719
            Module.prototype.getEdges = function (es) {                                                                // 2720
                var _this = this;                                                                                      // 2721
                this.outgoing.forAll(function (ms, edgetype) {                                                         // 2722
                    ms.forAll(function (target) {                                                                      // 2723
                        es.push(new PowerEdge(_this.id, target.id, edgetype));                                         // 2724
                    });                                                                                                // 2725
                });                                                                                                    // 2726
            };                                                                                                         // 2727
            Module.prototype.isLeaf = function () {                                                                    // 2728
                return this.children.count() === 0;                                                                    // 2729
            };                                                                                                         // 2730
            Module.prototype.isIsland = function () {                                                                  // 2731
                return this.outgoing.count() === 0 && this.incoming.count() === 0;                                     // 2732
            };                                                                                                         // 2733
            Module.prototype.isPredefined = function () {                                                              // 2734
                return typeof this.definition !== "undefined";                                                         // 2735
            };                                                                                                         // 2736
            return Module;                                                                                             // 2737
        })();                                                                                                          // 2738
        powergraph.Module = Module;                                                                                    // 2739
        function intersection(m, n) {                                                                                  // 2740
            var i = {};                                                                                                // 2741
            for (var v in m)                                                                                           // 2742
                if (v in n)                                                                                            // 2743
                    i[v] = m[v];                                                                                       // 2744
            return i;                                                                                                  // 2745
        }                                                                                                              // 2746
        var ModuleSet = (function () {                                                                                 // 2747
            function ModuleSet() {                                                                                     // 2748
                this.table = {};                                                                                       // 2749
            }                                                                                                          // 2750
            ModuleSet.prototype.count = function () {                                                                  // 2751
                return Object.keys(this.table).length;                                                                 // 2752
            };                                                                                                         // 2753
            ModuleSet.prototype.intersection = function (other) {                                                      // 2754
                var result = new ModuleSet();                                                                          // 2755
                result.table = intersection(this.table, other.table);                                                  // 2756
                return result;                                                                                         // 2757
            };                                                                                                         // 2758
            ModuleSet.prototype.intersectionCount = function (other) {                                                 // 2759
                return this.intersection(other).count();                                                               // 2760
            };                                                                                                         // 2761
            ModuleSet.prototype.contains = function (id) {                                                             // 2762
                return id in this.table;                                                                               // 2763
            };                                                                                                         // 2764
            ModuleSet.prototype.add = function (m) {                                                                   // 2765
                this.table[m.id] = m;                                                                                  // 2766
            };                                                                                                         // 2767
            ModuleSet.prototype.remove = function (m) {                                                                // 2768
                delete this.table[m.id];                                                                               // 2769
            };                                                                                                         // 2770
            ModuleSet.prototype.forAll = function (f) {                                                                // 2771
                for (var mid in this.table) {                                                                          // 2772
                    f(this.table[mid]);                                                                                // 2773
                }                                                                                                      // 2774
            };                                                                                                         // 2775
            ModuleSet.prototype.modules = function () {                                                                // 2776
                var vs = [];                                                                                           // 2777
                this.forAll(function (m) {                                                                             // 2778
                    if (!m.isPredefined())                                                                             // 2779
                        vs.push(m);                                                                                    // 2780
                });                                                                                                    // 2781
                return vs;                                                                                             // 2782
            };                                                                                                         // 2783
            return ModuleSet;                                                                                          // 2784
        })();                                                                                                          // 2785
        powergraph.ModuleSet = ModuleSet;                                                                              // 2786
        var LinkSets = (function () {                                                                                  // 2787
            function LinkSets() {                                                                                      // 2788
                this.sets = {};                                                                                        // 2789
                this.n = 0;                                                                                            // 2790
            }                                                                                                          // 2791
            LinkSets.prototype.count = function () {                                                                   // 2792
                return this.n;                                                                                         // 2793
            };                                                                                                         // 2794
            LinkSets.prototype.contains = function (id) {                                                              // 2795
                var result = false;                                                                                    // 2796
                this.forAllModules(function (m) {                                                                      // 2797
                    if (!result && m.id == id) {                                                                       // 2798
                        result = true;                                                                                 // 2799
                    }                                                                                                  // 2800
                });                                                                                                    // 2801
                return result;                                                                                         // 2802
            };                                                                                                         // 2803
            LinkSets.prototype.add = function (linktype, m) {                                                          // 2804
                var s = linktype in this.sets ? this.sets[linktype] : this.sets[linktype] = new ModuleSet();           // 2805
                s.add(m);                                                                                              // 2806
                ++this.n;                                                                                              // 2807
            };                                                                                                         // 2808
            LinkSets.prototype.remove = function (linktype, m) {                                                       // 2809
                var ms = this.sets[linktype];                                                                          // 2810
                ms.remove(m);                                                                                          // 2811
                if (ms.count() === 0) {                                                                                // 2812
                    delete this.sets[linktype];                                                                        // 2813
                }                                                                                                      // 2814
                --this.n;                                                                                              // 2815
            };                                                                                                         // 2816
            LinkSets.prototype.forAll = function (f) {                                                                 // 2817
                for (var linktype in this.sets) {                                                                      // 2818
                    f(this.sets[linktype], linktype);                                                                  // 2819
                }                                                                                                      // 2820
            };                                                                                                         // 2821
            LinkSets.prototype.forAllModules = function (f) {                                                          // 2822
                this.forAll(function (ms, lt) { return ms.forAll(f); });                                               // 2823
            };                                                                                                         // 2824
            LinkSets.prototype.intersection = function (other) {                                                       // 2825
                var result = new LinkSets();                                                                           // 2826
                this.forAll(function (ms, lt) {                                                                        // 2827
                    if (lt in other.sets) {                                                                            // 2828
                        var i = ms.intersection(other.sets[lt]), n = i.count();                                        // 2829
                        if (n > 0) {                                                                                   // 2830
                            result.sets[lt] = i;                                                                       // 2831
                            result.n += n;                                                                             // 2832
                        }                                                                                              // 2833
                    }                                                                                                  // 2834
                });                                                                                                    // 2835
                return result;                                                                                         // 2836
            };                                                                                                         // 2837
            return LinkSets;                                                                                           // 2838
        })();                                                                                                          // 2839
        powergraph.LinkSets = LinkSets;                                                                                // 2840
        function intersectionCount(m, n) {                                                                             // 2841
            return Object.keys(intersection(m, n)).length;                                                             // 2842
        }                                                                                                              // 2843
        function getGroups(nodes, links, la, rootGroup) {                                                              // 2844
            var n = nodes.length, c = new powergraph.Configuration(n, links, la, rootGroup);                           // 2845
            while (c.greedyMerge())                                                                                    // 2846
                ;                                                                                                      // 2847
            var powerEdges = [];                                                                                       // 2848
            var g = c.getGroupHierarchy(powerEdges);                                                                   // 2849
            powerEdges.forEach(function (e) {                                                                          // 2850
                var f = function (end) {                                                                               // 2851
                    var g = e[end];                                                                                    // 2852
                    if (typeof g == "number")                                                                          // 2853
                        e[end] = nodes[g];                                                                             // 2854
                };                                                                                                     // 2855
                f("source");                                                                                           // 2856
                f("target");                                                                                           // 2857
            });                                                                                                        // 2858
            return { groups: g, powerEdges: powerEdges };                                                              // 2859
        }                                                                                                              // 2860
        powergraph.getGroups = getGroups;                                                                              // 2861
    })(powergraph = cola.powergraph || (cola.powergraph = {}));                                                        // 2862
})(cola || (cola = {}));                                                                                               // 2863
/**                                                                                                                    // 2864
 * @module cola                                                                                                        // 2865
 */                                                                                                                    // 2866
var cola;                                                                                                              // 2867
(function (cola) {                                                                                                     // 2868
    // compute the size of the union of two sets a and b                                                               // 2869
    function unionCount(a, b) {                                                                                        // 2870
        var u = {};                                                                                                    // 2871
        for (var i in a)                                                                                               // 2872
            u[i] = {};                                                                                                 // 2873
        for (var i in b)                                                                                               // 2874
            u[i] = {};                                                                                                 // 2875
        return Object.keys(u).length;                                                                                  // 2876
    }                                                                                                                  // 2877
    // compute the size of the intersection of two sets a and b                                                        // 2878
    function intersectionCount(a, b) {                                                                                 // 2879
        var n = 0;                                                                                                     // 2880
        for (var i in a)                                                                                               // 2881
            if (typeof b[i] !== 'undefined')                                                                           // 2882
                ++n;                                                                                                   // 2883
        return n;                                                                                                      // 2884
    }                                                                                                                  // 2885
    function getNeighbours(links, la) {                                                                                // 2886
        var neighbours = {};                                                                                           // 2887
        var addNeighbours = function (u, v) {                                                                          // 2888
            if (typeof neighbours[u] === 'undefined')                                                                  // 2889
                neighbours[u] = {};                                                                                    // 2890
            neighbours[u][v] = {};                                                                                     // 2891
        };                                                                                                             // 2892
        links.forEach(function (e) {                                                                                   // 2893
            var u = la.getSourceIndex(e), v = la.getTargetIndex(e);                                                    // 2894
            addNeighbours(u, v);                                                                                       // 2895
            addNeighbours(v, u);                                                                                       // 2896
        });                                                                                                            // 2897
        return neighbours;                                                                                             // 2898
    }                                                                                                                  // 2899
    // modify the lengths of the specified links by the result of function f weighted by w                             // 2900
    function computeLinkLengths(links, w, f, la) {                                                                     // 2901
        var neighbours = getNeighbours(links, la);                                                                     // 2902
        links.forEach(function (l) {                                                                                   // 2903
            var a = neighbours[la.getSourceIndex(l)];                                                                  // 2904
            var b = neighbours[la.getTargetIndex(l)];                                                                  // 2905
            la.setLength(l, 1 + w * f(a, b));                                                                          // 2906
        });                                                                                                            // 2907
    }                                                                                                                  // 2908
    /** modify the specified link lengths based on the symmetric difference of their neighbours                        // 2909
     * @class symmetricDiffLinkLengths                                                                                 // 2910
     */                                                                                                                // 2911
    function symmetricDiffLinkLengths(links, la, w) {                                                                  // 2912
        if (w === void 0) { w = 1; }                                                                                   // 2913
        computeLinkLengths(links, w, function (a, b) { return Math.sqrt(unionCount(a, b) - intersectionCount(a, b)); }, la);
    }                                                                                                                  // 2915
    cola.symmetricDiffLinkLengths = symmetricDiffLinkLengths;                                                          // 2916
    /** modify the specified links lengths based on the jaccard difference between their neighbours                    // 2917
     * @class jaccardLinkLengths                                                                                       // 2918
     */                                                                                                                // 2919
    function jaccardLinkLengths(links, la, w) {                                                                        // 2920
        if (w === void 0) { w = 1; }                                                                                   // 2921
        computeLinkLengths(links, w, function (a, b) {                                                                 // 2922
            return Math.min(Object.keys(a).length, Object.keys(b).length) < 1.1 ? 0 : intersectionCount(a, b) / unionCount(a, b);
        }, la);                                                                                                        // 2924
    }                                                                                                                  // 2925
    cola.jaccardLinkLengths = jaccardLinkLengths;                                                                      // 2926
    /** generate separation constraints for all edges unless both their source and sink are in the same strongly connected component
     * @class generateDirectedEdgeConstraints                                                                          // 2928
     */                                                                                                                // 2929
    function generateDirectedEdgeConstraints(n, links, axis, la) {                                                     // 2930
        var components = stronglyConnectedComponents(n, links, la);                                                    // 2931
        var nodes = {};                                                                                                // 2932
        components.forEach(function (c, i) {                                                                           // 2933
            return c.forEach(function (v) { return nodes[v] = i; });                                                   // 2934
        });                                                                                                            // 2935
        var constraints = [];                                                                                          // 2936
        links.forEach(function (l) {                                                                                   // 2937
            var ui = la.getSourceIndex(l), vi = la.getTargetIndex(l), u = nodes[ui], v = nodes[vi];                    // 2938
            if (u !== v) {                                                                                             // 2939
                constraints.push({                                                                                     // 2940
                    axis: axis,                                                                                        // 2941
                    left: ui,                                                                                          // 2942
                    right: vi,                                                                                         // 2943
                    gap: la.getMinSeparation(l)                                                                        // 2944
                });                                                                                                    // 2945
            }                                                                                                          // 2946
        });                                                                                                            // 2947
        return constraints;                                                                                            // 2948
    }                                                                                                                  // 2949
    cola.generateDirectedEdgeConstraints = generateDirectedEdgeConstraints;                                            // 2950
    /**                                                                                                                // 2951
     * Tarjan's strongly connected components algorithm for directed graphs                                            // 2952
     * returns an array of arrays of node indicies in each of the strongly connected components.                       // 2953
     * a vertex not in a SCC of two or more nodes is it's own SCC.                                                     // 2954
     * adaptation of https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm                  // 2955
     */                                                                                                                // 2956
    function stronglyConnectedComponents(numVertices, edges, la) {                                                     // 2957
        var nodes = [];                                                                                                // 2958
        var index = 0;                                                                                                 // 2959
        var stack = [];                                                                                                // 2960
        var components = [];                                                                                           // 2961
        function strongConnect(v) {                                                                                    // 2962
            // Set the depth index for v to the smallest unused index                                                  // 2963
            v.index = v.lowlink = index++;                                                                             // 2964
            stack.push(v);                                                                                             // 2965
            v.onStack = true;                                                                                          // 2966
            // Consider successors of v                                                                                // 2967
            for (var _i = 0, _a = v.out; _i < _a.length; _i++) {                                                       // 2968
                var w = _a[_i];                                                                                        // 2969
                if (typeof w.index === 'undefined') {                                                                  // 2970
                    // Successor w has not yet been visited; recurse on it                                             // 2971
                    strongConnect(w);                                                                                  // 2972
                    v.lowlink = Math.min(v.lowlink, w.lowlink);                                                        // 2973
                }                                                                                                      // 2974
                else if (w.onStack) {                                                                                  // 2975
                    // Successor w is in stack S and hence in the current SCC                                          // 2976
                    v.lowlink = Math.min(v.lowlink, w.index);                                                          // 2977
                }                                                                                                      // 2978
            }                                                                                                          // 2979
            // If v is a root node, pop the stack and generate an SCC                                                  // 2980
            if (v.lowlink === v.index) {                                                                               // 2981
                // start a new strongly connected component                                                            // 2982
                var component = [];                                                                                    // 2983
                while (stack.length) {                                                                                 // 2984
                    w = stack.pop();                                                                                   // 2985
                    w.onStack = false;                                                                                 // 2986
                    //add w to current strongly connected component                                                    // 2987
                    component.push(w);                                                                                 // 2988
                    if (w === v)                                                                                       // 2989
                        break;                                                                                         // 2990
                }                                                                                                      // 2991
                // output the current strongly connected component                                                     // 2992
                components.push(component.map(function (v) { return v.id; }));                                         // 2993
            }                                                                                                          // 2994
        }                                                                                                              // 2995
        for (var i = 0; i < numVertices; i++) {                                                                        // 2996
            nodes.push({ id: i, out: [] });                                                                            // 2997
        }                                                                                                              // 2998
        for (var _i = 0; _i < edges.length; _i++) {                                                                    // 2999
            var e = edges[_i];                                                                                         // 3000
            var v_1 = nodes[la.getSourceIndex(e)], w = nodes[la.getTargetIndex(e)];                                    // 3001
            v_1.out.push(w);                                                                                           // 3002
        }                                                                                                              // 3003
        for (var _a = 0; _a < nodes.length; _a++) {                                                                    // 3004
            var v = nodes[_a];                                                                                         // 3005
            if (typeof v.index === 'undefined')                                                                        // 3006
                strongConnect(v);                                                                                      // 3007
        }                                                                                                              // 3008
        return components;                                                                                             // 3009
    }                                                                                                                  // 3010
    cola.stronglyConnectedComponents = stronglyConnectedComponents;                                                    // 3011
})(cola || (cola = {}));                                                                                               // 3012
var PairingHeap = (function () {                                                                                       // 3013
    // from: https://gist.github.com/nervoussystem                                                                     // 3014
    //{elem:object, subheaps:[array of heaps]}                                                                         // 3015
    function PairingHeap(elem) {                                                                                       // 3016
        this.elem = elem;                                                                                              // 3017
        this.subheaps = [];                                                                                            // 3018
    }                                                                                                                  // 3019
    PairingHeap.prototype.toString = function (selector) {                                                             // 3020
        var str = "", needComma = false;                                                                               // 3021
        for (var i = 0; i < this.subheaps.length; ++i) {                                                               // 3022
            var subheap = this.subheaps[i];                                                                            // 3023
            if (!subheap.elem) {                                                                                       // 3024
                needComma = false;                                                                                     // 3025
                continue;                                                                                              // 3026
            }                                                                                                          // 3027
            if (needComma) {                                                                                           // 3028
                str = str + ",";                                                                                       // 3029
            }                                                                                                          // 3030
            str = str + subheap.toString(selector);                                                                    // 3031
            needComma = true;                                                                                          // 3032
        }                                                                                                              // 3033
        if (str !== "") {                                                                                              // 3034
            str = "(" + str + ")";                                                                                     // 3035
        }                                                                                                              // 3036
        return (this.elem ? selector(this.elem) : "") + str;                                                           // 3037
    };                                                                                                                 // 3038
    PairingHeap.prototype.forEach = function (f) {                                                                     // 3039
        if (!this.empty()) {                                                                                           // 3040
            f(this.elem, this);                                                                                        // 3041
            this.subheaps.forEach(function (s) { return s.forEach(f); });                                              // 3042
        }                                                                                                              // 3043
    };                                                                                                                 // 3044
    PairingHeap.prototype.count = function () {                                                                        // 3045
        return this.empty() ? 0 : 1 + this.subheaps.reduce(function (n, h) {                                           // 3046
            return n + h.count();                                                                                      // 3047
        }, 0);                                                                                                         // 3048
    };                                                                                                                 // 3049
    PairingHeap.prototype.min = function () {                                                                          // 3050
        return this.elem;                                                                                              // 3051
    };                                                                                                                 // 3052
    PairingHeap.prototype.empty = function () {                                                                        // 3053
        return this.elem == null;                                                                                      // 3054
    };                                                                                                                 // 3055
    PairingHeap.prototype.contains = function (h) {                                                                    // 3056
        if (this === h)                                                                                                // 3057
            return true;                                                                                               // 3058
        for (var i = 0; i < this.subheaps.length; i++) {                                                               // 3059
            if (this.subheaps[i].contains(h))                                                                          // 3060
                return true;                                                                                           // 3061
        }                                                                                                              // 3062
        return false;                                                                                                  // 3063
    };                                                                                                                 // 3064
    PairingHeap.prototype.isHeap = function (lessThan) {                                                               // 3065
        var _this = this;                                                                                              // 3066
        return this.subheaps.every(function (h) { return lessThan(_this.elem, h.elem) && h.isHeap(lessThan); });       // 3067
    };                                                                                                                 // 3068
    PairingHeap.prototype.insert = function (obj, lessThan) {                                                          // 3069
        return this.merge(new PairingHeap(obj), lessThan);                                                             // 3070
    };                                                                                                                 // 3071
    PairingHeap.prototype.merge = function (heap2, lessThan) {                                                         // 3072
        if (this.empty())                                                                                              // 3073
            return heap2;                                                                                              // 3074
        else if (heap2.empty())                                                                                        // 3075
            return this;                                                                                               // 3076
        else if (lessThan(this.elem, heap2.elem)) {                                                                    // 3077
            this.subheaps.push(heap2);                                                                                 // 3078
            return this;                                                                                               // 3079
        }                                                                                                              // 3080
        else {                                                                                                         // 3081
            heap2.subheaps.push(this);                                                                                 // 3082
            return heap2;                                                                                              // 3083
        }                                                                                                              // 3084
    };                                                                                                                 // 3085
    PairingHeap.prototype.removeMin = function (lessThan) {                                                            // 3086
        if (this.empty())                                                                                              // 3087
            return null;                                                                                               // 3088
        else                                                                                                           // 3089
            return this.mergePairs(lessThan);                                                                          // 3090
    };                                                                                                                 // 3091
    PairingHeap.prototype.mergePairs = function (lessThan) {                                                           // 3092
        if (this.subheaps.length == 0)                                                                                 // 3093
            return new PairingHeap(null);                                                                              // 3094
        else if (this.subheaps.length == 1) {                                                                          // 3095
            return this.subheaps[0];                                                                                   // 3096
        }                                                                                                              // 3097
        else {                                                                                                         // 3098
            var firstPair = this.subheaps.pop().merge(this.subheaps.pop(), lessThan);                                  // 3099
            var remaining = this.mergePairs(lessThan);                                                                 // 3100
            return firstPair.merge(remaining, lessThan);                                                               // 3101
        }                                                                                                              // 3102
    };                                                                                                                 // 3103
    PairingHeap.prototype.decreaseKey = function (subheap, newValue, setHeapNode, lessThan) {                          // 3104
        var newHeap = subheap.removeMin(lessThan);                                                                     // 3105
        //reassign subheap values to preserve tree                                                                     // 3106
        subheap.elem = newHeap.elem;                                                                                   // 3107
        subheap.subheaps = newHeap.subheaps;                                                                           // 3108
        if (setHeapNode !== null && newHeap.elem !== null) {                                                           // 3109
            setHeapNode(subheap.elem, subheap);                                                                        // 3110
        }                                                                                                              // 3111
        var pairingNode = new PairingHeap(newValue);                                                                   // 3112
        if (setHeapNode !== null) {                                                                                    // 3113
            setHeapNode(newValue, pairingNode);                                                                        // 3114
        }                                                                                                              // 3115
        return this.merge(pairingNode, lessThan);                                                                      // 3116
    };                                                                                                                 // 3117
    return PairingHeap;                                                                                                // 3118
})();                                                                                                                  // 3119
/**                                                                                                                    // 3120
 * @class PriorityQueue a min priority queue backed by a pairing heap                                                  // 3121
 */                                                                                                                    // 3122
var PriorityQueue = (function () {                                                                                     // 3123
    function PriorityQueue(lessThan) {                                                                                 // 3124
        this.lessThan = lessThan;                                                                                      // 3125
    }                                                                                                                  // 3126
    /**                                                                                                                // 3127
     * @method top                                                                                                     // 3128
     * @return the top element (the min element as defined by lessThan)                                                // 3129
     */                                                                                                                // 3130
    PriorityQueue.prototype.top = function () {                                                                        // 3131
        if (this.empty()) {                                                                                            // 3132
            return null;                                                                                               // 3133
        }                                                                                                              // 3134
        return this.root.elem;                                                                                         // 3135
    };                                                                                                                 // 3136
    /**                                                                                                                // 3137
     * @method push                                                                                                    // 3138
     * put things on the heap                                                                                          // 3139
     */                                                                                                                // 3140
    PriorityQueue.prototype.push = function () {                                                                       // 3141
        var args = [];                                                                                                 // 3142
        for (var _i = 0; _i < arguments.length; _i++) {                                                                // 3143
            args[_i - 0] = arguments[_i];                                                                              // 3144
        }                                                                                                              // 3145
        var pairingNode;                                                                                               // 3146
        for (var i = 0, arg; arg = args[i]; ++i) {                                                                     // 3147
            pairingNode = new PairingHeap(arg);                                                                        // 3148
            this.root = this.empty() ?                                                                                 // 3149
                pairingNode : this.root.merge(pairingNode, this.lessThan);                                             // 3150
        }                                                                                                              // 3151
        return pairingNode;                                                                                            // 3152
    };                                                                                                                 // 3153
    /**                                                                                                                // 3154
     * @method empty                                                                                                   // 3155
     * @return true if no more elements in queue                                                                       // 3156
     */                                                                                                                // 3157
    PriorityQueue.prototype.empty = function () {                                                                      // 3158
        return !this.root || !this.root.elem;                                                                          // 3159
    };                                                                                                                 // 3160
    /**                                                                                                                // 3161
     * @method isHeap check heap condition (for testing)                                                               // 3162
     * @return true if queue is in valid state                                                                         // 3163
     */                                                                                                                // 3164
    PriorityQueue.prototype.isHeap = function () {                                                                     // 3165
        return this.root.isHeap(this.lessThan);                                                                        // 3166
    };                                                                                                                 // 3167
    /**                                                                                                                // 3168
     * @method forEach apply f to each element of the queue                                                            // 3169
     * @param f function to apply                                                                                      // 3170
     */                                                                                                                // 3171
    PriorityQueue.prototype.forEach = function (f) {                                                                   // 3172
        this.root.forEach(f);                                                                                          // 3173
    };                                                                                                                 // 3174
    /**                                                                                                                // 3175
     * @method pop remove and return the min element from the queue                                                    // 3176
     */                                                                                                                // 3177
    PriorityQueue.prototype.pop = function () {                                                                        // 3178
        if (this.empty()) {                                                                                            // 3179
            return null;                                                                                               // 3180
        }                                                                                                              // 3181
        var obj = this.root.min();                                                                                     // 3182
        this.root = this.root.removeMin(this.lessThan);                                                                // 3183
        return obj;                                                                                                    // 3184
    };                                                                                                                 // 3185
    /**                                                                                                                // 3186
     * @method reduceKey reduce the key value of the specified heap node                                               // 3187
     */                                                                                                                // 3188
    PriorityQueue.prototype.reduceKey = function (heapNode, newKey, setHeapNode) {                                     // 3189
        if (setHeapNode === void 0) { setHeapNode = null; }                                                            // 3190
        this.root = this.root.decreaseKey(heapNode, newKey, setHeapNode, this.lessThan);                               // 3191
    };                                                                                                                 // 3192
    PriorityQueue.prototype.toString = function (selector) {                                                           // 3193
        return this.root.toString(selector);                                                                           // 3194
    };                                                                                                                 // 3195
    /**                                                                                                                // 3196
     * @method count                                                                                                   // 3197
     * @return number of elements in queue                                                                             // 3198
     */                                                                                                                // 3199
    PriorityQueue.prototype.count = function () {                                                                      // 3200
        return this.root.count();                                                                                      // 3201
    };                                                                                                                 // 3202
    return PriorityQueue;                                                                                              // 3203
})();                                                                                                                  // 3204
///<reference path="pqueue.ts"/>                                                                                       // 3205
/**                                                                                                                    // 3206
 * @module shortestpaths                                                                                               // 3207
 */                                                                                                                    // 3208
var cola;                                                                                                              // 3209
(function (cola) {                                                                                                     // 3210
    var shortestpaths;                                                                                                 // 3211
    (function (shortestpaths) {                                                                                        // 3212
        var Neighbour = (function () {                                                                                 // 3213
            function Neighbour(id, distance) {                                                                         // 3214
                this.id = id;                                                                                          // 3215
                this.distance = distance;                                                                              // 3216
            }                                                                                                          // 3217
            return Neighbour;                                                                                          // 3218
        })();                                                                                                          // 3219
        var Node = (function () {                                                                                      // 3220
            function Node(id) {                                                                                        // 3221
                this.id = id;                                                                                          // 3222
                this.neighbours = [];                                                                                  // 3223
            }                                                                                                          // 3224
            return Node;                                                                                               // 3225
        })();                                                                                                          // 3226
        var QueueEntry = (function () {                                                                                // 3227
            function QueueEntry(node, prev, d) {                                                                       // 3228
                this.node = node;                                                                                      // 3229
                this.prev = prev;                                                                                      // 3230
                this.d = d;                                                                                            // 3231
            }                                                                                                          // 3232
            return QueueEntry;                                                                                         // 3233
        })();                                                                                                          // 3234
        /**                                                                                                            // 3235
         * calculates all-pairs shortest paths or shortest paths from a single node                                    // 3236
         * @class Calculator                                                                                           // 3237
         * @constructor                                                                                                // 3238
         * @param n {number} number of nodes                                                                           // 3239
         * @param es {Edge[]} array of edges                                                                           // 3240
         */                                                                                                            // 3241
        var Calculator = (function () {                                                                                // 3242
            function Calculator(n, es, getSourceIndex, getTargetIndex, getLength) {                                    // 3243
                this.n = n;                                                                                            // 3244
                this.es = es;                                                                                          // 3245
                this.neighbours = new Array(this.n);                                                                   // 3246
                var i = this.n;                                                                                        // 3247
                while (i--)                                                                                            // 3248
                    this.neighbours[i] = new Node(i);                                                                  // 3249
                i = this.es.length;                                                                                    // 3250
                while (i--) {                                                                                          // 3251
                    var e = this.es[i];                                                                                // 3252
                    var u = getSourceIndex(e), v = getTargetIndex(e);                                                  // 3253
                    var d = getLength(e);                                                                              // 3254
                    this.neighbours[u].neighbours.push(new Neighbour(v, d));                                           // 3255
                    this.neighbours[v].neighbours.push(new Neighbour(u, d));                                           // 3256
                }                                                                                                      // 3257
            }                                                                                                          // 3258
            /**                                                                                                        // 3259
             * compute shortest paths for graph over n nodes with edges an array of source/target pairs                // 3260
             * edges may optionally have a length attribute.  1 is the default.                                        // 3261
             * Uses Johnson's algorithm.                                                                               // 3262
             *                                                                                                         // 3263
             * @method DistanceMatrix                                                                                  // 3264
             * @return the distance matrix                                                                             // 3265
             */                                                                                                        // 3266
            Calculator.prototype.DistanceMatrix = function () {                                                        // 3267
                var D = new Array(this.n);                                                                             // 3268
                for (var i = 0; i < this.n; ++i) {                                                                     // 3269
                    D[i] = this.dijkstraNeighbours(i);                                                                 // 3270
                }                                                                                                      // 3271
                return D;                                                                                              // 3272
            };                                                                                                         // 3273
            /**                                                                                                        // 3274
             * get shortest paths from a specified start node                                                          // 3275
             * @method DistancesFromNode                                                                               // 3276
             * @param start node index                                                                                 // 3277
             * @return array of path lengths                                                                           // 3278
             */                                                                                                        // 3279
            Calculator.prototype.DistancesFromNode = function (start) {                                                // 3280
                return this.dijkstraNeighbours(start);                                                                 // 3281
            };                                                                                                         // 3282
            Calculator.prototype.PathFromNodeToNode = function (start, end) {                                          // 3283
                return this.dijkstraNeighbours(start, end);                                                            // 3284
            };                                                                                                         // 3285
            // find shortest path from start to end, with the opportunity at                                           // 3286
            // each edge traversal to compute a custom cost based on the                                               // 3287
            // previous edge.  For example, to penalise bends.                                                         // 3288
            Calculator.prototype.PathFromNodeToNodeWithPrevCost = function (start, end, prevCost) {                    // 3289
                var q = new PriorityQueue(function (a, b) { return a.d <= b.d; }), u = this.neighbours[start], qu = new QueueEntry(u, null, 0), visitedFrom = {};
                q.push(qu);                                                                                            // 3291
                while (!q.empty()) {                                                                                   // 3292
                    qu = q.pop();                                                                                      // 3293
                    u = qu.node;                                                                                       // 3294
                    if (u.id === end) {                                                                                // 3295
                        break;                                                                                         // 3296
                    }                                                                                                  // 3297
                    var i = u.neighbours.length;                                                                       // 3298
                    while (i--) {                                                                                      // 3299
                        var neighbour = u.neighbours[i], v = this.neighbours[neighbour.id];                            // 3300
                        // don't double back                                                                           // 3301
                        if (qu.prev && v.id === qu.prev.node.id)                                                       // 3302
                            continue;                                                                                  // 3303
                        // don't retraverse an edge if it has already been explored                                    // 3304
                        // from a lower cost route                                                                     // 3305
                        var viduid = v.id + ',' + u.id;                                                                // 3306
                        if (viduid in visitedFrom && visitedFrom[viduid] <= qu.d)                                      // 3307
                            continue;                                                                                  // 3308
                        var cc = qu.prev ? prevCost(qu.prev.node.id, u.id, v.id) : 0, t = qu.d + neighbour.distance + cc;
                        // store cost of this traversal                                                                // 3310
                        visitedFrom[viduid] = t;                                                                       // 3311
                        q.push(new QueueEntry(v, qu, t));                                                              // 3312
                    }                                                                                                  // 3313
                }                                                                                                      // 3314
                var path = [];                                                                                         // 3315
                while (qu.prev) {                                                                                      // 3316
                    qu = qu.prev;                                                                                      // 3317
                    path.push(qu.node.id);                                                                             // 3318
                }                                                                                                      // 3319
                return path;                                                                                           // 3320
            };                                                                                                         // 3321
            Calculator.prototype.dijkstraNeighbours = function (start, dest) {                                         // 3322
                if (dest === void 0) { dest = -1; }                                                                    // 3323
                var q = new PriorityQueue(function (a, b) { return a.d <= b.d; }), i = this.neighbours.length, d = new Array(i);
                while (i--) {                                                                                          // 3325
                    var node = this.neighbours[i];                                                                     // 3326
                    node.d = i === start ? 0 : Number.POSITIVE_INFINITY;                                               // 3327
                    node.q = q.push(node);                                                                             // 3328
                }                                                                                                      // 3329
                while (!q.empty()) {                                                                                   // 3330
                    // console.log(q.toString(function (u) { return u.id + "=" + (u.d === Number.POSITIVE_INFINITY ? "\u221E" : u.d.toFixed(2) )}));
                    var u = q.pop();                                                                                   // 3332
                    d[u.id] = u.d;                                                                                     // 3333
                    if (u.id === dest) {                                                                               // 3334
                        var path = [];                                                                                 // 3335
                        var v = u;                                                                                     // 3336
                        while (typeof v.prev !== 'undefined') {                                                        // 3337
                            path.push(v.prev.id);                                                                      // 3338
                            v = v.prev;                                                                                // 3339
                        }                                                                                              // 3340
                        return path;                                                                                   // 3341
                    }                                                                                                  // 3342
                    i = u.neighbours.length;                                                                           // 3343
                    while (i--) {                                                                                      // 3344
                        var neighbour = u.neighbours[i];                                                               // 3345
                        var v = this.neighbours[neighbour.id];                                                         // 3346
                        var t = u.d + neighbour.distance;                                                              // 3347
                        if (u.d !== Number.MAX_VALUE && v.d > t) {                                                     // 3348
                            v.d = t;                                                                                   // 3349
                            v.prev = u;                                                                                // 3350
                            q.reduceKey(v.q, v, function (e, q) { return e.q = q; });                                  // 3351
                        }                                                                                              // 3352
                    }                                                                                                  // 3353
                }                                                                                                      // 3354
                return d;                                                                                              // 3355
            };                                                                                                         // 3356
            return Calculator;                                                                                         // 3357
        })();                                                                                                          // 3358
        shortestpaths.Calculator = Calculator;                                                                         // 3359
    })(shortestpaths = cola.shortestpaths || (cola.shortestpaths = {}));                                               // 3360
})(cola || (cola = {}));                                                                                               // 3361
///<reference path="handledisconnected.ts"/>                                                                           // 3362
///<reference path="geom.ts"/>                                                                                         // 3363
///<reference path="descent.ts"/>                                                                                      // 3364
///<reference path="powergraph.ts"/>                                                                                   // 3365
///<reference path="linklengths.ts"/>                                                                                  // 3366
///<reference path="shortestpaths.ts"/>                                                                                // 3367
/**                                                                                                                    // 3368
 * @module cola                                                                                                        // 3369
 */                                                                                                                    // 3370
var cola;                                                                                                              // 3371
(function (cola) {                                                                                                     // 3372
    /**                                                                                                                // 3373
     * The layout process fires three events:                                                                          // 3374
     *  - start: layout iterations started                                                                             // 3375
     *  - tick: fired once per iteration, listen to this to animate                                                    // 3376
     *  - end: layout converged, you might like to zoom-to-fit or something at notification of this event              // 3377
     */                                                                                                                // 3378
    (function (EventType) {                                                                                            // 3379
        EventType[EventType["start"] = 0] = "start";                                                                   // 3380
        EventType[EventType["tick"] = 1] = "tick";                                                                     // 3381
        EventType[EventType["end"] = 2] = "end";                                                                       // 3382
    })(cola.EventType || (cola.EventType = {}));                                                                       // 3383
    var EventType = cola.EventType;                                                                                    // 3384
    ;                                                                                                                  // 3385
    function isGroup(g) {                                                                                              // 3386
        return typeof g.leaves !== 'undefined' || typeof g.groups !== 'undefined';                                     // 3387
    }                                                                                                                  // 3388
    /**                                                                                                                // 3389
     * Main interface to cola layout.                                                                                  // 3390
     * @class Layout                                                                                                   // 3391
     */                                                                                                                // 3392
    var Layout = (function () {                                                                                        // 3393
        function Layout() {                                                                                            // 3394
            var _this = this;                                                                                          // 3395
            this._canvasSize = [1, 1];                                                                                 // 3396
            this._linkDistance = 20;                                                                                   // 3397
            this._defaultNodeSize = 10;                                                                                // 3398
            this._linkLengthCalculator = null;                                                                         // 3399
            this._linkType = null;                                                                                     // 3400
            this._avoidOverlaps = false;                                                                               // 3401
            this._handleDisconnected = true;                                                                           // 3402
            this._running = false;                                                                                     // 3403
            this._nodes = [];                                                                                          // 3404
            this._groups = [];                                                                                         // 3405
            this._rootGroup = null;                                                                                    // 3406
            this._links = [];                                                                                          // 3407
            this._constraints = [];                                                                                    // 3408
            this._distanceMatrix = null;                                                                               // 3409
            this._descent = null;                                                                                      // 3410
            this._directedLinkConstraints = null;                                                                      // 3411
            this._threshold = 0.01;                                                                                    // 3412
            this._visibilityGraph = null;                                                                              // 3413
            this._groupCompactness = 1e-6;                                                                             // 3414
            // sub-class and override this property to replace with a more sophisticated eventing mechanism            // 3415
            this.event = null;                                                                                         // 3416
            this.linkAccessor = {                                                                                      // 3417
                getSourceIndex: Layout.getSourceIndex,                                                                 // 3418
                getTargetIndex: Layout.getTargetIndex,                                                                 // 3419
                setLength: Layout.setLinkLength,                                                                       // 3420
                getType: function (l) { return typeof _this._linkType === "function" ? _this._linkType(l) : 0; }       // 3421
            };                                                                                                         // 3422
        }                                                                                                              // 3423
        // subscribe a listener to an event                                                                            // 3424
        // sub-class and override this method to replace with a more sophisticated eventing mechanism                  // 3425
        Layout.prototype.on = function (e, listener) {                                                                 // 3426
            // override me!                                                                                            // 3427
            if (!this.event)                                                                                           // 3428
                this.event = {};                                                                                       // 3429
            if (typeof e === 'string') {                                                                               // 3430
                this.event[EventType[e]] = listener;                                                                   // 3431
            }                                                                                                          // 3432
            else {                                                                                                     // 3433
                this.event[e] = listener;                                                                              // 3434
            }                                                                                                          // 3435
            return this;                                                                                               // 3436
        };                                                                                                             // 3437
        // a function that is notified of events like "tick"                                                           // 3438
        // sub-class and override this method to replace with a more sophisticated eventing mechanism                  // 3439
        Layout.prototype.trigger = function (e) {                                                                      // 3440
            if (this.event && typeof this.event[e.type] !== 'undefined') {                                             // 3441
                this.event[e.type](e);                                                                                 // 3442
            }                                                                                                          // 3443
        };                                                                                                             // 3444
        // a function that kicks off the iteration tick loop                                                           // 3445
        // it calls tick() repeatedly until tick returns true (is converged)                                           // 3446
        // subclass and override it with something fancier (e.g. dispatch tick on a timer)                             // 3447
        Layout.prototype.kick = function () {                                                                          // 3448
            while (!this.tick())                                                                                       // 3449
                ;                                                                                                      // 3450
        };                                                                                                             // 3451
        /**                                                                                                            // 3452
         * iterate the layout.  Returns true when layout converged.                                                    // 3453
         */                                                                                                            // 3454
        Layout.prototype.tick = function () {                                                                          // 3455
            if (this._alpha < this._threshold) {                                                                       // 3456
                this._running = false;                                                                                 // 3457
                this.trigger({ type: EventType.end, alpha: this._alpha = 0, stress: this._lastStress });               // 3458
                return true;                                                                                           // 3459
            }                                                                                                          // 3460
            var n = this._nodes.length, m = this._links.length;                                                        // 3461
            var o, i;                                                                                                  // 3462
            this._descent.locks.clear();                                                                               // 3463
            for (i = 0; i < n; ++i) {                                                                                  // 3464
                o = this._nodes[i];                                                                                    // 3465
                if (o.fixed) {                                                                                         // 3466
                    if (typeof o.px === 'undefined' || typeof o.py === 'undefined') {                                  // 3467
                        o.px = o.x;                                                                                    // 3468
                        o.py = o.y;                                                                                    // 3469
                    }                                                                                                  // 3470
                    var p = [o.px, o.py];                                                                              // 3471
                    this._descent.locks.add(i, p);                                                                     // 3472
                }                                                                                                      // 3473
            }                                                                                                          // 3474
            var s1 = this._descent.rungeKutta();                                                                       // 3475
            //var s1 = descent.reduceStress();                                                                         // 3476
            if (s1 === 0) {                                                                                            // 3477
                this._alpha = 0;                                                                                       // 3478
            }                                                                                                          // 3479
            else if (typeof this._lastStress !== 'undefined') {                                                        // 3480
                this._alpha = s1; //Math.abs(Math.abs(this._lastStress / s1) - 1);                                     // 3481
            }                                                                                                          // 3482
            this._lastStress = s1;                                                                                     // 3483
            this.updateNodePositions();                                                                                // 3484
            this.trigger({ type: EventType.tick, alpha: this._alpha, stress: this._lastStress });                      // 3485
            return false;                                                                                              // 3486
        };                                                                                                             // 3487
        // copy positions out of descent instance into each of the nodes' center coords                                // 3488
        Layout.prototype.updateNodePositions = function () {                                                           // 3489
            var x = this._descent.x[0], y = this._descent.x[1];                                                        // 3490
            var o, i = this._nodes.length;                                                                             // 3491
            while (i--) {                                                                                              // 3492
                o = this._nodes[i];                                                                                    // 3493
                o.x = x[i];                                                                                            // 3494
                o.y = y[i];                                                                                            // 3495
            }                                                                                                          // 3496
        };                                                                                                             // 3497
        Layout.prototype.nodes = function (v) {                                                                        // 3498
            if (!v) {                                                                                                  // 3499
                if (this._nodes.length === 0 && this._links.length > 0) {                                              // 3500
                    // if we have links but no nodes, create the nodes array now with empty objects for the links to point at.
                    // in this case the links are expected to be numeric indices for nodes in the range 0..n-1 where n is the number of nodes
                    var n = 0;                                                                                         // 3503
                    this._links.forEach(function (l) {                                                                 // 3504
                        n = Math.max(n, l.source, l.target);                                                           // 3505
                    });                                                                                                // 3506
                    this._nodes = new Array(++n);                                                                      // 3507
                    for (var i = 0; i < n; ++i) {                                                                      // 3508
                        this._nodes[i] = {};                                                                           // 3509
                    }                                                                                                  // 3510
                }                                                                                                      // 3511
                return this._nodes;                                                                                    // 3512
            }                                                                                                          // 3513
            this._nodes = v;                                                                                           // 3514
            return this;                                                                                               // 3515
        };                                                                                                             // 3516
        Layout.prototype.groups = function (x) {                                                                       // 3517
            var _this = this;                                                                                          // 3518
            if (!x)                                                                                                    // 3519
                return this._groups;                                                                                   // 3520
            this._groups = x;                                                                                          // 3521
            this._rootGroup = {};                                                                                      // 3522
            this._groups.forEach(function (g) {                                                                        // 3523
                if (typeof g.padding === "undefined")                                                                  // 3524
                    g.padding = 1;                                                                                     // 3525
                if (typeof g.leaves !== "undefined")                                                                   // 3526
                    g.leaves.forEach(function (v, i) { (g.leaves[i] = _this._nodes[v]).parent = g; });                 // 3527
                if (typeof g.groups !== "undefined")                                                                   // 3528
                    g.groups.forEach(function (gi, i) { (g.groups[i] = _this._groups[gi]).parent = g; });              // 3529
            });                                                                                                        // 3530
            this._rootGroup.leaves = this._nodes.filter(function (v) { return typeof v.parent === 'undefined'; });     // 3531
            this._rootGroup.groups = this._groups.filter(function (g) { return typeof g.parent === 'undefined'; });    // 3532
            return this;                                                                                               // 3533
        };                                                                                                             // 3534
        Layout.prototype.powerGraphGroups = function (f) {                                                             // 3535
            var g = cola.powergraph.getGroups(this._nodes, this._links, this.linkAccessor, this._rootGroup);           // 3536
            this.groups(g.groups);                                                                                     // 3537
            f(g);                                                                                                      // 3538
            return this;                                                                                               // 3539
        };                                                                                                             // 3540
        Layout.prototype.avoidOverlaps = function (v) {                                                                // 3541
            if (!arguments.length)                                                                                     // 3542
                return this._avoidOverlaps;                                                                            // 3543
            this._avoidOverlaps = v;                                                                                   // 3544
            return this;                                                                                               // 3545
        };                                                                                                             // 3546
        Layout.prototype.handleDisconnected = function (v) {                                                           // 3547
            if (!arguments.length)                                                                                     // 3548
                return this._handleDisconnected;                                                                       // 3549
            this._handleDisconnected = v;                                                                              // 3550
            return this;                                                                                               // 3551
        };                                                                                                             // 3552
        /**                                                                                                            // 3553
         * causes constraints to be generated such that directed graphs are laid out either from left-to-right or top-to-bottom.
         * a separation constraint is generated in the selected axis for each edge that is not involved in a cycle (part of a strongly connected component)
         * @param axis {string} 'x' for left-to-right, 'y' for top-to-bottom                                           // 3556
         * @param minSeparation {number|link=>number} either a number specifying a minimum spacing required across all links or a function to return the minimum spacing for each link
         */                                                                                                            // 3558
        Layout.prototype.flowLayout = function (axis, minSeparation) {                                                 // 3559
            if (!arguments.length)                                                                                     // 3560
                axis = 'y';                                                                                            // 3561
            this._directedLinkConstraints = {                                                                          // 3562
                axis: axis,                                                                                            // 3563
                getMinSeparation: typeof minSeparation === 'number' ? function () { return minSeparation; } : minSeparation
            };                                                                                                         // 3565
            return this;                                                                                               // 3566
        };                                                                                                             // 3567
        Layout.prototype.links = function (x) {                                                                        // 3568
            if (!arguments.length)                                                                                     // 3569
                return this._links;                                                                                    // 3570
            this._links = x;                                                                                           // 3571
            return this;                                                                                               // 3572
        };                                                                                                             // 3573
        Layout.prototype.constraints = function (c) {                                                                  // 3574
            if (!arguments.length)                                                                                     // 3575
                return this._constraints;                                                                              // 3576
            this._constraints = c;                                                                                     // 3577
            return this;                                                                                               // 3578
        };                                                                                                             // 3579
        Layout.prototype.distanceMatrix = function (d) {                                                               // 3580
            if (!arguments.length)                                                                                     // 3581
                return this._distanceMatrix;                                                                           // 3582
            this._distanceMatrix = d;                                                                                  // 3583
            return this;                                                                                               // 3584
        };                                                                                                             // 3585
        Layout.prototype.size = function (x) {                                                                         // 3586
            if (!x)                                                                                                    // 3587
                return this._canvasSize;                                                                               // 3588
            this._canvasSize = x;                                                                                      // 3589
            return this;                                                                                               // 3590
        };                                                                                                             // 3591
        Layout.prototype.defaultNodeSize = function (x) {                                                              // 3592
            if (!x)                                                                                                    // 3593
                return this._defaultNodeSize;                                                                          // 3594
            this._defaultNodeSize = x;                                                                                 // 3595
            return this;                                                                                               // 3596
        };                                                                                                             // 3597
        Layout.prototype.groupCompactness = function (x) {                                                             // 3598
            if (!x)                                                                                                    // 3599
                return this._groupCompactness;                                                                         // 3600
            this._groupCompactness = x;                                                                                // 3601
            return this;                                                                                               // 3602
        };                                                                                                             // 3603
        Layout.prototype.linkDistance = function (x) {                                                                 // 3604
            if (!x) {                                                                                                  // 3605
                return this._linkDistance;                                                                             // 3606
            }                                                                                                          // 3607
            this._linkDistance = typeof x === "function" ? x : +x;                                                     // 3608
            this._linkLengthCalculator = null;                                                                         // 3609
            return this;                                                                                               // 3610
        };                                                                                                             // 3611
        Layout.prototype.linkType = function (f) {                                                                     // 3612
            this._linkType = f;                                                                                        // 3613
            return this;                                                                                               // 3614
        };                                                                                                             // 3615
        Layout.prototype.convergenceThreshold = function (x) {                                                         // 3616
            if (!x)                                                                                                    // 3617
                return this._threshold;                                                                                // 3618
            this._threshold = typeof x === "function" ? x : +x;                                                        // 3619
            return this;                                                                                               // 3620
        };                                                                                                             // 3621
        Layout.prototype.alpha = function (x) {                                                                        // 3622
            if (!arguments.length)                                                                                     // 3623
                return this._alpha;                                                                                    // 3624
            else {                                                                                                     // 3625
                x = +x;                                                                                                // 3626
                if (this._alpha) {                                                                                     // 3627
                    if (x > 0)                                                                                         // 3628
                        this._alpha = x; // we might keep it hot                                                       // 3629
                    else                                                                                               // 3630
                        this._alpha = 0; // or, next tick will dispatch "end"                                          // 3631
                }                                                                                                      // 3632
                else if (x > 0) {                                                                                      // 3633
                    if (!this._running) {                                                                              // 3634
                        this._running = true;                                                                          // 3635
                        this.trigger({ type: EventType.start, alpha: this._alpha = x });                               // 3636
                        this.kick();                                                                                   // 3637
                    }                                                                                                  // 3638
                }                                                                                                      // 3639
                return this;                                                                                           // 3640
            }                                                                                                          // 3641
        };                                                                                                             // 3642
        Layout.prototype.getLinkLength = function (link) {                                                             // 3643
            return typeof this._linkDistance === "function" ? +(this._linkDistance(link)) : this._linkDistance;        // 3644
        };                                                                                                             // 3645
        Layout.setLinkLength = function (link, length) {                                                               // 3646
            link.length = length;                                                                                      // 3647
        };                                                                                                             // 3648
        Layout.prototype.getLinkType = function (link) {                                                               // 3649
            return typeof this._linkType === "function" ? this._linkType(link) : 0;                                    // 3650
        };                                                                                                             // 3651
        /**                                                                                                            // 3652
         * compute an ideal length for each link based on the graph structure around that link.                        // 3653
         * you can use this (for example) to create extra space around hub-nodes in dense graphs.                      // 3654
         * In particular this calculation is based on the "symmetric difference" in the neighbour sets of the source and target:
         * i.e. if neighbours of source is a and neighbours of target are b then calculation is: sqrt(|a union b| - |a intersection b|)
         * Actual computation based on inspection of link structure occurs in start(), so links themselves             // 3657
         * don't have to have been assigned before invoking this function.                                             // 3658
         * @param {number} [idealLength] the base length for an edge when its source and start have no other common neighbours (e.g. 40)
         * @param {number} [w] a multiplier for the effect of the length adjustment (e.g. 0.7)                         // 3660
         */                                                                                                            // 3661
        Layout.prototype.symmetricDiffLinkLengths = function (idealLength, w) {                                        // 3662
            var _this = this;                                                                                          // 3663
            if (w === void 0) { w = 1; }                                                                               // 3664
            this.linkDistance(function (l) { return idealLength * l.length; });                                        // 3665
            this._linkLengthCalculator = function () { return cola.symmetricDiffLinkLengths(_this._links, _this.linkAccessor, w); };
            return this;                                                                                               // 3667
        };                                                                                                             // 3668
        /**                                                                                                            // 3669
         * compute an ideal length for each link based on the graph structure around that link.                        // 3670
         * you can use this (for example) to create extra space around hub-nodes in dense graphs.                      // 3671
         * In particular this calculation is based on the "symmetric difference" in the neighbour sets of the source and target:
         * i.e. if neighbours of source is a and neighbours of target are b then calculation is: |a intersection b|/|a union b|
         * Actual computation based on inspection of link structure occurs in start(), so links themselves             // 3674
         * don't have to have been assigned before invoking this function.                                             // 3675
         * @param {number} [idealLength] the base length for an edge when its source and start have no other common neighbours (e.g. 40)
         * @param {number} [w] a multiplier for the effect of the length adjustment (e.g. 0.7)                         // 3677
         */                                                                                                            // 3678
        Layout.prototype.jaccardLinkLengths = function (idealLength, w) {                                              // 3679
            var _this = this;                                                                                          // 3680
            if (w === void 0) { w = 1; }                                                                               // 3681
            this.linkDistance(function (l) { return idealLength * l.length; });                                        // 3682
            this._linkLengthCalculator = function () { return cola.jaccardLinkLengths(_this._links, _this.linkAccessor, w); };
            return this;                                                                                               // 3684
        };                                                                                                             // 3685
        /**                                                                                                            // 3686
         * start the layout process                                                                                    // 3687
         * @method start                                                                                               // 3688
         * @param {number} [initialUnconstrainedIterations=0] unconstrained initial layout iterations                  // 3689
         * @param {number} [initialUserConstraintIterations=0] initial layout iterations with user-specified constraints
         * @param {number} [initialAllConstraintsIterations=0] initial layout iterations with all constraints including non-overlap
         * @param {number} [gridSnapIterations=0] iterations of "grid snap", which pulls nodes towards grid cell centers - grid of size node[0].width - only really makes sense if all nodes have the same width and height
         * @param [keepRunning=true] keep iterating asynchronously via the tick method                                 // 3693
         */                                                                                                            // 3694
        Layout.prototype.start = function (initialUnconstrainedIterations, initialUserConstraintIterations, initialAllConstraintsIterations, gridSnapIterations, keepRunning) {
            var _this = this;                                                                                          // 3696
            if (initialUnconstrainedIterations === void 0) { initialUnconstrainedIterations = 0; }                     // 3697
            if (initialUserConstraintIterations === void 0) { initialUserConstraintIterations = 0; }                   // 3698
            if (initialAllConstraintsIterations === void 0) { initialAllConstraintsIterations = 0; }                   // 3699
            if (gridSnapIterations === void 0) { gridSnapIterations = 0; }                                             // 3700
            if (keepRunning === void 0) { keepRunning = true; }                                                        // 3701
            var i, j, n = this.nodes().length, N = n + 2 * this._groups.length, m = this._links.length, w = this._canvasSize[0], h = this._canvasSize[1];
            if (this._linkLengthCalculator)                                                                            // 3703
                this._linkLengthCalculator();                                                                          // 3704
            var x = new Array(N), y = new Array(N);                                                                    // 3705
            var G = null;                                                                                              // 3706
            var ao = this._avoidOverlaps;                                                                              // 3707
            this._nodes.forEach(function (v, i) {                                                                      // 3708
                v.index = i;                                                                                           // 3709
                if (typeof v.x === 'undefined') {                                                                      // 3710
                    v.x = w / 2, v.y = h / 2;                                                                          // 3711
                }                                                                                                      // 3712
                x[i] = v.x, y[i] = v.y;                                                                                // 3713
            });                                                                                                        // 3714
            //should we do this to clearly label groups?                                                               // 3715
            //this._groups.forEach((g, i) => g.groupIndex = i);                                                        // 3716
            var distances;                                                                                             // 3717
            if (this._distanceMatrix) {                                                                                // 3718
                // use the user specified distanceMatrix                                                               // 3719
                distances = this._distanceMatrix;                                                                      // 3720
            }                                                                                                          // 3721
            else {                                                                                                     // 3722
                // construct an n X n distance matrix based on shortest paths through graph (with respect to edge.length).
                distances = (new cola.shortestpaths.Calculator(N, this._links, Layout.getSourceIndex, Layout.getTargetIndex, function (l) { return _this.getLinkLength(l); })).DistanceMatrix();
                // G is a square matrix with G[i][j] = 1 iff there exists an edge between node i and node j            // 3725
                // otherwise 2. (                                                                                      // 3726
                G = cola.Descent.createSquareMatrix(N, function () { return 2; });                                     // 3727
                this._links.forEach(function (l) {                                                                     // 3728
                    if (typeof l.source == "number")                                                                   // 3729
                        l.source = _this._nodes[l.source];                                                             // 3730
                    if (typeof l.target == "number")                                                                   // 3731
                        l.target = _this._nodes[l.target];                                                             // 3732
                });                                                                                                    // 3733
                this._links.forEach(function (e) {                                                                     // 3734
                    var u = Layout.getSourceIndex(e), v = Layout.getTargetIndex(e);                                    // 3735
                    G[u][v] = G[v][u] = e.weight || 1;                                                                 // 3736
                });                                                                                                    // 3737
            }                                                                                                          // 3738
            var D = cola.Descent.createSquareMatrix(N, function (i, j) {                                               // 3739
                return distances[i][j];                                                                                // 3740
            });                                                                                                        // 3741
            if (this._rootGroup && typeof this._rootGroup.groups !== 'undefined') {                                    // 3742
                var i = n;                                                                                             // 3743
                var addAttraction = function (i, j, strength, idealDistance) {                                         // 3744
                    G[i][j] = G[j][i] = strength;                                                                      // 3745
                    D[i][j] = D[j][i] = idealDistance;                                                                 // 3746
                };                                                                                                     // 3747
                this._groups.forEach(function (g) {                                                                    // 3748
                    addAttraction(i, i + 1, _this._groupCompactness, 0.1);                                             // 3749
                    // todo: add terms here attracting children of the group to the group dummy nodes                  // 3750
                    //if (typeof g.leaves !== 'undefined')                                                             // 3751
                    //    g.leaves.forEach(l => {                                                                      // 3752
                    //        addAttraction(l.index, i, 1e-4, 0.1);                                                    // 3753
                    //        addAttraction(l.index, i + 1, 1e-4, 0.1);                                                // 3754
                    //    });                                                                                          // 3755
                    //if (typeof g.groups !== 'undefined')                                                             // 3756
                    //    g.groups.forEach(g => {                                                                      // 3757
                    //        var gid = n + g.groupIndex * 2;                                                          // 3758
                    //        addAttraction(gid, i, 0.1, 0.1);                                                         // 3759
                    //        addAttraction(gid + 1, i, 0.1, 0.1);                                                     // 3760
                    //        addAttraction(gid, i + 1, 0.1, 0.1);                                                     // 3761
                    //        addAttraction(gid + 1, i + 1, 0.1, 0.1);                                                 // 3762
                    //    });                                                                                          // 3763
                    x[i] = 0, y[i++] = 0;                                                                              // 3764
                    x[i] = 0, y[i++] = 0;                                                                              // 3765
                });                                                                                                    // 3766
            }                                                                                                          // 3767
            else                                                                                                       // 3768
                this._rootGroup = { leaves: this._nodes, groups: [] };                                                 // 3769
            var curConstraints = this._constraints || [];                                                              // 3770
            if (this._directedLinkConstraints) {                                                                       // 3771
                this.linkAccessor.getMinSeparation = this._directedLinkConstraints.getMinSeparation;                   // 3772
                curConstraints = curConstraints.concat(cola.generateDirectedEdgeConstraints(n, this._links, this._directedLinkConstraints.axis, (this.linkAccessor)));
            }                                                                                                          // 3774
            this.avoidOverlaps(false);                                                                                 // 3775
            this._descent = new cola.Descent([x, y], D);                                                               // 3776
            this._descent.locks.clear();                                                                               // 3777
            for (var i = 0; i < n; ++i) {                                                                              // 3778
                var o = this._nodes[i];                                                                                // 3779
                if (o.fixed) {                                                                                         // 3780
                    o.px = o.x;                                                                                        // 3781
                    o.py = o.y;                                                                                        // 3782
                    var p = [o.x, o.y];                                                                                // 3783
                    this._descent.locks.add(i, p);                                                                     // 3784
                }                                                                                                      // 3785
            }                                                                                                          // 3786
            this._descent.threshold = this._threshold;                                                                 // 3787
            // apply initialIterations without user constraints or nonoverlap constraints                              // 3788
            // if groups are specified, dummy nodes and edges will be added to untangle                                // 3789
            // with respect to group connectivity                                                                      // 3790
            this.initialLayout(initialUnconstrainedIterations, x, y);                                                  // 3791
            // apply initialIterations with user constraints but no nonoverlap constraints                             // 3792
            if (curConstraints.length > 0)                                                                             // 3793
                this._descent.project = new cola.vpsc.Projection(this._nodes, this._groups, this._rootGroup, curConstraints).projectFunctions();
            this._descent.run(initialUserConstraintIterations);                                                        // 3795
            this.separateOverlappingComponents(w, h);                                                                  // 3796
            // subsequent iterations will apply all constraints                                                        // 3797
            this.avoidOverlaps(ao);                                                                                    // 3798
            if (ao) {                                                                                                  // 3799
                this._nodes.forEach(function (v, i) { v.x = x[i], v.y = y[i]; });                                      // 3800
                this._descent.project = new cola.vpsc.Projection(this._nodes, this._groups, this._rootGroup, curConstraints, true).projectFunctions();
                this._nodes.forEach(function (v, i) { x[i] = v.x, y[i] = v.y; });                                      // 3802
            }                                                                                                          // 3803
            // allow not immediately connected nodes to relax apart (p-stress)                                         // 3804
            this._descent.G = G;                                                                                       // 3805
            this._descent.run(initialAllConstraintsIterations);                                                        // 3806
            if (gridSnapIterations) {                                                                                  // 3807
                this._descent.snapStrength = 1000;                                                                     // 3808
                this._descent.snapGridSize = this._nodes[0].width;                                                     // 3809
                this._descent.numGridSnapNodes = n;                                                                    // 3810
                this._descent.scaleSnapByMaxH = n != N; // if we have groups then need to scale hessian so grid forces still apply
                var G0 = cola.Descent.createSquareMatrix(N, function (i, j) {                                          // 3812
                    if (i >= n || j >= n)                                                                              // 3813
                        return G[i][j];                                                                                // 3814
                    return 0;                                                                                          // 3815
                });                                                                                                    // 3816
                this._descent.G = G0;                                                                                  // 3817
                this._descent.run(gridSnapIterations);                                                                 // 3818
            }                                                                                                          // 3819
            this.updateNodePositions();                                                                                // 3820
            this.separateOverlappingComponents(w, h);                                                                  // 3821
            return keepRunning ? this.resume() : this;                                                                 // 3822
        };                                                                                                             // 3823
        Layout.prototype.initialLayout = function (iterations, x, y) {                                                 // 3824
            if (this._groups.length > 0 && iterations > 0) {                                                           // 3825
                // construct a flat graph with dummy nodes for the groups and edges connecting group dummy nodes to their children
                // todo: edges attached to groups are replaced with edges connected to the corresponding group dummy node
                var n = this._nodes.length;                                                                            // 3828
                var edges = this._links.map(function (e) { return { source: e.source.index, target: e.target.index }; });
                var vs = this._nodes.map(function (v) { return { index: v.index }; });                                 // 3830
                this._groups.forEach(function (g, i) {                                                                 // 3831
                    vs.push({ index: g.index = n + i });                                                               // 3832
                });                                                                                                    // 3833
                this._groups.forEach(function (g, i) {                                                                 // 3834
                    if (typeof g.leaves !== 'undefined')                                                               // 3835
                        g.leaves.forEach(function (v) { return edges.push({ source: g.index, target: v.index }); });   // 3836
                    if (typeof g.groups !== 'undefined')                                                               // 3837
                        g.groups.forEach(function (gg) { return edges.push({ source: g.index, target: gg.index }); });
                });                                                                                                    // 3839
                // layout the flat graph with dummy nodes and edges                                                    // 3840
                new cola.Layout()                                                                                      // 3841
                    .size(this.size())                                                                                 // 3842
                    .nodes(vs)                                                                                         // 3843
                    .links(edges)                                                                                      // 3844
                    .avoidOverlaps(false)                                                                              // 3845
                    .linkDistance(this.linkDistance())                                                                 // 3846
                    .symmetricDiffLinkLengths(5)                                                                       // 3847
                    .convergenceThreshold(1e-4)                                                                        // 3848
                    .start(iterations, 0, 0, 0, false);                                                                // 3849
                this._nodes.forEach(function (v) {                                                                     // 3850
                    x[v.index] = vs[v.index].x;                                                                        // 3851
                    y[v.index] = vs[v.index].y;                                                                        // 3852
                });                                                                                                    // 3853
            }                                                                                                          // 3854
            else {                                                                                                     // 3855
                this._descent.run(iterations);                                                                         // 3856
            }                                                                                                          // 3857
        };                                                                                                             // 3858
        // recalculate nodes position for disconnected graphs                                                          // 3859
        Layout.prototype.separateOverlappingComponents = function (width, height) {                                    // 3860
            var _this = this;                                                                                          // 3861
            // recalculate nodes position for disconnected graphs                                                      // 3862
            if (!this._distanceMatrix && this._handleDisconnected) {                                                   // 3863
                var x = this._descent.x[0], y = this._descent.x[1];                                                    // 3864
                this._nodes.forEach(function (v, i) { v.x = x[i], v.y = y[i]; });                                      // 3865
                var graphs = cola.separateGraphs(this._nodes, this._links);                                            // 3866
                cola.applyPacking(graphs, width, height, this._defaultNodeSize);                                       // 3867
                this._nodes.forEach(function (v, i) {                                                                  // 3868
                    _this._descent.x[0][i] = v.x, _this._descent.x[1][i] = v.y;                                        // 3869
                    if (v.bounds) {                                                                                    // 3870
                        v.bounds.setXCentre(v.x);                                                                      // 3871
                        v.bounds.setYCentre(v.y);                                                                      // 3872
                    }                                                                                                  // 3873
                });                                                                                                    // 3874
            }                                                                                                          // 3875
        };                                                                                                             // 3876
        Layout.prototype.resume = function () {                                                                        // 3877
            return this.alpha(0.1);                                                                                    // 3878
        };                                                                                                             // 3879
        Layout.prototype.stop = function () {                                                                          // 3880
            return this.alpha(0);                                                                                      // 3881
        };                                                                                                             // 3882
        /// find a visibility graph over the set of nodes.  assumes all nodes have a                                   // 3883
        /// bounds property (a rectangle) and that no pair of bounds overlaps.                                         // 3884
        Layout.prototype.prepareEdgeRouting = function (nodeMargin) {                                                  // 3885
            if (nodeMargin === void 0) { nodeMargin = 0; }                                                             // 3886
            this._visibilityGraph = new cola.geom.TangentVisibilityGraph(this._nodes.map(function (v) {                // 3887
                return v.bounds.inflate(-nodeMargin).vertices();                                                       // 3888
            }));                                                                                                       // 3889
        };                                                                                                             // 3890
        /// find a route avoiding node bounds for the given edge.                                                      // 3891
        /// assumes the visibility graph has been created (by prepareEdgeRouting method)                               // 3892
        /// and also assumes that nodes have an index property giving their position in the                            // 3893
        /// node array.  This index property is created by the start() method.                                         // 3894
        Layout.prototype.routeEdge = function (edge, draw) {                                                           // 3895
            var lineData = [];                                                                                         // 3896
            //if (d.source.id === 10 && d.target.id === 11) {                                                          // 3897
            //    debugger;                                                                                            // 3898
            //}                                                                                                        // 3899
            var vg2 = new cola.geom.TangentVisibilityGraph(this._visibilityGraph.P, { V: this._visibilityGraph.V, E: this._visibilityGraph.E }), port1 = { x: edge.source.x, y: edge.source.y }, port2 = { x: edge.target.x, y: edge.target.y }, start = vg2.addPoint(port1, edge.source.index), end = vg2.addPoint(port2, edge.target.index);
            vg2.addEdgeIfVisible(port1, port2, edge.source.index, edge.target.index);                                  // 3901
            if (typeof draw !== 'undefined') {                                                                         // 3902
                draw(vg2);                                                                                             // 3903
            }                                                                                                          // 3904
            var sourceInd = function (e) { return e.source.id; }, targetInd = function (e) { return e.target.id; }, length = function (e) { return e.length(); }, spCalc = new cola.shortestpaths.Calculator(vg2.V.length, vg2.E, sourceInd, targetInd, length), shortestPath = spCalc.PathFromNodeToNode(start.id, end.id);
            if (shortestPath.length === 1 || shortestPath.length === vg2.V.length) {                                   // 3906
                var route = cola.vpsc.makeEdgeBetween(edge.source.innerBounds, edge.target.innerBounds, 5);            // 3907
                lineData = [route.sourceIntersection, route.arrowStart];                                               // 3908
            }                                                                                                          // 3909
            else {                                                                                                     // 3910
                var n = shortestPath.length - 2, p = vg2.V[shortestPath[n]].p, q = vg2.V[shortestPath[0]].p, lineData = [edge.source.innerBounds.rayIntersection(p.x, p.y)];
                for (var i = n; i >= 0; --i)                                                                           // 3912
                    lineData.push(vg2.V[shortestPath[i]].p);                                                           // 3913
                lineData.push(cola.vpsc.makeEdgeTo(q, edge.target.innerBounds, 5));                                    // 3914
            }                                                                                                          // 3915
            //lineData.forEach((v, i) => {                                                                             // 3916
            //    if (i > 0) {                                                                                         // 3917
            //        var u = lineData[i - 1];                                                                         // 3918
            //        this._nodes.forEach(function (node) {                                                            // 3919
            //            if (node.id === getSourceIndex(d) || node.id === getTargetIndex(d)) return;                  // 3920
            //            var ints = node.innerBounds.lineIntersections(u.x, u.y, v.x, v.y);                           // 3921
            //            if (ints.length > 0) {                                                                       // 3922
            //                debugger;                                                                                // 3923
            //            }                                                                                            // 3924
            //        })                                                                                               // 3925
            //    }                                                                                                    // 3926
            //})                                                                                                       // 3927
            return lineData;                                                                                           // 3928
        };                                                                                                             // 3929
        //The link source and target may be just a node index, or they may be references to nodes themselves.          // 3930
        Layout.getSourceIndex = function (e) {                                                                         // 3931
            return typeof e.source === 'number' ? e.source : e.source.index;                                           // 3932
        };                                                                                                             // 3933
        //The link source and target may be just a node index, or they may be references to nodes themselves.          // 3934
        Layout.getTargetIndex = function (e) {                                                                         // 3935
            return typeof e.target === 'number' ? e.target : e.target.index;                                           // 3936
        };                                                                                                             // 3937
        // Get a string ID for a given link.                                                                           // 3938
        Layout.linkId = function (e) {                                                                                 // 3939
            return Layout.getSourceIndex(e) + "-" + Layout.getTargetIndex(e);                                          // 3940
        };                                                                                                             // 3941
        // The fixed property has three bits:                                                                          // 3942
        // Bit 1 can be set externally (e.g., d.fixed = true) and show persist.                                        // 3943
        // Bit 2 stores the dragging state, from mousedown to mouseup.                                                 // 3944
        // Bit 3 stores the hover state, from mouseover to mouseout.                                                   // 3945
        Layout.dragStart = function (d) {                                                                              // 3946
            if (isGroup(d)) {                                                                                          // 3947
                Layout.storeOffset(d, Layout.dragOrigin(d));                                                           // 3948
            }                                                                                                          // 3949
            else {                                                                                                     // 3950
                Layout.stopNode(d);                                                                                    // 3951
                d.fixed |= 2; // set bit 2                                                                             // 3952
            }                                                                                                          // 3953
        };                                                                                                             // 3954
        // we clobber any existing desired positions for nodes                                                         // 3955
        // in case another tick event occurs before the drag                                                           // 3956
        Layout.stopNode = function (v) {                                                                               // 3957
            v.px = v.x;                                                                                                // 3958
            v.py = v.y;                                                                                                // 3959
        };                                                                                                             // 3960
        // we store offsets for each node relative to the centre of the ancestor group                                 // 3961
        // being dragged in a pair of properties on the node                                                           // 3962
        Layout.storeOffset = function (d, origin) {                                                                    // 3963
            if (typeof d.leaves !== 'undefined') {                                                                     // 3964
                d.leaves.forEach(function (v) {                                                                        // 3965
                    v.fixed |= 2;                                                                                      // 3966
                    Layout.stopNode(v);                                                                                // 3967
                    v._dragGroupOffsetX = v.x - origin.x;                                                              // 3968
                    v._dragGroupOffsetY = v.y - origin.y;                                                              // 3969
                });                                                                                                    // 3970
            }                                                                                                          // 3971
            if (typeof d.groups !== 'undefined') {                                                                     // 3972
                d.groups.forEach(function (g) { return Layout.storeOffset(g, origin); });                              // 3973
            }                                                                                                          // 3974
        };                                                                                                             // 3975
        // the drag origin is taken as the centre of the node or group                                                 // 3976
        Layout.dragOrigin = function (d) {                                                                             // 3977
            if (isGroup(d)) {                                                                                          // 3978
                return {                                                                                               // 3979
                    x: d.bounds.cx(),                                                                                  // 3980
                    y: d.bounds.cy()                                                                                   // 3981
                };                                                                                                     // 3982
            }                                                                                                          // 3983
            else {                                                                                                     // 3984
                return d;                                                                                              // 3985
            }                                                                                                          // 3986
        };                                                                                                             // 3987
        // for groups, the drag translation is propagated down to all of the children of                               // 3988
        // the group.                                                                                                  // 3989
        Layout.drag = function (d, position) {                                                                         // 3990
            if (isGroup(d)) {                                                                                          // 3991
                if (typeof d.leaves !== 'undefined') {                                                                 // 3992
                    d.leaves.forEach(function (v) {                                                                    // 3993
                        d.bounds.setXCentre(position.x);                                                               // 3994
                        d.bounds.setYCentre(position.y);                                                               // 3995
                        v.px = v._dragGroupOffsetX + position.x;                                                       // 3996
                        v.py = v._dragGroupOffsetY + position.y;                                                       // 3997
                    });                                                                                                // 3998
                }                                                                                                      // 3999
                if (typeof d.groups !== 'undefined') {                                                                 // 4000
                    d.groups.forEach(function (g) { return Layout.drag(g, position); });                               // 4001
                }                                                                                                      // 4002
            }                                                                                                          // 4003
            else {                                                                                                     // 4004
                d.px = position.x;                                                                                     // 4005
                d.py = position.y;                                                                                     // 4006
            }                                                                                                          // 4007
        };                                                                                                             // 4008
        // we unset only bits 2 and 3 so that the user can fix nodes with another a different                          // 4009
        // bit such that the lock persists between drags                                                               // 4010
        Layout.dragEnd = function (d) {                                                                                // 4011
            if (isGroup(d)) {                                                                                          // 4012
                if (typeof d.leaves !== 'undefined') {                                                                 // 4013
                    d.leaves.forEach(function (v) {                                                                    // 4014
                        Layout.dragEnd(v);                                                                             // 4015
                        delete v._dragGroupOffsetX;                                                                    // 4016
                        delete v._dragGroupOffsetY;                                                                    // 4017
                    });                                                                                                // 4018
                }                                                                                                      // 4019
                if (typeof d.groups !== 'undefined') {                                                                 // 4020
                    d.groups.forEach(Layout.dragEnd);                                                                  // 4021
                }                                                                                                      // 4022
            }                                                                                                          // 4023
            else {                                                                                                     // 4024
                d.fixed &= ~6; // unset bits 2 and 3                                                                   // 4025
            }                                                                                                          // 4026
        };                                                                                                             // 4027
        // in d3 hover temporarily locks nodes, currently not used in cola                                             // 4028
        Layout.mouseOver = function (d) {                                                                              // 4029
            d.fixed |= 4; // set bit 3                                                                                 // 4030
            d.px = d.x, d.py = d.y; // set velocity to zero                                                            // 4031
        };                                                                                                             // 4032
        // in d3 hover temporarily locks nodes, currently not used in cola                                             // 4033
        Layout.mouseOut = function (d) {                                                                               // 4034
            d.fixed &= ~4; // unset bit 3                                                                              // 4035
        };                                                                                                             // 4036
        return Layout;                                                                                                 // 4037
    })();                                                                                                              // 4038
    cola.Layout = Layout;                                                                                              // 4039
})(cola || (cola = {}));                                                                                               // 4040
///<reference path="../extern/d3.d.ts"/>                                                                               // 4041
///<reference path="layout.ts"/>                                                                                       // 4042
var cola;                                                                                                              // 4043
(function (cola) {                                                                                                     // 4044
    var D3StyleLayoutAdaptor = (function (_super) {                                                                    // 4045
        __extends(D3StyleLayoutAdaptor, _super);                                                                       // 4046
        function D3StyleLayoutAdaptor() {                                                                              // 4047
            _super.call(this);                                                                                         // 4048
            this.event = d3.dispatch(cola.EventType[cola.EventType.start], cola.EventType[cola.EventType.tick], cola.EventType[cola.EventType.end]);
            // bit of trickyness remapping 'this' so we can reference it in the function body.                         // 4050
            var d3layout = this;                                                                                       // 4051
            var drag;                                                                                                  // 4052
            this.drag = function () {                                                                                  // 4053
                if (!drag) {                                                                                           // 4054
                    var drag = d3.behavior.drag()                                                                      // 4055
                        .origin(cola.Layout.dragOrigin)                                                                // 4056
                        .on("dragstart.d3adaptor", cola.Layout.dragStart)                                              // 4057
                        .on("drag.d3adaptor", function (d) {                                                           // 4058
                        cola.Layout.drag(d, d3.event);                                                                 // 4059
                        d3layout.resume(); // restart annealing                                                        // 4060
                    })                                                                                                 // 4061
                        .on("dragend.d3adaptor", cola.Layout.dragEnd);                                                 // 4062
                }                                                                                                      // 4063
                if (!arguments.length)                                                                                 // 4064
                    return drag;                                                                                       // 4065
                // this is the context of the function, i.e. the d3 selection                                          // 4066
                this //.on("mouseover.adaptor", colaMouseover)                                                         // 4067
                    .call(drag);                                                                                       // 4068
            };                                                                                                         // 4069
        }                                                                                                              // 4070
        D3StyleLayoutAdaptor.prototype.trigger = function (e) {                                                        // 4071
            var d3event = { type: cola.EventType[e.type], alpha: e.alpha, stress: e.stress };                          // 4072
            this.event[d3event.type](d3event); // via d3 dispatcher, e.g. event.start(e);                              // 4073
        };                                                                                                             // 4074
        // iterate layout using a d3.timer, which queues calls to tick repeatedly until tick returns true              // 4075
        D3StyleLayoutAdaptor.prototype.kick = function () {                                                            // 4076
            var _this = this;                                                                                          // 4077
            d3.timer(function () { return _super.prototype.tick.call(_this); });                                       // 4078
        };                                                                                                             // 4079
        // a function for binding to events on the adapter                                                             // 4080
        D3StyleLayoutAdaptor.prototype.on = function (eventType, listener) {                                           // 4081
            if (typeof eventType === 'string') {                                                                       // 4082
                this.event.on(eventType, listener);                                                                    // 4083
            }                                                                                                          // 4084
            else {                                                                                                     // 4085
                this.event.on(cola.EventType[eventType], listener);                                                    // 4086
            }                                                                                                          // 4087
            return this;                                                                                               // 4088
        };                                                                                                             // 4089
        return D3StyleLayoutAdaptor;                                                                                   // 4090
    })(cola.Layout);                                                                                                   // 4091
    cola.D3StyleLayoutAdaptor = D3StyleLayoutAdaptor;                                                                  // 4092
    /**                                                                                                                // 4093
     * provides an interface for use with d3:                                                                          // 4094
     * - uses the d3 event system to dispatch layout events such as:                                                   // 4095
     *   o "start" (start layout process)                                                                              // 4096
     *   o "tick" (after each layout iteration)                                                                        // 4097
     *   o "end" (layout converged and complete).                                                                      // 4098
     * - uses the d3 timer to queue layout iterations.                                                                 // 4099
     * - sets up d3.behavior.drag to drag nodes                                                                        // 4100
     *   o use `node.call(<the returned instance of Layout>.drag)` to make nodes draggable                             // 4101
     * returns an instance of the cola.Layout itself with which the user                                               // 4102
     * can interact directly.                                                                                          // 4103
     */                                                                                                                // 4104
    function d3adaptor() {                                                                                             // 4105
        return new D3StyleLayoutAdaptor();                                                                             // 4106
    }                                                                                                                  // 4107
    cola.d3adaptor = d3adaptor;                                                                                        // 4108
})(cola || (cola = {}));                                                                                               // 4109
/// <reference path="rectangle.ts"/>                                                                                   // 4110
/// <reference path="shortestpaths.ts"/>                                                                               // 4111
/// <reference path="geom.ts"/>                                                                                        // 4112
/// <reference path="vpsc.ts"/>                                                                                        // 4113
var cola;                                                                                                              // 4114
(function (cola) {                                                                                                     // 4115
    var NodeWrapper = (function () {                                                                                   // 4116
        function NodeWrapper(id, rect, children) {                                                                     // 4117
            this.id = id;                                                                                              // 4118
            this.rect = rect;                                                                                          // 4119
            this.children = children;                                                                                  // 4120
            this.leaf = typeof children === 'undefined' || children.length === 0;                                      // 4121
        }                                                                                                              // 4122
        return NodeWrapper;                                                                                            // 4123
    })();                                                                                                              // 4124
    cola.NodeWrapper = NodeWrapper;                                                                                    // 4125
    var Vert = (function () {                                                                                          // 4126
        function Vert(id, x, y, node, line) {                                                                          // 4127
            if (node === void 0) { node = null; }                                                                      // 4128
            if (line === void 0) { line = null; }                                                                      // 4129
            this.id = id;                                                                                              // 4130
            this.x = x;                                                                                                // 4131
            this.y = y;                                                                                                // 4132
            this.node = node;                                                                                          // 4133
            this.line = line;                                                                                          // 4134
        }                                                                                                              // 4135
        return Vert;                                                                                                   // 4136
    })();                                                                                                              // 4137
    cola.Vert = Vert;                                                                                                  // 4138
    var LongestCommonSubsequence = (function () {                                                                      // 4139
        function LongestCommonSubsequence(s, t) {                                                                      // 4140
            this.s = s;                                                                                                // 4141
            this.t = t;                                                                                                // 4142
            var mf = LongestCommonSubsequence.findMatch(s, t);                                                         // 4143
            var tr = t.slice(0).reverse();                                                                             // 4144
            var mr = LongestCommonSubsequence.findMatch(s, tr);                                                        // 4145
            if (mf.length >= mr.length) {                                                                              // 4146
                this.length = mf.length;                                                                               // 4147
                this.si = mf.si;                                                                                       // 4148
                this.ti = mf.ti;                                                                                       // 4149
                this.reversed = false;                                                                                 // 4150
            }                                                                                                          // 4151
            else {                                                                                                     // 4152
                this.length = mr.length;                                                                               // 4153
                this.si = mr.si;                                                                                       // 4154
                this.ti = t.length - mr.ti - mr.length;                                                                // 4155
                this.reversed = true;                                                                                  // 4156
            }                                                                                                          // 4157
        }                                                                                                              // 4158
        LongestCommonSubsequence.findMatch = function (s, t) {                                                         // 4159
            var m = s.length;                                                                                          // 4160
            var n = t.length;                                                                                          // 4161
            var match = { length: 0, si: -1, ti: -1 };                                                                 // 4162
            var l = new Array(m);                                                                                      // 4163
            for (var i = 0; i < m; i++) {                                                                              // 4164
                l[i] = new Array(n);                                                                                   // 4165
                for (var j = 0; j < n; j++)                                                                            // 4166
                    if (s[i] === t[j]) {                                                                               // 4167
                        var v = l[i][j] = (i === 0 || j === 0) ? 1 : l[i - 1][j - 1] + 1;                              // 4168
                        if (v > match.length) {                                                                        // 4169
                            match.length = v;                                                                          // 4170
                            match.si = i - v + 1;                                                                      // 4171
                            match.ti = j - v + 1;                                                                      // 4172
                        }                                                                                              // 4173
                        ;                                                                                              // 4174
                    }                                                                                                  // 4175
                    else                                                                                               // 4176
                        l[i][j] = 0;                                                                                   // 4177
            }                                                                                                          // 4178
            return match;                                                                                              // 4179
        };                                                                                                             // 4180
        LongestCommonSubsequence.prototype.getSequence = function () {                                                 // 4181
            return this.length >= 0 ? this.s.slice(this.si, this.si + this.length) : [];                               // 4182
        };                                                                                                             // 4183
        return LongestCommonSubsequence;                                                                               // 4184
    })();                                                                                                              // 4185
    cola.LongestCommonSubsequence = LongestCommonSubsequence;                                                          // 4186
    var GridRouter = (function () {                                                                                    // 4187
        function GridRouter(originalnodes, accessor, groupPadding) {                                                   // 4188
            var _this = this;                                                                                          // 4189
            if (groupPadding === void 0) { groupPadding = 12; }                                                        // 4190
            this.originalnodes = originalnodes;                                                                        // 4191
            this.groupPadding = groupPadding;                                                                          // 4192
            this.leaves = null;                                                                                        // 4193
            this.nodes = originalnodes.map(function (v, i) { return new NodeWrapper(i, accessor.getBounds(v), accessor.getChildren(v)); });
            this.leaves = this.nodes.filter(function (v) { return v.leaf; });                                          // 4195
            this.groups = this.nodes.filter(function (g) { return !g.leaf; });                                         // 4196
            this.cols = this.getGridLines('x');                                                                        // 4197
            this.rows = this.getGridLines('y');                                                                        // 4198
            // create parents for each node or group that is a member of another's children                            // 4199
            this.groups.forEach(function (v) {                                                                         // 4200
                return v.children.forEach(function (c) { return _this.nodes[c].parent = v; });                         // 4201
            });                                                                                                        // 4202
            // root claims the remaining orphans                                                                       // 4203
            this.root = { children: [] };                                                                              // 4204
            this.nodes.forEach(function (v) {                                                                          // 4205
                if (typeof v.parent === 'undefined') {                                                                 // 4206
                    v.parent = _this.root;                                                                             // 4207
                    _this.root.children.push(v.id);                                                                    // 4208
                }                                                                                                      // 4209
                // each node will have grid vertices associated with it,                                               // 4210
                // some inside the node and some on the boundary                                                       // 4211
                // leaf nodes will have exactly one internal node at the center                                        // 4212
                // and four boundary nodes                                                                             // 4213
                // groups will have potentially many of each                                                           // 4214
                v.ports = [];                                                                                          // 4215
            });                                                                                                        // 4216
            // nodes ordered by their position in the group hierarchy                                                  // 4217
            this.backToFront = this.nodes.slice(0);                                                                    // 4218
            this.backToFront.sort(function (x, y) { return _this.getDepth(x) - _this.getDepth(y); });                  // 4219
            // compute boundary rectangles for each group                                                              // 4220
            // has to be done from front to back, i.e. inside groups to outside groups                                 // 4221
            // such that each can be made large enough to enclose its interior                                         // 4222
            var frontToBackGroups = this.backToFront.slice(0).reverse().filter(function (g) { return !g.leaf; });      // 4223
            frontToBackGroups.forEach(function (v) {                                                                   // 4224
                var r = cola.vpsc.Rectangle.empty();                                                                   // 4225
                v.children.forEach(function (c) { return r = r.union(_this.nodes[c].rect); });                         // 4226
                v.rect = r.inflate(_this.groupPadding);                                                                // 4227
            });                                                                                                        // 4228
            var colMids = this.midPoints(this.cols.map(function (r) { return r.pos; }));                               // 4229
            var rowMids = this.midPoints(this.rows.map(function (r) { return r.pos; }));                               // 4230
            // setup extents of lines                                                                                  // 4231
            var rowx = colMids[0], rowX = colMids[colMids.length - 1];                                                 // 4232
            var coly = rowMids[0], colY = rowMids[rowMids.length - 1];                                                 // 4233
            // horizontal lines                                                                                        // 4234
            var hlines = this.rows.map(function (r) { return { x1: rowx, x2: rowX, y1: r.pos, y2: r.pos }; })          // 4235
                .concat(rowMids.map(function (m) { return { x1: rowx, x2: rowX, y1: m, y2: m }; }));                   // 4236
            // vertical lines                                                                                          // 4237
            var vlines = this.cols.map(function (c) { return { x1: c.pos, x2: c.pos, y1: coly, y2: colY }; })          // 4238
                .concat(colMids.map(function (m) { return { x1: m, x2: m, y1: coly, y2: colY }; }));                   // 4239
            // the full set of lines                                                                                   // 4240
            var lines = hlines.concat(vlines);                                                                         // 4241
            // we record the vertices associated with each line                                                        // 4242
            lines.forEach(function (l) { return l.verts = []; });                                                      // 4243
            // the routing graph                                                                                       // 4244
            this.verts = [];                                                                                           // 4245
            this.edges = [];                                                                                           // 4246
            // create vertices at the crossings of horizontal and vertical grid-lines                                  // 4247
            hlines.forEach(function (h) {                                                                              // 4248
                return vlines.forEach(function (v) {                                                                   // 4249
                    var p = new Vert(_this.verts.length, v.x1, h.y1);                                                  // 4250
                    h.verts.push(p);                                                                                   // 4251
                    v.verts.push(p);                                                                                   // 4252
                    _this.verts.push(p);                                                                               // 4253
                    // assign vertices to the nodes immediately under them                                             // 4254
                    var i = _this.backToFront.length;                                                                  // 4255
                    while (i-- > 0) {                                                                                  // 4256
                        var node = _this.backToFront[i], r = node.rect;                                                // 4257
                        var dx = Math.abs(p.x - r.cx()), dy = Math.abs(p.y - r.cy());                                  // 4258
                        if (dx < r.width() / 2 && dy < r.height() / 2) {                                               // 4259
                            p.node = node;                                                                             // 4260
                            break;                                                                                     // 4261
                        }                                                                                              // 4262
                    }                                                                                                  // 4263
                });                                                                                                    // 4264
            });                                                                                                        // 4265
            lines.forEach(function (l, li) {                                                                           // 4266
                // create vertices at the intersections of nodes and lines                                             // 4267
                _this.nodes.forEach(function (v, i) {                                                                  // 4268
                    v.rect.lineIntersections(l.x1, l.y1, l.x2, l.y2).forEach(function (intersect, j) {                 // 4269
                        //console.log(li+','+i+','+j+':'+intersect.x + ',' + intersect.y);                             // 4270
                        var p = new Vert(_this.verts.length, intersect.x, intersect.y, v, l);                          // 4271
                        _this.verts.push(p);                                                                           // 4272
                        l.verts.push(p);                                                                               // 4273
                        v.ports.push(p);                                                                               // 4274
                    });                                                                                                // 4275
                });                                                                                                    // 4276
                // split lines into edges joining vertices                                                             // 4277
                var isHoriz = Math.abs(l.y1 - l.y2) < 0.1;                                                             // 4278
                var delta = function (a, b) { return isHoriz ? b.x - a.x : b.y - a.y; };                               // 4279
                l.verts.sort(delta);                                                                                   // 4280
                for (var i = 1; i < l.verts.length; i++) {                                                             // 4281
                    var u = l.verts[i - 1], v = l.verts[i];                                                            // 4282
                    if (u.node && u.node === v.node && u.node.leaf)                                                    // 4283
                        continue;                                                                                      // 4284
                    _this.edges.push({ source: u.id, target: v.id, length: Math.abs(delta(u, v)) });                   // 4285
                }                                                                                                      // 4286
            });                                                                                                        // 4287
        }                                                                                                              // 4288
        GridRouter.prototype.avg = function (a) { return a.reduce(function (x, y) { return x + y; }) / a.length; };    // 4289
        // in the given axis, find sets of leaves overlapping in that axis                                             // 4290
        // center of each GridLine is average of all nodes in column                                                   // 4291
        GridRouter.prototype.getGridLines = function (axis) {                                                          // 4292
            var columns = [];                                                                                          // 4293
            var ls = this.leaves.slice(0, this.leaves.length);                                                         // 4294
            while (ls.length > 0) {                                                                                    // 4295
                // find a column of all leaves overlapping in axis with the first leaf                                 // 4296
                var overlapping = ls.filter(function (v) { return v.rect['overlap' + axis.toUpperCase()](ls[0].rect); });
                var col = {                                                                                            // 4298
                    nodes: overlapping,                                                                                // 4299
                    pos: this.avg(overlapping.map(function (v) { return v.rect['c' + axis](); }))                      // 4300
                };                                                                                                     // 4301
                columns.push(col);                                                                                     // 4302
                col.nodes.forEach(function (v) { return ls.splice(ls.indexOf(v), 1); });                               // 4303
            }                                                                                                          // 4304
            columns.sort(function (a, b) { return a.pos - b.pos; });                                                   // 4305
            return columns;                                                                                            // 4306
        };                                                                                                             // 4307
        // get the depth of the given node in the group hierarchy                                                      // 4308
        GridRouter.prototype.getDepth = function (v) {                                                                 // 4309
            var depth = 0;                                                                                             // 4310
            while (v.parent !== this.root) {                                                                           // 4311
                depth++;                                                                                               // 4312
                v = v.parent;                                                                                          // 4313
            }                                                                                                          // 4314
            return depth;                                                                                              // 4315
        };                                                                                                             // 4316
        // medial axes between node centres and also boundary lines for the grid                                       // 4317
        GridRouter.prototype.midPoints = function (a) {                                                                // 4318
            var gap = a[1] - a[0];                                                                                     // 4319
            var mids = [a[0] - gap / 2];                                                                               // 4320
            for (var i = 1; i < a.length; i++) {                                                                       // 4321
                mids.push((a[i] + a[i - 1]) / 2);                                                                      // 4322
            }                                                                                                          // 4323
            mids.push(a[a.length - 1] + gap / 2);                                                                      // 4324
            return mids;                                                                                               // 4325
        };                                                                                                             // 4326
        // find path from v to root including both v and root                                                          // 4327
        GridRouter.prototype.findLineage = function (v) {                                                              // 4328
            var lineage = [v];                                                                                         // 4329
            do {                                                                                                       // 4330
                v = v.parent;                                                                                          // 4331
                lineage.push(v);                                                                                       // 4332
            } while (v !== this.root);                                                                                 // 4333
            return lineage.reverse();                                                                                  // 4334
        };                                                                                                             // 4335
        // find path connecting a and b through their lowest common ancestor                                           // 4336
        GridRouter.prototype.findAncestorPathBetween = function (a, b) {                                               // 4337
            var aa = this.findLineage(a), ba = this.findLineage(b), i = 0;                                             // 4338
            while (aa[i] === ba[i])                                                                                    // 4339
                i++;                                                                                                   // 4340
            // i-1 to include common ancestor only once (as first element)                                             // 4341
            return { commonAncestor: aa[i - 1], lineages: aa.slice(i).concat(ba.slice(i)) };                           // 4342
        };                                                                                                             // 4343
        // when finding a path between two nodes a and b, siblings of a and b on the                                   // 4344
        // paths from a and b to their least common ancestor are obstacles                                             // 4345
        GridRouter.prototype.siblingObstacles = function (a, b) {                                                      // 4346
            var _this = this;                                                                                          // 4347
            var path = this.findAncestorPathBetween(a, b);                                                             // 4348
            var lineageLookup = {};                                                                                    // 4349
            path.lineages.forEach(function (v) { return lineageLookup[v.id] = {}; });                                  // 4350
            var obstacles = path.commonAncestor.children.filter(function (v) { return !(v in lineageLookup); });       // 4351
            path.lineages                                                                                              // 4352
                .filter(function (v) { return v.parent !== path.commonAncestor; })                                     // 4353
                .forEach(function (v) { return obstacles = obstacles.concat(v.parent.children.filter(function (c) { return c !== v.id; })); });
            return obstacles.map(function (v) { return _this.nodes[v]; });                                             // 4355
        };                                                                                                             // 4356
        // for the given routes, extract all the segments orthogonal to the axis x                                     // 4357
        // and return all them grouped by x position                                                                   // 4358
        GridRouter.getSegmentSets = function (routes, x, y) {                                                          // 4359
            // vsegments is a list of vertical segments sorted by x position                                           // 4360
            var vsegments = [];                                                                                        // 4361
            for (var ei = 0; ei < routes.length; ei++) {                                                               // 4362
                var route = routes[ei];                                                                                // 4363
                for (var si = 0; si < route.length; si++) {                                                            // 4364
                    var s = route[si];                                                                                 // 4365
                    s.edgeid = ei;                                                                                     // 4366
                    s.i = si;                                                                                          // 4367
                    var sdx = s[1][x] - s[0][x];                                                                       // 4368
                    if (Math.abs(sdx) < 0.1) {                                                                         // 4369
                        vsegments.push(s);                                                                             // 4370
                    }                                                                                                  // 4371
                }                                                                                                      // 4372
            }                                                                                                          // 4373
            vsegments.sort(function (a, b) { return a[0][x] - b[0][x]; });                                             // 4374
            // vsegmentsets is a set of sets of segments grouped by x position                                         // 4375
            var vsegmentsets = [];                                                                                     // 4376
            var segmentset = null;                                                                                     // 4377
            for (var i = 0; i < vsegments.length; i++) {                                                               // 4378
                var s = vsegments[i];                                                                                  // 4379
                if (!segmentset || Math.abs(s[0][x] - segmentset.pos) > 0.1) {                                         // 4380
                    segmentset = { pos: s[0][x], segments: [] };                                                       // 4381
                    vsegmentsets.push(segmentset);                                                                     // 4382
                }                                                                                                      // 4383
                segmentset.segments.push(s);                                                                           // 4384
            }                                                                                                          // 4385
            return vsegmentsets;                                                                                       // 4386
        };                                                                                                             // 4387
        // for all segments in this bundle create a vpsc problem such that                                             // 4388
        // each segment's x position is a variable and separation constraints                                          // 4389
        // are given by the partial order over the edges to which the segments belong                                  // 4390
        // for each pair s1,s2 of segments in the open set:                                                            // 4391
        //   e1 = edge of s1, e2 = edge of s2                                                                          // 4392
        //   if leftOf(e1,e2) create constraint s1.x + gap <= s2.x                                                     // 4393
        //   else if leftOf(e2,e1) create cons. s2.x + gap <= s1.x                                                     // 4394
        GridRouter.nudgeSegs = function (x, y, routes, segments, leftOf, gap) {                                        // 4395
            var n = segments.length;                                                                                   // 4396
            if (n <= 1)                                                                                                // 4397
                return;                                                                                                // 4398
            var vs = segments.map(function (s) { return new cola.vpsc.Variable(s[0][x]); });                           // 4399
            var cs = [];                                                                                               // 4400
            for (var i = 0; i < n; i++) {                                                                              // 4401
                for (var j = 0; j < n; j++) {                                                                          // 4402
                    if (i === j)                                                                                       // 4403
                        continue;                                                                                      // 4404
                    var s1 = segments[i], s2 = segments[j], e1 = s1.edgeid, e2 = s2.edgeid, lind = -1, rind = -1;      // 4405
                    // in page coordinates (not cartesian) the notion of 'leftof' is flipped in the horizontal axis from the vertical axis
                    // that is, when nudging vertical segments, if they increase in the y(conj) direction the segment belonging to the
                    // 'left' edge actually needs to be nudged to the right                                            // 4408
                    // when nudging horizontal segments, if the segments increase in the x direction                   // 4409
                    // then the 'left' segment needs to go higher, i.e. to have y pos less than that of the right      // 4410
                    if (x == 'x') {                                                                                    // 4411
                        if (leftOf(e1, e2)) {                                                                          // 4412
                            //console.log('s1: ' + s1[0][x] + ',' + s1[0][y] + '-' + s1[1][x] + ',' + s1[1][y]);       // 4413
                            if (s1[0][y] < s1[1][y]) {                                                                 // 4414
                                lind = j, rind = i;                                                                    // 4415
                            }                                                                                          // 4416
                            else {                                                                                     // 4417
                                lind = i, rind = j;                                                                    // 4418
                            }                                                                                          // 4419
                        }                                                                                              // 4420
                    }                                                                                                  // 4421
                    else {                                                                                             // 4422
                        if (leftOf(e1, e2)) {                                                                          // 4423
                            if (s1[0][y] < s1[1][y]) {                                                                 // 4424
                                lind = i, rind = j;                                                                    // 4425
                            }                                                                                          // 4426
                            else {                                                                                     // 4427
                                lind = j, rind = i;                                                                    // 4428
                            }                                                                                          // 4429
                        }                                                                                              // 4430
                    }                                                                                                  // 4431
                    if (lind >= 0) {                                                                                   // 4432
                        //console.log(x+' constraint: ' + lind + '<' + rind);                                          // 4433
                        cs.push(new cola.vpsc.Constraint(vs[lind], vs[rind], gap));                                    // 4434
                    }                                                                                                  // 4435
                }                                                                                                      // 4436
            }                                                                                                          // 4437
            var solver = new cola.vpsc.Solver(vs, cs);                                                                 // 4438
            solver.solve();                                                                                            // 4439
            vs.forEach(function (v, i) {                                                                               // 4440
                var s = segments[i];                                                                                   // 4441
                var pos = v.position();                                                                                // 4442
                s[0][x] = s[1][x] = pos;                                                                               // 4443
                var route = routes[s.edgeid];                                                                          // 4444
                if (s.i > 0)                                                                                           // 4445
                    route[s.i - 1][1][x] = pos;                                                                        // 4446
                if (s.i < route.length - 1)                                                                            // 4447
                    route[s.i + 1][0][x] = pos;                                                                        // 4448
            });                                                                                                        // 4449
        };                                                                                                             // 4450
        GridRouter.nudgeSegments = function (routes, x, y, leftOf, gap) {                                              // 4451
            var vsegmentsets = GridRouter.getSegmentSets(routes, x, y);                                                // 4452
            // scan the grouped (by x) segment sets to find co-linear bundles                                          // 4453
            for (var i = 0; i < vsegmentsets.length; i++) {                                                            // 4454
                var ss = vsegmentsets[i];                                                                              // 4455
                var events = [];                                                                                       // 4456
                for (var j = 0; j < ss.segments.length; j++) {                                                         // 4457
                    var s = ss.segments[j];                                                                            // 4458
                    events.push({ type: 0, s: s, pos: Math.min(s[0][y], s[1][y]) });                                   // 4459
                    events.push({ type: 1, s: s, pos: Math.max(s[0][y], s[1][y]) });                                   // 4460
                }                                                                                                      // 4461
                events.sort(function (a, b) { return a.pos - b.pos + a.type - b.type; });                              // 4462
                var open = [];                                                                                         // 4463
                var openCount = 0;                                                                                     // 4464
                events.forEach(function (e) {                                                                          // 4465
                    if (e.type === 0) {                                                                                // 4466
                        open.push(e.s);                                                                                // 4467
                        openCount++;                                                                                   // 4468
                    }                                                                                                  // 4469
                    else {                                                                                             // 4470
                        openCount--;                                                                                   // 4471
                    }                                                                                                  // 4472
                    if (openCount == 0) {                                                                              // 4473
                        GridRouter.nudgeSegs(x, y, routes, open, leftOf, gap);                                         // 4474
                        open = [];                                                                                     // 4475
                    }                                                                                                  // 4476
                });                                                                                                    // 4477
            }                                                                                                          // 4478
        };                                                                                                             // 4479
        // obtain routes for the specified edges, nicely nudged apart                                                  // 4480
        // warning: edge paths may be reversed such that common paths are ordered consistently within bundles!         // 4481
        // @param edges list of edges                                                                                  // 4482
        // @param nudgeGap how much to space parallel edge segements                                                   // 4483
        // @param source function to retrieve the index of the source node for a given edge                            // 4484
        // @param target function to retrieve the index of the target node for a given edge                            // 4485
        // @returns an array giving, for each edge, an array of segments, each segment a pair of points in an array    // 4486
        GridRouter.prototype.routeEdges = function (edges, nudgeGap, source, target) {                                 // 4487
            var _this = this;                                                                                          // 4488
            var routePaths = edges.map(function (e) { return _this.route(source(e), target(e)); });                    // 4489
            var order = cola.GridRouter.orderEdges(routePaths);                                                        // 4490
            var routes = routePaths.map(function (e) { return cola.GridRouter.makeSegments(e); });                     // 4491
            cola.GridRouter.nudgeSegments(routes, 'x', 'y', order, nudgeGap);                                          // 4492
            cola.GridRouter.nudgeSegments(routes, 'y', 'x', order, nudgeGap);                                          // 4493
            cola.GridRouter.unreverseEdges(routes, routePaths);                                                        // 4494
            return routes;                                                                                             // 4495
        };                                                                                                             // 4496
        // path may have been reversed by the subsequence processing in orderEdges                                     // 4497
        // so now we need to restore the original order                                                                // 4498
        GridRouter.unreverseEdges = function (routes, routePaths) {                                                    // 4499
            routes.forEach(function (segments, i) {                                                                    // 4500
                var path = routePaths[i];                                                                              // 4501
                if (path.reversed) {                                                                                   // 4502
                    segments.reverse(); // reverse order of segments                                                   // 4503
                    segments.forEach(function (segment) {                                                              // 4504
                        segment.reverse(); // reverse each segment                                                     // 4505
                    });                                                                                                // 4506
                }                                                                                                      // 4507
            });                                                                                                        // 4508
        };                                                                                                             // 4509
        GridRouter.angleBetween2Lines = function (line1, line2) {                                                      // 4510
            var angle1 = Math.atan2(line1[0].y - line1[1].y, line1[0].x - line1[1].x);                                 // 4511
            var angle2 = Math.atan2(line2[0].y - line2[1].y, line2[0].x - line2[1].x);                                 // 4512
            var diff = angle1 - angle2;                                                                                // 4513
            if (diff > Math.PI || diff < -Math.PI) {                                                                   // 4514
                diff = angle2 - angle1;                                                                                // 4515
            }                                                                                                          // 4516
            return diff;                                                                                               // 4517
        };                                                                                                             // 4518
        // does the path a-b-c describe a left turn?                                                                   // 4519
        GridRouter.isLeft = function (a, b, c) {                                                                       // 4520
            return ((b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)) <= 0;                                       // 4521
        };                                                                                                             // 4522
        // for the given list of ordered pairs, returns a function that (efficiently) looks-up a specific pair to      // 4523
        // see if it exists in the list                                                                                // 4524
        GridRouter.getOrder = function (pairs) {                                                                       // 4525
            var outgoing = {};                                                                                         // 4526
            for (var i = 0; i < pairs.length; i++) {                                                                   // 4527
                var p = pairs[i];                                                                                      // 4528
                if (typeof outgoing[p.l] === 'undefined')                                                              // 4529
                    outgoing[p.l] = {};                                                                                // 4530
                outgoing[p.l][p.r] = true;                                                                             // 4531
            }                                                                                                          // 4532
            return function (l, r) { return typeof outgoing[l] !== 'undefined' && outgoing[l][r]; };                   // 4533
        };                                                                                                             // 4534
        // returns an ordering (a lookup function) that determines the correct order to nudge the                      // 4535
        // edge paths apart to minimize crossings                                                                      // 4536
        GridRouter.orderEdges = function (edges) {                                                                     // 4537
            var edgeOrder = [];                                                                                        // 4538
            for (var i = 0; i < edges.length - 1; i++) {                                                               // 4539
                for (var j = i + 1; j < edges.length; j++) {                                                           // 4540
                    var e = edges[i], f = edges[j], lcs = new cola.LongestCommonSubsequence(e, f);                     // 4541
                    var u, vi, vj;                                                                                     // 4542
                    if (lcs.length === 0)                                                                              // 4543
                        continue; // no common subpath                                                                 // 4544
                    if (lcs.reversed) {                                                                                // 4545
                        // if we found a common subpath but one of the edges runs the wrong way,                       // 4546
                        // then reverse f.                                                                             // 4547
                        f.reverse();                                                                                   // 4548
                        f.reversed = true;                                                                             // 4549
                        lcs = new cola.LongestCommonSubsequence(e, f);                                                 // 4550
                    }                                                                                                  // 4551
                    if ((lcs.si <= 0 || lcs.ti <= 0) &&                                                                // 4552
                        (lcs.si + lcs.length >= e.length || lcs.ti + lcs.length >= f.length)) {                        // 4553
                        // the paths do not diverge, so make an arbitrary ordering decision                            // 4554
                        edgeOrder.push({ l: i, r: j });                                                                // 4555
                        continue;                                                                                      // 4556
                    }                                                                                                  // 4557
                    if (lcs.si + lcs.length >= e.length || lcs.ti + lcs.length >= f.length) {                          // 4558
                        // if the common subsequence of the                                                            // 4559
                        // two edges being considered goes all the way to the                                          // 4560
                        // end of one (or both) of the lines then we have to                                           // 4561
                        // base our ordering decision on the other end of the                                          // 4562
                        // common subsequence                                                                          // 4563
                        u = e[lcs.si + 1];                                                                             // 4564
                        vj = e[lcs.si - 1];                                                                            // 4565
                        vi = f[lcs.ti - 1];                                                                            // 4566
                    }                                                                                                  // 4567
                    else {                                                                                             // 4568
                        u = e[lcs.si + lcs.length - 2];                                                                // 4569
                        vi = e[lcs.si + lcs.length];                                                                   // 4570
                        vj = f[lcs.ti + lcs.length];                                                                   // 4571
                    }                                                                                                  // 4572
                    if (GridRouter.isLeft(u, vi, vj)) {                                                                // 4573
                        edgeOrder.push({ l: j, r: i });                                                                // 4574
                    }                                                                                                  // 4575
                    else {                                                                                             // 4576
                        edgeOrder.push({ l: i, r: j });                                                                // 4577
                    }                                                                                                  // 4578
                }                                                                                                      // 4579
            }                                                                                                          // 4580
            //edgeOrder.forEach(function (e) { console.log('l:' + e.l + ',r:' + e.r) });                               // 4581
            return cola.GridRouter.getOrder(edgeOrder);                                                                // 4582
        };                                                                                                             // 4583
        // for an orthogonal path described by a sequence of points, create a list of segments                         // 4584
        // if consecutive segments would make a straight line they are merged into a single segment                    // 4585
        // segments are over cloned points, not the original vertices                                                  // 4586
        GridRouter.makeSegments = function (path) {                                                                    // 4587
            function copyPoint(p) {                                                                                    // 4588
                return { x: p.x, y: p.y };                                                                             // 4589
            }                                                                                                          // 4590
            var isStraight = function (a, b, c) { return Math.abs((b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)) < 0.001; };
            var segments = [];                                                                                         // 4592
            var a = copyPoint(path[0]);                                                                                // 4593
            for (var i = 1; i < path.length; i++) {                                                                    // 4594
                var b = copyPoint(path[i]), c = i < path.length - 1 ? path[i + 1] : null;                              // 4595
                if (!c || !isStraight(a, b, c)) {                                                                      // 4596
                    segments.push([a, b]);                                                                             // 4597
                    a = b;                                                                                             // 4598
                }                                                                                                      // 4599
            }                                                                                                          // 4600
            return segments;                                                                                           // 4601
        };                                                                                                             // 4602
        // find a route between node s and node t                                                                      // 4603
        // returns an array of indices to verts                                                                        // 4604
        GridRouter.prototype.route = function (s, t) {                                                                 // 4605
            var _this = this;                                                                                          // 4606
            var source = this.nodes[s], target = this.nodes[t];                                                        // 4607
            this.obstacles = this.siblingObstacles(source, target);                                                    // 4608
            var obstacleLookup = {};                                                                                   // 4609
            this.obstacles.forEach(function (o) { return obstacleLookup[o.id] = o; });                                 // 4610
            this.passableEdges = this.edges.filter(function (e) {                                                      // 4611
                var u = _this.verts[e.source], v = _this.verts[e.target];                                              // 4612
                return !(u.node && u.node.id in obstacleLookup                                                         // 4613
                    || v.node && v.node.id in obstacleLookup);                                                         // 4614
            });                                                                                                        // 4615
            // add dummy segments linking ports inside source and target                                               // 4616
            for (var i = 1; i < source.ports.length; i++) {                                                            // 4617
                var u = source.ports[0].id;                                                                            // 4618
                var v = source.ports[i].id;                                                                            // 4619
                this.passableEdges.push({                                                                              // 4620
                    source: u,                                                                                         // 4621
                    target: v,                                                                                         // 4622
                    length: 0                                                                                          // 4623
                });                                                                                                    // 4624
            }                                                                                                          // 4625
            for (var i = 1; i < target.ports.length; i++) {                                                            // 4626
                var u = target.ports[0].id;                                                                            // 4627
                var v = target.ports[i].id;                                                                            // 4628
                this.passableEdges.push({                                                                              // 4629
                    source: u,                                                                                         // 4630
                    target: v,                                                                                         // 4631
                    length: 0                                                                                          // 4632
                });                                                                                                    // 4633
            }                                                                                                          // 4634
            var getSource = function (e) { return e.source; }, getTarget = function (e) { return e.target; }, getLength = function (e) { return e.length; };
            var shortestPathCalculator = new cola.shortestpaths.Calculator(this.verts.length, this.passableEdges, getSource, getTarget, getLength);
            var bendPenalty = function (u, v, w) {                                                                     // 4637
                var a = _this.verts[u], b = _this.verts[v], c = _this.verts[w];                                        // 4638
                var dx = Math.abs(c.x - a.x), dy = Math.abs(c.y - a.y);                                                // 4639
                // don't count bends from internal node edges                                                          // 4640
                if (a.node === source && a.node === b.node || b.node === target && b.node === c.node)                  // 4641
                    return 0;                                                                                          // 4642
                return dx > 1 && dy > 1 ? 1000 : 0;                                                                    // 4643
            };                                                                                                         // 4644
            // get shortest path                                                                                       // 4645
            var shortestPath = shortestPathCalculator.PathFromNodeToNodeWithPrevCost(source.ports[0].id, target.ports[0].id, bendPenalty);
            // shortest path is reversed and does not include the target port                                          // 4647
            var pathPoints = shortestPath.reverse().map(function (vi) { return _this.verts[vi]; });                    // 4648
            pathPoints.push(this.nodes[target.id].ports[0]);                                                           // 4649
            // filter out any extra end points that are inside the source or target (i.e. the dummy segments above)    // 4650
            return pathPoints.filter(function (v, i) {                                                                 // 4651
                return !(i < pathPoints.length - 1 && pathPoints[i + 1].node === source && v.node === source           // 4652
                    || i > 0 && v.node === target && pathPoints[i - 1].node === target);                               // 4653
            });                                                                                                        // 4654
        };                                                                                                             // 4655
        GridRouter.getRoutePath = function (route, cornerradius, arrowwidth, arrowheight) {                            // 4656
            var result = {                                                                                             // 4657
                routepath: 'M ' + route[0][0].x + ' ' + route[0][0].y + ' ',                                           // 4658
                arrowpath: ''                                                                                          // 4659
            };                                                                                                         // 4660
            if (route.length > 1) {                                                                                    // 4661
                for (var i = 0; i < route.length; i++) {                                                               // 4662
                    var li = route[i];                                                                                 // 4663
                    var x = li[1].x, y = li[1].y;                                                                      // 4664
                    var dx = x - li[0].x;                                                                              // 4665
                    var dy = y - li[0].y;                                                                              // 4666
                    if (i < route.length - 1) {                                                                        // 4667
                        if (Math.abs(dx) > 0) {                                                                        // 4668
                            x -= dx / Math.abs(dx) * cornerradius;                                                     // 4669
                        }                                                                                              // 4670
                        else {                                                                                         // 4671
                            y -= dy / Math.abs(dy) * cornerradius;                                                     // 4672
                        }                                                                                              // 4673
                        result.routepath += 'L ' + x + ' ' + y + ' ';                                                  // 4674
                        var l = route[i + 1];                                                                          // 4675
                        var x0 = l[0].x, y0 = l[0].y;                                                                  // 4676
                        var x1 = l[1].x;                                                                               // 4677
                        var y1 = l[1].y;                                                                               // 4678
                        dx = x1 - x0;                                                                                  // 4679
                        dy = y1 - y0;                                                                                  // 4680
                        var angle = GridRouter.angleBetween2Lines(li, l) < 0 ? 1 : 0;                                  // 4681
                        //console.log(cola.GridRouter.angleBetween2Lines(li, l))                                       // 4682
                        var x2, y2;                                                                                    // 4683
                        if (Math.abs(dx) > 0) {                                                                        // 4684
                            x2 = x0 + dx / Math.abs(dx) * cornerradius;                                                // 4685
                            y2 = y0;                                                                                   // 4686
                        }                                                                                              // 4687
                        else {                                                                                         // 4688
                            x2 = x0;                                                                                   // 4689
                            y2 = y0 + dy / Math.abs(dy) * cornerradius;                                                // 4690
                        }                                                                                              // 4691
                        var cx = Math.abs(x2 - x);                                                                     // 4692
                        var cy = Math.abs(y2 - y);                                                                     // 4693
                        result.routepath += 'A ' + cx + ' ' + cy + ' 0 0 ' + angle + ' ' + x2 + ' ' + y2 + ' ';        // 4694
                    }                                                                                                  // 4695
                    else {                                                                                             // 4696
                        var arrowtip = [x, y];                                                                         // 4697
                        var arrowcorner1, arrowcorner2;                                                                // 4698
                        if (Math.abs(dx) > 0) {                                                                        // 4699
                            x -= dx / Math.abs(dx) * arrowheight;                                                      // 4700
                            arrowcorner1 = [x, y + arrowwidth];                                                        // 4701
                            arrowcorner2 = [x, y - arrowwidth];                                                        // 4702
                        }                                                                                              // 4703
                        else {                                                                                         // 4704
                            y -= dy / Math.abs(dy) * arrowheight;                                                      // 4705
                            arrowcorner1 = [x + arrowwidth, y];                                                        // 4706
                            arrowcorner2 = [x - arrowwidth, y];                                                        // 4707
                        }                                                                                              // 4708
                        result.routepath += 'L ' + x + ' ' + y + ' ';                                                  // 4709
                        if (arrowheight > 0) {                                                                         // 4710
                            result.arrowpath = 'M ' + arrowtip[0] + ' ' + arrowtip[1] + ' L ' + arrowcorner1[0] + ' ' + arrowcorner1[1]
                                + ' L ' + arrowcorner2[0] + ' ' + arrowcorner2[1];                                     // 4712
                        }                                                                                              // 4713
                    }                                                                                                  // 4714
                }                                                                                                      // 4715
            }                                                                                                          // 4716
            else {                                                                                                     // 4717
                var li = route[0];                                                                                     // 4718
                var x = li[1].x, y = li[1].y;                                                                          // 4719
                var dx = x - li[0].x;                                                                                  // 4720
                var dy = y - li[0].y;                                                                                  // 4721
                var arrowtip = [x, y];                                                                                 // 4722
                var arrowcorner1, arrowcorner2;                                                                        // 4723
                if (Math.abs(dx) > 0) {                                                                                // 4724
                    x -= dx / Math.abs(dx) * arrowheight;                                                              // 4725
                    arrowcorner1 = [x, y + arrowwidth];                                                                // 4726
                    arrowcorner2 = [x, y - arrowwidth];                                                                // 4727
                }                                                                                                      // 4728
                else {                                                                                                 // 4729
                    y -= dy / Math.abs(dy) * arrowheight;                                                              // 4730
                    arrowcorner1 = [x + arrowwidth, y];                                                                // 4731
                    arrowcorner2 = [x - arrowwidth, y];                                                                // 4732
                }                                                                                                      // 4733
                result.routepath += 'L ' + x + ' ' + y + ' ';                                                          // 4734
                if (arrowheight > 0) {                                                                                 // 4735
                    result.arrowpath = 'M ' + arrowtip[0] + ' ' + arrowtip[1] + ' L ' + arrowcorner1[0] + ' ' + arrowcorner1[1]
                        + ' L ' + arrowcorner2[0] + ' ' + arrowcorner2[1];                                             // 4737
                }                                                                                                      // 4738
            }                                                                                                          // 4739
            return result;                                                                                             // 4740
        };                                                                                                             // 4741
        return GridRouter;                                                                                             // 4742
    })();                                                                                                              // 4743
    cola.GridRouter = GridRouter;                                                                                      // 4744
})(cola || (cola = {}));                                                                                               // 4745
/**                                                                                                                    // 4746
 * Use cola to do a layout in 3D!! Yay.                                                                                // 4747
 * Pretty simple for the moment.                                                                                       // 4748
 */                                                                                                                    // 4749
var cola;                                                                                                              // 4750
(function (cola) {                                                                                                     // 4751
    var Link3D = (function () {                                                                                        // 4752
        function Link3D(source, target) {                                                                              // 4753
            this.source = source;                                                                                      // 4754
            this.target = target;                                                                                      // 4755
        }                                                                                                              // 4756
        Link3D.prototype.actualLength = function (x) {                                                                 // 4757
            var _this = this;                                                                                          // 4758
            return Math.sqrt(x.reduce(function (c, v) {                                                                // 4759
                var dx = v[_this.target] - v[_this.source];                                                            // 4760
                return c + dx * dx;                                                                                    // 4761
            }, 0));                                                                                                    // 4762
        };                                                                                                             // 4763
        return Link3D;                                                                                                 // 4764
    })();                                                                                                              // 4765
    cola.Link3D = Link3D;                                                                                              // 4766
    var Node3D = (function () {                                                                                        // 4767
        function Node3D(x, y, z) {                                                                                     // 4768
            if (x === void 0) { x = 0; }                                                                               // 4769
            if (y === void 0) { y = 0; }                                                                               // 4770
            if (z === void 0) { z = 0; }                                                                               // 4771
            this.x = x;                                                                                                // 4772
            this.y = y;                                                                                                // 4773
            this.z = z;                                                                                                // 4774
        }                                                                                                              // 4775
        return Node3D;                                                                                                 // 4776
    })();                                                                                                              // 4777
    cola.Node3D = Node3D;                                                                                              // 4778
    var Layout3D = (function () {                                                                                      // 4779
        function Layout3D(nodes, links, idealLinkLength) {                                                             // 4780
            var _this = this;                                                                                          // 4781
            if (idealLinkLength === void 0) { idealLinkLength = 1; }                                                   // 4782
            this.nodes = nodes;                                                                                        // 4783
            this.links = links;                                                                                        // 4784
            this.idealLinkLength = idealLinkLength;                                                                    // 4785
            this.constraints = null;                                                                                   // 4786
            this.useJaccardLinkLengths = true;                                                                         // 4787
            this.result = new Array(Layout3D.k);                                                                       // 4788
            for (var i = 0; i < Layout3D.k; ++i) {                                                                     // 4789
                this.result[i] = new Array(nodes.length);                                                              // 4790
            }                                                                                                          // 4791
            nodes.forEach(function (v, i) {                                                                            // 4792
                for (var _i = 0, _a = Layout3D.dims; _i < _a.length; _i++) {                                           // 4793
                    var dim = _a[_i];                                                                                  // 4794
                    if (typeof v[dim] == 'undefined')                                                                  // 4795
                        v[dim] = Math.random();                                                                        // 4796
                }                                                                                                      // 4797
                _this.result[0][i] = v.x;                                                                              // 4798
                _this.result[1][i] = v.y;                                                                              // 4799
                _this.result[2][i] = v.z;                                                                              // 4800
            });                                                                                                        // 4801
        }                                                                                                              // 4802
        ;                                                                                                              // 4803
        Layout3D.prototype.linkLength = function (l) {                                                                 // 4804
            return l.actualLength(this.result);                                                                        // 4805
        };                                                                                                             // 4806
        Layout3D.prototype.start = function (iterations) {                                                             // 4807
            var _this = this;                                                                                          // 4808
            if (iterations === void 0) { iterations = 100; }                                                           // 4809
            var n = this.nodes.length;                                                                                 // 4810
            var linkAccessor = new LinkAccessor();                                                                     // 4811
            if (this.useJaccardLinkLengths)                                                                            // 4812
                cola.jaccardLinkLengths(this.links, linkAccessor, 1.5);                                                // 4813
            this.links.forEach(function (e) { return e.length *= _this.idealLinkLength; });                            // 4814
            // Create the distance matrix that Cola needs                                                              // 4815
            var distanceMatrix = (new cola.shortestpaths.Calculator(n, this.links, function (e) { return e.source; }, function (e) { return e.target; }, function (e) { return e.length; })).DistanceMatrix();
            var D = cola.Descent.createSquareMatrix(n, function (i, j) { return distanceMatrix[i][j]; });              // 4817
            // G is a square matrix with G[i][j] = 1 iff there exists an edge between node i and node j                // 4818
            // otherwise 2.                                                                                            // 4819
            var G = cola.Descent.createSquareMatrix(n, function () { return 2; });                                     // 4820
            this.links.forEach(function (_a) {                                                                         // 4821
                var source = _a.source, target = _a.target;                                                            // 4822
                return G[source][target] = G[target][source] = 1;                                                      // 4823
            });                                                                                                        // 4824
            this.descent = new cola.Descent(this.result, D);                                                           // 4825
            this.descent.threshold = 1e-3;                                                                             // 4826
            this.descent.G = G;                                                                                        // 4827
            //let constraints = this.links.map(e=> <any>{                                                              // 4828
            //    axis: 'y', left: e.source, right: e.target, gap: e.length*1.5                                        // 4829
            //});                                                                                                      // 4830
            if (this.constraints)                                                                                      // 4831
                this.descent.project = new cola.vpsc.Projection(this.nodes, null, null, this.constraints).projectFunctions();
            for (var i = 0; i < this.nodes.length; i++) {                                                              // 4833
                var v = this.nodes[i];                                                                                 // 4834
                if (v.fixed) {                                                                                         // 4835
                    this.descent.locks.add(i, [v.x, v.y, v.z]);                                                        // 4836
                }                                                                                                      // 4837
            }                                                                                                          // 4838
            this.descent.run(iterations);                                                                              // 4839
            return this;                                                                                               // 4840
        };                                                                                                             // 4841
        Layout3D.prototype.tick = function () {                                                                        // 4842
            this.descent.locks.clear();                                                                                // 4843
            for (var i = 0; i < this.nodes.length; i++) {                                                              // 4844
                var v = this.nodes[i];                                                                                 // 4845
                if (v.fixed) {                                                                                         // 4846
                    this.descent.locks.add(i, [v.x, v.y, v.z]);                                                        // 4847
                }                                                                                                      // 4848
            }                                                                                                          // 4849
            return this.descent.rungeKutta();                                                                          // 4850
        };                                                                                                             // 4851
        Layout3D.dims = ['x', 'y', 'z'];                                                                               // 4852
        Layout3D.k = Layout3D.dims.length;                                                                             // 4853
        return Layout3D;                                                                                               // 4854
    })();                                                                                                              // 4855
    cola.Layout3D = Layout3D;                                                                                          // 4856
    var LinkAccessor = (function () {                                                                                  // 4857
        function LinkAccessor() {                                                                                      // 4858
        }                                                                                                              // 4859
        LinkAccessor.prototype.getSourceIndex = function (e) { return e.source; };                                     // 4860
        LinkAccessor.prototype.getTargetIndex = function (e) { return e.target; };                                     // 4861
        LinkAccessor.prototype.getLength = function (e) { return e.length; };                                          // 4862
        LinkAccessor.prototype.setLength = function (e, l) { e.length = l; };                                          // 4863
        return LinkAccessor;                                                                                           // 4864
    })();                                                                                                              // 4865
})(cola || (cola = {}));                                                                                               // 4866
/**                                                                                                                    // 4867
 * When compiled, this file will build a CommonJS module for WebCola.                                                  // 4868
 *                                                                                                                     // 4869
 * Unfortunately, internal and external TypeScript modules do not get                                                  // 4870
 * along well. This method of converting internal modules to external                                                  // 4871
 * modules is a bit of a hack, but is minimally invasive (i.e., no modules                                             // 4872
 * need to be rewritten as external modules and modules can still span                                                 // 4873
 * multiple files)                                                                                                     // 4874
 *                                                                                                                     // 4875
 * When starting a new project from scratch where CommonJS compatibility                                               // 4876
 * is desired, consider instead preferring external modules to internal                                                // 4877
 * modules.                                                                                                            // 4878
 */                                                                                                                    // 4879
///<reference path="./src/d3adaptor.ts"/>                                                                              // 4880
///<reference path="./src/descent.ts"/>                                                                                // 4881
///<reference path="./src/geom.ts"/>                                                                                   // 4882
///<reference path="./src/gridrouter.ts"/>                                                                             // 4883
///<reference path="./src/handledisconnected.ts"/>                                                                     // 4884
///<reference path="./src/layout.ts"/>                                                                                 // 4885
///<reference path="./src/layout3d.ts"/>                                                                               // 4886
///<reference path="./src/linklengths.ts"/>                                                                            // 4887
///<reference path="./src/powergraph.ts"/>                                                                             // 4888
///<reference path="./src/pqueue.ts"/>                                                                                 // 4889
///<reference path="./src/rectangle.ts"/>                                                                              // 4890
///<reference path="./src/shortestpaths.ts"/>                                                                          // 4891
///<reference path="./src/vpsc.ts"/>                                                                                   // 4892
///<reference path="./src/rbtree.ts"/>                                                                                 // 4893
// Export cola as a CommonJS module. Note that we're bypassing TypeScript's external                                   // 4894
// module system here. Because internal modules were written with the browser in mind,                                 // 4895
// TypeScript's model is that the current context is the global context (i.e., window.cola                             // 4896
// === cola), so `export = cola` is transpiled as a no-op.                                                             // 4897
module.exports = cola;                                                                                                 // 4898
                                                                                                                       // 4899
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}}},"meteor-node-stubs":{"package.json":function(require,exports){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/package.json                                                                         //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
exports.name = "meteor-node-stubs";                                                                                    // 1
exports.version = "0.2.1";                                                                                             // 2
exports.main = "index.js";                                                                                             // 3
                                                                                                                       // 4
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"index.js":["./map.json",function(require,exports){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/index.js                                                                             //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
var map = require("./map.json");                                                                                       // 1
var meteorAliases = {};                                                                                                // 2
                                                                                                                       // 3
Object.keys(map).forEach(function (id) {                                                                               // 4
  if (typeof map[id] === "string") {                                                                                   // 5
    try {                                                                                                              // 6
      exports[id] = meteorAliases[id + ".js"] =                                                                        // 7
        require.resolve(map[id]);                                                                                      // 8
    } catch (e) {                                                                                                      // 9
      // Resolution can fail at runtime if the stub was not included in the                                            // 10
      // bundle because nothing depended on it.                                                                        // 11
    }                                                                                                                  // 12
  } else {                                                                                                             // 13
    exports[id] = map[id];                                                                                             // 14
    meteorAliases[id + ".js"] = function(){};                                                                          // 15
  }                                                                                                                    // 16
});                                                                                                                    // 17
                                                                                                                       // 18
if (typeof meteorInstall === "function") {                                                                             // 19
  meteorInstall({                                                                                                      // 20
    // Install the aliases into a node_modules directory one level up from                                             // 21
    // the root directory, so that they do not clutter the namespace                                                   // 22
    // available to apps and packages.                                                                                 // 23
    "..": {                                                                                                            // 24
      node_modules: meteorAliases                                                                                      // 25
    }                                                                                                                  // 26
  });                                                                                                                  // 27
}                                                                                                                      // 28
                                                                                                                       // 29
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}],"map.json":function(require,exports,module){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/map.json                                                                             //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
module.exports = {                                                                                                     // 1
  "assert": "assert/",                                                                                                 // 2
  "buffer": "buffer/",                                                                                                 // 3
  "child_process": null,                                                                                               // 4
  "cluster": null,                                                                                                     // 5
  "console": "console-browserify",                                                                                     // 6
  "constants": "constants-browserify",                                                                                 // 7
  "crypto": "crypto-browserify",                                                                                       // 8
  "dgram": null,                                                                                                       // 9
  "dns": null,                                                                                                         // 10
  "domain": "domain-browser",                                                                                          // 11
  "events": "events/",                                                                                                 // 12
  "fs": null,                                                                                                          // 13
  "http": "http-browserify",                                                                                           // 14
  "https": "https-browserify",                                                                                         // 15
  "module": null,                                                                                                      // 16
  "net": null,                                                                                                         // 17
  "os": "os-browserify/browser.js",                                                                                    // 18
  "path": "path-browserify",                                                                                           // 19
  "process": "process/browser.js",                                                                                     // 20
  "punycode": "punycode/",                                                                                             // 21
  "querystring": "querystring-es3/",                                                                                   // 22
  "readline": null,                                                                                                    // 23
  "repl": null,                                                                                                        // 24
  "stream": "stream-browserify",                                                                                       // 25
  "_stream_duplex": "readable-stream/duplex.js",                                                                       // 26
  "_stream_passthrough": "readable-stream/passthrough.js",                                                             // 27
  "_stream_readable": "readable-stream/readable.js",                                                                   // 28
  "_stream_transform": "readable-stream/transform.js",                                                                 // 29
  "_stream_writable": "readable-stream/writable.js",                                                                   // 30
  "string_decoder": "string_decoder/",                                                                                 // 31
  "sys": "util/util.js",                                                                                               // 32
  "timers": "timers-browserify",                                                                                       // 33
  "tls": null,                                                                                                         // 34
  "tty": "tty-browserify",                                                                                             // 35
  "url": "url/",                                                                                                       // 36
  "util": "util/util.js",                                                                                              // 37
  "vm": "vm-browserify",                                                                                               // 38
  "zlib": "browserify-zlib"                                                                                            // 39
};                                                                                                                     // 40
                                                                                                                       // 41
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"deps":{"buffer.js":["buffer/",function(require){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/deps/buffer.js                                                                       //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
require("buffer/");                                                                                                    // 1
                                                                                                                       // 2
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}],"process.js":["process/browser.js",function(require){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/deps/process.js                                                                      //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
require("process/browser.js");                                                                                         // 1
                                                                                                                       // 2
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}],"domain.js":["domain-browser",function(require){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/deps/domain.js                                                                       //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
require("domain-browser");                                                                                             // 1
                                                                                                                       // 2
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}]},"node_modules":{"buffer":{"package.json":function(require,exports){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/node_modules/buffer/package.json                                                     //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
exports.name = "buffer";                                                                                               // 1
exports.version = "4.5.0";                                                                                             // 2
exports.main = "index.js";                                                                                             // 3
                                                                                                                       // 4
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"index.js":["base64-js","ieee754","isarray",function(require,exports,module){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/node_modules/buffer/index.js                                                         //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
/*!                                                                                                                    // 1
 * The buffer module from node.js, for the browser.                                                                    // 2
 *                                                                                                                     // 3
 * @author   Feross Aboukhadijeh <feross@feross.org> <http://feross.org>                                               // 4
 * @license  MIT                                                                                                       // 5
 */                                                                                                                    // 6
/* eslint-disable no-proto */                                                                                          // 7
                                                                                                                       // 8
'use strict'                                                                                                           // 9
                                                                                                                       // 10
var base64 = require('base64-js')                                                                                      // 11
var ieee754 = require('ieee754')                                                                                       // 12
var isArray = require('isarray')                                                                                       // 13
                                                                                                                       // 14
exports.Buffer = Buffer                                                                                                // 15
exports.SlowBuffer = SlowBuffer                                                                                        // 16
exports.INSPECT_MAX_BYTES = 50                                                                                         // 17
Buffer.poolSize = 8192 // not used by this implementation                                                              // 18
                                                                                                                       // 19
var rootParent = {}                                                                                                    // 20
                                                                                                                       // 21
/**                                                                                                                    // 22
 * If `Buffer.TYPED_ARRAY_SUPPORT`:                                                                                    // 23
 *   === true    Use Uint8Array implementation (fastest)                                                               // 24
 *   === false   Use Object implementation (most compatible, even IE6)                                                 // 25
 *                                                                                                                     // 26
 * Browsers that support typed arrays are IE 10+, Firefox 4+, Chrome 7+, Safari 5.1+,                                  // 27
 * Opera 11.6+, iOS 4.2+.                                                                                              // 28
 *                                                                                                                     // 29
 * Due to various browser bugs, sometimes the Object implementation will be used even                                  // 30
 * when the browser supports typed arrays.                                                                             // 31
 *                                                                                                                     // 32
 * Note:                                                                                                               // 33
 *                                                                                                                     // 34
 *   - Firefox 4-29 lacks support for adding new properties to `Uint8Array` instances,                                 // 35
 *     See: https://bugzilla.mozilla.org/show_bug.cgi?id=695438.                                                       // 36
 *                                                                                                                     // 37
 *   - Chrome 9-10 is missing the `TypedArray.prototype.subarray` function.                                            // 38
 *                                                                                                                     // 39
 *   - IE10 has a broken `TypedArray.prototype.subarray` function which returns arrays of                              // 40
 *     incorrect length in some situations.                                                                            // 41
                                                                                                                       // 42
 * We detect these buggy browsers and set `Buffer.TYPED_ARRAY_SUPPORT` to `false` so they                              // 43
 * get the Object implementation, which is slower but behaves correctly.                                               // 44
 */                                                                                                                    // 45
Buffer.TYPED_ARRAY_SUPPORT = global.TYPED_ARRAY_SUPPORT !== undefined                                                  // 46
  ? global.TYPED_ARRAY_SUPPORT                                                                                         // 47
  : typedArraySupport()                                                                                                // 48
                                                                                                                       // 49
function typedArraySupport () {                                                                                        // 50
  try {                                                                                                                // 51
    var arr = new Uint8Array(1)                                                                                        // 52
    arr.foo = function () { return 42 }                                                                                // 53
    return arr.foo() === 42 && // typed array instances can be augmented                                               // 54
        typeof arr.subarray === 'function' && // chrome 9-10 lack `subarray`                                           // 55
        arr.subarray(1, 1).byteLength === 0 // ie10 has broken `subarray`                                              // 56
  } catch (e) {                                                                                                        // 57
    return false                                                                                                       // 58
  }                                                                                                                    // 59
}                                                                                                                      // 60
                                                                                                                       // 61
function kMaxLength () {                                                                                               // 62
  return Buffer.TYPED_ARRAY_SUPPORT                                                                                    // 63
    ? 0x7fffffff                                                                                                       // 64
    : 0x3fffffff                                                                                                       // 65
}                                                                                                                      // 66
                                                                                                                       // 67
/**                                                                                                                    // 68
 * The Buffer constructor returns instances of `Uint8Array` that have their                                            // 69
 * prototype changed to `Buffer.prototype`. Furthermore, `Buffer` is a subclass of                                     // 70
 * `Uint8Array`, so the returned instances will have all the node `Buffer` methods                                     // 71
 * and the `Uint8Array` methods. Square bracket notation works as expected -- it                                       // 72
 * returns a single octet.                                                                                             // 73
 *                                                                                                                     // 74
 * The `Uint8Array` prototype remains unmodified.                                                                      // 75
 */                                                                                                                    // 76
function Buffer (arg) {                                                                                                // 77
  if (!(this instanceof Buffer)) {                                                                                     // 78
    // Avoid going through an ArgumentsAdaptorTrampoline in the common case.                                           // 79
    if (arguments.length > 1) return new Buffer(arg, arguments[1])                                                     // 80
    return new Buffer(arg)                                                                                             // 81
  }                                                                                                                    // 82
                                                                                                                       // 83
  if (!Buffer.TYPED_ARRAY_SUPPORT) {                                                                                   // 84
    this.length = 0                                                                                                    // 85
    this.parent = undefined                                                                                            // 86
  }                                                                                                                    // 87
                                                                                                                       // 88
  // Common case.                                                                                                      // 89
  if (typeof arg === 'number') {                                                                                       // 90
    return fromNumber(this, arg)                                                                                       // 91
  }                                                                                                                    // 92
                                                                                                                       // 93
  // Slightly less common case.                                                                                        // 94
  if (typeof arg === 'string') {                                                                                       // 95
    return fromString(this, arg, arguments.length > 1 ? arguments[1] : 'utf8')                                         // 96
  }                                                                                                                    // 97
                                                                                                                       // 98
  // Unusual.                                                                                                          // 99
  return fromObject(this, arg)                                                                                         // 100
}                                                                                                                      // 101
                                                                                                                       // 102
// TODO: Legacy, not needed anymore. Remove in next major version.                                                     // 103
Buffer._augment = function (arr) {                                                                                     // 104
  arr.__proto__ = Buffer.prototype                                                                                     // 105
  return arr                                                                                                           // 106
}                                                                                                                      // 107
                                                                                                                       // 108
function fromNumber (that, length) {                                                                                   // 109
  that = allocate(that, length < 0 ? 0 : checked(length) | 0)                                                          // 110
  if (!Buffer.TYPED_ARRAY_SUPPORT) {                                                                                   // 111
    for (var i = 0; i < length; i++) {                                                                                 // 112
      that[i] = 0                                                                                                      // 113
    }                                                                                                                  // 114
  }                                                                                                                    // 115
  return that                                                                                                          // 116
}                                                                                                                      // 117
                                                                                                                       // 118
function fromString (that, string, encoding) {                                                                         // 119
  if (typeof encoding !== 'string' || encoding === '') encoding = 'utf8'                                               // 120
                                                                                                                       // 121
  // Assumption: byteLength() return value is always < kMaxLength.                                                     // 122
  var length = byteLength(string, encoding) | 0                                                                        // 123
  that = allocate(that, length)                                                                                        // 124
                                                                                                                       // 125
  that.write(string, encoding)                                                                                         // 126
  return that                                                                                                          // 127
}                                                                                                                      // 128
                                                                                                                       // 129
function fromObject (that, object) {                                                                                   // 130
  if (Buffer.isBuffer(object)) return fromBuffer(that, object)                                                         // 131
                                                                                                                       // 132
  if (isArray(object)) return fromArray(that, object)                                                                  // 133
                                                                                                                       // 134
  if (object == null) {                                                                                                // 135
    throw new TypeError('must start with number, buffer, array or string')                                             // 136
  }                                                                                                                    // 137
                                                                                                                       // 138
  if (typeof ArrayBuffer !== 'undefined') {                                                                            // 139
    if (object.buffer instanceof ArrayBuffer) {                                                                        // 140
      return fromTypedArray(that, object)                                                                              // 141
    }                                                                                                                  // 142
    if (object instanceof ArrayBuffer) {                                                                               // 143
      return fromArrayBuffer(that, object)                                                                             // 144
    }                                                                                                                  // 145
  }                                                                                                                    // 146
                                                                                                                       // 147
  if (object.length) return fromArrayLike(that, object)                                                                // 148
                                                                                                                       // 149
  return fromJsonObject(that, object)                                                                                  // 150
}                                                                                                                      // 151
                                                                                                                       // 152
function fromBuffer (that, buffer) {                                                                                   // 153
  var length = checked(buffer.length) | 0                                                                              // 154
  that = allocate(that, length)                                                                                        // 155
  buffer.copy(that, 0, 0, length)                                                                                      // 156
  return that                                                                                                          // 157
}                                                                                                                      // 158
                                                                                                                       // 159
function fromArray (that, array) {                                                                                     // 160
  var length = checked(array.length) | 0                                                                               // 161
  that = allocate(that, length)                                                                                        // 162
  for (var i = 0; i < length; i += 1) {                                                                                // 163
    that[i] = array[i] & 255                                                                                           // 164
  }                                                                                                                    // 165
  return that                                                                                                          // 166
}                                                                                                                      // 167
                                                                                                                       // 168
// Duplicate of fromArray() to keep fromArray() monomorphic.                                                           // 169
function fromTypedArray (that, array) {                                                                                // 170
  var length = checked(array.length) | 0                                                                               // 171
  that = allocate(that, length)                                                                                        // 172
  // Truncating the elements is probably not what people expect from typed                                             // 173
  // arrays with BYTES_PER_ELEMENT > 1 but it's compatible with the behavior                                           // 174
  // of the old Buffer constructor.                                                                                    // 175
  for (var i = 0; i < length; i += 1) {                                                                                // 176
    that[i] = array[i] & 255                                                                                           // 177
  }                                                                                                                    // 178
  return that                                                                                                          // 179
}                                                                                                                      // 180
                                                                                                                       // 181
function fromArrayBuffer (that, array) {                                                                               // 182
  array.byteLength // this throws if `array` is not a valid ArrayBuffer                                                // 183
                                                                                                                       // 184
  if (Buffer.TYPED_ARRAY_SUPPORT) {                                                                                    // 185
    // Return an augmented `Uint8Array` instance, for best performance                                                 // 186
    that = new Uint8Array(array)                                                                                       // 187
    that.__proto__ = Buffer.prototype                                                                                  // 188
  } else {                                                                                                             // 189
    // Fallback: Return an object instance of the Buffer class                                                         // 190
    that = fromTypedArray(that, new Uint8Array(array))                                                                 // 191
  }                                                                                                                    // 192
  return that                                                                                                          // 193
}                                                                                                                      // 194
                                                                                                                       // 195
function fromArrayLike (that, array) {                                                                                 // 196
  var length = checked(array.length) | 0                                                                               // 197
  that = allocate(that, length)                                                                                        // 198
  for (var i = 0; i < length; i += 1) {                                                                                // 199
    that[i] = array[i] & 255                                                                                           // 200
  }                                                                                                                    // 201
  return that                                                                                                          // 202
}                                                                                                                      // 203
                                                                                                                       // 204
// Deserialize { type: 'Buffer', data: [1,2,3,...] } into a Buffer object.                                             // 205
// Returns a zero-length buffer for inputs that don't conform to the spec.                                             // 206
function fromJsonObject (that, object) {                                                                               // 207
  var array                                                                                                            // 208
  var length = 0                                                                                                       // 209
                                                                                                                       // 210
  if (object.type === 'Buffer' && isArray(object.data)) {                                                              // 211
    array = object.data                                                                                                // 212
    length = checked(array.length) | 0                                                                                 // 213
  }                                                                                                                    // 214
  that = allocate(that, length)                                                                                        // 215
                                                                                                                       // 216
  for (var i = 0; i < length; i += 1) {                                                                                // 217
    that[i] = array[i] & 255                                                                                           // 218
  }                                                                                                                    // 219
  return that                                                                                                          // 220
}                                                                                                                      // 221
                                                                                                                       // 222
if (Buffer.TYPED_ARRAY_SUPPORT) {                                                                                      // 223
  Buffer.prototype.__proto__ = Uint8Array.prototype                                                                    // 224
  Buffer.__proto__ = Uint8Array                                                                                        // 225
  if (typeof Symbol !== 'undefined' && Symbol.species &&                                                               // 226
      Buffer[Symbol.species] === Buffer) {                                                                             // 227
    // Fix subarray() in ES2016. See: https://github.com/feross/buffer/pull/97                                         // 228
    Object.defineProperty(Buffer, Symbol.species, {                                                                    // 229
      value: null,                                                                                                     // 230
      configurable: true                                                                                               // 231
    })                                                                                                                 // 232
  }                                                                                                                    // 233
} else {                                                                                                               // 234
  // pre-set for values that may exist in the future                                                                   // 235
  Buffer.prototype.length = undefined                                                                                  // 236
  Buffer.prototype.parent = undefined                                                                                  // 237
}                                                                                                                      // 238
                                                                                                                       // 239
function allocate (that, length) {                                                                                     // 240
  if (Buffer.TYPED_ARRAY_SUPPORT) {                                                                                    // 241
    // Return an augmented `Uint8Array` instance, for best performance                                                 // 242
    that = new Uint8Array(length)                                                                                      // 243
    that.__proto__ = Buffer.prototype                                                                                  // 244
  } else {                                                                                                             // 245
    // Fallback: Return an object instance of the Buffer class                                                         // 246
    that.length = length                                                                                               // 247
  }                                                                                                                    // 248
                                                                                                                       // 249
  var fromPool = length !== 0 && length <= Buffer.poolSize >>> 1                                                       // 250
  if (fromPool) that.parent = rootParent                                                                               // 251
                                                                                                                       // 252
  return that                                                                                                          // 253
}                                                                                                                      // 254
                                                                                                                       // 255
function checked (length) {                                                                                            // 256
  // Note: cannot use `length < kMaxLength` here because that fails when                                               // 257
  // length is NaN (which is otherwise coerced to zero.)                                                               // 258
  if (length >= kMaxLength()) {                                                                                        // 259
    throw new RangeError('Attempt to allocate Buffer larger than maximum ' +                                           // 260
                         'size: 0x' + kMaxLength().toString(16) + ' bytes')                                            // 261
  }                                                                                                                    // 262
  return length | 0                                                                                                    // 263
}                                                                                                                      // 264
                                                                                                                       // 265
function SlowBuffer (subject, encoding) {                                                                              // 266
  if (!(this instanceof SlowBuffer)) return new SlowBuffer(subject, encoding)                                          // 267
                                                                                                                       // 268
  var buf = new Buffer(subject, encoding)                                                                              // 269
  delete buf.parent                                                                                                    // 270
  return buf                                                                                                           // 271
}                                                                                                                      // 272
                                                                                                                       // 273
Buffer.isBuffer = function isBuffer (b) {                                                                              // 274
  return !!(b != null && b._isBuffer)                                                                                  // 275
}                                                                                                                      // 276
                                                                                                                       // 277
Buffer.compare = function compare (a, b) {                                                                             // 278
  if (!Buffer.isBuffer(a) || !Buffer.isBuffer(b)) {                                                                    // 279
    throw new TypeError('Arguments must be Buffers')                                                                   // 280
  }                                                                                                                    // 281
                                                                                                                       // 282
  if (a === b) return 0                                                                                                // 283
                                                                                                                       // 284
  var x = a.length                                                                                                     // 285
  var y = b.length                                                                                                     // 286
                                                                                                                       // 287
  var i = 0                                                                                                            // 288
  var len = Math.min(x, y)                                                                                             // 289
  while (i < len) {                                                                                                    // 290
    if (a[i] !== b[i]) break                                                                                           // 291
                                                                                                                       // 292
    ++i                                                                                                                // 293
  }                                                                                                                    // 294
                                                                                                                       // 295
  if (i !== len) {                                                                                                     // 296
    x = a[i]                                                                                                           // 297
    y = b[i]                                                                                                           // 298
  }                                                                                                                    // 299
                                                                                                                       // 300
  if (x < y) return -1                                                                                                 // 301
  if (y < x) return 1                                                                                                  // 302
  return 0                                                                                                             // 303
}                                                                                                                      // 304
                                                                                                                       // 305
Buffer.isEncoding = function isEncoding (encoding) {                                                                   // 306
  switch (String(encoding).toLowerCase()) {                                                                            // 307
    case 'hex':                                                                                                        // 308
    case 'utf8':                                                                                                       // 309
    case 'utf-8':                                                                                                      // 310
    case 'ascii':                                                                                                      // 311
    case 'binary':                                                                                                     // 312
    case 'base64':                                                                                                     // 313
    case 'raw':                                                                                                        // 314
    case 'ucs2':                                                                                                       // 315
    case 'ucs-2':                                                                                                      // 316
    case 'utf16le':                                                                                                    // 317
    case 'utf-16le':                                                                                                   // 318
      return true                                                                                                      // 319
    default:                                                                                                           // 320
      return false                                                                                                     // 321
  }                                                                                                                    // 322
}                                                                                                                      // 323
                                                                                                                       // 324
Buffer.concat = function concat (list, length) {                                                                       // 325
  if (!isArray(list)) throw new TypeError('list argument must be an Array of Buffers.')                                // 326
                                                                                                                       // 327
  if (list.length === 0) {                                                                                             // 328
    return new Buffer(0)                                                                                               // 329
  }                                                                                                                    // 330
                                                                                                                       // 331
  var i                                                                                                                // 332
  if (length === undefined) {                                                                                          // 333
    length = 0                                                                                                         // 334
    for (i = 0; i < list.length; i++) {                                                                                // 335
      length += list[i].length                                                                                         // 336
    }                                                                                                                  // 337
  }                                                                                                                    // 338
                                                                                                                       // 339
  var buf = new Buffer(length)                                                                                         // 340
  var pos = 0                                                                                                          // 341
  for (i = 0; i < list.length; i++) {                                                                                  // 342
    var item = list[i]                                                                                                 // 343
    item.copy(buf, pos)                                                                                                // 344
    pos += item.length                                                                                                 // 345
  }                                                                                                                    // 346
  return buf                                                                                                           // 347
}                                                                                                                      // 348
                                                                                                                       // 349
function byteLength (string, encoding) {                                                                               // 350
  if (typeof string !== 'string') string = '' + string                                                                 // 351
                                                                                                                       // 352
  var len = string.length                                                                                              // 353
  if (len === 0) return 0                                                                                              // 354
                                                                                                                       // 355
  // Use a for loop to avoid recursion                                                                                 // 356
  var loweredCase = false                                                                                              // 357
  for (;;) {                                                                                                           // 358
    switch (encoding) {                                                                                                // 359
      case 'ascii':                                                                                                    // 360
      case 'binary':                                                                                                   // 361
      // Deprecated                                                                                                    // 362
      case 'raw':                                                                                                      // 363
      case 'raws':                                                                                                     // 364
        return len                                                                                                     // 365
      case 'utf8':                                                                                                     // 366
      case 'utf-8':                                                                                                    // 367
        return utf8ToBytes(string).length                                                                              // 368
      case 'ucs2':                                                                                                     // 369
      case 'ucs-2':                                                                                                    // 370
      case 'utf16le':                                                                                                  // 371
      case 'utf-16le':                                                                                                 // 372
        return len * 2                                                                                                 // 373
      case 'hex':                                                                                                      // 374
        return len >>> 1                                                                                               // 375
      case 'base64':                                                                                                   // 376
        return base64ToBytes(string).length                                                                            // 377
      default:                                                                                                         // 378
        if (loweredCase) return utf8ToBytes(string).length // assume utf8                                              // 379
        encoding = ('' + encoding).toLowerCase()                                                                       // 380
        loweredCase = true                                                                                             // 381
    }                                                                                                                  // 382
  }                                                                                                                    // 383
}                                                                                                                      // 384
Buffer.byteLength = byteLength                                                                                         // 385
                                                                                                                       // 386
function slowToString (encoding, start, end) {                                                                         // 387
  var loweredCase = false                                                                                              // 388
                                                                                                                       // 389
  start = start | 0                                                                                                    // 390
  end = end === undefined || end === Infinity ? this.length : end | 0                                                  // 391
                                                                                                                       // 392
  if (!encoding) encoding = 'utf8'                                                                                     // 393
  if (start < 0) start = 0                                                                                             // 394
  if (end > this.length) end = this.length                                                                             // 395
  if (end <= start) return ''                                                                                          // 396
                                                                                                                       // 397
  while (true) {                                                                                                       // 398
    switch (encoding) {                                                                                                // 399
      case 'hex':                                                                                                      // 400
        return hexSlice(this, start, end)                                                                              // 401
                                                                                                                       // 402
      case 'utf8':                                                                                                     // 403
      case 'utf-8':                                                                                                    // 404
        return utf8Slice(this, start, end)                                                                             // 405
                                                                                                                       // 406
      case 'ascii':                                                                                                    // 407
        return asciiSlice(this, start, end)                                                                            // 408
                                                                                                                       // 409
      case 'binary':                                                                                                   // 410
        return binarySlice(this, start, end)                                                                           // 411
                                                                                                                       // 412
      case 'base64':                                                                                                   // 413
        return base64Slice(this, start, end)                                                                           // 414
                                                                                                                       // 415
      case 'ucs2':                                                                                                     // 416
      case 'ucs-2':                                                                                                    // 417
      case 'utf16le':                                                                                                  // 418
      case 'utf-16le':                                                                                                 // 419
        return utf16leSlice(this, start, end)                                                                          // 420
                                                                                                                       // 421
      default:                                                                                                         // 422
        if (loweredCase) throw new TypeError('Unknown encoding: ' + encoding)                                          // 423
        encoding = (encoding + '').toLowerCase()                                                                       // 424
        loweredCase = true                                                                                             // 425
    }                                                                                                                  // 426
  }                                                                                                                    // 427
}                                                                                                                      // 428
                                                                                                                       // 429
// The property is used by `Buffer.isBuffer` and `is-buffer` (in Safari 5-7) to detect                                 // 430
// Buffer instances.                                                                                                   // 431
Buffer.prototype._isBuffer = true                                                                                      // 432
                                                                                                                       // 433
Buffer.prototype.toString = function toString () {                                                                     // 434
  var length = this.length | 0                                                                                         // 435
  if (length === 0) return ''                                                                                          // 436
  if (arguments.length === 0) return utf8Slice(this, 0, length)                                                        // 437
  return slowToString.apply(this, arguments)                                                                           // 438
}                                                                                                                      // 439
                                                                                                                       // 440
Buffer.prototype.equals = function equals (b) {                                                                        // 441
  if (!Buffer.isBuffer(b)) throw new TypeError('Argument must be a Buffer')                                            // 442
  if (this === b) return true                                                                                          // 443
  return Buffer.compare(this, b) === 0                                                                                 // 444
}                                                                                                                      // 445
                                                                                                                       // 446
Buffer.prototype.inspect = function inspect () {                                                                       // 447
  var str = ''                                                                                                         // 448
  var max = exports.INSPECT_MAX_BYTES                                                                                  // 449
  if (this.length > 0) {                                                                                               // 450
    str = this.toString('hex', 0, max).match(/.{2}/g).join(' ')                                                        // 451
    if (this.length > max) str += ' ... '                                                                              // 452
  }                                                                                                                    // 453
  return '<Buffer ' + str + '>'                                                                                        // 454
}                                                                                                                      // 455
                                                                                                                       // 456
Buffer.prototype.compare = function compare (b) {                                                                      // 457
  if (!Buffer.isBuffer(b)) throw new TypeError('Argument must be a Buffer')                                            // 458
  if (this === b) return 0                                                                                             // 459
  return Buffer.compare(this, b)                                                                                       // 460
}                                                                                                                      // 461
                                                                                                                       // 462
Buffer.prototype.indexOf = function indexOf (val, byteOffset) {                                                        // 463
  if (byteOffset > 0x7fffffff) byteOffset = 0x7fffffff                                                                 // 464
  else if (byteOffset < -0x80000000) byteOffset = -0x80000000                                                          // 465
  byteOffset >>= 0                                                                                                     // 466
                                                                                                                       // 467
  if (this.length === 0) return -1                                                                                     // 468
  if (byteOffset >= this.length) return -1                                                                             // 469
                                                                                                                       // 470
  // Negative offsets start from the end of the buffer                                                                 // 471
  if (byteOffset < 0) byteOffset = Math.max(this.length + byteOffset, 0)                                               // 472
                                                                                                                       // 473
  if (typeof val === 'string') {                                                                                       // 474
    if (val.length === 0) return -1 // special case: looking for empty string always fails                             // 475
    return String.prototype.indexOf.call(this, val, byteOffset)                                                        // 476
  }                                                                                                                    // 477
  if (Buffer.isBuffer(val)) {                                                                                          // 478
    return arrayIndexOf(this, val, byteOffset)                                                                         // 479
  }                                                                                                                    // 480
  if (typeof val === 'number') {                                                                                       // 481
    if (Buffer.TYPED_ARRAY_SUPPORT && Uint8Array.prototype.indexOf === 'function') {                                   // 482
      return Uint8Array.prototype.indexOf.call(this, val, byteOffset)                                                  // 483
    }                                                                                                                  // 484
    return arrayIndexOf(this, [ val ], byteOffset)                                                                     // 485
  }                                                                                                                    // 486
                                                                                                                       // 487
  function arrayIndexOf (arr, val, byteOffset) {                                                                       // 488
    var foundIndex = -1                                                                                                // 489
    for (var i = 0; byteOffset + i < arr.length; i++) {                                                                // 490
      if (arr[byteOffset + i] === val[foundIndex === -1 ? 0 : i - foundIndex]) {                                       // 491
        if (foundIndex === -1) foundIndex = i                                                                          // 492
        if (i - foundIndex + 1 === val.length) return byteOffset + foundIndex                                          // 493
      } else {                                                                                                         // 494
        foundIndex = -1                                                                                                // 495
      }                                                                                                                // 496
    }                                                                                                                  // 497
    return -1                                                                                                          // 498
  }                                                                                                                    // 499
                                                                                                                       // 500
  throw new TypeError('val must be string, number or Buffer')                                                          // 501
}                                                                                                                      // 502
                                                                                                                       // 503
function hexWrite (buf, string, offset, length) {                                                                      // 504
  offset = Number(offset) || 0                                                                                         // 505
  var remaining = buf.length - offset                                                                                  // 506
  if (!length) {                                                                                                       // 507
    length = remaining                                                                                                 // 508
  } else {                                                                                                             // 509
    length = Number(length)                                                                                            // 510
    if (length > remaining) {                                                                                          // 511
      length = remaining                                                                                               // 512
    }                                                                                                                  // 513
  }                                                                                                                    // 514
                                                                                                                       // 515
  // must be an even number of digits                                                                                  // 516
  var strLen = string.length                                                                                           // 517
  if (strLen % 2 !== 0) throw new Error('Invalid hex string')                                                          // 518
                                                                                                                       // 519
  if (length > strLen / 2) {                                                                                           // 520
    length = strLen / 2                                                                                                // 521
  }                                                                                                                    // 522
  for (var i = 0; i < length; i++) {                                                                                   // 523
    var parsed = parseInt(string.substr(i * 2, 2), 16)                                                                 // 524
    if (isNaN(parsed)) throw new Error('Invalid hex string')                                                           // 525
    buf[offset + i] = parsed                                                                                           // 526
  }                                                                                                                    // 527
  return i                                                                                                             // 528
}                                                                                                                      // 529
                                                                                                                       // 530
function utf8Write (buf, string, offset, length) {                                                                     // 531
  return blitBuffer(utf8ToBytes(string, buf.length - offset), buf, offset, length)                                     // 532
}                                                                                                                      // 533
                                                                                                                       // 534
function asciiWrite (buf, string, offset, length) {                                                                    // 535
  return blitBuffer(asciiToBytes(string), buf, offset, length)                                                         // 536
}                                                                                                                      // 537
                                                                                                                       // 538
function binaryWrite (buf, string, offset, length) {                                                                   // 539
  return asciiWrite(buf, string, offset, length)                                                                       // 540
}                                                                                                                      // 541
                                                                                                                       // 542
function base64Write (buf, string, offset, length) {                                                                   // 543
  return blitBuffer(base64ToBytes(string), buf, offset, length)                                                        // 544
}                                                                                                                      // 545
                                                                                                                       // 546
function ucs2Write (buf, string, offset, length) {                                                                     // 547
  return blitBuffer(utf16leToBytes(string, buf.length - offset), buf, offset, length)                                  // 548
}                                                                                                                      // 549
                                                                                                                       // 550
Buffer.prototype.write = function write (string, offset, length, encoding) {                                           // 551
  // Buffer#write(string)                                                                                              // 552
  if (offset === undefined) {                                                                                          // 553
    encoding = 'utf8'                                                                                                  // 554
    length = this.length                                                                                               // 555
    offset = 0                                                                                                         // 556
  // Buffer#write(string, encoding)                                                                                    // 557
  } else if (length === undefined && typeof offset === 'string') {                                                     // 558
    encoding = offset                                                                                                  // 559
    length = this.length                                                                                               // 560
    offset = 0                                                                                                         // 561
  // Buffer#write(string, offset[, length][, encoding])                                                                // 562
  } else if (isFinite(offset)) {                                                                                       // 563
    offset = offset | 0                                                                                                // 564
    if (isFinite(length)) {                                                                                            // 565
      length = length | 0                                                                                              // 566
      if (encoding === undefined) encoding = 'utf8'                                                                    // 567
    } else {                                                                                                           // 568
      encoding = length                                                                                                // 569
      length = undefined                                                                                               // 570
    }                                                                                                                  // 571
  // legacy write(string, encoding, offset, length) - remove in v0.13                                                  // 572
  } else {                                                                                                             // 573
    var swap = encoding                                                                                                // 574
    encoding = offset                                                                                                  // 575
    offset = length | 0                                                                                                // 576
    length = swap                                                                                                      // 577
  }                                                                                                                    // 578
                                                                                                                       // 579
  var remaining = this.length - offset                                                                                 // 580
  if (length === undefined || length > remaining) length = remaining                                                   // 581
                                                                                                                       // 582
  if ((string.length > 0 && (length < 0 || offset < 0)) || offset > this.length) {                                     // 583
    throw new RangeError('attempt to write outside buffer bounds')                                                     // 584
  }                                                                                                                    // 585
                                                                                                                       // 586
  if (!encoding) encoding = 'utf8'                                                                                     // 587
                                                                                                                       // 588
  var loweredCase = false                                                                                              // 589
  for (;;) {                                                                                                           // 590
    switch (encoding) {                                                                                                // 591
      case 'hex':                                                                                                      // 592
        return hexWrite(this, string, offset, length)                                                                  // 593
                                                                                                                       // 594
      case 'utf8':                                                                                                     // 595
      case 'utf-8':                                                                                                    // 596
        return utf8Write(this, string, offset, length)                                                                 // 597
                                                                                                                       // 598
      case 'ascii':                                                                                                    // 599
        return asciiWrite(this, string, offset, length)                                                                // 600
                                                                                                                       // 601
      case 'binary':                                                                                                   // 602
        return binaryWrite(this, string, offset, length)                                                               // 603
                                                                                                                       // 604
      case 'base64':                                                                                                   // 605
        // Warning: maxLength not taken into account in base64Write                                                    // 606
        return base64Write(this, string, offset, length)                                                               // 607
                                                                                                                       // 608
      case 'ucs2':                                                                                                     // 609
      case 'ucs-2':                                                                                                    // 610
      case 'utf16le':                                                                                                  // 611
      case 'utf-16le':                                                                                                 // 612
        return ucs2Write(this, string, offset, length)                                                                 // 613
                                                                                                                       // 614
      default:                                                                                                         // 615
        if (loweredCase) throw new TypeError('Unknown encoding: ' + encoding)                                          // 616
        encoding = ('' + encoding).toLowerCase()                                                                       // 617
        loweredCase = true                                                                                             // 618
    }                                                                                                                  // 619
  }                                                                                                                    // 620
}                                                                                                                      // 621
                                                                                                                       // 622
Buffer.prototype.toJSON = function toJSON () {                                                                         // 623
  return {                                                                                                             // 624
    type: 'Buffer',                                                                                                    // 625
    data: Array.prototype.slice.call(this._arr || this, 0)                                                             // 626
  }                                                                                                                    // 627
}                                                                                                                      // 628
                                                                                                                       // 629
function base64Slice (buf, start, end) {                                                                               // 630
  if (start === 0 && end === buf.length) {                                                                             // 631
    return base64.fromByteArray(buf)                                                                                   // 632
  } else {                                                                                                             // 633
    return base64.fromByteArray(buf.slice(start, end))                                                                 // 634
  }                                                                                                                    // 635
}                                                                                                                      // 636
                                                                                                                       // 637
function utf8Slice (buf, start, end) {                                                                                 // 638
  end = Math.min(buf.length, end)                                                                                      // 639
  var res = []                                                                                                         // 640
                                                                                                                       // 641
  var i = start                                                                                                        // 642
  while (i < end) {                                                                                                    // 643
    var firstByte = buf[i]                                                                                             // 644
    var codePoint = null                                                                                               // 645
    var bytesPerSequence = (firstByte > 0xEF) ? 4                                                                      // 646
      : (firstByte > 0xDF) ? 3                                                                                         // 647
      : (firstByte > 0xBF) ? 2                                                                                         // 648
      : 1                                                                                                              // 649
                                                                                                                       // 650
    if (i + bytesPerSequence <= end) {                                                                                 // 651
      var secondByte, thirdByte, fourthByte, tempCodePoint                                                             // 652
                                                                                                                       // 653
      switch (bytesPerSequence) {                                                                                      // 654
        case 1:                                                                                                        // 655
          if (firstByte < 0x80) {                                                                                      // 656
            codePoint = firstByte                                                                                      // 657
          }                                                                                                            // 658
          break                                                                                                        // 659
        case 2:                                                                                                        // 660
          secondByte = buf[i + 1]                                                                                      // 661
          if ((secondByte & 0xC0) === 0x80) {                                                                          // 662
            tempCodePoint = (firstByte & 0x1F) << 0x6 | (secondByte & 0x3F)                                            // 663
            if (tempCodePoint > 0x7F) {                                                                                // 664
              codePoint = tempCodePoint                                                                                // 665
            }                                                                                                          // 666
          }                                                                                                            // 667
          break                                                                                                        // 668
        case 3:                                                                                                        // 669
          secondByte = buf[i + 1]                                                                                      // 670
          thirdByte = buf[i + 2]                                                                                       // 671
          if ((secondByte & 0xC0) === 0x80 && (thirdByte & 0xC0) === 0x80) {                                           // 672
            tempCodePoint = (firstByte & 0xF) << 0xC | (secondByte & 0x3F) << 0x6 | (thirdByte & 0x3F)                 // 673
            if (tempCodePoint > 0x7FF && (tempCodePoint < 0xD800 || tempCodePoint > 0xDFFF)) {                         // 674
              codePoint = tempCodePoint                                                                                // 675
            }                                                                                                          // 676
          }                                                                                                            // 677
          break                                                                                                        // 678
        case 4:                                                                                                        // 679
          secondByte = buf[i + 1]                                                                                      // 680
          thirdByte = buf[i + 2]                                                                                       // 681
          fourthByte = buf[i + 3]                                                                                      // 682
          if ((secondByte & 0xC0) === 0x80 && (thirdByte & 0xC0) === 0x80 && (fourthByte & 0xC0) === 0x80) {           // 683
            tempCodePoint = (firstByte & 0xF) << 0x12 | (secondByte & 0x3F) << 0xC | (thirdByte & 0x3F) << 0x6 | (fourthByte & 0x3F)
            if (tempCodePoint > 0xFFFF && tempCodePoint < 0x110000) {                                                  // 685
              codePoint = tempCodePoint                                                                                // 686
            }                                                                                                          // 687
          }                                                                                                            // 688
      }                                                                                                                // 689
    }                                                                                                                  // 690
                                                                                                                       // 691
    if (codePoint === null) {                                                                                          // 692
      // we did not generate a valid codePoint so insert a                                                             // 693
      // replacement char (U+FFFD) and advance only 1 byte                                                             // 694
      codePoint = 0xFFFD                                                                                               // 695
      bytesPerSequence = 1                                                                                             // 696
    } else if (codePoint > 0xFFFF) {                                                                                   // 697
      // encode to utf16 (surrogate pair dance)                                                                        // 698
      codePoint -= 0x10000                                                                                             // 699
      res.push(codePoint >>> 10 & 0x3FF | 0xD800)                                                                      // 700
      codePoint = 0xDC00 | codePoint & 0x3FF                                                                           // 701
    }                                                                                                                  // 702
                                                                                                                       // 703
    res.push(codePoint)                                                                                                // 704
    i += bytesPerSequence                                                                                              // 705
  }                                                                                                                    // 706
                                                                                                                       // 707
  return decodeCodePointsArray(res)                                                                                    // 708
}                                                                                                                      // 709
                                                                                                                       // 710
// Based on http://stackoverflow.com/a/22747272/680742, the browser with                                               // 711
// the lowest limit is Chrome, with 0x10000 args.                                                                      // 712
// We go 1 magnitude less, for safety                                                                                  // 713
var MAX_ARGUMENTS_LENGTH = 0x1000                                                                                      // 714
                                                                                                                       // 715
function decodeCodePointsArray (codePoints) {                                                                          // 716
  var len = codePoints.length                                                                                          // 717
  if (len <= MAX_ARGUMENTS_LENGTH) {                                                                                   // 718
    return String.fromCharCode.apply(String, codePoints) // avoid extra slice()                                        // 719
  }                                                                                                                    // 720
                                                                                                                       // 721
  // Decode in chunks to avoid "call stack size exceeded".                                                             // 722
  var res = ''                                                                                                         // 723
  var i = 0                                                                                                            // 724
  while (i < len) {                                                                                                    // 725
    res += String.fromCharCode.apply(                                                                                  // 726
      String,                                                                                                          // 727
      codePoints.slice(i, i += MAX_ARGUMENTS_LENGTH)                                                                   // 728
    )                                                                                                                  // 729
  }                                                                                                                    // 730
  return res                                                                                                           // 731
}                                                                                                                      // 732
                                                                                                                       // 733
function asciiSlice (buf, start, end) {                                                                                // 734
  var ret = ''                                                                                                         // 735
  end = Math.min(buf.length, end)                                                                                      // 736
                                                                                                                       // 737
  for (var i = start; i < end; i++) {                                                                                  // 738
    ret += String.fromCharCode(buf[i] & 0x7F)                                                                          // 739
  }                                                                                                                    // 740
  return ret                                                                                                           // 741
}                                                                                                                      // 742
                                                                                                                       // 743
function binarySlice (buf, start, end) {                                                                               // 744
  var ret = ''                                                                                                         // 745
  end = Math.min(buf.length, end)                                                                                      // 746
                                                                                                                       // 747
  for (var i = start; i < end; i++) {                                                                                  // 748
    ret += String.fromCharCode(buf[i])                                                                                 // 749
  }                                                                                                                    // 750
  return ret                                                                                                           // 751
}                                                                                                                      // 752
                                                                                                                       // 753
function hexSlice (buf, start, end) {                                                                                  // 754
  var len = buf.length                                                                                                 // 755
                                                                                                                       // 756
  if (!start || start < 0) start = 0                                                                                   // 757
  if (!end || end < 0 || end > len) end = len                                                                          // 758
                                                                                                                       // 759
  var out = ''                                                                                                         // 760
  for (var i = start; i < end; i++) {                                                                                  // 761
    out += toHex(buf[i])                                                                                               // 762
  }                                                                                                                    // 763
  return out                                                                                                           // 764
}                                                                                                                      // 765
                                                                                                                       // 766
function utf16leSlice (buf, start, end) {                                                                              // 767
  var bytes = buf.slice(start, end)                                                                                    // 768
  var res = ''                                                                                                         // 769
  for (var i = 0; i < bytes.length; i += 2) {                                                                          // 770
    res += String.fromCharCode(bytes[i] + bytes[i + 1] * 256)                                                          // 771
  }                                                                                                                    // 772
  return res                                                                                                           // 773
}                                                                                                                      // 774
                                                                                                                       // 775
Buffer.prototype.slice = function slice (start, end) {                                                                 // 776
  var len = this.length                                                                                                // 777
  start = ~~start                                                                                                      // 778
  end = end === undefined ? len : ~~end                                                                                // 779
                                                                                                                       // 780
  if (start < 0) {                                                                                                     // 781
    start += len                                                                                                       // 782
    if (start < 0) start = 0                                                                                           // 783
  } else if (start > len) {                                                                                            // 784
    start = len                                                                                                        // 785
  }                                                                                                                    // 786
                                                                                                                       // 787
  if (end < 0) {                                                                                                       // 788
    end += len                                                                                                         // 789
    if (end < 0) end = 0                                                                                               // 790
  } else if (end > len) {                                                                                              // 791
    end = len                                                                                                          // 792
  }                                                                                                                    // 793
                                                                                                                       // 794
  if (end < start) end = start                                                                                         // 795
                                                                                                                       // 796
  var newBuf                                                                                                           // 797
  if (Buffer.TYPED_ARRAY_SUPPORT) {                                                                                    // 798
    newBuf = this.subarray(start, end)                                                                                 // 799
    newBuf.__proto__ = Buffer.prototype                                                                                // 800
  } else {                                                                                                             // 801
    var sliceLen = end - start                                                                                         // 802
    newBuf = new Buffer(sliceLen, undefined)                                                                           // 803
    for (var i = 0; i < sliceLen; i++) {                                                                               // 804
      newBuf[i] = this[i + start]                                                                                      // 805
    }                                                                                                                  // 806
  }                                                                                                                    // 807
                                                                                                                       // 808
  if (newBuf.length) newBuf.parent = this.parent || this                                                               // 809
                                                                                                                       // 810
  return newBuf                                                                                                        // 811
}                                                                                                                      // 812
                                                                                                                       // 813
/*                                                                                                                     // 814
 * Need to make sure that buffer isn't trying to write out of bounds.                                                  // 815
 */                                                                                                                    // 816
function checkOffset (offset, ext, length) {                                                                           // 817
  if ((offset % 1) !== 0 || offset < 0) throw new RangeError('offset is not uint')                                     // 818
  if (offset + ext > length) throw new RangeError('Trying to access beyond buffer length')                             // 819
}                                                                                                                      // 820
                                                                                                                       // 821
Buffer.prototype.readUIntLE = function readUIntLE (offset, byteLength, noAssert) {                                     // 822
  offset = offset | 0                                                                                                  // 823
  byteLength = byteLength | 0                                                                                          // 824
  if (!noAssert) checkOffset(offset, byteLength, this.length)                                                          // 825
                                                                                                                       // 826
  var val = this[offset]                                                                                               // 827
  var mul = 1                                                                                                          // 828
  var i = 0                                                                                                            // 829
  while (++i < byteLength && (mul *= 0x100)) {                                                                         // 830
    val += this[offset + i] * mul                                                                                      // 831
  }                                                                                                                    // 832
                                                                                                                       // 833
  return val                                                                                                           // 834
}                                                                                                                      // 835
                                                                                                                       // 836
Buffer.prototype.readUIntBE = function readUIntBE (offset, byteLength, noAssert) {                                     // 837
  offset = offset | 0                                                                                                  // 838
  byteLength = byteLength | 0                                                                                          // 839
  if (!noAssert) {                                                                                                     // 840
    checkOffset(offset, byteLength, this.length)                                                                       // 841
  }                                                                                                                    // 842
                                                                                                                       // 843
  var val = this[offset + --byteLength]                                                                                // 844
  var mul = 1                                                                                                          // 845
  while (byteLength > 0 && (mul *= 0x100)) {                                                                           // 846
    val += this[offset + --byteLength] * mul                                                                           // 847
  }                                                                                                                    // 848
                                                                                                                       // 849
  return val                                                                                                           // 850
}                                                                                                                      // 851
                                                                                                                       // 852
Buffer.prototype.readUInt8 = function readUInt8 (offset, noAssert) {                                                   // 853
  if (!noAssert) checkOffset(offset, 1, this.length)                                                                   // 854
  return this[offset]                                                                                                  // 855
}                                                                                                                      // 856
                                                                                                                       // 857
Buffer.prototype.readUInt16LE = function readUInt16LE (offset, noAssert) {                                             // 858
  if (!noAssert) checkOffset(offset, 2, this.length)                                                                   // 859
  return this[offset] | (this[offset + 1] << 8)                                                                        // 860
}                                                                                                                      // 861
                                                                                                                       // 862
Buffer.prototype.readUInt16BE = function readUInt16BE (offset, noAssert) {                                             // 863
  if (!noAssert) checkOffset(offset, 2, this.length)                                                                   // 864
  return (this[offset] << 8) | this[offset + 1]                                                                        // 865
}                                                                                                                      // 866
                                                                                                                       // 867
Buffer.prototype.readUInt32LE = function readUInt32LE (offset, noAssert) {                                             // 868
  if (!noAssert) checkOffset(offset, 4, this.length)                                                                   // 869
                                                                                                                       // 870
  return ((this[offset]) |                                                                                             // 871
      (this[offset + 1] << 8) |                                                                                        // 872
      (this[offset + 2] << 16)) +                                                                                      // 873
      (this[offset + 3] * 0x1000000)                                                                                   // 874
}                                                                                                                      // 875
                                                                                                                       // 876
Buffer.prototype.readUInt32BE = function readUInt32BE (offset, noAssert) {                                             // 877
  if (!noAssert) checkOffset(offset, 4, this.length)                                                                   // 878
                                                                                                                       // 879
  return (this[offset] * 0x1000000) +                                                                                  // 880
    ((this[offset + 1] << 16) |                                                                                        // 881
    (this[offset + 2] << 8) |                                                                                          // 882
    this[offset + 3])                                                                                                  // 883
}                                                                                                                      // 884
                                                                                                                       // 885
Buffer.prototype.readIntLE = function readIntLE (offset, byteLength, noAssert) {                                       // 886
  offset = offset | 0                                                                                                  // 887
  byteLength = byteLength | 0                                                                                          // 888
  if (!noAssert) checkOffset(offset, byteLength, this.length)                                                          // 889
                                                                                                                       // 890
  var val = this[offset]                                                                                               // 891
  var mul = 1                                                                                                          // 892
  var i = 0                                                                                                            // 893
  while (++i < byteLength && (mul *= 0x100)) {                                                                         // 894
    val += this[offset + i] * mul                                                                                      // 895
  }                                                                                                                    // 896
  mul *= 0x80                                                                                                          // 897
                                                                                                                       // 898
  if (val >= mul) val -= Math.pow(2, 8 * byteLength)                                                                   // 899
                                                                                                                       // 900
  return val                                                                                                           // 901
}                                                                                                                      // 902
                                                                                                                       // 903
Buffer.prototype.readIntBE = function readIntBE (offset, byteLength, noAssert) {                                       // 904
  offset = offset | 0                                                                                                  // 905
  byteLength = byteLength | 0                                                                                          // 906
  if (!noAssert) checkOffset(offset, byteLength, this.length)                                                          // 907
                                                                                                                       // 908
  var i = byteLength                                                                                                   // 909
  var mul = 1                                                                                                          // 910
  var val = this[offset + --i]                                                                                         // 911
  while (i > 0 && (mul *= 0x100)) {                                                                                    // 912
    val += this[offset + --i] * mul                                                                                    // 913
  }                                                                                                                    // 914
  mul *= 0x80                                                                                                          // 915
                                                                                                                       // 916
  if (val >= mul) val -= Math.pow(2, 8 * byteLength)                                                                   // 917
                                                                                                                       // 918
  return val                                                                                                           // 919
}                                                                                                                      // 920
                                                                                                                       // 921
Buffer.prototype.readInt8 = function readInt8 (offset, noAssert) {                                                     // 922
  if (!noAssert) checkOffset(offset, 1, this.length)                                                                   // 923
  if (!(this[offset] & 0x80)) return (this[offset])                                                                    // 924
  return ((0xff - this[offset] + 1) * -1)                                                                              // 925
}                                                                                                                      // 926
                                                                                                                       // 927
Buffer.prototype.readInt16LE = function readInt16LE (offset, noAssert) {                                               // 928
  if (!noAssert) checkOffset(offset, 2, this.length)                                                                   // 929
  var val = this[offset] | (this[offset + 1] << 8)                                                                     // 930
  return (val & 0x8000) ? val | 0xFFFF0000 : val                                                                       // 931
}                                                                                                                      // 932
                                                                                                                       // 933
Buffer.prototype.readInt16BE = function readInt16BE (offset, noAssert) {                                               // 934
  if (!noAssert) checkOffset(offset, 2, this.length)                                                                   // 935
  var val = this[offset + 1] | (this[offset] << 8)                                                                     // 936
  return (val & 0x8000) ? val | 0xFFFF0000 : val                                                                       // 937
}                                                                                                                      // 938
                                                                                                                       // 939
Buffer.prototype.readInt32LE = function readInt32LE (offset, noAssert) {                                               // 940
  if (!noAssert) checkOffset(offset, 4, this.length)                                                                   // 941
                                                                                                                       // 942
  return (this[offset]) |                                                                                              // 943
    (this[offset + 1] << 8) |                                                                                          // 944
    (this[offset + 2] << 16) |                                                                                         // 945
    (this[offset + 3] << 24)                                                                                           // 946
}                                                                                                                      // 947
                                                                                                                       // 948
Buffer.prototype.readInt32BE = function readInt32BE (offset, noAssert) {                                               // 949
  if (!noAssert) checkOffset(offset, 4, this.length)                                                                   // 950
                                                                                                                       // 951
  return (this[offset] << 24) |                                                                                        // 952
    (this[offset + 1] << 16) |                                                                                         // 953
    (this[offset + 2] << 8) |                                                                                          // 954
    (this[offset + 3])                                                                                                 // 955
}                                                                                                                      // 956
                                                                                                                       // 957
Buffer.prototype.readFloatLE = function readFloatLE (offset, noAssert) {                                               // 958
  if (!noAssert) checkOffset(offset, 4, this.length)                                                                   // 959
  return ieee754.read(this, offset, true, 23, 4)                                                                       // 960
}                                                                                                                      // 961
                                                                                                                       // 962
Buffer.prototype.readFloatBE = function readFloatBE (offset, noAssert) {                                               // 963
  if (!noAssert) checkOffset(offset, 4, this.length)                                                                   // 964
  return ieee754.read(this, offset, false, 23, 4)                                                                      // 965
}                                                                                                                      // 966
                                                                                                                       // 967
Buffer.prototype.readDoubleLE = function readDoubleLE (offset, noAssert) {                                             // 968
  if (!noAssert) checkOffset(offset, 8, this.length)                                                                   // 969
  return ieee754.read(this, offset, true, 52, 8)                                                                       // 970
}                                                                                                                      // 971
                                                                                                                       // 972
Buffer.prototype.readDoubleBE = function readDoubleBE (offset, noAssert) {                                             // 973
  if (!noAssert) checkOffset(offset, 8, this.length)                                                                   // 974
  return ieee754.read(this, offset, false, 52, 8)                                                                      // 975
}                                                                                                                      // 976
                                                                                                                       // 977
function checkInt (buf, value, offset, ext, max, min) {                                                                // 978
  if (!Buffer.isBuffer(buf)) throw new TypeError('buffer must be a Buffer instance')                                   // 979
  if (value > max || value < min) throw new RangeError('value is out of bounds')                                       // 980
  if (offset + ext > buf.length) throw new RangeError('index out of range')                                            // 981
}                                                                                                                      // 982
                                                                                                                       // 983
Buffer.prototype.writeUIntLE = function writeUIntLE (value, offset, byteLength, noAssert) {                            // 984
  value = +value                                                                                                       // 985
  offset = offset | 0                                                                                                  // 986
  byteLength = byteLength | 0                                                                                          // 987
  if (!noAssert) checkInt(this, value, offset, byteLength, Math.pow(2, 8 * byteLength), 0)                             // 988
                                                                                                                       // 989
  var mul = 1                                                                                                          // 990
  var i = 0                                                                                                            // 991
  this[offset] = value & 0xFF                                                                                          // 992
  while (++i < byteLength && (mul *= 0x100)) {                                                                         // 993
    this[offset + i] = (value / mul) & 0xFF                                                                            // 994
  }                                                                                                                    // 995
                                                                                                                       // 996
  return offset + byteLength                                                                                           // 997
}                                                                                                                      // 998
                                                                                                                       // 999
Buffer.prototype.writeUIntBE = function writeUIntBE (value, offset, byteLength, noAssert) {                            // 1000
  value = +value                                                                                                       // 1001
  offset = offset | 0                                                                                                  // 1002
  byteLength = byteLength | 0                                                                                          // 1003
  if (!noAssert) checkInt(this, value, offset, byteLength, Math.pow(2, 8 * byteLength), 0)                             // 1004
                                                                                                                       // 1005
  var i = byteLength - 1                                                                                               // 1006
  var mul = 1                                                                                                          // 1007
  this[offset + i] = value & 0xFF                                                                                      // 1008
  while (--i >= 0 && (mul *= 0x100)) {                                                                                 // 1009
    this[offset + i] = (value / mul) & 0xFF                                                                            // 1010
  }                                                                                                                    // 1011
                                                                                                                       // 1012
  return offset + byteLength                                                                                           // 1013
}                                                                                                                      // 1014
                                                                                                                       // 1015
Buffer.prototype.writeUInt8 = function writeUInt8 (value, offset, noAssert) {                                          // 1016
  value = +value                                                                                                       // 1017
  offset = offset | 0                                                                                                  // 1018
  if (!noAssert) checkInt(this, value, offset, 1, 0xff, 0)                                                             // 1019
  if (!Buffer.TYPED_ARRAY_SUPPORT) value = Math.floor(value)                                                           // 1020
  this[offset] = (value & 0xff)                                                                                        // 1021
  return offset + 1                                                                                                    // 1022
}                                                                                                                      // 1023
                                                                                                                       // 1024
function objectWriteUInt16 (buf, value, offset, littleEndian) {                                                        // 1025
  if (value < 0) value = 0xffff + value + 1                                                                            // 1026
  for (var i = 0, j = Math.min(buf.length - offset, 2); i < j; i++) {                                                  // 1027
    buf[offset + i] = (value & (0xff << (8 * (littleEndian ? i : 1 - i)))) >>>                                         // 1028
      (littleEndian ? i : 1 - i) * 8                                                                                   // 1029
  }                                                                                                                    // 1030
}                                                                                                                      // 1031
                                                                                                                       // 1032
Buffer.prototype.writeUInt16LE = function writeUInt16LE (value, offset, noAssert) {                                    // 1033
  value = +value                                                                                                       // 1034
  offset = offset | 0                                                                                                  // 1035
  if (!noAssert) checkInt(this, value, offset, 2, 0xffff, 0)                                                           // 1036
  if (Buffer.TYPED_ARRAY_SUPPORT) {                                                                                    // 1037
    this[offset] = (value & 0xff)                                                                                      // 1038
    this[offset + 1] = (value >>> 8)                                                                                   // 1039
  } else {                                                                                                             // 1040
    objectWriteUInt16(this, value, offset, true)                                                                       // 1041
  }                                                                                                                    // 1042
  return offset + 2                                                                                                    // 1043
}                                                                                                                      // 1044
                                                                                                                       // 1045
Buffer.prototype.writeUInt16BE = function writeUInt16BE (value, offset, noAssert) {                                    // 1046
  value = +value                                                                                                       // 1047
  offset = offset | 0                                                                                                  // 1048
  if (!noAssert) checkInt(this, value, offset, 2, 0xffff, 0)                                                           // 1049
  if (Buffer.TYPED_ARRAY_SUPPORT) {                                                                                    // 1050
    this[offset] = (value >>> 8)                                                                                       // 1051
    this[offset + 1] = (value & 0xff)                                                                                  // 1052
  } else {                                                                                                             // 1053
    objectWriteUInt16(this, value, offset, false)                                                                      // 1054
  }                                                                                                                    // 1055
  return offset + 2                                                                                                    // 1056
}                                                                                                                      // 1057
                                                                                                                       // 1058
function objectWriteUInt32 (buf, value, offset, littleEndian) {                                                        // 1059
  if (value < 0) value = 0xffffffff + value + 1                                                                        // 1060
  for (var i = 0, j = Math.min(buf.length - offset, 4); i < j; i++) {                                                  // 1061
    buf[offset + i] = (value >>> (littleEndian ? i : 3 - i) * 8) & 0xff                                                // 1062
  }                                                                                                                    // 1063
}                                                                                                                      // 1064
                                                                                                                       // 1065
Buffer.prototype.writeUInt32LE = function writeUInt32LE (value, offset, noAssert) {                                    // 1066
  value = +value                                                                                                       // 1067
  offset = offset | 0                                                                                                  // 1068
  if (!noAssert) checkInt(this, value, offset, 4, 0xffffffff, 0)                                                       // 1069
  if (Buffer.TYPED_ARRAY_SUPPORT) {                                                                                    // 1070
    this[offset + 3] = (value >>> 24)                                                                                  // 1071
    this[offset + 2] = (value >>> 16)                                                                                  // 1072
    this[offset + 1] = (value >>> 8)                                                                                   // 1073
    this[offset] = (value & 0xff)                                                                                      // 1074
  } else {                                                                                                             // 1075
    objectWriteUInt32(this, value, offset, true)                                                                       // 1076
  }                                                                                                                    // 1077
  return offset + 4                                                                                                    // 1078
}                                                                                                                      // 1079
                                                                                                                       // 1080
Buffer.prototype.writeUInt32BE = function writeUInt32BE (value, offset, noAssert) {                                    // 1081
  value = +value                                                                                                       // 1082
  offset = offset | 0                                                                                                  // 1083
  if (!noAssert) checkInt(this, value, offset, 4, 0xffffffff, 0)                                                       // 1084
  if (Buffer.TYPED_ARRAY_SUPPORT) {                                                                                    // 1085
    this[offset] = (value >>> 24)                                                                                      // 1086
    this[offset + 1] = (value >>> 16)                                                                                  // 1087
    this[offset + 2] = (value >>> 8)                                                                                   // 1088
    this[offset + 3] = (value & 0xff)                                                                                  // 1089
  } else {                                                                                                             // 1090
    objectWriteUInt32(this, value, offset, false)                                                                      // 1091
  }                                                                                                                    // 1092
  return offset + 4                                                                                                    // 1093
}                                                                                                                      // 1094
                                                                                                                       // 1095
Buffer.prototype.writeIntLE = function writeIntLE (value, offset, byteLength, noAssert) {                              // 1096
  value = +value                                                                                                       // 1097
  offset = offset | 0                                                                                                  // 1098
  if (!noAssert) {                                                                                                     // 1099
    var limit = Math.pow(2, 8 * byteLength - 1)                                                                        // 1100
                                                                                                                       // 1101
    checkInt(this, value, offset, byteLength, limit - 1, -limit)                                                       // 1102
  }                                                                                                                    // 1103
                                                                                                                       // 1104
  var i = 0                                                                                                            // 1105
  var mul = 1                                                                                                          // 1106
  var sub = value < 0 ? 1 : 0                                                                                          // 1107
  this[offset] = value & 0xFF                                                                                          // 1108
  while (++i < byteLength && (mul *= 0x100)) {                                                                         // 1109
    this[offset + i] = ((value / mul) >> 0) - sub & 0xFF                                                               // 1110
  }                                                                                                                    // 1111
                                                                                                                       // 1112
  return offset + byteLength                                                                                           // 1113
}                                                                                                                      // 1114
                                                                                                                       // 1115
Buffer.prototype.writeIntBE = function writeIntBE (value, offset, byteLength, noAssert) {                              // 1116
  value = +value                                                                                                       // 1117
  offset = offset | 0                                                                                                  // 1118
  if (!noAssert) {                                                                                                     // 1119
    var limit = Math.pow(2, 8 * byteLength - 1)                                                                        // 1120
                                                                                                                       // 1121
    checkInt(this, value, offset, byteLength, limit - 1, -limit)                                                       // 1122
  }                                                                                                                    // 1123
                                                                                                                       // 1124
  var i = byteLength - 1                                                                                               // 1125
  var mul = 1                                                                                                          // 1126
  var sub = value < 0 ? 1 : 0                                                                                          // 1127
  this[offset + i] = value & 0xFF                                                                                      // 1128
  while (--i >= 0 && (mul *= 0x100)) {                                                                                 // 1129
    this[offset + i] = ((value / mul) >> 0) - sub & 0xFF                                                               // 1130
  }                                                                                                                    // 1131
                                                                                                                       // 1132
  return offset + byteLength                                                                                           // 1133
}                                                                                                                      // 1134
                                                                                                                       // 1135
Buffer.prototype.writeInt8 = function writeInt8 (value, offset, noAssert) {                                            // 1136
  value = +value                                                                                                       // 1137
  offset = offset | 0                                                                                                  // 1138
  if (!noAssert) checkInt(this, value, offset, 1, 0x7f, -0x80)                                                         // 1139
  if (!Buffer.TYPED_ARRAY_SUPPORT) value = Math.floor(value)                                                           // 1140
  if (value < 0) value = 0xff + value + 1                                                                              // 1141
  this[offset] = (value & 0xff)                                                                                        // 1142
  return offset + 1                                                                                                    // 1143
}                                                                                                                      // 1144
                                                                                                                       // 1145
Buffer.prototype.writeInt16LE = function writeInt16LE (value, offset, noAssert) {                                      // 1146
  value = +value                                                                                                       // 1147
  offset = offset | 0                                                                                                  // 1148
  if (!noAssert) checkInt(this, value, offset, 2, 0x7fff, -0x8000)                                                     // 1149
  if (Buffer.TYPED_ARRAY_SUPPORT) {                                                                                    // 1150
    this[offset] = (value & 0xff)                                                                                      // 1151
    this[offset + 1] = (value >>> 8)                                                                                   // 1152
  } else {                                                                                                             // 1153
    objectWriteUInt16(this, value, offset, true)                                                                       // 1154
  }                                                                                                                    // 1155
  return offset + 2                                                                                                    // 1156
}                                                                                                                      // 1157
                                                                                                                       // 1158
Buffer.prototype.writeInt16BE = function writeInt16BE (value, offset, noAssert) {                                      // 1159
  value = +value                                                                                                       // 1160
  offset = offset | 0                                                                                                  // 1161
  if (!noAssert) checkInt(this, value, offset, 2, 0x7fff, -0x8000)                                                     // 1162
  if (Buffer.TYPED_ARRAY_SUPPORT) {                                                                                    // 1163
    this[offset] = (value >>> 8)                                                                                       // 1164
    this[offset + 1] = (value & 0xff)                                                                                  // 1165
  } else {                                                                                                             // 1166
    objectWriteUInt16(this, value, offset, false)                                                                      // 1167
  }                                                                                                                    // 1168
  return offset + 2                                                                                                    // 1169
}                                                                                                                      // 1170
                                                                                                                       // 1171
Buffer.prototype.writeInt32LE = function writeInt32LE (value, offset, noAssert) {                                      // 1172
  value = +value                                                                                                       // 1173
  offset = offset | 0                                                                                                  // 1174
  if (!noAssert) checkInt(this, value, offset, 4, 0x7fffffff, -0x80000000)                                             // 1175
  if (Buffer.TYPED_ARRAY_SUPPORT) {                                                                                    // 1176
    this[offset] = (value & 0xff)                                                                                      // 1177
    this[offset + 1] = (value >>> 8)                                                                                   // 1178
    this[offset + 2] = (value >>> 16)                                                                                  // 1179
    this[offset + 3] = (value >>> 24)                                                                                  // 1180
  } else {                                                                                                             // 1181
    objectWriteUInt32(this, value, offset, true)                                                                       // 1182
  }                                                                                                                    // 1183
  return offset + 4                                                                                                    // 1184
}                                                                                                                      // 1185
                                                                                                                       // 1186
Buffer.prototype.writeInt32BE = function writeInt32BE (value, offset, noAssert) {                                      // 1187
  value = +value                                                                                                       // 1188
  offset = offset | 0                                                                                                  // 1189
  if (!noAssert) checkInt(this, value, offset, 4, 0x7fffffff, -0x80000000)                                             // 1190
  if (value < 0) value = 0xffffffff + value + 1                                                                        // 1191
  if (Buffer.TYPED_ARRAY_SUPPORT) {                                                                                    // 1192
    this[offset] = (value >>> 24)                                                                                      // 1193
    this[offset + 1] = (value >>> 16)                                                                                  // 1194
    this[offset + 2] = (value >>> 8)                                                                                   // 1195
    this[offset + 3] = (value & 0xff)                                                                                  // 1196
  } else {                                                                                                             // 1197
    objectWriteUInt32(this, value, offset, false)                                                                      // 1198
  }                                                                                                                    // 1199
  return offset + 4                                                                                                    // 1200
}                                                                                                                      // 1201
                                                                                                                       // 1202
function checkIEEE754 (buf, value, offset, ext, max, min) {                                                            // 1203
  if (offset + ext > buf.length) throw new RangeError('index out of range')                                            // 1204
  if (offset < 0) throw new RangeError('index out of range')                                                           // 1205
}                                                                                                                      // 1206
                                                                                                                       // 1207
function writeFloat (buf, value, offset, littleEndian, noAssert) {                                                     // 1208
  if (!noAssert) {                                                                                                     // 1209
    checkIEEE754(buf, value, offset, 4, 3.4028234663852886e+38, -3.4028234663852886e+38)                               // 1210
  }                                                                                                                    // 1211
  ieee754.write(buf, value, offset, littleEndian, 23, 4)                                                               // 1212
  return offset + 4                                                                                                    // 1213
}                                                                                                                      // 1214
                                                                                                                       // 1215
Buffer.prototype.writeFloatLE = function writeFloatLE (value, offset, noAssert) {                                      // 1216
  return writeFloat(this, value, offset, true, noAssert)                                                               // 1217
}                                                                                                                      // 1218
                                                                                                                       // 1219
Buffer.prototype.writeFloatBE = function writeFloatBE (value, offset, noAssert) {                                      // 1220
  return writeFloat(this, value, offset, false, noAssert)                                                              // 1221
}                                                                                                                      // 1222
                                                                                                                       // 1223
function writeDouble (buf, value, offset, littleEndian, noAssert) {                                                    // 1224
  if (!noAssert) {                                                                                                     // 1225
    checkIEEE754(buf, value, offset, 8, 1.7976931348623157E+308, -1.7976931348623157E+308)                             // 1226
  }                                                                                                                    // 1227
  ieee754.write(buf, value, offset, littleEndian, 52, 8)                                                               // 1228
  return offset + 8                                                                                                    // 1229
}                                                                                                                      // 1230
                                                                                                                       // 1231
Buffer.prototype.writeDoubleLE = function writeDoubleLE (value, offset, noAssert) {                                    // 1232
  return writeDouble(this, value, offset, true, noAssert)                                                              // 1233
}                                                                                                                      // 1234
                                                                                                                       // 1235
Buffer.prototype.writeDoubleBE = function writeDoubleBE (value, offset, noAssert) {                                    // 1236
  return writeDouble(this, value, offset, false, noAssert)                                                             // 1237
}                                                                                                                      // 1238
                                                                                                                       // 1239
// copy(targetBuffer, targetStart=0, sourceStart=0, sourceEnd=buffer.length)                                           // 1240
Buffer.prototype.copy = function copy (target, targetStart, start, end) {                                              // 1241
  if (!start) start = 0                                                                                                // 1242
  if (!end && end !== 0) end = this.length                                                                             // 1243
  if (targetStart >= target.length) targetStart = target.length                                                        // 1244
  if (!targetStart) targetStart = 0                                                                                    // 1245
  if (end > 0 && end < start) end = start                                                                              // 1246
                                                                                                                       // 1247
  // Copy 0 bytes; we're done                                                                                          // 1248
  if (end === start) return 0                                                                                          // 1249
  if (target.length === 0 || this.length === 0) return 0                                                               // 1250
                                                                                                                       // 1251
  // Fatal error conditions                                                                                            // 1252
  if (targetStart < 0) {                                                                                               // 1253
    throw new RangeError('targetStart out of bounds')                                                                  // 1254
  }                                                                                                                    // 1255
  if (start < 0 || start >= this.length) throw new RangeError('sourceStart out of bounds')                             // 1256
  if (end < 0) throw new RangeError('sourceEnd out of bounds')                                                         // 1257
                                                                                                                       // 1258
  // Are we oob?                                                                                                       // 1259
  if (end > this.length) end = this.length                                                                             // 1260
  if (target.length - targetStart < end - start) {                                                                     // 1261
    end = target.length - targetStart + start                                                                          // 1262
  }                                                                                                                    // 1263
                                                                                                                       // 1264
  var len = end - start                                                                                                // 1265
  var i                                                                                                                // 1266
                                                                                                                       // 1267
  if (this === target && start < targetStart && targetStart < end) {                                                   // 1268
    // descending copy from end                                                                                        // 1269
    for (i = len - 1; i >= 0; i--) {                                                                                   // 1270
      target[i + targetStart] = this[i + start]                                                                        // 1271
    }                                                                                                                  // 1272
  } else if (len < 1000 || !Buffer.TYPED_ARRAY_SUPPORT) {                                                              // 1273
    // ascending copy from start                                                                                       // 1274
    for (i = 0; i < len; i++) {                                                                                        // 1275
      target[i + targetStart] = this[i + start]                                                                        // 1276
    }                                                                                                                  // 1277
  } else {                                                                                                             // 1278
    Uint8Array.prototype.set.call(                                                                                     // 1279
      target,                                                                                                          // 1280
      this.subarray(start, start + len),                                                                               // 1281
      targetStart                                                                                                      // 1282
    )                                                                                                                  // 1283
  }                                                                                                                    // 1284
                                                                                                                       // 1285
  return len                                                                                                           // 1286
}                                                                                                                      // 1287
                                                                                                                       // 1288
// fill(value, start=0, end=buffer.length)                                                                             // 1289
Buffer.prototype.fill = function fill (value, start, end) {                                                            // 1290
  if (!value) value = 0                                                                                                // 1291
  if (!start) start = 0                                                                                                // 1292
  if (!end) end = this.length                                                                                          // 1293
                                                                                                                       // 1294
  if (end < start) throw new RangeError('end < start')                                                                 // 1295
                                                                                                                       // 1296
  // Fill 0 bytes; we're done                                                                                          // 1297
  if (end === start) return                                                                                            // 1298
  if (this.length === 0) return                                                                                        // 1299
                                                                                                                       // 1300
  if (start < 0 || start >= this.length) throw new RangeError('start out of bounds')                                   // 1301
  if (end < 0 || end > this.length) throw new RangeError('end out of bounds')                                          // 1302
                                                                                                                       // 1303
  var i                                                                                                                // 1304
  if (typeof value === 'number') {                                                                                     // 1305
    for (i = start; i < end; i++) {                                                                                    // 1306
      this[i] = value                                                                                                  // 1307
    }                                                                                                                  // 1308
  } else {                                                                                                             // 1309
    var bytes = utf8ToBytes(value.toString())                                                                          // 1310
    var len = bytes.length                                                                                             // 1311
    for (i = start; i < end; i++) {                                                                                    // 1312
      this[i] = bytes[i % len]                                                                                         // 1313
    }                                                                                                                  // 1314
  }                                                                                                                    // 1315
                                                                                                                       // 1316
  return this                                                                                                          // 1317
}                                                                                                                      // 1318
                                                                                                                       // 1319
// HELPER FUNCTIONS                                                                                                    // 1320
// ================                                                                                                    // 1321
                                                                                                                       // 1322
var INVALID_BASE64_RE = /[^+\/0-9A-Za-z-_]/g                                                                           // 1323
                                                                                                                       // 1324
function base64clean (str) {                                                                                           // 1325
  // Node strips out invalid characters like \n and \t from the string, base64-js does not                             // 1326
  str = stringtrim(str).replace(INVALID_BASE64_RE, '')                                                                 // 1327
  // Node converts strings with length < 2 to ''                                                                       // 1328
  if (str.length < 2) return ''                                                                                        // 1329
  // Node allows for non-padded base64 strings (missing trailing ===), base64-js does not                              // 1330
  while (str.length % 4 !== 0) {                                                                                       // 1331
    str = str + '='                                                                                                    // 1332
  }                                                                                                                    // 1333
  return str                                                                                                           // 1334
}                                                                                                                      // 1335
                                                                                                                       // 1336
function stringtrim (str) {                                                                                            // 1337
  if (str.trim) return str.trim()                                                                                      // 1338
  return str.replace(/^\s+|\s+$/g, '')                                                                                 // 1339
}                                                                                                                      // 1340
                                                                                                                       // 1341
function toHex (n) {                                                                                                   // 1342
  if (n < 16) return '0' + n.toString(16)                                                                              // 1343
  return n.toString(16)                                                                                                // 1344
}                                                                                                                      // 1345
                                                                                                                       // 1346
function utf8ToBytes (string, units) {                                                                                 // 1347
  units = units || Infinity                                                                                            // 1348
  var codePoint                                                                                                        // 1349
  var length = string.length                                                                                           // 1350
  var leadSurrogate = null                                                                                             // 1351
  var bytes = []                                                                                                       // 1352
                                                                                                                       // 1353
  for (var i = 0; i < length; i++) {                                                                                   // 1354
    codePoint = string.charCodeAt(i)                                                                                   // 1355
                                                                                                                       // 1356
    // is surrogate component                                                                                          // 1357
    if (codePoint > 0xD7FF && codePoint < 0xE000) {                                                                    // 1358
      // last char was a lead                                                                                          // 1359
      if (!leadSurrogate) {                                                                                            // 1360
        // no lead yet                                                                                                 // 1361
        if (codePoint > 0xDBFF) {                                                                                      // 1362
          // unexpected trail                                                                                          // 1363
          if ((units -= 3) > -1) bytes.push(0xEF, 0xBF, 0xBD)                                                          // 1364
          continue                                                                                                     // 1365
        } else if (i + 1 === length) {                                                                                 // 1366
          // unpaired lead                                                                                             // 1367
          if ((units -= 3) > -1) bytes.push(0xEF, 0xBF, 0xBD)                                                          // 1368
          continue                                                                                                     // 1369
        }                                                                                                              // 1370
                                                                                                                       // 1371
        // valid lead                                                                                                  // 1372
        leadSurrogate = codePoint                                                                                      // 1373
                                                                                                                       // 1374
        continue                                                                                                       // 1375
      }                                                                                                                // 1376
                                                                                                                       // 1377
      // 2 leads in a row                                                                                              // 1378
      if (codePoint < 0xDC00) {                                                                                        // 1379
        if ((units -= 3) > -1) bytes.push(0xEF, 0xBF, 0xBD)                                                            // 1380
        leadSurrogate = codePoint                                                                                      // 1381
        continue                                                                                                       // 1382
      }                                                                                                                // 1383
                                                                                                                       // 1384
      // valid surrogate pair                                                                                          // 1385
      codePoint = (leadSurrogate - 0xD800 << 10 | codePoint - 0xDC00) + 0x10000                                        // 1386
    } else if (leadSurrogate) {                                                                                        // 1387
      // valid bmp char, but last char was a lead                                                                      // 1388
      if ((units -= 3) > -1) bytes.push(0xEF, 0xBF, 0xBD)                                                              // 1389
    }                                                                                                                  // 1390
                                                                                                                       // 1391
    leadSurrogate = null                                                                                               // 1392
                                                                                                                       // 1393
    // encode utf8                                                                                                     // 1394
    if (codePoint < 0x80) {                                                                                            // 1395
      if ((units -= 1) < 0) break                                                                                      // 1396
      bytes.push(codePoint)                                                                                            // 1397
    } else if (codePoint < 0x800) {                                                                                    // 1398
      if ((units -= 2) < 0) break                                                                                      // 1399
      bytes.push(                                                                                                      // 1400
        codePoint >> 0x6 | 0xC0,                                                                                       // 1401
        codePoint & 0x3F | 0x80                                                                                        // 1402
      )                                                                                                                // 1403
    } else if (codePoint < 0x10000) {                                                                                  // 1404
      if ((units -= 3) < 0) break                                                                                      // 1405
      bytes.push(                                                                                                      // 1406
        codePoint >> 0xC | 0xE0,                                                                                       // 1407
        codePoint >> 0x6 & 0x3F | 0x80,                                                                                // 1408
        codePoint & 0x3F | 0x80                                                                                        // 1409
      )                                                                                                                // 1410
    } else if (codePoint < 0x110000) {                                                                                 // 1411
      if ((units -= 4) < 0) break                                                                                      // 1412
      bytes.push(                                                                                                      // 1413
        codePoint >> 0x12 | 0xF0,                                                                                      // 1414
        codePoint >> 0xC & 0x3F | 0x80,                                                                                // 1415
        codePoint >> 0x6 & 0x3F | 0x80,                                                                                // 1416
        codePoint & 0x3F | 0x80                                                                                        // 1417
      )                                                                                                                // 1418
    } else {                                                                                                           // 1419
      throw new Error('Invalid code point')                                                                            // 1420
    }                                                                                                                  // 1421
  }                                                                                                                    // 1422
                                                                                                                       // 1423
  return bytes                                                                                                         // 1424
}                                                                                                                      // 1425
                                                                                                                       // 1426
function asciiToBytes (str) {                                                                                          // 1427
  var byteArray = []                                                                                                   // 1428
  for (var i = 0; i < str.length; i++) {                                                                               // 1429
    // Node's code seems to be doing this and not & 0x7F..                                                             // 1430
    byteArray.push(str.charCodeAt(i) & 0xFF)                                                                           // 1431
  }                                                                                                                    // 1432
  return byteArray                                                                                                     // 1433
}                                                                                                                      // 1434
                                                                                                                       // 1435
function utf16leToBytes (str, units) {                                                                                 // 1436
  var c, hi, lo                                                                                                        // 1437
  var byteArray = []                                                                                                   // 1438
  for (var i = 0; i < str.length; i++) {                                                                               // 1439
    if ((units -= 2) < 0) break                                                                                        // 1440
                                                                                                                       // 1441
    c = str.charCodeAt(i)                                                                                              // 1442
    hi = c >> 8                                                                                                        // 1443
    lo = c % 256                                                                                                       // 1444
    byteArray.push(lo)                                                                                                 // 1445
    byteArray.push(hi)                                                                                                 // 1446
  }                                                                                                                    // 1447
                                                                                                                       // 1448
  return byteArray                                                                                                     // 1449
}                                                                                                                      // 1450
                                                                                                                       // 1451
function base64ToBytes (str) {                                                                                         // 1452
  return base64.toByteArray(base64clean(str))                                                                          // 1453
}                                                                                                                      // 1454
                                                                                                                       // 1455
function blitBuffer (src, dst, offset, length) {                                                                       // 1456
  for (var i = 0; i < length; i++) {                                                                                   // 1457
    if ((i + offset >= dst.length) || (i >= src.length)) break                                                         // 1458
    dst[i + offset] = src[i]                                                                                           // 1459
  }                                                                                                                    // 1460
  return i                                                                                                             // 1461
}                                                                                                                      // 1462
                                                                                                                       // 1463
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}]},"base64-js":{"package.json":function(require,exports){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/node_modules/base64-js/package.json                                                  //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
exports.name = "base64-js";                                                                                            // 1
exports.version = "1.0.4";                                                                                             // 2
exports.main = "lib/b64.js";                                                                                           // 3
                                                                                                                       // 4
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"lib":{"b64.js":function(require,exports){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/node_modules/base64-js/lib/b64.js                                                    //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
;(function (exports) {                                                                                                 // 1
  'use strict'                                                                                                         // 2
                                                                                                                       // 3
  var i                                                                                                                // 4
  var code = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'                                        // 5
  var lookup = []                                                                                                      // 6
  for (i = 0; i < code.length; i++) {                                                                                  // 7
    lookup[i] = code[i]                                                                                                // 8
  }                                                                                                                    // 9
  var revLookup = []                                                                                                   // 10
                                                                                                                       // 11
  for (i = 0; i < code.length; ++i) {                                                                                  // 12
    revLookup[code.charCodeAt(i)] = i                                                                                  // 13
  }                                                                                                                    // 14
  revLookup['-'.charCodeAt(0)] = 62                                                                                    // 15
  revLookup['_'.charCodeAt(0)] = 63                                                                                    // 16
                                                                                                                       // 17
  var Arr = (typeof Uint8Array !== 'undefined')                                                                        // 18
    ? Uint8Array                                                                                                       // 19
    : Array                                                                                                            // 20
                                                                                                                       // 21
  function decode (elt) {                                                                                              // 22
    var v = revLookup[elt.charCodeAt(0)]                                                                               // 23
    return v !== undefined ? v : -1                                                                                    // 24
  }                                                                                                                    // 25
                                                                                                                       // 26
  function b64ToByteArray (b64) {                                                                                      // 27
    var i, j, l, tmp, placeHolders, arr                                                                                // 28
                                                                                                                       // 29
    if (b64.length % 4 > 0) {                                                                                          // 30
      throw new Error('Invalid string. Length must be a multiple of 4')                                                // 31
    }                                                                                                                  // 32
                                                                                                                       // 33
    // the number of equal signs (place holders)                                                                       // 34
    // if there are two placeholders, than the two characters before it                                                // 35
    // represent one byte                                                                                              // 36
    // if there is only one, then the three characters before it represent 2 bytes                                     // 37
    // this is just a cheap hack to not do indexOf twice                                                               // 38
    var len = b64.length                                                                                               // 39
    placeHolders = b64.charAt(len - 2) === '=' ? 2 : b64.charAt(len - 1) === '=' ? 1 : 0                               // 40
                                                                                                                       // 41
    // base64 is 4/3 + up to two characters of the original data                                                       // 42
    arr = new Arr(b64.length * 3 / 4 - placeHolders)                                                                   // 43
                                                                                                                       // 44
    // if there are placeholders, only get up to the last complete 4 chars                                             // 45
    l = placeHolders > 0 ? b64.length - 4 : b64.length                                                                 // 46
                                                                                                                       // 47
    var L = 0                                                                                                          // 48
                                                                                                                       // 49
    function push (v) {                                                                                                // 50
      arr[L++] = v                                                                                                     // 51
    }                                                                                                                  // 52
                                                                                                                       // 53
    for (i = 0, j = 0; i < l; i += 4, j += 3) {                                                                        // 54
      tmp = (decode(b64.charAt(i)) << 18) | (decode(b64.charAt(i + 1)) << 12) | (decode(b64.charAt(i + 2)) << 6) | decode(b64.charAt(i + 3))
      push((tmp & 0xFF0000) >> 16)                                                                                     // 56
      push((tmp & 0xFF00) >> 8)                                                                                        // 57
      push(tmp & 0xFF)                                                                                                 // 58
    }                                                                                                                  // 59
                                                                                                                       // 60
    if (placeHolders === 2) {                                                                                          // 61
      tmp = (decode(b64.charAt(i)) << 2) | (decode(b64.charAt(i + 1)) >> 4)                                            // 62
      push(tmp & 0xFF)                                                                                                 // 63
    } else if (placeHolders === 1) {                                                                                   // 64
      tmp = (decode(b64.charAt(i)) << 10) | (decode(b64.charAt(i + 1)) << 4) | (decode(b64.charAt(i + 2)) >> 2)        // 65
      push((tmp >> 8) & 0xFF)                                                                                          // 66
      push(tmp & 0xFF)                                                                                                 // 67
    }                                                                                                                  // 68
                                                                                                                       // 69
    return arr                                                                                                         // 70
  }                                                                                                                    // 71
                                                                                                                       // 72
  function encode (num) {                                                                                              // 73
    return lookup[num]                                                                                                 // 74
  }                                                                                                                    // 75
                                                                                                                       // 76
  function tripletToBase64 (num) {                                                                                     // 77
    return encode(num >> 18 & 0x3F) + encode(num >> 12 & 0x3F) + encode(num >> 6 & 0x3F) + encode(num & 0x3F)          // 78
  }                                                                                                                    // 79
                                                                                                                       // 80
  function encodeChunk (uint8, start, end) {                                                                           // 81
    var temp                                                                                                           // 82
    var output = []                                                                                                    // 83
    for (var i = start; i < end; i += 3) {                                                                             // 84
      temp = (uint8[i] << 16) + (uint8[i + 1] << 8) + (uint8[i + 2])                                                   // 85
      output.push(tripletToBase64(temp))                                                                               // 86
    }                                                                                                                  // 87
    return output.join('')                                                                                             // 88
  }                                                                                                                    // 89
                                                                                                                       // 90
  function uint8ToBase64 (uint8) {                                                                                     // 91
    var i                                                                                                              // 92
    var extraBytes = uint8.length % 3 // if we have 1 byte left, pad 2 bytes                                           // 93
    var output = ''                                                                                                    // 94
    var parts = []                                                                                                     // 95
    var temp, length                                                                                                   // 96
    var maxChunkLength = 16383 // must be multiple of 3                                                                // 97
                                                                                                                       // 98
    // go through the array every three bytes, we'll deal with trailing stuff later                                    // 99
                                                                                                                       // 100
    for (i = 0, length = uint8.length - extraBytes; i < length; i += maxChunkLength) {                                 // 101
      parts.push(encodeChunk(uint8, i, (i + maxChunkLength) > length ? length : (i + maxChunkLength)))                 // 102
    }                                                                                                                  // 103
                                                                                                                       // 104
    // pad the end with zeros, but make sure to not forget the extra bytes                                             // 105
    switch (extraBytes) {                                                                                              // 106
      case 1:                                                                                                          // 107
        temp = uint8[uint8.length - 1]                                                                                 // 108
        output += encode(temp >> 2)                                                                                    // 109
        output += encode((temp << 4) & 0x3F)                                                                           // 110
        output += '=='                                                                                                 // 111
        break                                                                                                          // 112
      case 2:                                                                                                          // 113
        temp = (uint8[uint8.length - 2] << 8) + (uint8[uint8.length - 1])                                              // 114
        output += encode(temp >> 10)                                                                                   // 115
        output += encode((temp >> 4) & 0x3F)                                                                           // 116
        output += encode((temp << 2) & 0x3F)                                                                           // 117
        output += '='                                                                                                  // 118
        break                                                                                                          // 119
      default:                                                                                                         // 120
        break                                                                                                          // 121
    }                                                                                                                  // 122
                                                                                                                       // 123
    parts.push(output)                                                                                                 // 124
                                                                                                                       // 125
    return parts.join('')                                                                                              // 126
  }                                                                                                                    // 127
                                                                                                                       // 128
  exports.toByteArray = b64ToByteArray                                                                                 // 129
  exports.fromByteArray = uint8ToBase64                                                                                // 130
}(typeof exports === 'undefined' ? (this.base64js = {}) : exports))                                                    // 131
                                                                                                                       // 132
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}}},"ieee754":{"package.json":function(require,exports){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/node_modules/ieee754/package.json                                                    //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
exports.name = "ieee754";                                                                                              // 1
exports.version = "1.1.6";                                                                                             // 2
exports.main = "index.js";                                                                                             // 3
                                                                                                                       // 4
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"index.js":function(require,exports){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/node_modules/ieee754/index.js                                                        //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
exports.read = function (buffer, offset, isLE, mLen, nBytes) {                                                         // 1
  var e, m                                                                                                             // 2
  var eLen = nBytes * 8 - mLen - 1                                                                                     // 3
  var eMax = (1 << eLen) - 1                                                                                           // 4
  var eBias = eMax >> 1                                                                                                // 5
  var nBits = -7                                                                                                       // 6
  var i = isLE ? (nBytes - 1) : 0                                                                                      // 7
  var d = isLE ? -1 : 1                                                                                                // 8
  var s = buffer[offset + i]                                                                                           // 9
                                                                                                                       // 10
  i += d                                                                                                               // 11
                                                                                                                       // 12
  e = s & ((1 << (-nBits)) - 1)                                                                                        // 13
  s >>= (-nBits)                                                                                                       // 14
  nBits += eLen                                                                                                        // 15
  for (; nBits > 0; e = e * 256 + buffer[offset + i], i += d, nBits -= 8) {}                                           // 16
                                                                                                                       // 17
  m = e & ((1 << (-nBits)) - 1)                                                                                        // 18
  e >>= (-nBits)                                                                                                       // 19
  nBits += mLen                                                                                                        // 20
  for (; nBits > 0; m = m * 256 + buffer[offset + i], i += d, nBits -= 8) {}                                           // 21
                                                                                                                       // 22
  if (e === 0) {                                                                                                       // 23
    e = 1 - eBias                                                                                                      // 24
  } else if (e === eMax) {                                                                                             // 25
    return m ? NaN : ((s ? -1 : 1) * Infinity)                                                                         // 26
  } else {                                                                                                             // 27
    m = m + Math.pow(2, mLen)                                                                                          // 28
    e = e - eBias                                                                                                      // 29
  }                                                                                                                    // 30
  return (s ? -1 : 1) * m * Math.pow(2, e - mLen)                                                                      // 31
}                                                                                                                      // 32
                                                                                                                       // 33
exports.write = function (buffer, value, offset, isLE, mLen, nBytes) {                                                 // 34
  var e, m, c                                                                                                          // 35
  var eLen = nBytes * 8 - mLen - 1                                                                                     // 36
  var eMax = (1 << eLen) - 1                                                                                           // 37
  var eBias = eMax >> 1                                                                                                // 38
  var rt = (mLen === 23 ? Math.pow(2, -24) - Math.pow(2, -77) : 0)                                                     // 39
  var i = isLE ? 0 : (nBytes - 1)                                                                                      // 40
  var d = isLE ? 1 : -1                                                                                                // 41
  var s = value < 0 || (value === 0 && 1 / value < 0) ? 1 : 0                                                          // 42
                                                                                                                       // 43
  value = Math.abs(value)                                                                                              // 44
                                                                                                                       // 45
  if (isNaN(value) || value === Infinity) {                                                                            // 46
    m = isNaN(value) ? 1 : 0                                                                                           // 47
    e = eMax                                                                                                           // 48
  } else {                                                                                                             // 49
    e = Math.floor(Math.log(value) / Math.LN2)                                                                         // 50
    if (value * (c = Math.pow(2, -e)) < 1) {                                                                           // 51
      e--                                                                                                              // 52
      c *= 2                                                                                                           // 53
    }                                                                                                                  // 54
    if (e + eBias >= 1) {                                                                                              // 55
      value += rt / c                                                                                                  // 56
    } else {                                                                                                           // 57
      value += rt * Math.pow(2, 1 - eBias)                                                                             // 58
    }                                                                                                                  // 59
    if (value * c >= 2) {                                                                                              // 60
      e++                                                                                                              // 61
      c /= 2                                                                                                           // 62
    }                                                                                                                  // 63
                                                                                                                       // 64
    if (e + eBias >= eMax) {                                                                                           // 65
      m = 0                                                                                                            // 66
      e = eMax                                                                                                         // 67
    } else if (e + eBias >= 1) {                                                                                       // 68
      m = (value * c - 1) * Math.pow(2, mLen)                                                                          // 69
      e = e + eBias                                                                                                    // 70
    } else {                                                                                                           // 71
      m = value * Math.pow(2, eBias - 1) * Math.pow(2, mLen)                                                           // 72
      e = 0                                                                                                            // 73
    }                                                                                                                  // 74
  }                                                                                                                    // 75
                                                                                                                       // 76
  for (; mLen >= 8; buffer[offset + i] = m & 0xff, i += d, m /= 256, mLen -= 8) {}                                     // 77
                                                                                                                       // 78
  e = (e << mLen) | m                                                                                                  // 79
  eLen += mLen                                                                                                         // 80
  for (; eLen > 0; buffer[offset + i] = e & 0xff, i += d, e /= 256, eLen -= 8) {}                                      // 81
                                                                                                                       // 82
  buffer[offset + i - d] |= s * 128                                                                                    // 83
}                                                                                                                      // 84
                                                                                                                       // 85
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}},"isarray":{"package.json":function(require,exports){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/node_modules/isarray/package.json                                                    //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
exports.name = "isarray";                                                                                              // 1
exports.version = "1.0.0";                                                                                             // 2
exports.main = "index.js";                                                                                             // 3
                                                                                                                       // 4
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"index.js":function(require,exports,module){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/node_modules/isarray/index.js                                                        //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
var toString = {}.toString;                                                                                            // 1
                                                                                                                       // 2
module.exports = Array.isArray || function (arr) {                                                                     // 3
  return toString.call(arr) == '[object Array]';                                                                       // 4
};                                                                                                                     // 5
                                                                                                                       // 6
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}},"process":{"browser.js":function(require,exports,module){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/node_modules/process/browser.js                                                      //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
// shim for using process in browser                                                                                   // 1
                                                                                                                       // 2
var process = module.exports = {};                                                                                     // 3
var queue = [];                                                                                                        // 4
var draining = false;                                                                                                  // 5
var currentQueue;                                                                                                      // 6
var queueIndex = -1;                                                                                                   // 7
                                                                                                                       // 8
function cleanUpNextTick() {                                                                                           // 9
    draining = false;                                                                                                  // 10
    if (currentQueue.length) {                                                                                         // 11
        queue = currentQueue.concat(queue);                                                                            // 12
    } else {                                                                                                           // 13
        queueIndex = -1;                                                                                               // 14
    }                                                                                                                  // 15
    if (queue.length) {                                                                                                // 16
        drainQueue();                                                                                                  // 17
    }                                                                                                                  // 18
}                                                                                                                      // 19
                                                                                                                       // 20
function drainQueue() {                                                                                                // 21
    if (draining) {                                                                                                    // 22
        return;                                                                                                        // 23
    }                                                                                                                  // 24
    var timeout = setTimeout(cleanUpNextTick);                                                                         // 25
    draining = true;                                                                                                   // 26
                                                                                                                       // 27
    var len = queue.length;                                                                                            // 28
    while(len) {                                                                                                       // 29
        currentQueue = queue;                                                                                          // 30
        queue = [];                                                                                                    // 31
        while (++queueIndex < len) {                                                                                   // 32
            if (currentQueue) {                                                                                        // 33
                currentQueue[queueIndex].run();                                                                        // 34
            }                                                                                                          // 35
        }                                                                                                              // 36
        queueIndex = -1;                                                                                               // 37
        len = queue.length;                                                                                            // 38
    }                                                                                                                  // 39
    currentQueue = null;                                                                                               // 40
    draining = false;                                                                                                  // 41
    clearTimeout(timeout);                                                                                             // 42
}                                                                                                                      // 43
                                                                                                                       // 44
process.nextTick = function (fun) {                                                                                    // 45
    var args = new Array(arguments.length - 1);                                                                        // 46
    if (arguments.length > 1) {                                                                                        // 47
        for (var i = 1; i < arguments.length; i++) {                                                                   // 48
            args[i - 1] = arguments[i];                                                                                // 49
        }                                                                                                              // 50
    }                                                                                                                  // 51
    queue.push(new Item(fun, args));                                                                                   // 52
    if (queue.length === 1 && !draining) {                                                                             // 53
        setTimeout(drainQueue, 0);                                                                                     // 54
    }                                                                                                                  // 55
};                                                                                                                     // 56
                                                                                                                       // 57
// v8 likes predictible objects                                                                                        // 58
function Item(fun, array) {                                                                                            // 59
    this.fun = fun;                                                                                                    // 60
    this.array = array;                                                                                                // 61
}                                                                                                                      // 62
Item.prototype.run = function () {                                                                                     // 63
    this.fun.apply(null, this.array);                                                                                  // 64
};                                                                                                                     // 65
process.title = 'browser';                                                                                             // 66
process.browser = true;                                                                                                // 67
process.env = {};                                                                                                      // 68
process.argv = [];                                                                                                     // 69
process.version = ''; // empty string to avoid regexp issues                                                           // 70
process.versions = {};                                                                                                 // 71
                                                                                                                       // 72
function noop() {}                                                                                                     // 73
                                                                                                                       // 74
process.on = noop;                                                                                                     // 75
process.addListener = noop;                                                                                            // 76
process.once = noop;                                                                                                   // 77
process.off = noop;                                                                                                    // 78
process.removeListener = noop;                                                                                         // 79
process.removeAllListeners = noop;                                                                                     // 80
process.emit = noop;                                                                                                   // 81
                                                                                                                       // 82
process.binding = function (name) {                                                                                    // 83
    throw new Error('process.binding is not supported');                                                               // 84
};                                                                                                                     // 85
                                                                                                                       // 86
process.cwd = function () { return '/' };                                                                              // 87
process.chdir = function (dir) {                                                                                       // 88
    throw new Error('process.chdir is not supported');                                                                 // 89
};                                                                                                                     // 90
process.umask = function() { return 0; };                                                                              // 91
                                                                                                                       // 92
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}},"domain-browser":{"package.json":function(require,exports){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/node_modules/domain-browser/package.json                                             //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
exports.name = "domain-browser";                                                                                       // 1
exports.version = "1.1.7";                                                                                             // 2
exports.main = "./index.js";                                                                                           // 3
                                                                                                                       // 4
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"index.js":["events",function(require,exports,module){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/node_modules/domain-browser/index.js                                                 //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
// This file should be ES5 compatible                                                                                  // 1
/* eslint prefer-spread:0, no-var:0, prefer-reflect:0, no-magic-numbers:0 */                                           // 2
'use strict'                                                                                                           // 3
module.exports = (function () {                                                                                        // 4
	// Import Events                                                                                                      // 5
	var events = require('events')                                                                                        // 6
                                                                                                                       // 7
	// Export Domain                                                                                                      // 8
	var domain = {}                                                                                                       // 9
	domain.createDomain = domain.create = function () {                                                                   // 10
		var d = new events.EventEmitter()                                                                                    // 11
                                                                                                                       // 12
		function emitError (e) {                                                                                             // 13
			d.emit('error', e)                                                                                                  // 14
		}                                                                                                                    // 15
                                                                                                                       // 16
		d.add = function (emitter) {                                                                                         // 17
			emitter.on('error', emitError)                                                                                      // 18
		}                                                                                                                    // 19
		d.remove = function (emitter) {                                                                                      // 20
			emitter.removeListener('error', emitError)                                                                          // 21
		}                                                                                                                    // 22
		d.bind = function (fn) {                                                                                             // 23
			return function () {                                                                                                // 24
				var args = Array.prototype.slice.call(arguments)                                                                   // 25
				try {                                                                                                              // 26
					fn.apply(null, args)                                                                                              // 27
				}                                                                                                                  // 28
				catch (err) {                                                                                                      // 29
					emitError(err)                                                                                                    // 30
				}                                                                                                                  // 31
			}                                                                                                                   // 32
		}                                                                                                                    // 33
		d.intercept = function (fn) {                                                                                        // 34
			return function (err) {                                                                                             // 35
				if ( err ) {                                                                                                       // 36
					emitError(err)                                                                                                    // 37
				}                                                                                                                  // 38
				else {                                                                                                             // 39
					var args = Array.prototype.slice.call(arguments, 1)                                                               // 40
					try {                                                                                                             // 41
						fn.apply(null, args)                                                                                             // 42
					}                                                                                                                 // 43
					catch (err) {                                                                                                     // 44
						emitError(err)                                                                                                   // 45
					}                                                                                                                 // 46
				}                                                                                                                  // 47
			}                                                                                                                   // 48
		}                                                                                                                    // 49
		d.run = function (fn) {                                                                                              // 50
			try {                                                                                                               // 51
				fn()                                                                                                               // 52
			}                                                                                                                   // 53
			catch (err) {                                                                                                       // 54
				emitError(err)                                                                                                     // 55
			}                                                                                                                   // 56
			return this                                                                                                         // 57
		}                                                                                                                    // 58
		d.dispose = function () {                                                                                            // 59
			this.removeAllListeners()                                                                                           // 60
			return this                                                                                                         // 61
		}                                                                                                                    // 62
		d.enter = d.exit = function () {                                                                                     // 63
			return this                                                                                                         // 64
		}                                                                                                                    // 65
		return d                                                                                                             // 66
	}                                                                                                                     // 67
	return domain                                                                                                         // 68
}).call(this)                                                                                                          // 69
                                                                                                                       // 70
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}]},"events":{"package.json":function(require,exports){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/node_modules/events/package.json                                                     //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
exports.name = "events";                                                                                               // 1
exports.version = "1.1.0";                                                                                             // 2
exports.main = "./events.js";                                                                                          // 3
                                                                                                                       // 4
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"events.js":function(require,exports,module){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// node_modules/meteor-node-stubs/node_modules/events/events.js                                                        //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
// Copyright Joyent, Inc. and other Node contributors.                                                                 // 1
//                                                                                                                     // 2
// Permission is hereby granted, free of charge, to any person obtaining a                                             // 3
// copy of this software and associated documentation files (the                                                       // 4
// "Software"), to deal in the Software without restriction, including                                                 // 5
// without limitation the rights to use, copy, modify, merge, publish,                                                 // 6
// distribute, sublicense, and/or sell copies of the Software, and to permit                                           // 7
// persons to whom the Software is furnished to do so, subject to the                                                  // 8
// following conditions:                                                                                               // 9
//                                                                                                                     // 10
// The above copyright notice and this permission notice shall be included                                             // 11
// in all copies or substantial portions of the Software.                                                              // 12
//                                                                                                                     // 13
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS                                             // 14
// OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF                                                          // 15
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN                                           // 16
// NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,                                            // 17
// DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR                                               // 18
// OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE                                           // 19
// USE OR OTHER DEALINGS IN THE SOFTWARE.                                                                              // 20
                                                                                                                       // 21
function EventEmitter() {                                                                                              // 22
  this._events = this._events || {};                                                                                   // 23
  this._maxListeners = this._maxListeners || undefined;                                                                // 24
}                                                                                                                      // 25
module.exports = EventEmitter;                                                                                         // 26
                                                                                                                       // 27
// Backwards-compat with node 0.10.x                                                                                   // 28
EventEmitter.EventEmitter = EventEmitter;                                                                              // 29
                                                                                                                       // 30
EventEmitter.prototype._events = undefined;                                                                            // 31
EventEmitter.prototype._maxListeners = undefined;                                                                      // 32
                                                                                                                       // 33
// By default EventEmitters will print a warning if more than 10 listeners are                                         // 34
// added to it. This is a useful default which helps finding memory leaks.                                             // 35
EventEmitter.defaultMaxListeners = 10;                                                                                 // 36
                                                                                                                       // 37
// Obviously not all Emitters should be limited to 10. This function allows                                            // 38
// that to be increased. Set to zero for unlimited.                                                                    // 39
EventEmitter.prototype.setMaxListeners = function(n) {                                                                 // 40
  if (!isNumber(n) || n < 0 || isNaN(n))                                                                               // 41
    throw TypeError('n must be a positive number');                                                                    // 42
  this._maxListeners = n;                                                                                              // 43
  return this;                                                                                                         // 44
};                                                                                                                     // 45
                                                                                                                       // 46
EventEmitter.prototype.emit = function(type) {                                                                         // 47
  var er, handler, len, args, i, listeners;                                                                            // 48
                                                                                                                       // 49
  if (!this._events)                                                                                                   // 50
    this._events = {};                                                                                                 // 51
                                                                                                                       // 52
  // If there is no 'error' event listener then throw.                                                                 // 53
  if (type === 'error') {                                                                                              // 54
    if (!this._events.error ||                                                                                         // 55
        (isObject(this._events.error) && !this._events.error.length)) {                                                // 56
      er = arguments[1];                                                                                               // 57
      if (er instanceof Error) {                                                                                       // 58
        throw er; // Unhandled 'error' event                                                                           // 59
      }                                                                                                                // 60
      throw TypeError('Uncaught, unspecified "error" event.');                                                         // 61
    }                                                                                                                  // 62
  }                                                                                                                    // 63
                                                                                                                       // 64
  handler = this._events[type];                                                                                        // 65
                                                                                                                       // 66
  if (isUndefined(handler))                                                                                            // 67
    return false;                                                                                                      // 68
                                                                                                                       // 69
  if (isFunction(handler)) {                                                                                           // 70
    switch (arguments.length) {                                                                                        // 71
      // fast cases                                                                                                    // 72
      case 1:                                                                                                          // 73
        handler.call(this);                                                                                            // 74
        break;                                                                                                         // 75
      case 2:                                                                                                          // 76
        handler.call(this, arguments[1]);                                                                              // 77
        break;                                                                                                         // 78
      case 3:                                                                                                          // 79
        handler.call(this, arguments[1], arguments[2]);                                                                // 80
        break;                                                                                                         // 81
      // slower                                                                                                        // 82
      default:                                                                                                         // 83
        args = Array.prototype.slice.call(arguments, 1);                                                               // 84
        handler.apply(this, args);                                                                                     // 85
    }                                                                                                                  // 86
  } else if (isObject(handler)) {                                                                                      // 87
    args = Array.prototype.slice.call(arguments, 1);                                                                   // 88
    listeners = handler.slice();                                                                                       // 89
    len = listeners.length;                                                                                            // 90
    for (i = 0; i < len; i++)                                                                                          // 91
      listeners[i].apply(this, args);                                                                                  // 92
  }                                                                                                                    // 93
                                                                                                                       // 94
  return true;                                                                                                         // 95
};                                                                                                                     // 96
                                                                                                                       // 97
EventEmitter.prototype.addListener = function(type, listener) {                                                        // 98
  var m;                                                                                                               // 99
                                                                                                                       // 100
  if (!isFunction(listener))                                                                                           // 101
    throw TypeError('listener must be a function');                                                                    // 102
                                                                                                                       // 103
  if (!this._events)                                                                                                   // 104
    this._events = {};                                                                                                 // 105
                                                                                                                       // 106
  // To avoid recursion in the case that type === "newListener"! Before                                                // 107
  // adding it to the listeners, first emit "newListener".                                                             // 108
  if (this._events.newListener)                                                                                        // 109
    this.emit('newListener', type,                                                                                     // 110
              isFunction(listener.listener) ?                                                                          // 111
              listener.listener : listener);                                                                           // 112
                                                                                                                       // 113
  if (!this._events[type])                                                                                             // 114
    // Optimize the case of one listener. Don't need the extra array object.                                           // 115
    this._events[type] = listener;                                                                                     // 116
  else if (isObject(this._events[type]))                                                                               // 117
    // If we've already got an array, just append.                                                                     // 118
    this._events[type].push(listener);                                                                                 // 119
  else                                                                                                                 // 120
    // Adding the second element, need to change to array.                                                             // 121
    this._events[type] = [this._events[type], listener];                                                               // 122
                                                                                                                       // 123
  // Check for listener leak                                                                                           // 124
  if (isObject(this._events[type]) && !this._events[type].warned) {                                                    // 125
    if (!isUndefined(this._maxListeners)) {                                                                            // 126
      m = this._maxListeners;                                                                                          // 127
    } else {                                                                                                           // 128
      m = EventEmitter.defaultMaxListeners;                                                                            // 129
    }                                                                                                                  // 130
                                                                                                                       // 131
    if (m && m > 0 && this._events[type].length > m) {                                                                 // 132
      this._events[type].warned = true;                                                                                // 133
      console.error('(node) warning: possible EventEmitter memory ' +                                                  // 134
                    'leak detected. %d listeners added. ' +                                                            // 135
                    'Use emitter.setMaxListeners() to increase limit.',                                                // 136
                    this._events[type].length);                                                                        // 137
      if (typeof console.trace === 'function') {                                                                       // 138
        // not supported in IE 10                                                                                      // 139
        console.trace();                                                                                               // 140
      }                                                                                                                // 141
    }                                                                                                                  // 142
  }                                                                                                                    // 143
                                                                                                                       // 144
  return this;                                                                                                         // 145
};                                                                                                                     // 146
                                                                                                                       // 147
EventEmitter.prototype.on = EventEmitter.prototype.addListener;                                                        // 148
                                                                                                                       // 149
EventEmitter.prototype.once = function(type, listener) {                                                               // 150
  if (!isFunction(listener))                                                                                           // 151
    throw TypeError('listener must be a function');                                                                    // 152
                                                                                                                       // 153
  var fired = false;                                                                                                   // 154
                                                                                                                       // 155
  function g() {                                                                                                       // 156
    this.removeListener(type, g);                                                                                      // 157
                                                                                                                       // 158
    if (!fired) {                                                                                                      // 159
      fired = true;                                                                                                    // 160
      listener.apply(this, arguments);                                                                                 // 161
    }                                                                                                                  // 162
  }                                                                                                                    // 163
                                                                                                                       // 164
  g.listener = listener;                                                                                               // 165
  this.on(type, g);                                                                                                    // 166
                                                                                                                       // 167
  return this;                                                                                                         // 168
};                                                                                                                     // 169
                                                                                                                       // 170
// emits a 'removeListener' event iff the listener was removed                                                         // 171
EventEmitter.prototype.removeListener = function(type, listener) {                                                     // 172
  var list, position, length, i;                                                                                       // 173
                                                                                                                       // 174
  if (!isFunction(listener))                                                                                           // 175
    throw TypeError('listener must be a function');                                                                    // 176
                                                                                                                       // 177
  if (!this._events || !this._events[type])                                                                            // 178
    return this;                                                                                                       // 179
                                                                                                                       // 180
  list = this._events[type];                                                                                           // 181
  length = list.length;                                                                                                // 182
  position = -1;                                                                                                       // 183
                                                                                                                       // 184
  if (list === listener ||                                                                                             // 185
      (isFunction(list.listener) && list.listener === listener)) {                                                     // 186
    delete this._events[type];                                                                                         // 187
    if (this._events.removeListener)                                                                                   // 188
      this.emit('removeListener', type, listener);                                                                     // 189
                                                                                                                       // 190
  } else if (isObject(list)) {                                                                                         // 191
    for (i = length; i-- > 0;) {                                                                                       // 192
      if (list[i] === listener ||                                                                                      // 193
          (list[i].listener && list[i].listener === listener)) {                                                       // 194
        position = i;                                                                                                  // 195
        break;                                                                                                         // 196
      }                                                                                                                // 197
    }                                                                                                                  // 198
                                                                                                                       // 199
    if (position < 0)                                                                                                  // 200
      return this;                                                                                                     // 201
                                                                                                                       // 202
    if (list.length === 1) {                                                                                           // 203
      list.length = 0;                                                                                                 // 204
      delete this._events[type];                                                                                       // 205
    } else {                                                                                                           // 206
      list.splice(position, 1);                                                                                        // 207
    }                                                                                                                  // 208
                                                                                                                       // 209
    if (this._events.removeListener)                                                                                   // 210
      this.emit('removeListener', type, listener);                                                                     // 211
  }                                                                                                                    // 212
                                                                                                                       // 213
  return this;                                                                                                         // 214
};                                                                                                                     // 215
                                                                                                                       // 216
EventEmitter.prototype.removeAllListeners = function(type) {                                                           // 217
  var key, listeners;                                                                                                  // 218
                                                                                                                       // 219
  if (!this._events)                                                                                                   // 220
    return this;                                                                                                       // 221
                                                                                                                       // 222
  // not listening for removeListener, no need to emit                                                                 // 223
  if (!this._events.removeListener) {                                                                                  // 224
    if (arguments.length === 0)                                                                                        // 225
      this._events = {};                                                                                               // 226
    else if (this._events[type])                                                                                       // 227
      delete this._events[type];                                                                                       // 228
    return this;                                                                                                       // 229
  }                                                                                                                    // 230
                                                                                                                       // 231
  // emit removeListener for all listeners on all events                                                               // 232
  if (arguments.length === 0) {                                                                                        // 233
    for (key in this._events) {                                                                                        // 234
      if (key === 'removeListener') continue;                                                                          // 235
      this.removeAllListeners(key);                                                                                    // 236
    }                                                                                                                  // 237
    this.removeAllListeners('removeListener');                                                                         // 238
    this._events = {};                                                                                                 // 239
    return this;                                                                                                       // 240
  }                                                                                                                    // 241
                                                                                                                       // 242
  listeners = this._events[type];                                                                                      // 243
                                                                                                                       // 244
  if (isFunction(listeners)) {                                                                                         // 245
    this.removeListener(type, listeners);                                                                              // 246
  } else if (listeners) {                                                                                              // 247
    // LIFO order                                                                                                      // 248
    while (listeners.length)                                                                                           // 249
      this.removeListener(type, listeners[listeners.length - 1]);                                                      // 250
  }                                                                                                                    // 251
  delete this._events[type];                                                                                           // 252
                                                                                                                       // 253
  return this;                                                                                                         // 254
};                                                                                                                     // 255
                                                                                                                       // 256
EventEmitter.prototype.listeners = function(type) {                                                                    // 257
  var ret;                                                                                                             // 258
  if (!this._events || !this._events[type])                                                                            // 259
    ret = [];                                                                                                          // 260
  else if (isFunction(this._events[type]))                                                                             // 261
    ret = [this._events[type]];                                                                                        // 262
  else                                                                                                                 // 263
    ret = this._events[type].slice();                                                                                  // 264
  return ret;                                                                                                          // 265
};                                                                                                                     // 266
                                                                                                                       // 267
EventEmitter.prototype.listenerCount = function(type) {                                                                // 268
  if (this._events) {                                                                                                  // 269
    var evlistener = this._events[type];                                                                               // 270
                                                                                                                       // 271
    if (isFunction(evlistener))                                                                                        // 272
      return 1;                                                                                                        // 273
    else if (evlistener)                                                                                               // 274
      return evlistener.length;                                                                                        // 275
  }                                                                                                                    // 276
  return 0;                                                                                                            // 277
};                                                                                                                     // 278
                                                                                                                       // 279
EventEmitter.listenerCount = function(emitter, type) {                                                                 // 280
  return emitter.listenerCount(type);                                                                                  // 281
};                                                                                                                     // 282
                                                                                                                       // 283
function isFunction(arg) {                                                                                             // 284
  return typeof arg === 'function';                                                                                    // 285
}                                                                                                                      // 286
                                                                                                                       // 287
function isNumber(arg) {                                                                                               // 288
  return typeof arg === 'number';                                                                                      // 289
}                                                                                                                      // 290
                                                                                                                       // 291
function isObject(arg) {                                                                                               // 292
  return typeof arg === 'object' && arg !== null;                                                                      // 293
}                                                                                                                      // 294
                                                                                                                       // 295
function isUndefined(arg) {                                                                                            // 296
  return arg === void 0;                                                                                               // 297
}                                                                                                                      // 298
                                                                                                                       // 299
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}}}}}},{"extensions":[".js",".json"]});
var exports = require("./node_modules/meteor/modules/client.js");

/* Exports */
if (typeof Package === 'undefined') Package = {};
(function (pkg, symbols) {
  for (var s in symbols)
    (s in pkg) || (pkg[s] = symbols[s]);
})(Package.modules = exports, {
  meteorInstall: meteorInstall,
  Buffer: Buffer,
  process: process
});

})();
