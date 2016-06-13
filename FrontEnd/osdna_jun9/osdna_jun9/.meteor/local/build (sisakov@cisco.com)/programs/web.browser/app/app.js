var require = meteorInstall({"client":{"templates":{"template.d3plusgraph.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/templates/template.d3plusgraph.js                                                                            //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
                                                                                                                       // 1
Template.__checkName("d3plusgraph");                                                                                   // 2
Template["d3plusgraph"] = new Template("Template.d3plusgraph", (function() {                                           // 3
  var view = this;                                                                                                     // 4
  return HTML.Raw('<div id="viz">Hello</div>');                                                                        // 5
}));                                                                                                                   // 6
                                                                                                                       // 7
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"template.envdialog.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/templates/template.envdialog.js                                                                              //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
                                                                                                                       // 1
Template.__checkName("envdialog");                                                                                     // 2
Template["envdialog"] = new Template("Template.envdialog", (function() {                                               // 3
  var view = this;                                                                                                     // 4
  return [ HTML.Raw('<!-- <button id="show-dialog" type="button" class="mdl-button">Show Dialog</button> -->\n    <!-- Colored FAB button with ripple -->\n    <button id="show-dialog" class="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect mdl-button--colored">\n        <i class="material-icons">add</i>\n    </button>\n    <div class="mdl-tooltip" for="show-dialog">\n        Add new enviroment\n    </div>\n\n    '), HTML.getTag("dialog")({
    "class": "mdl-dialog"                                                                                              // 6
  }, "\n        ", HTML.H5({                                                                                           // 7
    "class": "mdl-dialog__title"                                                                                       // 8
  }, "Add new enviroment"), "\n\n        ", HTML.DIV({                                                                 // 9
    "class": "mdl-dialog__content"                                                                                     // 10
  }, "\n\n            ", HTML.DIV({                                                                                    // 11
    "class": "mdl-tabs mdl-js-tabs mdl-js-ripple-effect"                                                               // 12
  }, "\n                ", HTML.DIV({                                                                                  // 13
    "class": "mdl-tabs__tab-bar"                                                                                       // 14
  }, "\n                    ", HTML.A({                                                                                // 15
    href: "#main-info-panel",                                                                                          // 16
    "class": "mdl-tabs__tab is-active"                                                                                 // 17
  }, "Main Info"), "\n                    ", HTML.A({                                                                  // 18
    href: "#endpoin-panel",                                                                                            // 19
    "class": "mdl-tabs__tab"                                                                                           // 20
  }, "OS API endpoin"), "\n                    ", HTML.A({                                                             // 21
    href: "#db-credentials-panel",                                                                                     // 22
    "class": "mdl-tabs__tab"                                                                                           // 23
  }, "OpenStack DB Credentials"), "\n                    ", HTML.A({                                                   // 24
    href: "#master-host-panel",                                                                                        // 25
    "class": "mdl-tabs__tab"                                                                                           // 26
  }, "Master Host Credentials"), "\n                    ", HTML.A({                                                    // 27
    href: "#nfv-panel",                                                                                                // 28
    "class": "mdl-tabs__tab"                                                                                           // 29
  }, "NFV Credentials"), "\n                "), "\n\n                ", HTML.DIV({                                     // 30
    "class": "mdl-tabs__panel is-active",                                                                              // 31
    id: "main-info-panel"                                                                                              // 32
  }, "\n                    ", HTML.Comment(" Textfield with Floating Label "), "\n                    ", HTML.FORM({  // 33
    action: "#"                                                                                                        // 34
  }, "\n                        ", HTML.DIV({                                                                          // 35
    "class": "mdl-grid"                                                                                                // 36
  }, "\n                            ", HTML.DIV({                                                                      // 37
    "class": "mdl-cell mdl-cell--4-col"                                                                                // 38
  }, "\n                                ", HTML.DIV({                                                                  // 39
    "class": "mdl-textfield mdl-js-textfield mdl-textfield--floating-label"                                            // 40
  }, "\n                                    ", HTML.INPUT({                                                            // 41
    "class": "mdl-textfield__input",                                                                                   // 42
    type: "text",                                                                                                      // 43
    id: "ownerName",                                                                                                   // 44
    value: "Koren Lev"                                                                                                 // 45
  }), "\n                                    ", HTML.LABEL({                                                           // 46
    "class": "mdl-textfield__label",                                                                                   // 47
    "for": "ownerName"                                                                                                 // 48
  }, "Owner"), "\n                                "), "\n                            "), "\n                            ", HTML.DIV({
    "class": "mdl-cell mdl-cell--8-col"                                                                                // 50
  }, "\n                                ", HTML.H6("Admin name, owner of project"), "\n                            "), "\n                            ", HTML.DIV({
    "class": "mdl-cell mdl-cell--4-col"                                                                                // 52
  }, "\n                                ", HTML.DIV({                                                                  // 53
    "class": "mdl-textfield mdl-js-textfield mdl-textfield--floating-label"                                            // 54
  }, "\n                                    ", HTML.INPUT({                                                            // 55
    "class": "mdl-textfield__input",                                                                                   // 56
    type: "text",                                                                                                      // 57
    id: "initialEnvName"                                                                                               // 58
  }), "\n                                    ", HTML.LABEL({                                                           // 59
    "class": "mdl-textfield__label",                                                                                   // 60
    "for": "initialEnvName"                                                                                            // 61
  }, "Enviroment name"), "\n                                "), "\n                            "), "\n                            ", HTML.DIV({
    "class": "mdl-cell mdl-cell--8-col"                                                                                // 63
  }, "\n                                ", HTML.H6("Enter name of your project"), "\n                            "), "\n                        "), "\n                    "), "\n                "), "\n\n                ", HTML.DIV({
    "class": "mdl-tabs__panel",                                                                                        // 65
    id: "endpoin-panel"                                                                                                // 66
  }, "\n                    ", HTML.FORM({                                                                             // 67
    action: "#"                                                                                                        // 68
  }, "\n                        ", HTML.DIV({                                                                          // 69
    "class": "mdl-grid"                                                                                                // 70
  }, "\n                            ", HTML.DIV({                                                                      // 71
    "class": "mdl-cell mdl-cell--4-col"                                                                                // 72
  }, "\n                                ", HTML.DIV({                                                                  // 73
    "class": "mdl-textfield mdl-js-textfield mdl-textfield--floating-label"                                            // 74
  }, "\n                                    ", HTML.INPUT({                                                            // 75
    "class": "mdl-textfield__input",                                                                                   // 76
    type: "text",                                                                                                      // 77
    id: "apiHost",                                                                                                     // 78
    pattern: "-?[0-9]*(\\.[0-9]+)?"                                                                                    // 79
  }), "\n                                    ", HTML.LABEL({                                                           // 80
    "class": "mdl-textfield__label",                                                                                   // 81
    "for": "apiHost"                                                                                                   // 82
  }, "API host"), "\n                                    ", HTML.SPAN({                                                // 83
    "class": "mdl-textfield__error"                                                                                    // 84
  }, "Input is not a number!"), "\n                                "), "\n                            "), "\n                            ", HTML.DIV({
    "class": "mdl-cell mdl-cell--8-col"                                                                                // 86
  }, "\n                                ", HTML.H6("This is API bla bla..."), "\n                            "), "\n                            ", HTML.DIV({
    "class": "mdl-cell mdl-cell--4-col"                                                                                // 88
  }, "\n                                ", HTML.DIV({                                                                  // 89
    "class": "mdl-textfield mdl-js-textfield mdl-textfield--floating-label"                                            // 90
  }, "\n                                    ", HTML.INPUT({                                                            // 91
    "class": "mdl-textfield__input",                                                                                   // 92
    type: "text",                                                                                                      // 93
    id: "adminToken"                                                                                                   // 94
  }), "\n                                    ", HTML.LABEL({                                                           // 95
    "class": "mdl-textfield__label",                                                                                   // 96
    "for": "adminToken"                                                                                                // 97
  }, "Admin token"), "\n                                "), "\n                            "), "\n                            ", HTML.DIV({
    "class": "mdl-cell mdl-cell--8-col"                                                                                // 99
  }, "\n                                ", HTML.H6("You can find token .."), "\n                            "), "\n                            ", HTML.DIV({
    "class": "mdl-cell mdl-cell--4-col"                                                                                // 101
  }, "\n                                ", HTML.DIV({                                                                  // 102
    "class": "mdl-textfield mdl-js-textfield mdl-textfield--floating-label"                                            // 103
  }, "\n                                    ", HTML.INPUT({                                                            // 104
    "class": "mdl-textfield__input",                                                                                   // 105
    type: "text",                                                                                                      // 106
    id: "apiUsername"                                                                                                  // 107
  }), "\n                                    ", HTML.LABEL({                                                           // 108
    "class": "mdl-textfield__label",                                                                                   // 109
    "for": "apiUsername"                                                                                               // 110
  }, "Username"), "\n                                "), "\n                            "), "\n                            ", HTML.DIV({
    "class": "mdl-cell mdl-cell--8-col"                                                                                // 112
  }, "\n                                ", HTML.H6("Some info about user name"), "\n                            "), "\n                            ", HTML.DIV({
    "class": "mdl-cell mdl-cell--4-col"                                                                                // 114
  }, "\n                                ", HTML.DIV({                                                                  // 115
    "class": "mdl-textfield mdl-js-textfield mdl-textfield--floating-label"                                            // 116
  }, "\n                                    ", HTML.INPUT({                                                            // 117
    "class": "mdl-textfield__input",                                                                                   // 118
    type: "password",                                                                                                  // 119
    id: "apiPassword"                                                                                                  // 120
  }), "\n                                    ", HTML.LABEL({                                                           // 121
    "class": "mdl-textfield__label",                                                                                   // 122
    "for": "apiPassword"                                                                                               // 123
  }, "Password"), "\n                                "), "\n                            "), "\n                            ", HTML.DIV({
    "class": "mdl-cell mdl-cell--8-col"                                                                                // 125
  }, "\n                                ", HTML.H6(), "\n                            "), "\n                        "), "\n                    "), "\n                "), "\n\n                ", HTML.DIV({
    "class": "mdl-tabs__panel",                                                                                        // 127
    id: "db-credentials-panel"                                                                                         // 128
  }, "\n                    ", HTML.UL("\n                        ", HTML.LI("Viserys"), "\n                    "), "\n                "), "\n\n                ", HTML.DIV({
    "class": "mdl-tabs__panel",                                                                                        // 130
    id: "master-host-panel"                                                                                            // 131
  }, "\n                    ", HTML.UL("\n                        ", HTML.LI("St"), "\n                    "), "\n                "), "\n\n                ", HTML.DIV({
    "class": "mdl-tabs__panel",                                                                                        // 133
    id: "nfv-panel"                                                                                                    // 134
  }, "\n                    ", HTML.UL("\n                        ", HTML.LI("Kor"), "\n                    "), "\n                    ", HTML.DIV({
    "class": "mdl-dialog__actions"                                                                                     // 136
  }, "\n                        ", HTML.BUTTON({                                                                       // 137
    type: "button",                                                                                                    // 138
    "class": "mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--colored"                    // 139
  }, "Submit"), "\n                        ", HTML.BUTTON({                                                            // 140
    type: "button",                                                                                                    // 141
    "class": "mdl-button close"                                                                                        // 142
  }, "Close"), "\n                    "), "\n                "), "\n            "), "\n        "), "\n\n    "), "\n    ", HTML.SCRIPT({
    src: "https://cdnjs.cloudflare.com/ajax/libs/dialog-polyfill/0.4.3/dialog-polyfill.min.js"                         // 144
  }) ];                                                                                                                // 145
}));                                                                                                                   // 146
                                                                                                                       // 147
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"template.header.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/templates/template.header.js                                                                                 //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
                                                                                                                       // 1
Template.__checkName("header");                                                                                        // 2
Template["header"] = new Template("Template.header", (function() {                                                     // 3
  var view = this;                                                                                                     // 4
  return "";                                                                                                           // 5
}));                                                                                                                   // 6
                                                                                                                       // 7
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"template.home.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/templates/template.home.js                                                                                   //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
                                                                                                                       // 1
Template.__checkName("home");                                                                                          // 2
Template["home"] = new Template("Template.home", (function() {                                                         // 3
  var view = this;                                                                                                     // 4
  return [ HTML.Raw('<link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.0.1/css/font-awesome.min.css">\n    '), Spacebars.include(view.lookupTemplate("topnavbarmenu")), "\n    ", Spacebars.include(view.lookupTemplate("multilevelorig")) ];
}));                                                                                                                   // 6
                                                                                                                       // 7
Template.__checkName("d3graph");                                                                                       // 8
Template["d3graph"] = new Template("Template.d3graph", (function() {                                                   // 9
  var view = this;                                                                                                     // 10
  return HTML.Raw('<div id="dgraphid"></div>');                                                                        // 11
}));                                                                                                                   // 12
                                                                                                                       // 13
Template.__checkName("multilevelorig");                                                                                // 14
Template["multilevelorig"] = new Template("Template.multilevelorig", (function() {                                     // 15
  var view = this;                                                                                                     // 16
  return [ HTML.DIV({                                                                                                  // 17
    id: "pushobj"                                                                                                      // 18
  }, "\n        ", Spacebars.include(view.lookupTemplate("breadcrumbMenu")), "\n        ", Spacebars.include(view.lookupTemplate("d3graph")), "\n    "), "\n    ", HTML.DIV({
    id: "menu"                                                                                                         // 20
  }, "\n        ", HTML.NAV("\n            ", HTML.Raw('<h2><i class="fa fa-reorder"></i>Env</h2>'), "\n            ", HTML.UL("\n                ", Blaze.Each(function() {
    return Spacebars.call(view.lookup("treeItems"));                                                                   // 22
  }, function() {                                                                                                      // 23
    return [ "\n                    ", Spacebars.include(view.lookupTemplate("multilevelorigNodeTemplate")), "\n                " ];
  }), "\n            "), "\n        "), "\n    ") ];                                                                   // 25
}));                                                                                                                   // 26
                                                                                                                       // 27
Template.__checkName("multilevelorigNodeTemplate");                                                                    // 28
Template["multilevelorigNodeTemplate"] = new Template("Template.multilevelorigNodeTemplate", (function() {             // 29
  var view = this;                                                                                                     // 30
  return HTML.LI({                                                                                                     // 31
    id: function() {                                                                                                   // 32
      return Spacebars.mustache(view.lookup("id"));                                                                    // 33
    },                                                                                                                 // 34
    title: function() {                                                                                                // 35
      return Spacebars.mustache(view.lookup("name"));                                                                  // 36
    },                                                                                                                 // 37
    type: function() {                                                                                                 // 38
      return Spacebars.mustache(view.lookup("type"));                                                                  // 39
    },                                                                                                                 // 40
    clique: function() {                                                                                               // 41
      return Spacebars.mustache(view.lookup("clique"));                                                                // 42
    },                                                                                                                 // 43
    objid: function() {                                                                                                // 44
      return Spacebars.mustache(Spacebars.dot(view.lookup("_id"), "_str"));                                            // 45
    }                                                                                                                  // 46
  }, "\n        ", HTML.A({                                                                                            // 47
    href: "#"                                                                                                          // 48
  }, HTML.Raw('<i class="fa fa-laptop"></i>'), Blaze.View("lookup:object_name", function() {                           // 49
    return Spacebars.mustache(view.lookup("object_name"));                                                             // 50
  })), "\n        ", Blaze.If(function() {                                                                             // 51
    return Spacebars.call(view.lookup("hasChildren"));                                                                 // 52
  }, function() {                                                                                                      // 53
    return [ "\n            ", HTML.H2(HTML.I({                                                                        // 54
      "class": "fa fa-laptop"                                                                                          // 55
    }), Blaze.View("lookup:object_name", function() {                                                                  // 56
      return Spacebars.mustache(view.lookup("object_name"));                                                           // 57
    })), "\n            ", HTML.UL("\n                ", Blaze.Each(function() {                                       // 58
      return Spacebars.call(view.lookup("children"));                                                                  // 59
    }, function() {                                                                                                    // 60
      return [ "\n                    ", Spacebars.include(view.lookupTemplate("multilevelorigNodeTemplate")), "\n                " ];
    }), "\n            "), "\n        " ];                                                                             // 62
  }), "\n    ");                                                                                                       // 63
}));                                                                                                                   // 64
                                                                                                                       // 65
Template.__checkName("breadcrumbMenu");                                                                                // 66
Template["breadcrumbMenu"] = new Template("Template.breadcrumbMenu", (function() {                                     // 67
  var view = this;                                                                                                     // 68
  return HTML.Raw('<ol class="breadcrumb">\n        <li class="active">All Categories</li>\n    </ol>');               // 69
}));                                                                                                                   // 70
                                                                                                                       // 71
Template.__checkName("topnavbarmenu");                                                                                 // 72
Template["topnavbarmenu"] = new Template("Template.topnavbarmenu", (function() {                                       // 73
  var view = this;                                                                                                     // 74
  return HTML.NAV({                                                                                                    // 75
    "class": "navbar navbar-inverse navbar-fixed-top"                                                                  // 76
  }, "\n        ", HTML.DIV({                                                                                          // 77
    "class": "container-fluid"                                                                                         // 78
  }, "\n            ", HTML.DIV({                                                                                      // 79
    "class": "navbar-header"                                                                                           // 80
  }, "\n                ", HTML.Raw('<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>'), "\n                ", HTML.A({
    "class": "navbar-brand",                                                                                           // 82
    href: function() {                                                                                                 // 83
      return Spacebars.mustache(view.lookup("pathFor"), Spacebars.kw({                                                 // 84
        route: "homePage"                                                                                              // 85
      }));                                                                                                             // 86
    }                                                                                                                  // 87
  }, "Project OSDNA"), "\n                ", HTML.DIV({                                                                // 88
    "class": "navbar-form navbar-left"                                                                                 // 89
  }, "\n                    ", Spacebars.include(view.lookupTemplate("envForm")), "\n                "), "\n            "), "\n            ", HTML.DIV({
    id: "navbar",                                                                                                      // 91
    "class": "navbar-collapse collapse"                                                                                // 92
  }, "\n                ", HTML.UL({                                                                                   // 93
    "class": "nav navbar-nav navbar-right"                                                                             // 94
  }, "\n                    ", HTML.LI(HTML.A({                                                                        // 95
    href: function() {                                                                                                 // 96
      return Spacebars.mustache(view.lookup("pathFor"), Spacebars.kw({                                                 // 97
        route: "home"                                                                                                  // 98
      }));                                                                                                             // 99
    }                                                                                                                  // 100
  }, "Graph")), "\n                    ", HTML.Raw('<li><a href="#">Settings</a></li>'), "\n                    ", HTML.Raw('<li><a href="#">Profile</a></li>'), "\n                    ", HTML.Raw('<li><a href="#">Help</a></li>'), "\n                "), "\n                ", HTML.Raw('<div class="navbar-form navbar-right">\n                    <input type="text" id="search" class="form-control" placeholder="Search...">\n                </div>'), "\n            "), "\n        "), "\n    ");
}));                                                                                                                   // 102
                                                                                                                       // 103
Template.__checkName("envForm");                                                                                       // 104
Template["envForm"] = new Template("Template.envForm", (function() {                                                   // 105
  var view = this;                                                                                                     // 106
  return HTML.FORM({                                                                                                   // 107
    id: "selEnvForm"                                                                                                   // 108
  }, "\n        ", HTML.SELECT({                                                                                       // 109
    "class": "form-control",                                                                                           // 110
    id: "envList"                                                                                                      // 111
  }, "\n            ", HTML.Raw("<option>Please Select Env</option>"), "\n            ", Blaze.Each(function() {       // 112
    return Spacebars.call(view.lookup("envList"));                                                                     // 113
  }, function() {                                                                                                      // 114
    return [ "\n                ", HTML.OPTION(HTML.Attrs({                                                            // 115
      value: function() {                                                                                              // 116
        return Spacebars.mustache(view.lookup("name"));                                                                // 117
      }                                                                                                                // 118
    }, function() {                                                                                                    // 119
      return Spacebars.attrMustache(view.lookup("selected"));                                                          // 120
    }), Blaze.View("lookup:name", function() {                                                                         // 121
      return Spacebars.mustache(view.lookup("name"));                                                                  // 122
    })), "\n            " ];                                                                                           // 123
  }), "\n        "), "\n    ");                                                                                        // 124
}));                                                                                                                   // 125
                                                                                                                       // 126
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"template.landingpage.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/templates/template.landingpage.js                                                                            //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
                                                                                                                       // 1
Template.__checkName("landingpage");                                                                                   // 2
Template["landingpage"] = new Template("Template.landingpage", (function() {                                           // 3
  var view = this;                                                                                                     // 4
  return [ HTML.Raw('<link rel="stylesheet" href="https://code.getmdl.io/1.1.3/material.blue-purple.min.css">\n    <!-- Animate CSS -->\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.1/animate.min.css">\n    '), Spacebars.include(view.lookupTemplate("envdialog")), HTML.Raw("\n    <!-- hero section -->\n    "), HTML.SECTION({
    "class": "home-fullscreen background-blue animated slideInUp"                                                      // 6
  }, "\n        ", HTML.Raw("<!-- Logo and navigation -->"), "\n        ", HTML.DIV({                                  // 7
    "class": "mdl-grid"                                                                                                // 8
  }, "\n            ", HTML.DIV({                                                                                      // 9
    "class": "mdl-cell mdl-cell--2-offset mdl-cell--2-col text-align-center",                                          // 10
    style: "padding-top: 15px;"                                                                                        // 11
  }, "\n                ", HTML.SVG({                                                                                  // 12
    x: "0px",                                                                                                          // 13
    y: "0px",                                                                                                          // 14
    viewBox: "0 234.9 612 323",                                                                                        // 15
    "enable-background": "new 0 234.9 612 323",                                                                        // 16
    "xml:space": "preserve",                                                                                           // 17
    height: "30"                                                                                                       // 18
  }, "\n            ", HTML.G("\n              ", HTML.RECT({                                                          // 19
    x: "173.4",                                                                                                        // 20
    y: "449.1",                                                                                                        // 21
    fill: "#fff",                                                                                                      // 22
    width: "27.2",                                                                                                     // 23
    height: "106.2"                                                                                                    // 24
  }), "\n              ", HTML.PATH({                                                                                  // 25
    fill: "#fff",                                                                                                      // 26
    d: "M416.5,479.7c-0.8-0.9-9.3-6-23-6c-17,0-29.8,11.9-29.8,28.1c0,16.1,11.9,28,29.8,28\n                c12.8,0,21.2-5.1,23-6v28.9c-3.4,0.8-12.8,3.4-24.7,3.4c-30.6,0-56.9-20.4-56.9-55.2c0-31.5,23.8-55.2,56.9-55.2\n                c12.8,0,22.1,3.4,24.7,3.4V479.7z"
  }), "\n              ", HTML.PATH({                                                                                  // 28
    fill: "#fff",                                                                                                      // 29
    d: "M136,479.7c-0.9-0.9-9.4-6-22.9-6c-17,0-29.8,11.9-29.8,28.1c0,16.1,11.9,28,29.8,28\n                c12.8,0,21.2-5.1,22.9-6v28.9c-3.4,0.8-12.8,3.4-24.6,3.4c-29.8,0-57-20.4-57-55.2c0-31.5,23.8-55.2,57-55.2\n                c12.8,0,22.1,3.4,24.6,3.4V479.7z"
  }), "\n              ", HTML.PATH({                                                                                  // 31
    fill: "#fff",                                                                                                      // 32
    d: "M556.8,502.7c0,30.6-23.8,55.2-56.1,55.2s-56.1-24.7-56.1-55.2s23.8-55.2,56.1-55.2\n                C533.8,447.4,556.8,472.1,556.8,502.7z M500.7,474.6c-16.2,0-28.1,12.8-28.1,28s11.9,28,28.1,28c16.2,0,28-12.8,28-28\n                S516.8,474.6,500.7,474.6z"
  }), "\n              ", HTML.PATH({                                                                                  // 34
    fill: "#fff",                                                                                                      // 35
    d: "M301.8,473.8c0,0-11.9-3.4-21.2-3.4c-11,0-17,3.4-17,8.5c0,6.8,7.6,8.5,11.9,10.2l7.6,2.5\n                c17,6,25.5,17.8,25.5,30.6c0,26.3-23.8,35.7-44.2,35.7c-14.4,0-28-2.5-28.9-2.5v-24.7c2.5,0.8,13.6,4.2,25.5,4.2\n                c13.6,0,19.6-4.2,19.6-10.2c0-5.1-5.1-8.5-11.9-10.2c-1.7-0.8-4.2-1.7-6-1.7c-15.3-5.1-27.2-13.6-27.2-31.4\n                c0-19.5,15.3-33.1,39.9-33.1c12.8,0,25.5,3.4,26.3,3.4V473.8z"
  }), "\n              ", HTML.PATH({                                                                                  // 37
    fill: "#fff",                                                                                                      // 38
    d: "M26.3,335.2c0-7.6-5.9-13.6-13.6-13.6s-13.6,5.9-13.6,13.6v28.1c0,7.6,5.9,13.6,13.6,13.6s13.6-6,13.6-13.6\n                V335.2z"
  }), "\n              ", HTML.PATH({                                                                                  // 40
    fill: "#fff",                                                                                                      // 41
    d: "M99.4,298.7c0-7.6-5.9-13.6-13.6-13.6s-12.7,6-12.7,13.6v64.6c0,7.6,5.9,13.6,13.6,13.6s13.6-6,13.6-13.6\n                v-64.6H99.4z"
  }), "\n              ", HTML.PATH({                                                                                  // 43
    fill: "#fff",                                                                                                      // 44
    d: "M173.4,248.5c0-7.7-5.9-13.6-13.6-13.6c-7.6,0-13.6,5.9-13.6,13.6v141.1c0,7.6,5.9,13.6,13.6,13.6\n                c7.7,0,13.6-6,13.6-13.6V248.5z"
  }), "\n              ", HTML.PATH({                                                                                  // 46
    fill: "#fff",                                                                                                      // 47
    d: "M246.5,298.7c0-7.6-6-13.6-13.6-13.6s-13.6,6-13.6,13.6v64.6c0,7.6,6,13.6,13.6,13.6s13.6-6,13.6-13.6\n                V298.7z"
  }), "\n              ", HTML.PATH({                                                                                  // 49
    fill: "#fff",                                                                                                      // 50
    d: "M319.6,335.2c0-7.6-5.9-13.6-13.6-13.6c-7.7,0-13.6,5.9-13.6,13.6v28.1c0,7.6,5.9,13.6,13.6,13.6\n                c7.7,0,13.6-6,13.6-13.6V335.2z"
  }), "\n              ", HTML.PATH({                                                                                  // 52
    fill: "#fff",                                                                                                      // 53
    d: "M392.7,298.7c0-7.6-6-13.6-13.6-13.6s-13.6,6-13.6,13.6v64.6c0,7.6,6,13.6,13.6,13.6\n                c7.7,0,13.6-6,13.6-13.6V298.7z"
  }), "\n              ", HTML.PATH({                                                                                  // 55
    fill: "#fff",                                                                                                      // 56
    d: "M465.8,248.5c0-7.7-6-13.6-13.6-13.6c-7.7,0-13.6,5.9-13.6,13.6v141.1c0,7.6,6,13.6,13.6,13.6\n                s13.6-6,13.6-13.6V248.5z"
  }), "\n              ", HTML.PATH({                                                                                  // 58
    fill: "#fff",                                                                                                      // 59
    d: "M538.9,298.7c0-7.6-6-13.6-13.6-13.6c-7.7,0-13.6,6-13.6,13.6v64.6c0,7.6,5.9,13.6,13.6,13.6\n                c7.6,0,13.6-6,13.6-13.6V298.7z"
  }), "\n              ", HTML.PATH({                                                                                  // 61
    fill: "#fff",                                                                                                      // 62
    d: "M612,335.2c0-7.6-5.9-13.6-13.6-13.6s-13.6,5.9-13.6,13.6v28.1c0,7.6,5.9,13.6,13.6,13.6s13.6-6,13.6-13.6\n                V335.2z"
  }), "\n            "), "\n        "), "\n            "), "\n            ", HTML.DIV({                                // 64
    "class": "mdl-cell mdl-cell--4-offset mdl-cell--2-col text-align-center"                                           // 65
  }, "\n                ", HTML.H5({                                                                                   // 66
    "class": "headline"                                                                                                // 67
  }, " ", HTML.A({                                                                                                     // 68
    "class": "mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent",                    // 69
    href: function() {                                                                                                 // 70
      return Spacebars.mustache(view.lookup("pathFor"), Spacebars.kw({                                                 // 71
        route: "homePage"                                                                                              // 72
      }));                                                                                                             // 73
    }                                                                                                                  // 74
  }, "OSDNA")), "\n            "), "\n        "), "\n        ", HTML.Raw("<!-- //Logo and navigation -->"), "\n        ", HTML.Raw("<!-- Main content -->"), "\n        ", HTML.Raw('<div class="mdl-grid">\n            <div class="mdl-cell mdl-cell--2-offset mdl-cell--8-col">\n                <h1 class="md-display-3 text-align-center">OpenStack Network <br> Discovery N Assurance</h1>\n            </div>\n\n            <div class="mdl-cell mdl-cell--2-offset mdl-cell--8-col">\n                <h5 class="text-align-center">We are going to enhance the way Cloud Network Administrators (CNA) and Tenant Network Administrators (TNA) Understands, Monitors and Troubleshoot highly distributed OpenStack Environments</h5>\n            </div>\n            <!--Button-->\n            <div class="mdl-cell mdl-cell--12-col text-align-center">\n                <button href="#" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">\n                    Start now\n                </button>\n            </div>\n            <!-- //Button-->\n            <div class="mdl-cell mdl-cell--12-col text-align-center">\n                <div class="home_mockups text-align-center">\n                    <img src="/home_mockups_11.png" alt="" class="img_responsive home_mockups_3 animated slideInUp" width="940" height="470">\n                    <img src="/home_mockups_21.png" alt="" class="img_responsive home_mockups_2 animated slideInUp" width="940" height="470">\n                    <img src="/home_mockups_31.png" alt="" class="img_responsive home_mockups_1 animated slideInUp" width="940" height="470">\n                </div>\n            </div>\n        </div>'), "\n        ", HTML.Raw("<!-- //Main content -->"), "\n    "), HTML.Raw('\n\n    <!-- section 2  -->\n    <section class="background-white">\n        <div class="mdl-grid">\n\n            <!-- first point -->\n            <div class="mdl-cell mdl-cell--1-offset mdl-cell--5-col">\n                <h3 class="title-border-bottom">Application Intent</h3>\n                <p class="font20">Provide CNA and TNA with support for: </p>\n                <ul class="font20">\n                    <li>Building virtual Network inventory and visualizing all low level details, inter-connections in real-time.</li>\n                    <li>Monitor virtual network objects.</li>\n                    <li>Troubleshoot failures and analyzing the root cause of failures in virtual networks.</li>\n                    <li>Assess impact of failure in virtual networks.</li>\n                </ul>\n                <!--Button-->\n                <button href="#" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--colored">\n                    Show more\n                </button>\n                <!-- //Button-->\n            </div>\n            <div class="mdl-cell mdl-cell--1-offset mdl-cell--5-col">\n                <img src="/logo_microscope_3.png" alt="" class="img_responsive wow slideInRight " data-wow-delay="0.3s" width="350" height="350">\n            </div>\n\n            <!-- second point -->\n            <div class="mdl-cell mdl-cell--1-offset mdl-cell--4-col">\n                <img src="/osdiagram.jpg" alt="" class="img_responsive wow slideInLeft" data-wow-delay="0.3s" width="350" height="350">\n            </div>\n            <div class="mdl-cell mdl-cell--1-offset mdl-cell--5-col">\n                <h3 class="title-border-bottom">Vision</h3>\n                <p class="font20">\n                    Substantially Simplifying OpenStack networking operations: maintenance, troubleshooting and monitoring, with added-value analytics.</p>\n                <button href="#" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--colored">\n                    Show more\n                </button>\n\n            </div>\n\n            <!-- third point -->\n            <div class="mdl-cell mdl-cell--1-offset mdl-cell--5-col">\n                <h3 class="title-border-bottom">Strategy</h3>\n                <p class="font20">Drive the adoption of a commercial, cisco-supported neutron networking assurance application.Create Operations application that dynamically discovers, display, monitors and analyze virtual networks in any OpenStack distribution with any Neutron plugin and dynamically analyze the information for assurance reporting, potentially a commercial offering (with limited open sourced functionality), to be sold to any OpenStack customers, admins and operators.Focus on multiple distributions and multiple plugins per distribution at High performance and scale.</p>\n                <!--Button-->\n                <button href="#" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--colored">\n                    Show more\n                </button>\n                <!-- //Button-->\n            </div>\n            <div class="mdl-cell mdl-cell--1-offset mdl-cell--5-col">\n                <img src="/dna-718905_1920.png" alt="" class="img_responsive wow slideInRight " data-wow-delay="0.3" width="400" height="300">\n            </div>\n        </div>\n    </section>\n\n    <!-- section Cisco partners -->\n    <section class="background-blue">\n        <div class="mdl-grid">\n\n            <div class="mdl-cell mdl-cell--4-col">\n                <div class="box text-align-center wow slideInUp">\n                    <div>\n                        <i class="material-icons md-48">flight_takeoff</i>\n                    </div>\n                    <div class="iconbox_content">\n                        <h3>First Partner</h3>\n                        <p>Lorem ipsum dolor sit amet, consectetur elit, sed do tempor incididunt dolore.</p>\n                    </div>\n                </div>\n            </div>\n\n            <div class="mdl-cell mdl-cell--4-col">\n                <div class="box text-align-center wow slideInUp" data-wow-delay="0.5s">\n                    <div>\n                        <i class="material-icons md-48">thumb_up</i>\n                    </div>\n                    <div class="iconbox_content">\n                        <h3>Second Partner</h3>\n                        <p>Lorem ipsum dolor sit amet, consectetur elit, sed do tempor incididunt dolore.</p>\n                    </div>\n                </div>\n            </div>\n\n            <div class="mdl-cell mdl-cell--4-col">\n                <div class="box text-align-center wow slideInUp" data-wow-delay="0.8s">\n                    <div>\n                        <i class="material-icons md-48">live_help</i>\n                    </div>\n                    <div class="iconbox_content">\n                        <h3>First Partner</h3>\n                        <p>Lorem ipsum dolor sit amet, consectetur elit, sed do tempor incididunt dolore.</p>\n                    </div>\n                </div>\n            </div>\n\n        </div>\n    </section>\n\n    <!-- Our team -->\n    <!-- section number 3  -->\n    <section class="background-white">\n        <div class="mdl-grid">\n            <!-- third point -->\n            <div class="mdl-cell mdl-cell--1-offset mdl-cell--5-col">\n                <h3 class="title-border-bottom">This is our amazing feature and it\'s awesome!</h3>\n                <p class="font20">Drive the adoption of a commercial, cisco-supported neutron networking assurance application.Create Operations application that dynamically discovers, display, monitors and analyze virtual networks in any OpenStack distribution with any Neutron plugin and dynamically analyze the information for assurance reporting, potentially a commercial offering (with limited open sourced functionality), to be sold to any OpenStack customers, admins and operators.</p>\n                <!--Button-->\n                <button href="#" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--colored">\n                    Show more\n                </button>\n                <!-- //Button-->\n            </div>\n            <div class="mdl-cell mdl-cell--1-offset mdl-cell--5-col">\n                <img src="/home_mockups_1.png" alt="" class="img_responsive wow slideInRight " data-wow-delay="0.3" width="500">\n            </div>\n        </div>\n    </section>\n\n    <section class="background-blue">\n        <div class="mdl-grid">\n            <div class="mdl-cell mdl-cell--12-col text-align-center">\n                <p>Cisco Systems, Inc © Copyright 2016</p>\n            </div>\n        </div>\n    </section>') ];
}));                                                                                                                   // 76
                                                                                                                       // 77
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"template.mainPage.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/templates/template.mainPage.js                                                                               //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
                                                                                                                       // 1
Template.__checkName("mainPage");                                                                                      // 2
Template["mainPage"] = new Template("Template.mainPage", (function() {                                                 // 3
  var view = this;                                                                                                     // 4
  return [ HTML.HEADER("\n        ", HTML.DIV({                                                                        // 5
    "class": "navbar",                                                                                                 // 6
    role: "navigation"                                                                                                 // 7
  }, "\n            ", HTML.DIV({                                                                                      // 8
    "class": "container"                                                                                               // 9
  }, "\n                ", HTML.DIV({                                                                                  // 10
    "class": "navbar-header"                                                                                           // 11
  }, "\n                    ", Blaze.If(function() {                                                                   // 12
    return Spacebars.call(view.lookup("currentUser"));                                                                 // 13
  }, function() {                                                                                                      // 14
    return [ "\n                    ", HTML.A({                                                                        // 15
      "class": "navbar-brand",                                                                                         // 16
      id: "logo",                                                                                                      // 17
      href: function() {                                                                                               // 18
        return Spacebars.mustache(view.lookup("pathFor"), Spacebars.kw({                                               // 19
          route: "home"                                                                                                // 20
        }));                                                                                                           // 21
      }                                                                                                                // 22
    }, "OSDNA - Dashboard"), "\n                    " ];                                                               // 23
  }), "\n                    ", HTML.Raw('<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#mynav">\n                        <span class="sr-only">Toggle navigation</span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                    </button>'), "\n                "), "\n                ", HTML.DIV({
    "class": "collapse navbar-collapse",                                                                               // 25
    id: "mynav"                                                                                                        // 26
  }, "\n                    ", HTML.UL({                                                                               // 27
    "class": "nav navbar-nav navbar-right"                                                                             // 28
  }, "\n                        ", HTML.Raw('<li><a href="#about">About</a></li>'), "\n                        ", HTML.Raw('<li><a href="#clients">Clients</a></li>'), "\n                        ", HTML.Raw('<li><a href="#process">Process</a></li>'), "\n                        ", HTML.Raw('<li><a href="#testimonials">Testimonials</a></li>'), "\n                        ", HTML.Raw('<li><a href="#blogs">Blogs</a></li>'), "\n                        ", HTML.LI(HTML.A({
    href: function() {                                                                                                 // 30
      return Spacebars.mustache(view.lookup("pathFor"), Spacebars.kw({                                                 // 31
        route: "landingpage"                                                                                           // 32
      }));                                                                                                             // 33
    }                                                                                                                  // 34
  }, "LandingPage")), "\n                        ", HTML.LI(HTML.A({                                                   // 35
    href: "#"                                                                                                          // 36
  }, Spacebars.include(view.lookupTemplate("loginButtons")))), "\n                    "), "\n                "), "\n            "), "\n        "), "\n        ", HTML.Raw('<div class="banner">\n            <h2>OSDNA - OpenStack Network Discovery N Assurance</h2>\n            <div class="info">\n                <a href="#process" title="">See our process</a>\n                <a href="#clients" title="">See our clients</a>\n            </div>\n        </div>'), "\n    "), HTML.Raw('\n    <section class="about" id="about">\n        <div class="container">\n            <div class="row">\n                <div class="col-xs-12">\n                    <h2>About</h2>\n                </div>\n            </div>\n            <div class="row">\n                <div class="col-xs-12 col-sm-4">\n                    <h4>Our history</h4>\n                    <p class="visible-lg">We are going to enhance the way Cloud Network Administrators (CNA) and Tenant Network Administrators (TNA) Understands, Monitors and Troubleshoot highly distributed OpenStack Environments.</p>\n                </div>\n                <div class="col-xs-12 col-sm-4">\n                    <h4>Our vision &amp; Strategy</h4>\n                    <p>Vision: Substantially Simplifying OpenStack networking operations: maintenance, troubleshooting and monitoring, with added-value analytics.</p>\n                    <p>Strategy: Drive the adoption of a commercial, cisco-supported neutron networking assurance application.Create Operations application that dynamically discovers, display, monitors and analyze virtual networks in any OpenStack distribution with any Neutron plugin and dynamically analyze the information for assurance reporting, potentially a commercial offering (with limited open sourced functionality), to be sold to any OpenStack customers, admins and operators.</p>\n                    <p class="visible-lg">Focus on multiple distributions and multiple plugins per distribution at High performance and scale.</p>\n                </div>\n                <div class="col-xs-12 col-sm-4">\n                    <h4>Application Intent</h4>\n                    <p>Provide CNA and TNA with support for: </p>\n                    <p>1. Building virtual Network inventory and visualizing all low level details, inter-connections in real-time. </p>\n                    <p>2. Monitor virtual network objects.</p>\n                    <p class="visible-lg">3. Troubleshoot failures and analyzing the root cause of failures in virtual networks. </p>\n                    <p class="visible-lg">4. Assess impact of failure in virtual networks.</p>\n\n                </div>\n            </div>\n        </div>\n    </section> <!-- end of about section-->\n    <hr>\n    <section class="clients" id="clients">\n        <div class="container">\n            <div class="row">\n                <div class="col-xs-12">\n                    <h2>Our Clients</h2>\n                </div>\n            </div>\n            <div class="row">\n                <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">\n                    <div class="clients-info">\n                        <h3>Client1</h3>\n                    </div>\n                </div>\n                <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">\n                    <div class="clients-info">\n                        <h3>Client2</h3>\n                    </div>\n                </div>\n                <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">\n                    <div class="clients-info">\n                        <h3>Client3</h3>\n                    </div>\n                </div>\n                <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">\n                    <div class="clients-info">\n                        <h3>Client4</h3>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </section> <!-- end of clients section-->\n    <hr>\n    <section class="process" id="process">\n        <div class="container">\n            <div class="row">\n                <div class="col-xs-12">\n                    <h2>Our Process</h2>\n                </div>\n            </div>\n            <div class="row">\n                <div class="col-xs-12 col-sm-6 col-md-3">\n                    <div class="method">\n                        <h3>Analyze</h3>\n                        <hr>\n                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>\n                        <h4>1</h4>\n                    </div>\n                </div>\n                <div class="col-xs-12 col-sm-6 col-md-3">\n                    <div class="method">\n                        <h3>Develop</h3>\n                        <hr>\n                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>\n                        <h4>2</h4>\n                    </div>\n                </div>\n                <div class="col-xs-12 col-sm-6 col-md-3">\n                    <div class="method">\n                        <h3>Test</h3>\n                        <hr>\n                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>\n                        <h4>3</h4>\n                    </div>\n                </div>\n                <div class="col-xs-12 col-sm-6 col-md-3">\n                    <div class="method">\n                        <h3>Deploy</h3>\n                        <hr>\n                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>\n                        <h4>4</h4>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </section> <!-- end of method section-->\n    <hr>\n    <section class="testimonials" id="testimonials">\n        <div class="container">\n            <div class="row">\n                <div class="col-xs-12">\n                    <h2>Our Testimonials</h2>\n                </div>\n            </div>\n            <div class="row">\n                <div class="col-xs-12 col-sm-4">\n                    <blockquote>\n                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tempore eligendi a officiis aspernatur nesciunt ducimus, placeat. Eum, ratione maxime fugiat deserunt doloremque laborum hic quisquam in, libero voluptatibus! Assumenda, eligendi.\n                        </p>\n                    </blockquote>\n                </div>\n                <div class="col-xs-12 col-sm-4">\n                    <blockquote>\n                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tempore eligendi a officiis aspernatur nesciunt ducimus, placeat. Eum, ratione maxime fugiat deserunt doloremque laborum hic quisquam in, libero voluptatibus! Assumenda, eligendi.\n                        </p>\n                    </blockquote>\n                </div>\n                <div class="col-xs-12 col-sm-4">\n                    <blockquote>\n                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tempore eligendi a officiis aspernatur nesciunt ducimus, placeat. Eum, ratione maxime fugiat deserunt doloremque laborum hic quisquam in, libero voluptatibus! Assumenda, eligendi.\n                        </p>\n                    </blockquote>\n                </div>\n            </div>\n        </div>\n    </section><!-- end of testimonials section-->\n    <hr>\n    <section class="blogs" id="blogs">\n        <div class="container">\n            <div class="row">\n                <div class="col-xs-12">\n                    <h2>Latest Blogs</h2>\n                </div>\n            </div>\n            <div class="row">\n                <div class="col-xs-12 col-lg-8">\n                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar scelerisque aliquet. Aliquam eu ultrices nisl. Mauris sit amet odio tincidunt, congue magna a, malesuada odio. Maecenas egestas metus leo, nec vulputate odio pulvinar sodales. Aenean a nunc nisi. Donec eleifend sodales mauris, ut egestas tellus ultrices nec. Integer in nisl vitae libero lobortis egestas. Proin nisi lacus, iaculis sit amet nibh vel, fringilla pellentesque est.</p>\n                    <p class="visible-lg">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut delectus ratione aut est, minus eius, dolorem blanditiis culpa ad iusto, accusamus iure alias nihil voluptatem soluta esse velit laudantium eum.</p>\n                    <p class="visible-lg">Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur.</p>\n                    <button type="button" class="btn btn-primary">Learn more</button>\n                </div>\n                <div class="visible-lg col-lg-4">\n                    <img class="img-responsive" src="http://placehold.it/450x300">\n                </div>\n            </div>\n        </div>\n    </section><!-- end of blogs section-->\n    <footer>\n        <p>Made by Ofir Ashery.</p>\n    </footer>') ];
}));                                                                                                                   // 38
                                                                                                                       // 39
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"template.threeTest.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/templates/template.threeTest.js                                                                              //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
                                                                                                                       // 1
Template.__checkName("threeTest");                                                                                     // 2
Template["threeTest"] = new Template("Template.threeTest", (function() {                                               // 3
  var view = this;                                                                                                     // 4
  return HTML.Raw('<div id="threeGraph"></div>');                                                                      // 5
}));                                                                                                                   // 6
                                                                                                                       // 7
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"template.threeTest2.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/templates/template.threeTest2.js                                                                             //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
                                                                                                                       // 1
Template.__checkName("threeTest2");                                                                                    // 2
Template["threeTest2"] = new Template("Template.threeTest2", (function() {                                             // 3
  var view = this;                                                                                                     // 4
  return HTML.Raw('<div id="canvas-force"></div>\n    <div id="tooltip-container"></div>');                            // 5
}));                                                                                                                   // 6
                                                                                                                       // 7
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"template.main.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/templates/template.main.js                                                                                   //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
                                                                                                                       // 1
Template.__checkName("main");                                                                                          // 2
Template["main"] = new Template("Template.main", (function() {                                                         // 3
  var view = this;                                                                                                     // 4
  return Spacebars.include(view.lookupTemplate("yield"));                                                              // 5
}));                                                                                                                   // 6
                                                                                                                       // 7
Template.__checkName("loading");                                                                                       // 8
Template["loading"] = new Template("Template.loading", (function() {                                                   // 9
  var view = this;                                                                                                     // 10
  return "";                                                                                                           // 11
}));                                                                                                                   // 12
                                                                                                                       // 13
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}},"lib":{"d3three.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/lib/d3three.js                                                                                               //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
var chartOffset = 0;                                                                                                   // 1
                                                                                                                       //
// D3.layout.force3d.js                                                                                                //
// (C) 2012 ziggy.jonsson.nyc@gmail.com                                                                                //
// BSD license (http://opensource.org/licenses/BSD-3-Clause)                                                           //
                                                                                                                       //
d3.layout.force3d = function () {                                                                                      // 7
  var forceXY = d3.layout.force(),                                                                                     // 8
      forceZ = d3.layout.force(),                                                                                      //
      zNodes = {},                                                                                                     //
      zLinks = {},                                                                                                     //
      nodeID = 1,                                                                                                      //
      linkID = 1,                                                                                                      //
      tickFunction = Object;                                                                                           //
                                                                                                                       //
  var force3d = {};                                                                                                    // 16
                                                                                                                       //
  Object.keys(forceXY).forEach(function (d) {                                                                          // 18
    force3d[d] = function () {                                                                                         // 19
      var result = forceXY[d].apply(this, arguments);                                                                  // 20
      if (d != "nodes" && d != "links") forceZ[d].apply(this, arguments);                                              // 21
      return result == forceXY ? force3d : result;                                                                     // 22
    };                                                                                                                 //
  });                                                                                                                  //
                                                                                                                       //
  force3d.on = function (name, fn) {                                                                                   // 27
    tickFunction = fn;                                                                                                 // 28
    return force3d;                                                                                                    // 29
  };                                                                                                                   //
                                                                                                                       //
  forceXY.on("tick", function () {                                                                                     // 33
                                                                                                                       //
    // Refresh zNodes add new, delete removed                                                                          //
    var _zNodes = {};                                                                                                  // 36
    forceXY.nodes().forEach(function (d, i) {                                                                          // 37
      if (!d.id) d.id = nodeID++;                                                                                      // 38
      _zNodes[d.id] = zNodes[d.id] || { x: d.z, px: d.z, py: d.z, y: d.z, id: d.id };                                  // 39
      d.z = _zNodes[d.id].x;                                                                                           // 40
    });                                                                                                                //
    zNodes = _zNodes;                                                                                                  // 42
                                                                                                                       //
    // Refresh zLinks add new, delete removed                                                                          //
    var _zLinks = {};                                                                                                  // 33
    forceXY.links().forEach(function (d) {                                                                             // 46
      var nytt = false;                                                                                                // 47
      if (!d.linkID) {                                                                                                 // 48
        d.linkID = linkID++;nytt = true;                                                                               // 48
      }                                                                                                                //
      _zLinks[d.linkID] = zLinks[d.linkID] || { target: zNodes[d.target.id], source: zNodes[d.source.id] };            // 49
    });                                                                                                                //
    zLinks = _zLinks;                                                                                                  // 52
                                                                                                                       //
    // Update the nodes/links in forceZ                                                                                //
    forceZ.nodes(d3.values(zNodes));                                                                                   // 33
    forceZ.links(d3.values(zLinks));                                                                                   // 56
    forceZ.start(); // Need to kick forceZ so we don't lose the update mechanism                                       // 57
                                                                                                                       //
    // And run the user defined function, if defined                                                                   //
    tickFunction();                                                                                                    // 33
  });                                                                                                                  //
                                                                                                                       //
  // Expose the sub-forces for debugging purposes                                                                      //
  force3d.xy = forceXY;                                                                                                // 7
  force3d.z = forceZ;                                                                                                  // 65
                                                                                                                       //
  return force3d;                                                                                                      // 67
};                                                                                                                     //
// end of d3.layout.force3d.js                                                                                         //
                                                                                                                       //
// Override default functions for d3                                                                                   //
THREE.Object3D.prototype.appendChild = function (c) {                                                                  // 72
  this.add(c);                                                                                                         // 73
  return c;                                                                                                            // 74
};                                                                                                                     //
THREE.Object3D.prototype.querySelectorAll = function () {                                                              // 76
  return [];                                                                                                           // 76
};                                                                                                                     //
                                                                                                                       //
// this one is to use D3's .attr() on THREE's objects                                                                  //
THREE.Object3D.prototype.setAttribute = function (name, value) {                                                       // 79
  var chain = name.split('.');                                                                                         // 80
  var object = this;                                                                                                   // 81
  for (var i = 0; i < chain.length - 1; i++) {                                                                         // 82
    object = object[chain[i]];                                                                                         // 83
  }                                                                                                                    //
  object[chain[chain.length - 1]] = value;                                                                             // 85
};                                                                                                                     //
                                                                                                                       //
// d3three object                                                                                                      //
D3THREE = function D3THREE(singleton) {                                                                                // 89
  this.labelGroup = new THREE.Object3D();                                                                              // 90
  this.maxY = 0;                                                                                                       // 91
  this.axisObjects = {};                                                                                               // 92
                                                                                                                       //
  this.running = true;                                                                                                 // 94
                                                                                                                       //
  if (singleton) {                                                                                                     // 96
    if (typeof d3three !== 'undefined') {                                                                              // 97
      d3three.stop();                                                                                                  // 98
    }                                                                                                                  //
    d3three = this;                                                                                                    // 100
  }                                                                                                                    //
                                                                                                                       //
  //if (!singleton) {                                                                                                  //
  //  d3threes.push(this);                                                                                             //
  //}                                                                                                                  //
};                                                                                                                     // 89
                                                                                                                       //
D3THREE.prototype.init = function (divId) {                                                                            // 108
  // standard THREE stuff, straight from examples                                                                      //
  this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true });              // 110
  this.renderer.shadowMap.enabled = true;                                                                              // 111
  this.renderer.shadowMap.type = THREE.PCFSoftShadow;                                                                  // 112
  this.renderer.shadowMapSoft = true;                                                                                  // 113
  this.renderer.shadowCameraNear = 1000;                                                                               // 114
  this.renderer.shadowCameraFar = 10000;                                                                               // 115
  this.renderer.shadowCameraFov = 50;                                                                                  // 116
  this.renderer.shadowMapBias = 0.0039;                                                                                // 117
  this.renderer.shadowMapDarkness = 0.25;                                                                              // 118
  this.renderer.shadowMapWidth = 10000;                                                                                // 119
  this.renderer.shadowMapHeight = 10000;                                                                               // 120
  this.renderer.physicallyBasedShading = true;                                                                         // 121
                                                                                                                       //
  this.divId = divId;                                                                                                  // 123
  this.width = document.getElementById(divId).offsetWidth;                                                             // 124
  this.height = document.getElementById(divId).offsetHeight;                                                           // 125
                                                                                                                       //
  this.renderer.setSize(this.width, this.height);                                                                      // 127
                                                                                                                       //
  document.getElementById(divId).appendChild(this.renderer.domElement);                                                // 129
                                                                                                                       //
  this.camera = new THREE.PerspectiveCamera(30, this.width / this.height, 1, 100000);                                  // 131
  this.camera.position.z = -1000;                                                                                      // 132
  this.camera.position.x = -800;                                                                                       // 133
  this.camera.position.y = 600;                                                                                        // 134
                                                                                                                       //
  this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);                                      // 136
                                                                                                                       //
  this.scene = new THREE.Scene();                                                                                      // 138
                                                                                                                       //
  this.defaultLight = new THREE.AmbientLight(0xbbbbb); // soft white light                                             // 140
  this.scene.add(this.defaultLight);                                                                                   // 108
                                                                                                                       //
  this.scene.add(this.labelGroup);                                                                                     // 143
                                                                                                                       //
  var self = this;                                                                                                     // 145
  window.addEventListener('resize', self.onWindowResize.bind(self), false);                                            // 146
};                                                                                                                     //
                                                                                                                       //
D3THREE.prototype.onWindowResize = function () {                                                                       // 149
  var self = this;                                                                                                     // 150
  self.camera.aspect = self.width / self.height;                                                                       // 151
  self.camera.updateProjectionMatrix();                                                                                // 152
                                                                                                                       //
  self.renderer.setSize(self.width, self.height);                                                                      // 154
};                                                                                                                     //
                                                                                                                       //
D3THREE.prototype.animate = function () {                                                                              // 157
  var self = this;                                                                                                     // 158
  if (this.running) {                                                                                                  // 159
    setTimeout(function () {                                                                                           // 160
      this.requestId = requestAnimationFrame(self.animate.bind(self));                                                 // 161
    }, 1000 / 15);                                                                                                     //
                                                                                                                       //
    self.renderer.render(self.scene, self.camera);                                                                     // 164
    self.controls.update();                                                                                            // 165
                                                                                                                       //
    self.labelGroup.children.forEach(function (l) {                                                                    // 167
      l.rotation.setFromRotationMatrix(self.camera.matrix, "YXZ");                                                     // 168
      l.rotation.x = 0;                                                                                                // 169
      l.rotation.z = 0;                                                                                                // 170
    });                                                                                                                //
  } else {                                                                                                             //
    window.removeEventListener('resize', self.onWindowResize.bind(self));                                              // 173
    while (self.scene.children.length > 0) {                                                                           // 174
      var childObject = self.scene.children[0];                                                                        // 175
      if (childObject.geometry) {                                                                                      // 176
        childObject.geometry.dispose();                                                                                // 177
      }                                                                                                                //
      if (childObject.material) {                                                                                      // 179
        childObject.material.dispose();                                                                                // 180
      }                                                                                                                //
      self.scene.remove(childObject);                                                                                  // 182
      delete childObject;                                                                                              // 183
    }                                                                                                                  //
                                                                                                                       //
    self.renderer.context = null;                                                                                      // 186
    self.renderer.domElement = null;                                                                                   // 187
    self.renderer = null;                                                                                              // 188
                                                                                                                       //
    self.camera = null;                                                                                                // 190
    self.controls = null;                                                                                              // 191
    self.scene = null;                                                                                                 // 192
    self.labelGroup = null;                                                                                            // 193
                                                                                                                       //
    cancelAnimationFrame(self.requestId);                                                                              // 195
  }                                                                                                                    //
};                                                                                                                     //
                                                                                                                       //
D3THREE.prototype.stop = function () {                                                                                 // 199
  this.running = false;                                                                                                // 200
};                                                                                                                     //
                                                                                                                       //
D3THREE.prototype.render = function (element, data) {                                                                  // 203
  element.render(data);                                                                                                // 204
};                                                                                                                     //
                                                                                                                       //
D3THREE.createAxis = function (dt) {                                                                                   // 207
  return new D3THREE.Axis(dt);                                                                                         // 208
};                                                                                                                     //
                                                                                                                       //
// d3three axis                                                                                                        //
D3THREE.Axis = function (dt) {                                                                                         // 212
  this._scale = d3.scale.linear();                                                                                     // 213
  this._orient = "x";                                                                                                  // 214
  this._tickFormat = function (d) {                                                                                    // 215
    return d;                                                                                                          // 215
  };                                                                                                                   //
  this._dt = dt;                                                                                                       // 216
};                                                                                                                     //
                                                                                                                       //
D3THREE.Axis.prototype.orient = function (o) {                                                                         // 219
  if (o) {                                                                                                             // 220
    this._dt.axisObjects[o] = this;                                                                                    // 221
    this._orient = o;                                                                                                  // 222
  }                                                                                                                    //
  return this;                                                                                                         // 224
};                                                                                                                     //
                                                                                                                       //
D3THREE.Axis.prototype.scale = function (s) {                                                                          // 227
  if (s) {                                                                                                             // 228
    this._scale = s;                                                                                                   // 229
  }                                                                                                                    //
  return this;                                                                                                         // 231
};                                                                                                                     //
                                                                                                                       //
D3THREE.Axis.prototype.tickFormat = function (f) {                                                                     // 234
  if (f) {                                                                                                             // 235
    this._tickFormat = f;                                                                                              // 236
  }                                                                                                                    //
  return this;                                                                                                         // 238
};                                                                                                                     //
                                                                                                                       //
D3THREE.Axis.prototype.interval = function () {                                                                        // 241
  var interval;                                                                                                        // 242
  if (typeof this._scale.rangeBand === 'function') {                                                                   // 243
    // ordinal scale                                                                                                   //
    interval = this._scale.range()[1];                                                                                 // 245
  } else {                                                                                                             //
    interval = this._scale.range()[1] / (this._scale.ticks().length - 1);                                              // 247
  }                                                                                                                    //
  return interval;                                                                                                     // 249
};                                                                                                                     //
                                                                                                                       //
D3THREE.Axis.prototype.ticks = function () {                                                                           // 252
  var ticks;                                                                                                           // 253
  if (typeof this._scale.rangeBand === 'function') {                                                                   // 254
    // ordinal scale                                                                                                   //
    ticks = this._scale.domain();                                                                                      // 256
  } else {                                                                                                             //
    ticks = this._scale.ticks();                                                                                       // 258
  }                                                                                                                    //
  return ticks;                                                                                                        // 260
};                                                                                                                     //
                                                                                                                       //
D3THREE.Axis.prototype.getRotationShift = function () {                                                                // 263
  return this.interval() * (this.ticks().length - 1) / 2;                                                              // 264
};                                                                                                                     //
                                                                                                                       //
D3THREE.Axis.prototype.render = function () {                                                                          // 267
  var material = new THREE.LineBasicMaterial({                                                                         // 268
    color: 0xbbbbbb,                                                                                                   // 269
    linewidth: 2                                                                                                       // 270
  });                                                                                                                  //
                                                                                                                       //
  var tickMaterial = new THREE.LineBasicMaterial({                                                                     // 273
    color: 0xbbbbbb,                                                                                                   // 274
    linewidth: 1                                                                                                       // 275
  });                                                                                                                  //
                                                                                                                       //
  var geometry = new THREE.Geometry();                                                                                 // 278
                                                                                                                       //
  interval = this.interval();                                                                                          // 280
                                                                                                                       //
  var interval = this.interval(),                                                                                      // 282
      ticks = this.ticks();                                                                                            //
                                                                                                                       //
  // x,y axis shift, so rotation is from center of screen                                                              //
  var xAxisShift = this._dt.axisObjects.x.getRotationShift(),                                                          // 267
      yAxisShift = this._dt.axisObjects.y.getRotationShift();                                                          //
                                                                                                                       //
  for (var i = 0; i < ticks.length; i++) {                                                                             // 288
    var tickMarGeometry = new THREE.Geometry();                                                                        // 289
                                                                                                                       //
    var shape = new THREE.TextGeometry(this._tickFormat(ticks[i]), {                                                   // 291
      size: 5,                                                                                                         // 293
      height: 1,                                                                                                       // 294
      curveSegments: 20                                                                                                // 295
    });                                                                                                                //
    var wrapper = new THREE.MeshBasicMaterial({ color: 0xbbbbbb });                                                    // 297
    var words = new THREE.Mesh(shape, wrapper);                                                                        // 298
                                                                                                                       //
    if (this._orient === "y") {                                                                                        // 300
      // tick                                                                                                          //
      geometry.vertices.push(new THREE.Vector3(i * interval - yAxisShift, chartOffset, 0 - xAxisShift));               // 302
                                                                                                                       //
      tickMarGeometry.vertices.push(new THREE.Vector3(i * interval - yAxisShift, chartOffset, 0 - xAxisShift));        // 304
      tickMarGeometry.vertices.push(new THREE.Vector3(i * interval - yAxisShift, -10 + chartOffset, 0 - xAxisShift));  // 305
      var tickLine = new THREE.Line(tickMarGeometry, tickMaterial);                                                    // 306
      this._dt.scene.add(tickLine);                                                                                    // 307
                                                                                                                       //
      if (i * interval > this._dt.maxY) {                                                                              // 309
        this._dt.maxY = i * interval;                                                                                  // 310
      }                                                                                                                //
                                                                                                                       //
      words.position.set(i * interval - yAxisShift, -20 + chartOffset, 0 - xAxisShift);                                // 313
    } else if (this._orient === "z") {                                                                                 //
      // tick                                                                                                          //
      geometry.vertices.push(new THREE.Vector3(0 + this._dt.maxY - yAxisShift, i * interval + chartOffset, 0 - xAxisShift));
                                                                                                                       //
      tickMarGeometry.vertices.push(new THREE.Vector3(0 + this._dt.maxY - yAxisShift, i * interval + chartOffset, 0 - xAxisShift));
      tickMarGeometry.vertices.push(new THREE.Vector3(10 + this._dt.maxY - yAxisShift, i * interval + chartOffset, 0 - xAxisShift));
      var tickLine = new THREE.Line(tickMarGeometry, tickMaterial);                                                    // 320
      this._dt.scene.add(tickLine);                                                                                    // 321
                                                                                                                       //
      words.position.set(20 + this._dt.maxY - yAxisShift, i * interval + chartOffset, 0 - xAxisShift);                 // 323
    } else if (this._orient === "x") {                                                                                 //
      // tick                                                                                                          //
      geometry.vertices.push(new THREE.Vector3(0 - yAxisShift, chartOffset, i * interval - xAxisShift));               // 326
                                                                                                                       //
      tickMarGeometry.vertices.push(new THREE.Vector3(0 - yAxisShift, 0 + chartOffset, i * interval - xAxisShift));    // 328
      tickMarGeometry.vertices.push(new THREE.Vector3(0 - yAxisShift, -10 + chartOffset, i * interval - xAxisShift));  // 329
      var tickLine = new THREE.Line(tickMarGeometry, tickMaterial);                                                    // 330
      this._dt.scene.add(tickLine);                                                                                    // 331
                                                                                                                       //
      words.position.set(0 - yAxisShift, -20 + chartOffset, i * interval - xAxisShift);                                // 333
    }                                                                                                                  //
                                                                                                                       //
    this._dt.labelGroup.add(words);                                                                                    // 336
  }                                                                                                                    //
                                                                                                                       //
  var line = new THREE.Line(geometry, material);                                                                       // 339
                                                                                                                       //
  this._dt.scene.add(line);                                                                                            // 341
};                                                                                                                     //
                                                                                                                       //
// Chart object                                                                                                        //
D3THREE.Chart = function () {};                                                                                        // 345
                                                                                                                       //
D3THREE.Chart.prototype.config = function (c) {                                                                        // 348
  this._config = $.extend(this._config, c);                                                                            // 349
};                                                                                                                     //
                                                                                                                       //
D3THREE.Chart.prototype.init = function (dt) {                                                                         // 352
  this._dt = dt;                                                                                                       // 353
  // mouse move                                                                                                        //
  var self = this;                                                                                                     // 352
  this._dt.renderer.domElement.addEventListener('mousemove', function (e) {                                            // 356
    self.onDocumentMouseMove(e);                                                                                       // 357
  }, false);                                                                                                           //
};                                                                                                                     //
                                                                                                                       //
var cumulativeOffset = function cumulativeOffset(element) {                                                            // 361
  var top = 0,                                                                                                         // 362
      left = 0;                                                                                                        //
  do {                                                                                                                 // 363
    top += element.offsetTop || 0;                                                                                     // 364
    left += element.offsetLeft || 0;                                                                                   // 365
    element = element.offsetParent;                                                                                    // 366
  } while (element);                                                                                                   //
                                                                                                                       //
  return {                                                                                                             // 369
    top: top,                                                                                                          // 370
    left: left                                                                                                         // 371
  };                                                                                                                   //
};                                                                                                                     //
                                                                                                                       //
D3THREE.Chart.prototype.detectNodeHover = function (e) {                                                               // 375
  var boundingRect = this._dt.renderer.domElement.getBoundingClientRect();                                             // 376
                                                                                                                       //
  var vector = new THREE.Vector3();                                                                                    // 378
  vector.x = (e.clientX - boundingRect.left) / this._dt.renderer.domElement.width * 2 - 1;                             // 379
  vector.y = 1 - (e.clientY - boundingRect.top) / this._dt.renderer.domElement.height * 2;                             // 380
  vector.z = 1;                                                                                                        // 381
                                                                                                                       //
  // create a check ray                                                                                                //
  vector.unproject(this._dt.camera);                                                                                   // 375
  var ray = new THREE.Raycaster(this._dt.camera.position, vector.sub(this._dt.camera.position).normalize());           // 385
                                                                                                                       //
  var intersects = ray.intersectObjects(this._nodeGroup.children);                                                     // 388
                                                                                                                       //
  for (var i = 0; i < this._nodeGroup.children.length; i++) {                                                          // 390
    this._nodeGroup.children[i].material.opacity = 1;                                                                  // 391
  }                                                                                                                    //
                                                                                                                       //
  if (intersects.length > 0) {                                                                                         // 394
    var obj = intersects[0].object;                                                                                    // 395
    obj.material.opacity = 0.5;                                                                                        // 396
                                                                                                                       //
    var html = "";                                                                                                     // 398
                                                                                                                       //
    html += "<div class=\"tooltip_kv\">";                                                                              // 400
    html += "<span>";                                                                                                  // 401
    html += "x: " + this._dt.axisObjects.x._tickFormat(obj.userData.x);                                                // 402
    html += "</span><br>";                                                                                             // 403
    html += "<span>";                                                                                                  // 404
    html += "y: " + this._dt.axisObjects.y._tickFormat(obj.userData.y);                                                // 405
    html += "</span><br>";                                                                                             // 406
    html += "<span>";                                                                                                  // 407
    html += "z: " + this._dt.axisObjects.z._tickFormat(obj.userData.z);                                                // 408
    html += "</span><br>";                                                                                             // 409
    html += "</div>";                                                                                                  // 410
                                                                                                                       //
    document.getElementById("tooltip-container").innerHTML = html;                                                     // 412
    document.getElementById("tooltip-container").style.display = "block";                                              // 413
                                                                                                                       //
    document.getElementById("tooltip-container").style.top = e.pageY + 10 + "px";                                      // 415
    document.getElementById("tooltip-container").style.left = e.pageX + 10 + "px";                                     // 416
  } else {                                                                                                             //
    document.getElementById("tooltip-container").style.display = "none";                                               // 418
  }                                                                                                                    //
};                                                                                                                     //
                                                                                                                       //
// Scatter plot                                                                                                        //
D3THREE.Scatter = function (dt) {                                                                                      // 423
  this.init(dt);                                                                                                       // 424
                                                                                                                       //
  this._nodeGroup = new THREE.Object3D();                                                                              // 426
                                                                                                                       //
  this._config = { color: 0x4682B4, pointRadius: 5 };                                                                  // 428
};                                                                                                                     //
                                                                                                                       //
D3THREE.Scatter.prototype = new D3THREE.Chart();                                                                       // 431
                                                                                                                       //
D3THREE.Scatter.prototype.onDocumentMouseMove = function (e) {                                                         // 433
  // detect intersected spheres                                                                                        //
  this.detectNodeHover(e);                                                                                             // 435
};                                                                                                                     //
                                                                                                                       //
D3THREE.Scatter.prototype.render = function (data) {                                                                   // 438
  var geometry = new THREE.SphereGeometry(this._config.pointRadius, 32, 32);                                           // 439
                                                                                                                       //
  this._dt.scene.add(this._nodeGroup);                                                                                 // 441
                                                                                                                       //
  // x,y axis shift, so rotation is from center of screen                                                              //
  var xAxisShift = this._dt.axisObjects.x.getRotationShift(),                                                          // 438
      yAxisShift = this._dt.axisObjects.y.getRotationShift();                                                          //
                                                                                                                       //
  var self = this;                                                                                                     // 447
  d3.select(this._nodeGroup).selectAll().data(data).enter().append(function (d) {                                      // 448
    var material = new THREE.MeshBasicMaterial({                                                                       // 452
      color: self._config.color });                                                                                    // 453
    var mesh = new THREE.Mesh(geometry, material);                                                                     // 454
    mesh.userData = { x: d.x, y: d.y, z: d.z };                                                                        // 455
    return mesh;                                                                                                       // 456
  }).attr("position.z", function (d) {                                                                                 //
    return self._dt.axisObjects.x._scale(d.x) - xAxisShift;                                                            // 459
  }).attr("position.x", function (d) {                                                                                 //
    return self._dt.axisObjects.y._scale(d.y) - yAxisShift;                                                            // 462
  }).attr("position.y", function (d) {                                                                                 //
    return self._dt.axisObjects.z._scale(d.z) + chartOffset;                                                           // 465
  });                                                                                                                  //
};                                                                                                                     //
                                                                                                                       //
// Surface plot                                                                                                        //
D3THREE.Surface = function (dt) {                                                                                      // 470
  this.init(dt);                                                                                                       // 471
                                                                                                                       //
  this._nodeGroup = new THREE.Object3D();                                                                              // 473
                                                                                                                       //
  this._config = { color: 0x4682B4, pointColor: 0xff7f0e, pointRadius: 2 };                                            // 475
};                                                                                                                     //
                                                                                                                       //
D3THREE.Surface.prototype = new D3THREE.Chart();                                                                       // 478
                                                                                                                       //
D3THREE.Surface.prototype.onDocumentMouseMove = function (e) {                                                         // 480
  // detect intersected spheres                                                                                        //
  var boundingRect = this._dt.renderer.domElement.getBoundingClientRect();                                             // 482
                                                                                                                       //
  var vector = new THREE.Vector3();                                                                                    // 484
  vector.x = (e.clientX - boundingRect.left) / this._dt.renderer.domElement.width * 2 - 1;                             // 485
  vector.y = 1 - (e.clientY - boundingRect.top) / this._dt.renderer.domElement.height * 2;                             // 486
  vector.z = 1;                                                                                                        // 487
                                                                                                                       //
  // create a check ray                                                                                                //
  vector.unproject(this._dt.camera);                                                                                   // 480
  var ray = new THREE.Raycaster(this._dt.camera.position, vector.sub(this._dt.camera.position).normalize());           // 491
                                                                                                                       //
  var meshIntersects = ray.intersectObjects([this._meshSurface]);                                                      // 494
                                                                                                                       //
  if (meshIntersects.length > 0) {                                                                                     // 496
    for (var i = 0; i < this._nodeGroup.children.length; i++) {                                                        // 497
      this._nodeGroup.children[i].visible = true;                                                                      // 498
      this._nodeGroup.children[i].material.opacity = 1;                                                                // 499
    }                                                                                                                  //
                                                                                                                       //
    this.detectNodeHover(e);                                                                                           // 502
  } else {                                                                                                             //
    // hide nodes                                                                                                      //
    for (var i = 0; i < this._nodeGroup.children.length; i++) {                                                        // 505
      this._nodeGroup.children[i].visible = false;                                                                     // 506
    }                                                                                                                  //
  }                                                                                                                    //
};                                                                                                                     //
                                                                                                                       //
D3THREE.Surface.prototype.render = function (threeData) {                                                              // 511
  /* render data points */                                                                                             //
  var geometry = new THREE.SphereGeometry(this._config.pointRadius, 32, 32);                                           // 513
                                                                                                                       //
  this._dt.scene.add(this._nodeGroup);                                                                                 // 515
                                                                                                                       //
  // x,y axis shift, so rotation is from center of screen                                                              //
  var xAxisShift = this._dt.axisObjects.x.getRotationShift(),                                                          // 511
      yAxisShift = this._dt.axisObjects.y.getRotationShift();                                                          //
                                                                                                                       //
  var self = this;                                                                                                     // 521
  d3.select(this._nodeGroup).selectAll().data(threeData).enter().append(function (d) {                                 // 522
    var material = new THREE.MeshBasicMaterial({                                                                       // 526
      color: self._config.pointColor });                                                                               // 527
    var mesh = new THREE.Mesh(geometry, material);                                                                     // 528
    mesh.userData = { x: d.x, y: d.y, z: d.z };                                                                        // 529
    mesh.visible = false;                                                                                              // 530
    return mesh;                                                                                                       // 531
  }).attr("position.z", function (d) {                                                                                 //
    return self._dt.axisObjects.x._scale(d.x) - xAxisShift;                                                            // 534
  }).attr("position.x", function (d) {                                                                                 //
    return self._dt.axisObjects.y._scale(d.y) - yAxisShift;                                                            // 537
  }).attr("position.y", function (d) {                                                                                 //
    return self._dt.axisObjects.z._scale(d.z) + chartOffset;                                                           // 540
  });                                                                                                                  //
                                                                                                                       //
  /* custom surface */                                                                                                 //
  function distance(v1, v2) {                                                                                          // 511
    var dx = v1.x - v2.x;                                                                                              // 546
    var dy = v1.y - v2.y;                                                                                              // 547
    var dz = v1.z - v2.z;                                                                                              // 548
                                                                                                                       //
    return Math.sqrt(dx * dx + dz * dz);                                                                               // 550
  }                                                                                                                    //
                                                                                                                       //
  var vertices = [];                                                                                                   // 553
  var holes = [];                                                                                                      // 554
  var triangles, mesh;                                                                                                 // 555
  var geometry = new THREE.Geometry();                                                                                 // 556
  var material = new THREE.MeshBasicMaterial({ color: this._config.color });                                           // 557
                                                                                                                       //
  for (var i = 0; i < threeData.length; i++) {                                                                         // 559
    vertices.push(new THREE.Vector3(self._dt.axisObjects.y._scale(threeData[i].y) - yAxisShift, self._dt.axisObjects.z._scale(threeData[i].z) + chartOffset, self._dt.axisObjects.x._scale(threeData[i].x) - xAxisShift));
  }                                                                                                                    //
                                                                                                                       //
  geometry.vertices = vertices;                                                                                        // 566
                                                                                                                       //
  for (var i = 0; i < vertices.length; i++) {                                                                          // 568
    // find three closest vertices to generate surface                                                                 //
    var v1, v2, v3;                                                                                                    // 570
    var distances = [];                                                                                                // 571
                                                                                                                       //
    // find vertices in same y or y + 1 row                                                                            //
    var minY = Number.MAX_VALUE;                                                                                       // 568
    for (var j = i + 1; j < vertices.length; j++) {                                                                    // 575
      if (i !== j && vertices[j].x > vertices[i].x) {                                                                  // 576
        if (vertices[j].x < minY) {                                                                                    // 577
          minY = vertices[j].x;                                                                                        // 578
        }                                                                                                              //
      }                                                                                                                //
    }                                                                                                                  //
                                                                                                                       //
    var rowVertices = [],                                                                                              // 583
        row2Vertices = [];                                                                                             //
    for (var j = i + 1; j < vertices.length; j++) {                                                                    // 584
      if (i !== j && vertices[j].x === vertices[i].x) {                                                                // 585
        rowVertices.push({ index: j, v: vertices[j] });                                                                // 586
      }                                                                                                                //
      if (i !== j && vertices[j].x === minY) {                                                                         // 588
        row2Vertices.push({ index: j, v: vertices[j] });                                                               // 589
      }                                                                                                                //
    }                                                                                                                  //
                                                                                                                       //
    if (rowVertices.length >= 1 && row2Vertices.length >= 2) {                                                         // 593
      // find smallest x                                                                                               //
      rowVertices.sort(function (a, b) {                                                                               // 595
        if (a.v.z < b.v.z) {                                                                                           // 596
          return -1;                                                                                                   // 597
        } else if (a.v.z === b.v.z) {                                                                                  //
          return 0;                                                                                                    // 599
        } else {                                                                                                       //
          return 1;                                                                                                    // 601
        }                                                                                                              //
      });                                                                                                              //
                                                                                                                       //
      v1 = rowVertices[0].index;                                                                                       // 605
                                                                                                                       //
      row2Vertices.sort(function (a, b) {                                                                              // 607
        if (a.v.z < b.v.z) {                                                                                           // 608
          return -1;                                                                                                   // 609
        } else if (a.v.z === b.v.z) {                                                                                  //
          return 0;                                                                                                    // 611
        } else {                                                                                                       //
          return 1;                                                                                                    // 613
        }                                                                                                              //
      });                                                                                                              //
                                                                                                                       //
      v2 = row2Vertices[0].index;                                                                                      // 617
      v3 = row2Vertices[1].index;                                                                                      // 618
                                                                                                                       //
      var fv = [i, v1, v2, v3];                                                                                        // 620
      fv = fv.sort(function (a, b) {                                                                                   // 621
        if (a < b) return -1;else if (a === b) return 0;else return 1;                                                 // 622
      });                                                                                                              //
                                                                                                                       //
      geometry.faces.push(new THREE.Face3(fv[1], fv[0], fv[3]));                                                       // 627
      geometry.faces.push(new THREE.Face3(fv[0], fv[2], fv[3]));                                                       // 628
    }                                                                                                                  //
  }                                                                                                                    //
                                                                                                                       //
  this._meshSurface = new THREE.Mesh(geometry, material);                                                              // 632
  this._dt.scene.add(this._meshSurface);                                                                               // 633
};                                                                                                                     //
                                                                                                                       //
// Bar plot                                                                                                            //
D3THREE.Bar = function (dt) {                                                                                          // 637
  this.init(dt);                                                                                                       // 638
                                                                                                                       //
  this._nodeGroup = new THREE.Object3D();                                                                              // 640
                                                                                                                       //
  this._config = { color: 0x4682B4, barSize: 5 };                                                                      // 642
};                                                                                                                     //
                                                                                                                       //
D3THREE.Bar.prototype = new D3THREE.Chart();                                                                           // 645
                                                                                                                       //
D3THREE.Bar.prototype.onDocumentMouseMove = function (e) {                                                             // 647
  this.detectNodeHover(e);                                                                                             // 648
};                                                                                                                     //
                                                                                                                       //
D3THREE.Bar.prototype.render = function (threeData) {                                                                  // 651
  /* render data points */                                                                                             //
  this._dt.scene.add(this._nodeGroup);                                                                                 // 653
                                                                                                                       //
  // x,y axis shift, so rotation is from center of screen                                                              //
  var xAxisShift = this._dt.axisObjects.x.getRotationShift(),                                                          // 651
      yAxisShift = this._dt.axisObjects.y.getRotationShift();                                                          //
                                                                                                                       //
  var self = this;                                                                                                     // 659
  d3.select(this._nodeGroup).selectAll().data(threeData).enter().append(function (d) {                                 // 660
    var height = self._dt.axisObjects.z._scale(d.z) + chartOffset;                                                     // 664
    var geometry = new THREE.BoxGeometry(self._config.barSize, height, self._config.barSize);                          // 665
    var material = new THREE.MeshBasicMaterial({                                                                       // 666
      color: self._config.color });                                                                                    // 667
    var mesh = new THREE.Mesh(geometry, material);                                                                     // 668
    mesh.userData = { x: d.x, y: d.y, z: d.z };                                                                        // 669
    return mesh;                                                                                                       // 670
  }).attr("position.z", function (d) {                                                                                 //
    return self._dt.axisObjects.x._scale(d.x) - xAxisShift;                                                            // 673
  }).attr("position.x", function (d) {                                                                                 //
    return self._dt.axisObjects.y._scale(d.y) - yAxisShift;                                                            // 676
  }).attr("position.y", function (d) {                                                                                 //
    var height = self._dt.axisObjects.z._scale(d.z) + chartOffset;                                                     // 679
    return height / 2;                                                                                                 // 680
  });                                                                                                                  //
};                                                                                                                     //
                                                                                                                       //
// Force layout plot                                                                                                   //
D3THREE.Force = function (dt) {                                                                                        // 685
  this.init(dt);                                                                                                       // 686
                                                                                                                       //
  this._nodeGroup = new THREE.Object3D();                                                                              // 688
                                                                                                                       //
  this._config = { color: 0x4682B4, linkColor: 0xcccccc, linkWidth: 1 };                                               // 690
};                                                                                                                     //
                                                                                                                       //
D3THREE.Force.prototype = new D3THREE.Chart();                                                                         // 693
                                                                                                                       //
D3THREE.Force.prototype.onDocumentMouseMove = function (e) {};                                                         // 695
                                                                                                                       //
D3THREE.Force.prototype.render = function (threeData) {                                                                // 698
  var spheres = [],                                                                                                    // 699
      three_links = [];                                                                                                //
  // Define the 3d force                                                                                               //
  var force = d3.layout.force3d().nodes(sort_data = []).links(links = []).size([50, 50]).gravity(0.3).charge(-400);    // 698
                                                                                                                       //
  var DISTANCE = 1;                                                                                                    // 708
                                                                                                                       //
  for (var i = 0; i < threeData.nodes.length; i++) {                                                                   // 710
    sort_data.push({ x: threeData.nodes.x + DISTANCE, y: threeData.nodes.y + DISTANCE, z: 0 });                        // 711
                                                                                                                       //
    // set up the sphere vars                                                                                          //
    var radius = 5,                                                                                                    // 710
        segments = 16,                                                                                                 //
        rings = 16;                                                                                                    //
                                                                                                                       //
    // create the sphere's material                                                                                    //
    var sphereMaterial = new THREE.MeshLambertMaterial({ color: this._config.color });                                 // 710
                                                                                                                       //
    var sphere = new THREE.Mesh(new THREE.SphereGeometry(radius, segments, rings), sphereMaterial);                    // 721
                                                                                                                       //
    spheres.push(sphere);                                                                                              // 728
                                                                                                                       //
    // add the sphere to the scene                                                                                     //
    this._dt.scene.add(sphere);                                                                                        // 710
  }                                                                                                                    //
                                                                                                                       //
  for (var i = 0; i < threeData.links.length; i++) {                                                                   // 734
    links.push({ target: sort_data[threeData.links[i].target], source: sort_data[threeData.links[i].source] });        // 735
                                                                                                                       //
    var material = new THREE.LineBasicMaterial({ color: this._config.linkColor,                                        // 737
      linewidth: this._config.linkWidth });                                                                            // 738
    var geometry = new THREE.Geometry();                                                                               // 739
                                                                                                                       //
    geometry.vertices.push(new THREE.Vector3(0, 0, 0));                                                                // 741
    geometry.vertices.push(new THREE.Vector3(0, 0, 0));                                                                // 742
    var line = new THREE.Line(geometry, material);                                                                     // 743
    line.userData = { source: threeData.links[i].source,                                                               // 744
      target: threeData.links[i].target };                                                                             // 745
    three_links.push(line);                                                                                            // 746
    this._dt.scene.add(line);                                                                                          // 747
                                                                                                                       //
    force.start();                                                                                                     // 749
  }                                                                                                                    //
                                                                                                                       //
  // set up the axes                                                                                                   //
  var x = d3.scale.linear().domain([0, 350]).range([0, 10]),                                                           // 698
      y = d3.scale.linear().domain([0, 350]).range([0, 10]),                                                           //
      z = d3.scale.linear().domain([0, 350]).range([0, 10]);                                                           //
                                                                                                                       //
  var self = this;                                                                                                     // 757
  force.on("tick", function (e) {                                                                                      // 758
    for (var i = 0; i < sort_data.length; i++) {                                                                       // 759
      spheres[i].position.set(x(sort_data[i].x) * 40 - 40, y(sort_data[i].y) * 40 - 40, z(sort_data[i].z) * 40 - 40);  // 760
                                                                                                                       //
      for (var j = 0; j < three_links.length; j++) {                                                                   // 762
        var line = three_links[j];                                                                                     // 763
        var vi = -1;                                                                                                   // 764
        if (line.userData.source === i) {                                                                              // 765
          vi = 0;                                                                                                      // 766
        }                                                                                                              //
        if (line.userData.target === i) {                                                                              // 768
          vi = 1;                                                                                                      // 769
        }                                                                                                              //
                                                                                                                       //
        if (vi >= 0) {                                                                                                 // 772
          line.geometry.vertices[vi].x = x(sort_data[i].x) * 40 - 40;                                                  // 773
          line.geometry.vertices[vi].y = y(sort_data[i].y) * 40 - 40;                                                  // 774
          line.geometry.vertices[vi].z = y(sort_data[i].z) * 40 - 40;                                                  // 775
          line.geometry.verticesNeedUpdate = true;                                                                     // 776
        }                                                                                                              //
      }                                                                                                                //
    }                                                                                                                  //
  });                                                                                                                  //
};                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"jquery.multilevelpushmenu.js":["babel-runtime/helpers/typeof",function(require){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/lib/jquery.multilevelpushmenu.js                                                                             //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
var _typeof2 = require('babel-runtime/helpers/typeof');                                                                //
                                                                                                                       //
var _typeof3 = _interopRequireDefault(_typeof2);                                                                       //
                                                                                                                       //
function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }                      //
                                                                                                                       //
/**                                                                                                                    //
 * jquery.multilevelpushmenu.js v2.1.4                                                                                 //
 *                                                                                                                     //
 * Licensed under the MIT license.                                                                                     //
 * http://www.opensource.org/licenses/mit-license.php                                                                  //
 *                                                                                                                     //
 * Copyright 2013-2014, Make IT d.o.o.                                                                                 //
 * http://multi-level-push-menu.make.rs                                                                                //
 * https://github.com/adgsm/multi-level-push-menu                                                                      //
 */                                                                                                                    //
(function ($) {                                                                                                        // 11
	$.fn.multilevelpushmenu = function (options) {                                                                        // 12
		"use strict";                                                                                                        // 13
                                                                                                                       //
		var args = arguments,                                                                                                // 14
		    returnValue = null;                                                                                              //
                                                                                                                       //
		this.each(function () {                                                                                              // 17
			var instance = this,                                                                                                // 18
			    $this = $(this),                                                                                                //
			    $container = $this.context != undefined ? $this : $('body'),                                                    //
			    menu = options && options.menu != undefined ? options.menu : $this.find('nav'),                                 //
			    clickEventType,                                                                                                 //
			    dragEventType;                                                                                                  //
                                                                                                                       //
			// Settings                                                                                                         //
			var settings = $.extend({                                                                                           // 17
				container: $container,                                                                                             // 26
				containersToPush: null,                                                                                            // 27
				menuID: ($container.prop('id') != undefined && $container.prop('id') != '' ? $container.prop('id') : this.nodeName.toLowerCase()) + "_multilevelpushmenu",
				wrapperClass: 'multilevelpushmenu_wrapper',                                                                        // 29
				menuInactiveClass: 'multilevelpushmenu_inactive',                                                                  // 30
				menu: menu,                                                                                                        // 31
				menuWidth: 0,                                                                                                      // 32
				menuHeight: 0,                                                                                                     // 33
				collapsed: false,                                                                                                  // 34
				fullCollapse: false,                                                                                               // 35
				direction: 'ltr',                                                                                                  // 36
				backText: 'Back',                                                                                                  // 37
				backItemClass: 'backItemClass',                                                                                    // 38
				backItemIcon: 'fa fa-angle-right',                                                                                 // 39
				groupIcon: 'fa fa-angle-left',                                                                                     // 40
				mode: 'overlap',                                                                                                   // 41
				overlapWidth: 40,                                                                                                  // 42
				preventItemClick: true,                                                                                            // 43
				preventGroupItemClick: true,                                                                                       // 44
				swipe: 'both',                                                                                                     // 45
				durationSlideOut: 400,                                                                                             // 46
				durationSlideDown: 500,                                                                                            // 47
				durationTransition: 400,                                                                                           // 48
				onCollapseMenuStart: function () {                                                                                 // 49
					function onCollapseMenuStart() {}                                                                                 // 49
                                                                                                                       //
					return onCollapseMenuStart;                                                                                       //
				}(),                                                                                                               //
				onCollapseMenuEnd: function () {                                                                                   // 50
					function onCollapseMenuEnd() {}                                                                                   // 50
                                                                                                                       //
					return onCollapseMenuEnd;                                                                                         //
				}(),                                                                                                               //
				onExpandMenuStart: function () {                                                                                   // 51
					function onExpandMenuStart() {}                                                                                   // 51
                                                                                                                       //
					return onExpandMenuStart;                                                                                         //
				}(),                                                                                                               //
				onExpandMenuEnd: function () {                                                                                     // 52
					function onExpandMenuEnd() {}                                                                                     // 52
                                                                                                                       //
					return onExpandMenuEnd;                                                                                           //
				}(),                                                                                                               //
				onGroupItemClick: function () {                                                                                    // 53
					function onGroupItemClick() {}                                                                                    // 53
                                                                                                                       //
					return onGroupItemClick;                                                                                          //
				}(),                                                                                                               //
				onItemClick: function () {                                                                                         // 54
					function onItemClick() {}                                                                                         // 54
                                                                                                                       //
					return onItemClick;                                                                                               //
				}(),                                                                                                               //
				onTitleItemClick: function () {                                                                                    // 55
					function onTitleItemClick() {}                                                                                    // 55
                                                                                                                       //
					return onTitleItemClick;                                                                                          //
				}(),                                                                                                               //
				onBackItemClick: function () {                                                                                     // 56
					function onBackItemClick() {}                                                                                     // 56
                                                                                                                       //
					return onBackItemClick;                                                                                           //
				}(),                                                                                                               //
				onMenuReady: function () {                                                                                         // 57
					function onMenuReady() {}                                                                                         // 57
                                                                                                                       //
					return onMenuReady;                                                                                               //
				}(),                                                                                                               //
				onMenuSwipe: function () {                                                                                         // 58
					function onMenuSwipe() {}                                                                                         // 58
                                                                                                                       //
					return onMenuSwipe;                                                                                               //
				}()                                                                                                                //
			}, options);                                                                                                        //
                                                                                                                       //
			// Store a settings reference withint the element's data                                                            //
			if (!$.data(instance, 'plugin_multilevelpushmenu')) {                                                               // 17
				$.data(instance, 'plugin_multilevelpushmenu', settings);                                                           // 63
				instance.settings = $.data(instance, 'plugin_multilevelpushmenu');                                                 // 64
			}                                                                                                                   //
                                                                                                                       //
			// Exposed methods                                                                                                  //
			var methods = {                                                                                                     // 17
				// Initialize menu                                                                                                 //
				init: function () {                                                                                                // 70
					function init() {                                                                                                 // 70
						return initialize.apply(this, Array.prototype.slice.call(arguments));                                            // 71
					}                                                                                                                 //
                                                                                                                       //
					return init;                                                                                                      //
				}(),                                                                                                               //
				// Collapse menu                                                                                                   //
				collapse: function () {                                                                                            // 74
					function collapse() {                                                                                             // 74
						return collapseMenu.apply(this, Array.prototype.slice.call(arguments));                                          // 75
					}                                                                                                                 //
                                                                                                                       //
					return collapse;                                                                                                  //
				}(),                                                                                                               //
				// Expand menu                                                                                                     //
				expand: function () {                                                                                              // 78
					function expand() {                                                                                               // 78
						return expandMenu.apply(this, Array.prototype.slice.call(arguments));                                            // 79
					}                                                                                                                 //
                                                                                                                       //
					return expand;                                                                                                    //
				}(),                                                                                                               //
				// Menu expanded                                                                                                   //
				menuexpanded: function () {                                                                                        // 82
					function menuexpanded() {                                                                                         // 82
						return menuExpanded.apply(this, Array.prototype.slice.call(arguments));                                          // 83
					}                                                                                                                 //
                                                                                                                       //
					return menuexpanded;                                                                                              //
				}(),                                                                                                               //
				// Active menu                                                                                                     //
				activemenu: function () {                                                                                          // 86
					function activemenu() {                                                                                           // 86
						return activeMenu.apply(this, Array.prototype.slice.call(arguments));                                            // 87
					}                                                                                                                 //
                                                                                                                       //
					return activemenu;                                                                                                //
				}(),                                                                                                               //
				// Find menu(s) by title                                                                                           //
				findmenusbytitle: function () {                                                                                    // 90
					function findmenusbytitle() {                                                                                     // 90
						return findMenusByTitle.apply(this, Array.prototype.slice.call(arguments));                                      // 91
					}                                                                                                                 //
                                                                                                                       //
					return findmenusbytitle;                                                                                          //
				}(),                                                                                                               //
				// Find item(s) by name                                                                                            //
				finditemsbyname: function () {                                                                                     // 94
					function finditemsbyname() {                                                                                      // 94
						return findItemsByName.apply(this, Array.prototype.slice.call(arguments));                                       // 95
					}                                                                                                                 //
                                                                                                                       //
					return finditemsbyname;                                                                                           //
				}(),                                                                                                               //
				// Find path to root menu collection                                                                               //
				pathtoroot: function () {                                                                                          // 98
					function pathtoroot() {                                                                                           // 98
						return pathToRoot.apply(this, Array.prototype.slice.call(arguments));                                            // 99
					}                                                                                                                 //
                                                                                                                       //
					return pathtoroot;                                                                                                //
				}(),                                                                                                               //
				// Find shared path to root of two menus                                                                           //
				comparepaths: function () {                                                                                        // 102
					function comparepaths() {                                                                                         // 102
						return comparePaths.apply(this, Array.prototype.slice.call(arguments));                                          // 103
					}                                                                                                                 //
                                                                                                                       //
					return comparepaths;                                                                                              //
				}(),                                                                                                               //
				// Get/Set settings options                                                                                        //
				option: function () {                                                                                              // 106
					function option() {                                                                                               // 106
						return manageOptions.apply(this, Array.prototype.slice.call(arguments));                                         // 107
					}                                                                                                                 //
                                                                                                                       //
					return option;                                                                                                    //
				}(),                                                                                                               //
				// Add item(s)                                                                                                     //
				additems: function () {                                                                                            // 110
					function additems() {                                                                                             // 110
						return addItems.apply(this, Array.prototype.slice.call(arguments));                                              // 111
					}                                                                                                                 //
                                                                                                                       //
					return additems;                                                                                                  //
				}(),                                                                                                               //
				// Remove item(s)                                                                                                  //
				removeitems: function () {                                                                                         // 114
					function removeitems() {                                                                                          // 114
						return removeItems.apply(this, Array.prototype.slice.call(arguments));                                           // 115
					}                                                                                                                 //
                                                                                                                       //
					return removeitems;                                                                                               //
				}(),                                                                                                               //
				// Size DOM elements                                                                                               //
				redraw: function () {                                                                                              // 118
					function redraw() {                                                                                               // 118
						return sizeDOMelements.apply(this, Array.prototype.slice.call(arguments));                                       // 119
					}                                                                                                                 //
                                                                                                                       //
					return redraw;                                                                                                    //
				}(),                                                                                                               //
				// Returns visible level holders                                                                                   //
				visiblemenus: function () {                                                                                        // 122
					function visiblemenus() {                                                                                         // 122
						return visibleLevelHolders.apply(this, Array.prototype.slice.call(arguments));                                   // 123
					}                                                                                                                 //
                                                                                                                       //
					return visiblemenus;                                                                                              //
				}(),                                                                                                               //
				// Returns visible level holders                                                                                   //
				hiddenmenus: function () {                                                                                         // 126
					function hiddenmenus() {                                                                                          // 126
						return hiddenLevelHolders.apply(this, Array.prototype.slice.call(arguments));                                    // 127
					}                                                                                                                 //
                                                                                                                       //
					return hiddenmenus;                                                                                               //
				}(),                                                                                                               //
				// Propagate event to underneath layer                                                                             //
				propagateevent: function () {                                                                                      // 130
					function propagateevent() {                                                                                       // 130
						return propagateEvent.apply(this, Array.prototype.slice.call(arguments));                                        // 131
					}                                                                                                                 //
                                                                                                                       //
					return propagateevent;                                                                                            //
				}()                                                                                                                //
			};                                                                                                                  //
                                                                                                                       //
			// IE 8 and modern browsers, prevent event propagation                                                              //
			function stopEventPropagation(e) {                                                                                  // 17
				if (e.stopPropagation && e.preventDefault) {                                                                       // 137
					e.stopPropagation();                                                                                              // 138
					e.preventDefault();                                                                                               // 139
				} else {                                                                                                           //
					e.cancelBubble = true;                                                                                            // 142
					e.returnValue = false;                                                                                            // 143
				}                                                                                                                  //
			}                                                                                                                   //
                                                                                                                       //
			// propagate event to underneath layer                                                                              //
			// http://jsfiddle.net/E9zTs/2/                                                                                     //
			function propagateEvent($element, event) {                                                                          // 17
				if ($element == undefined || event == undefined) return false;                                                     // 150
				$element.on(event, function (e, ee) {                                                                              // 151
					$element.hide();                                                                                                  // 152
					try {                                                                                                             // 153
						if (!e.pageX || !e.pageY) return false;                                                                          // 154
						ee = ee || {                                                                                                     // 155
							pageX: e.pageX,                                                                                                 // 156
							pageY: e.pageY                                                                                                  // 157
						};                                                                                                               //
						var next = document.elementFromPoint(ee.pageX, ee.pageY);                                                        // 159
						next = next.nodeType == 3 ? next.parentNode : next; //Opera                                                      // 160
						$(next).trigger(event, ee);                                                                                      // 153
					} catch (err) {                                                                                                   //
						$.error('Error while propagating event: ' + err.message);                                                        // 164
					} finally {                                                                                                       //
						$element.show();                                                                                                 // 167
					}                                                                                                                 //
				});                                                                                                                //
			}                                                                                                                   //
                                                                                                                       //
			// Create DOM structure if it does not already exist within the container (input: array)                            //
			function createDOMStructure() {                                                                                     // 17
				var $mainWrapper = $("<nav />").prop({ "id": instance.settings.menuID, "className": instance.settings.wrapperClass }).appendTo(instance.settings.container);
				createNestedDOMStructure(instance.settings.menu, $mainWrapper);                                                    // 177
			}                                                                                                                   //
			function createNestedDOMStructure(menus, $wrapper) {                                                                // 179
				if (menus.level == undefined) menus.level = 0;                                                                     // 180
				$.each(menus, function () {                                                                                        // 181
					var $levelHolder = $("<div />").attr({ "class": "levelHolderClass" + (instance.settings.direction == 'rtl' ? " rtl" : " ltr"), "data-level": menus.level, "style": (instance.settings.direction == 'rtl' ? "margin-right: " : "margin-left: ") + (menus.level == 0 && !instance.settings.collapsed ? 0 : "-200%") }).appendTo($wrapper),
					    extWidth = isValidDim(instance.settings.menuWidth) || isInt(instance.settings.menuWidth) && instance.settings.menuWidth > 0;
					$levelHolder.bind(dragEventType, function (e) {                                                                   // 186
						holderSwipe(e, $levelHolder);                                                                                    // 187
					});                                                                                                               //
					if (this.id != undefined) $levelHolder.attr({ "id": this.id });                                                   // 189
					var $title = $("<h2 />").attr({ "style": "text-align: " + (instance.settings.direction == 'rtl' ? "right" : "left") }).text(this.title).appendTo($levelHolder),
					    $titleIcon = $("<i />").prop({ "class": (instance.settings.direction == 'rtl' ? "floatLeft" : "floatRight") + " cursorPointer " + this.icon }).prependTo($title);
					$titleIcon.bind(clickEventType, function (e) {                                                                    // 197
						titleIconClick(e, $levelHolder, menus);                                                                          // 198
					});                                                                                                               //
					if (menus.level > 0) createBackItem($levelHolder);                                                                // 200
					var $itemGroup = $("<ul />").appendTo($levelHolder);                                                              // 201
					$.each(this.items, function () {                                                                                  // 203
						createItem(this, $levelHolder, -1);                                                                              // 204
					});                                                                                                               //
				});                                                                                                                //
			}                                                                                                                   //
                                                                                                                       //
			// Update DOM structure if it already exists in container (input: HTML markup)                                      //
			function updateDOMStructure() {                                                                                     // 17
				var $mainWrapper = instance.settings.container.find('nav').length > 0 ? instance.settings.container.find('nav') : instance.settings.menu;
				if ($mainWrapper.length == 0) return false;                                                                        // 212
				$mainWrapper.prop({ "id": instance.settings.menuID, "className": instance.settings.wrapperClass });                // 213
				updateNestedDOMStructure($mainWrapper);                                                                            // 214
			}                                                                                                                   //
			function updateNestedDOMStructure($wrapper) {                                                                       // 216
				if ($wrapper.level == undefined) $wrapper.level = 0;                                                               // 217
				$.each($wrapper, function () {                                                                                     // 218
					var $levelHolder = $("<div />").attr({ "class": "levelHolderClass" + (instance.settings.direction == 'rtl' ? " rtl" : " ltr"), "data-level": $wrapper.level, "style": (instance.settings.direction == 'rtl' ? "margin-right: " : "margin-left: ") + ($wrapper.level == 0 && !instance.settings.collapsed ? 0 : "-200%") }).appendTo($wrapper),
					    extWidth = isValidDim(instance.settings.menuWidth) || isInt(instance.settings.menuWidth) && instance.settings.menuWidth > 0;
					$levelHolder.bind(dragEventType, function (e) {                                                                   // 223
						holderSwipe(e, $levelHolder);                                                                                    // 224
					});                                                                                                               //
					var $title = $wrapper.children('h2');                                                                             // 226
					$title.attr({ "style": "text-align: " + (instance.settings.direction == 'rtl' ? "right" : "left") });             // 227
					$title.appendTo($levelHolder);                                                                                    // 228
					var $titleIcon = $title.children('i');                                                                            // 229
					$titleIcon.addClass((instance.settings.direction == 'rtl' ? "floatLeft" : "floatRight") + " cursorPointer");      // 230
					$titleIcon.bind(clickEventType, function (e) {                                                                    // 231
						titleIconClick(e, $levelHolder, $wrapper);                                                                       // 232
					});                                                                                                               //
					if ($wrapper.level > 0) createBackItem($levelHolder);                                                             // 234
					var $itemGroup = $wrapper.children('ul');                                                                         // 235
					$itemGroup.appendTo($levelHolder);                                                                                // 236
					$.each($itemGroup.children('li'), function () {                                                                   // 237
						var $item = $(this);                                                                                             // 238
						$item.attr({ "style": "text-align: " + (instance.settings.direction == 'rtl' ? "right" : "left") });             // 239
						var $itemAnchor = $item.children('a');                                                                           // 240
						var $itemIcon = $itemAnchor.children('i');                                                                       // 241
						$itemIcon.addClass(instance.settings.direction == 'rtl' ? "floatLeft" : "floatRight");                           // 242
						if ($item.children('ul').length > 0) {                                                                           // 243
							$itemAnchor.bind(clickEventType, function (e) {                                                                 // 244
								itemGroupAnchorClick(e, $levelHolder, $item);                                                                  // 245
							});                                                                                                             //
							createItemGroupIcon($itemAnchor);                                                                               // 247
							$item.level = $wrapper.level + 1;                                                                               // 248
							updateNestedDOMStructure($item);                                                                                // 249
						} else {                                                                                                         //
							$itemAnchor.bind(clickEventType, function (e) {                                                                 // 251
								itemAnchorClick(e, $levelHolder, $item);                                                                       // 252
							});                                                                                                             //
						}                                                                                                                //
					});                                                                                                               //
				});                                                                                                                //
			}                                                                                                                   //
                                                                                                                       //
			// Click event for title icon                                                                                       //
			function titleIconClick(e, $levelHolder, menus) {                                                                   // 17
				if ($(instance).find('div.levelHolderClass').is(':animated')) return false;                                        // 261
				instance.settings.onTitleItemClick.apply(this, Array.prototype.slice.call([e, $levelHolder, instance.settings]));  // 262
				stopEventPropagation(e);                                                                                           // 263
				var instanceFC = instance.settings.direction == 'rtl' ? parseInt($levelHolder.css('margin-right')) < 0 : parseInt($levelHolder.css('margin-left')) < 0;
				if (menus.level == 0 && instanceFC) {                                                                              // 268
					expandMenu();                                                                                                     // 269
				} else {                                                                                                           //
					var $nextLevelHolders = instance.settings.container.find('#' + instance.settings.menuID + ' div.levelHolderClass').filter(function () {
						var retObjs = instance.settings.direction == 'rtl' ? $(this).attr('data-level') > $levelHolder.attr('data-level') && parseInt($(this).css('margin-right')) >= 0 : $(this).attr('data-level') > $levelHolder.attr('data-level') && parseInt($(this).css('margin-left')) >= 0;
						return retObjs;                                                                                                  // 279
					}),                                                                                                               //
					    $prevLevelHolders = instance.settings.container.find('#' + instance.settings.menuID + ' div.levelHolderClass').filter(function () {
						var retObjs = instance.settings.direction == 'rtl' ? $(this).attr('data-level') <= $levelHolder.attr('data-level') && parseInt($(this).css('margin-right')) >= 0 : $(this).attr('data-level') <= $levelHolder.attr('data-level') && parseInt($(this).css('margin-left')) >= 0;
						return retObjs;                                                                                                  // 288
					}),                                                                                                               //
					    collapseAll = $nextLevelHolders.length == 0 && $prevLevelHolders.length == 1 ? collapseMenu() : collapseMenu(parseInt($levelHolder.attr('data-level')));
				}                                                                                                                  //
				$levelHolder.css('visibility', 'visible');                                                                         // 292
				$levelHolder.find('.' + instance.settings.backItemClass).css('visibility', 'visible');                             // 293
				$levelHolder.find('ul').css('visibility', 'visible');                                                              // 294
				$levelHolder.removeClass(instance.settings.menuInactiveClass);                                                     // 295
			}                                                                                                                   //
                                                                                                                       //
			// Create Back item DOM elements                                                                                    //
			function createBackItem($levelHolder) {                                                                             // 17
				var $backItem = $("<div />").attr({ "class": instance.settings.backItemClass }).appendTo($levelHolder),            // 300
				    $backItemAnchor = $("<a />").prop({ "href": "#" }).text(instance.settings.backText).appendTo($backItem),       //
				    $backItemIcon = $("<i />").prop({ "class": (instance.settings.direction == 'rtl' ? "floatLeft " : "floatRight ") + instance.settings.backItemIcon }).prependTo($backItemAnchor);
				$backItemAnchor.bind(clickEventType, function (e) {                                                                // 310
					backItemAnchorClick(e, $levelHolder);                                                                             // 311
				});                                                                                                                //
			}                                                                                                                   //
                                                                                                                       //
			// Click event for back item                                                                                        //
			function backItemAnchorClick(e, $levelHolder) {                                                                     // 17
				if ($(instance).find('div.levelHolderClass').is(':animated')) return false;                                        // 317
				instance.settings.onBackItemClick.apply(this, Array.prototype.slice.call([e, $levelHolder, instance.settings]));   // 318
				stopEventPropagation(e);                                                                                           // 319
				collapseMenu(parseInt($levelHolder.attr('data-level') - 1));                                                       // 320
			}                                                                                                                   //
                                                                                                                       //
			// Click event for group items                                                                                      //
			function itemGroupAnchorClick(e, $levelHolder, $item) {                                                             // 17
				if ($(instance).find('div.levelHolderClass').is(':animated')) return false;                                        // 325
				instance.settings.onGroupItemClick.apply(this, Array.prototype.slice.call([e, $levelHolder, $item, instance.settings]));
				expandMenu($item.find('div:first'));                                                                               // 327
				if (instance.settings.preventGroupItemClick) stopEventPropagation(e);                                              // 328
			}                                                                                                                   //
                                                                                                                       //
			// Create item group DOM element                                                                                    //
			function createItemGroupIcon($itemAnchor) {                                                                         // 17
				var $itemGroupIcon = $("<i />").attr({ "class": (instance.settings.direction == 'rtl' ? " floatRight iconSpacing_rtl " : " floatLeft iconSpacing_ltr ") + instance.settings.groupIcon }).prependTo($itemAnchor);
			}                                                                                                                   //
                                                                                                                       //
			// Create item DOM element                                                                                          //
			function createItem() {                                                                                             // 17
				var item = arguments[0],                                                                                           // 340
				    $levelHolder = arguments[1],                                                                                   //
				    position = arguments[2],                                                                                       //
				    $itemGroup = $levelHolder.find('ul:first'),                                                                    //
				    $item = $("<li />");                                                                                           //
				position < $itemGroup.children('li').length && position >= 0 ? $item.insertBefore($itemGroup.children('li').eq(position)) : $item.appendTo($itemGroup);
				$item.attr({ "style": "text-align: " + (instance.settings.direction == 'rtl' ? "right" : "left") });               // 347
				if (item.id != undefined) $item.attr({ "id": item.id });                                                           // 348
				var $itemAnchor = $("<a />").prop({ "href": item.link }).text(item.name).appendTo($item),                          // 349
				    $itemIcon = $("<i />").prop({ "class": (instance.settings.direction == 'rtl' ? "floatLeft " : "floatRight ") + item.icon }).prependTo($itemAnchor);
				if (item.items) {                                                                                                  // 356
					$itemAnchor.bind(clickEventType, function (e) {                                                                   // 357
						itemGroupAnchorClick(e, $levelHolder, $item);                                                                    // 358
					});                                                                                                               //
					createItemGroupIcon($itemAnchor);                                                                                 // 360
					item.items.level = parseInt($levelHolder.attr('data-level'), 10) + 1;                                             // 361
					createNestedDOMStructure(item.items, $item);                                                                      // 362
				} else {                                                                                                           //
					$itemAnchor.bind(clickEventType, function (e) {                                                                   // 364
						itemAnchorClick(e, $levelHolder, $item);                                                                         // 365
					});                                                                                                               //
				}                                                                                                                  //
			}                                                                                                                   //
                                                                                                                       //
			// Click event for items                                                                                            //
			function itemAnchorClick(e, $levelHolder, $item) {                                                                  // 17
				instance.settings.onItemClick.apply(this, Array.prototype.slice.call([e, $levelHolder, $item, instance.settings]));
				if (instance.settings.preventItemClick) stopEventPropagation(e);                                                   // 373
			}                                                                                                                   //
                                                                                                                       //
			// Swipe/Drag event for holders                                                                                     //
			function holderSwipe(emd, $levelHolder) {                                                                           // 17
				var extRes = instance.settings.onMenuSwipe.apply(this, Array.prototype.slice.call([emd, $levelHolder, instance.settings]));
				if (extRes == false) return false;                                                                                 // 379
				if ($(instance).find('div.levelHolderClass').is(':animated')) return false;                                        // 380
				var level = $levelHolder.attr('data-level') > 0 ? $levelHolder.attr('data-level') - 1 : undefined;                 // 381
				if (emd.type == 'touchmove' && instance.settings.swipe != 'desktop') {                                             // 382
					stopEventPropagation(emd);                                                                                        // 383
					emd = emd.touches ? emd : emd.originalEvent;                                                                      // 384
					if (!emd.touches || emd.touches.length <= 0) return false;                                                        // 385
					var touch = emd.touches[0];                                                                                       // 386
					instance.settings.container.unbind('touchend');                                                                   // 387
					instance.settings.container.bind('touchend', function (emm) {                                                     // 388
						stopEventPropagation(emm);                                                                                       // 389
						$levelHolder.significance = 0;                                                                                   // 390
						$levelHolder.swipeStart = 0;                                                                                     // 391
						instance.settings.container.unbind('touchend');                                                                  // 392
					});                                                                                                               //
					if ($levelHolder.swipeStart != undefined && $levelHolder.swipeStart != 0) {                                       // 394
						$levelHolder.significance = touch.pageX - $levelHolder.swipeStart;                                               // 395
					} else {                                                                                                          //
						$levelHolder.significance = 0;                                                                                   // 398
						$levelHolder.swipeStart = touch.pageX;                                                                           // 399
						return true;                                                                                                     // 400
					}                                                                                                                 //
					if (Math.abs($levelHolder.significance) > instance.settings.overlapWidth * .3) {                                  // 402
						if (instance.settings.direction == 'rtl') $levelHolder.significance *= -1;                                       // 403
						$levelHolder.significance > 0 ? expandMenu(level == undefined ? level : $levelHolder) : collapseMenu(level);     // 404
						$levelHolder.significance = 0;                                                                                   // 405
						$levelHolder.swipeStart = 0;                                                                                     // 406
					}                                                                                                                 //
				} else if (instance.settings.swipe != 'touchscreen') {                                                             //
					stopEventPropagation(emd);                                                                                        // 410
					var significance = 0;                                                                                             // 411
					$levelHolder.unbind('mousemove');                                                                                 // 412
					$levelHolder.bind('mousemove', function (emm) {                                                                   // 413
						significance = emm.clientX - emd.clientX;                                                                        // 414
						if (Math.abs(significance) > instance.settings.overlapWidth * .3) {                                              // 415
							$levelHolder.unbind('mousemove');                                                                               // 416
							if (instance.settings.direction == 'rtl') significance *= -1;                                                   // 417
							significance > 0 ? expandMenu(level == undefined ? level : $levelHolder) : collapseMenu(level);                 // 418
							return true;                                                                                                    // 419
						}                                                                                                                //
					});                                                                                                               //
					instance.settings.container.unbind('mouseup');                                                                    // 422
					instance.settings.container.bind('mouseup', function (e) {                                                        // 423
						stopEventPropagation(e);                                                                                         // 424
						$levelHolder.unbind('mousemove');                                                                                // 425
						instance.settings.container.unbind('mouseup');                                                                   // 426
					});                                                                                                               //
				}                                                                                                                  //
			}                                                                                                                   //
                                                                                                                       //
			// Returns visible level holders                                                                                    //
			function visibleLevelHolders() {                                                                                    // 17
				var $visibleLevelHolders = instance.settings.container.find('#' + instance.settings.menuID + ' div.levelHolderClass').filter(function () {
					var retObjs = instance.settings.direction == 'rtl' ? parseInt($(this).css('margin-right')) >= 0 && $(this).position().left < instance.settings.container.width() - instance.settings.overlapWidth : parseInt($(this).css('margin-left')) >= 0 && $(this).position().left >= 0;
					return retObjs;                                                                                                   // 440
				});                                                                                                                //
				if ($visibleLevelHolders.length < 1) $visibleLevelHolders = false;                                                 // 442
				return $visibleLevelHolders;                                                                                       // 443
			}                                                                                                                   //
                                                                                                                       //
			// Returns hidden level holders                                                                                     //
			function hiddenLevelHolders() {                                                                                     // 17
				var $hiddenLevelHolders = instance.settings.container.find('#' + instance.settings.menuID + ' div.levelHolderClass').filter(function () {
					var retObjs = instance.settings.direction == 'rtl' ? $(this).position().left > instance.settings.container.width() || parseInt($(this).css('margin-right')) < 0 : $(this).position().left < 0 || parseInt($(this).css('margin-left')) < 0;
					return retObjs;                                                                                                   // 455
				});                                                                                                                //
				if ($hiddenLevelHolders.length < 1) $hiddenLevelHolders = false;                                                   // 457
				return $hiddenLevelHolders;                                                                                        // 458
			}                                                                                                                   //
                                                                                                                       //
			// Sizing DOM elements per creation/update                                                                          //
			function sizeDOMelements() {                                                                                        // 17
				if (!instance.redraw) {                                                                                            // 463
					instance.redraw = true;                                                                                           // 464
					var forceWidth = arguments[0],                                                                                    // 465
					    forceHeight = arguments[1],                                                                                   //
					    filter = arguments[2],                                                                                        //
					    ieShadowFilterDistortion = $('#' + instance.settings.menuID + ' div.levelHolderClass').first().css('filter').match(/DXImageTransform\.Microsoft\.Shadow/) ? $('#' + instance.settings.menuID + ' div.levelHolderClass').first().get(0).filters.item("DXImageTransform.Microsoft.Shadow").strength : 0,
					    maxWidth = forceWidth == undefined ? Math.max.apply(null, $('#' + instance.settings.menuID + ' div.levelHolderClass').map(function () {
						return $(this).width();                                                                                          // 470
					}).get()) - ieShadowFilterDistortion : forceWidth - ieShadowFilterDistortion,                                     //
					    maxLevel = Math.max.apply(null, $('#' + instance.settings.menuID + ' div.levelHolderClass').map(function () {
						return $(this).attr('data-level');                                                                               // 472
					}).get()),                                                                                                        //
					    extWidth = isValidDim(instance.settings.menuWidth) || isInt(instance.settings.menuWidth) && instance.settings.menuWidth > 0,
					    extHeight = isValidDim(instance.settings.menuHeight) || isInt(instance.settings.menuHeight) && instance.settings.menuHeight > 0,
					    $objects = filter == undefined ? $('#' + instance.settings.menuID + ' div.levelHolderClass') : filter,        //
					    currWidth;                                                                                                    //
					if (!extWidth && instance.menuWidth != undefined) maxWidth = instance.menuWidth;                                  // 477
					extWidth && forceWidth == undefined ? $objects.width(instance.settings.menuWidth) : $objects.width(maxWidth);     // 478
					if (extWidth) {                                                                                                   // 479
						if (($objects.width() == 0 || isValidDim(instance.settings.menuWidth) && instance.settings.menuWidth.indexOf('%') != -1) && forceWidth == undefined) {
							$objects.css('min-width', '');                                                                                  // 481
							$objects.width(parseInt(instance.settings.container.parent().width() * parseInt(instance.settings.menuWidth) / 100));
						};                                                                                                               //
						maxWidth = $objects.width() - ieShadowFilterDistortion;                                                          // 484
						$objects.css('min-width', $objects.width() - ieShadowFilterDistortion + 'px');                                   // 485
					}                                                                                                                 //
					var maxExtWidth = extWidth && forceWidth == undefined ? $objects.width() - ieShadowFilterDistortion + maxLevel * (instance.settings.overlapWidth + ieShadowFilterDistortion) : maxWidth + maxLevel * (instance.settings.overlapWidth + ieShadowFilterDistortion),
					    maxHeight = forceHeight == undefined ? Math.max.apply(null, $('#' + instance.settings.menuID + ' div.levelHolderClass').map(function () {
						return $(this).height();                                                                                         // 489
					}).get()) : forceHeight;                                                                                          //
                                                                                                                       //
					instance.settings.container.css('min-height', '');                                                                // 491
					instance.settings.container.children('nav:first').css('min-height', '');                                          // 492
					if (extHeight) {                                                                                                  // 493
						instance.settings.container.height(instance.settings.menuHeight);                                                // 494
						instance.settings.container.css('min-height', instance.settings.menuHeight);                                     // 495
						instance.settings.container.children('nav:first').css('min-height', instance.settings.menuHeight);               // 496
						$('#' + instance.settings.menuID).height(instance.settings.menuHeight);                                          // 497
						maxHeight = instance.settings.container.height();                                                                // 498
					} else {                                                                                                          //
						$('#' + instance.settings.menuID).height(maxHeight);                                                             // 501
					}                                                                                                                 //
					instance.settings.container.css('min-height', maxHeight + 'px');                                                  // 503
					instance.settings.container.children('nav:first').css('min-height', maxHeight + 'px');                            // 504
					instance.settings.container.width(maxExtWidth);                                                                   // 505
					instance.settings.container.height(maxHeight);                                                                    // 506
					var $baseLevelHolder = $('#' + instance.settings.menuID + ' div.levelHolderClass:first'),                         // 507
					    $visibleLevelHolders = visibleLevelHolders(),                                                                 //
					    $hiddenLevelHolders = hiddenLevelHolders(),                                                                   //
					    $activeLevelHolder = activeMenu(),                                                                            //
					    activeLevel = $activeLevelHolder.length == 1 ? $activeLevelHolder.attr('data-level') : 0;                     //
					if ($visibleLevelHolders) $visibleLevelHolders.each(function () {                                                 // 512
						if (instance.settings.mode == 'overlap') $(this).width($(this).width() + (parseInt(activeLevel, 10) - parseInt($(this).attr('data-level'), 10)) * (instance.settings.overlapWidth + ieShadowFilterDistortion));
					});                                                                                                               //
					if ($hiddenLevelHolders) $hiddenLevelHolders.each(function () {                                                   // 517
						instance.settings.direction == 'rtl' ? $(this).css('margin-right', $(this).attr('data-level') == $baseLevelHolder.attr('data-level') && !instance.settings.fullCollapse ? $(this).width() * -1 + instance.settings.overlapWidth : $(this).width() * -2) : $(this).css('margin-left', $(this).attr('data-level') == $baseLevelHolder.attr('data-level') && !instance.settings.fullCollapse ? $(this).width() * -1 + instance.settings.overlapWidth : $(this).width() * -2);
					});                                                                                                               //
					currWidth = $baseLevelHolder.width() + parseInt($baseLevelHolder.css(instance.settings.direction == 'rtl' ? 'margin-right' : 'margin-left'), 10);
					sizeElementWidth(instance.settings.container, currWidth);                                                         // 525
					instance.menuWidth = maxWidth;                                                                                    // 526
					instance.menuHeight = maxHeight;                                                                                  // 527
					instance.redraw = false;                                                                                          // 528
				}                                                                                                                  //
			}                                                                                                                   //
                                                                                                                       //
			// Simple/singe DOM element width sizing                                                                            //
			function sizeElementWidth($element, size) {                                                                         // 17
				if ($element == undefined || size == undefined) return false;                                                      // 534
				$element.css('min-width', '');                                                                                     // 535
				$element.css('min-width', size + 'px');                                                                            // 536
				$element.children('nav:first').css('min-width', '');                                                               // 537
				$element.children('nav:first').css('min-width', size + 'px');                                                      // 538
				$element.width(size);                                                                                              // 539
			}                                                                                                                   //
                                                                                                                       //
			// Hide wrappers in browsers that                                                                                   //
			// does not understand negative margin in %                                                                         //
			// before DOM element got its dimensions                                                                            //
			function fixLazyBrowsers() {                                                                                        // 17
				var $baseLevelHolder = $('#' + instance.settings.menuID + ' div.levelHolderClass:first'),                          // 546
				    $hiddenLevelHolders = instance.settings.container.find('#' + instance.settings.menuID + ' div.levelHolderClass').filter(function () {
					var retObjs = instance.settings.direction == 'rtl' ? ($(this).position().left > instance.settings.container.width() || parseInt($(this).css('margin-right')) < 0) && $(this).attr('data-level') > $baseLevelHolder.attr('data-level') : ($(this).position().left < 0 || parseInt($(this).css('margin-left')) < 0) && $(this).attr('data-level') > $baseLevelHolder.attr('data-level');
					return retObjs;                                                                                                   // 554
				});                                                                                                                //
				$hiddenLevelHolders.each(function () {                                                                             // 556
					if (instance.settings.direction == 'rtl') {                                                                       // 557
						$(this).css('margin-right', $(this).attr('data-level') == $baseLevelHolder.attr('data-level') && !instance.settings.collapsed ? 0 : -2 * $(this).width());
					} else {                                                                                                          //
						$(this).css('margin-left', $(this).attr('data-level') == $baseLevelHolder.attr('data-level') && !instance.settings.collapsed ? 0 : -2 * $(this).width());
					}                                                                                                                 //
				});                                                                                                                //
				if (instance.settings.direction == 'rtl') {                                                                        // 564
					$baseLevelHolder.css('margin-right', !instance.settings.collapsed ? 0 : -2 * $baseLevelHolder.width());           // 565
				} else {                                                                                                           //
					$baseLevelHolder.css('margin-left', !instance.settings.collapsed ? 0 : -2 * $baseLevelHolder.width());            // 568
				}                                                                                                                  //
			}                                                                                                                   //
                                                                                                                       //
			// Is integer                                                                                                       //
			function isInt(n) {                                                                                                 // 17
				return typeof n === 'number' && parseFloat(n) == parseInt(n, 10) && !isNaN(n);                                     // 574
			}                                                                                                                   //
                                                                                                                       //
			// Is Valid CSS dimension                                                                                           //
			function isValidDim(s) {                                                                                            // 17
				return typeof s === 'string' && (s.indexOf('%') != -1 || s.indexOf('px') != -1 || s.indexOf('em') != -1);          // 579
			}                                                                                                                   //
                                                                                                                       //
			// Initialize menu level push menu                                                                                  //
			function initialize() {                                                                                             // 17
				var execute = options && options.menu != undefined ? createDOMStructure() : updateDOMStructure();                  // 584
				propagateEvent(instance.settings.container, clickEventType);                                                       // 585
				sizeDOMelements();                                                                                                 // 586
				fixLazyBrowsers();                                                                                                 // 587
				startMode(instance.settings.collapsed);                                                                            // 588
				instance.settings.onMenuReady.apply(this, Array.prototype.slice.call([instance.settings]));                        // 589
				return $this;                                                                                                      // 590
			}                                                                                                                   //
                                                                                                                       //
			// Initialize menu in collapsed/expanded mode                                                                       //
			function startMode(mode) {                                                                                          // 17
				if (mode) {                                                                                                        // 595
					var $baseLevelHolder = $('#' + instance.settings.menuID + ' div.levelHolderClass:first');                         // 596
					$baseLevelHolder.find('ul').hide();                                                                               // 597
					$baseLevelHolder.addClass(instance.settings.menuInactiveClass);                                                   // 598
					if (instance.settings.direction == 'rtl') {                                                                       // 599
						$baseLevelHolder.stop().animate({                                                                                // 600
							marginRight: -1 * $baseLevelHolder.width() + (instance.settings.fullCollapse ? 0 : instance.settings.overlapWidth)
						}, instance.settings.durationSlideOut);                                                                          //
					} else {                                                                                                          //
						$baseLevelHolder.stop().animate({                                                                                // 605
							marginLeft: -1 * $baseLevelHolder.width() + (instance.settings.fullCollapse ? 0 : instance.settings.overlapWidth)
						}, instance.settings.durationSlideOut);                                                                          //
					}                                                                                                                 //
				}                                                                                                                  //
			}                                                                                                                   //
                                                                                                                       //
			// Push container(s) of choice                                                                                      //
			function pushContainers(absMove) {                                                                                  // 17
				if (instance.settings.containersToPush == null) return false;                                                      // 614
				$.each(instance.settings.containersToPush, function () {                                                           // 615
					var lMr = parseInt($(this).css('margin-left')),                                                                   // 616
					    lM = isInt(lMr) ? lMr : 0,                                                                                    //
					    rMr = parseInt($(this).css('margin-right')),                                                                  //
					    rM = isInt(rMr) ? rMr : 0;                                                                                    //
					$(this).stop().animate({                                                                                          // 620
						marginLeft: lM + (instance.settings.direction == 'rtl' ? -1 : 1) * absMove,                                      // 621
						marginRight: rM + (instance.settings.direction == 'rtl' ? 1 : -1) * absMove                                      // 622
					}, instance.settings.durationSlideOut);                                                                           //
				});                                                                                                                //
			}                                                                                                                   //
                                                                                                                       //
			// Collapse menu                                                                                                    //
			function collapseMenu() {                                                                                           // 17
				if ($(instance).find('div.levelHolderClass').is(':animated')) return false;                                        // 629
				instance.settings.onCollapseMenuStart.apply(this, Array.prototype.slice.call([instance.settings]));                // 630
				var level = arguments[0],                                                                                          // 631
				    callbacks = arguments[1],                                                                                      //
				    collapingObjects = {},                                                                                         //
				    ieShadowFilterDistortion,                                                                                      //
				    lwidth,                                                                                                        //
				    lpush,                                                                                                         //
				    lMarginLeft,                                                                                                   //
				    lMarginLeftFC,                                                                                                 //
				    $baseLevelHolder = $('#' + instance.settings.menuID + ' div.levelHolderClass:first'),                          //
				    collapseAll = level == undefined ? true : false,                                                               //
				    currWidth;                                                                                                     //
				collapingObjects['collapsingEnded'] = false;                                                                       // 638
				if ((typeof level === 'undefined' ? 'undefined' : (0, _typeof3['default'])(level)) == 'object') {                  // 639
					level = level.attr('data-level');                                                                                 // 640
				} else if (typeof level == 'string') {                                                                             //
					var $selectedLevelHolder = findMenusByTitle(level);                                                               // 643
					if ($selectedLevelHolder && $selectedLevelHolder.length == 1) {                                                   // 644
						level = $selectedLevelHolder.attr('data-level');                                                                 // 645
					} else {                                                                                                          //
						level = $baseLevelHolder.attr('data-level');                                                                     // 648
					}                                                                                                                 //
				} else if (level == undefined || !isInt(level) || level < 0) {                                                     //
					level = $baseLevelHolder.attr('data-level');                                                                      // 652
				}                                                                                                                  //
				if (callbacks == undefined && (typeof callbacks === 'undefined' ? 'undefined' : (0, _typeof3['default'])(callbacks)) != 'object') {
					callbacks = [{ 'method': instance.settings.onCollapseMenuEnd, 'args': [instance.settings] }];                     // 655
				} else {                                                                                                           //
					$.merge(callbacks, [{ 'method': instance.settings.onCollapseMenuEnd, 'args': [instance.settings] }]);             // 657
				}                                                                                                                  //
				var $nextLevelHolders = instance.settings.container.find('#' + instance.settings.menuID + ' div.levelHolderClass').filter(function () {
					var retObjs = instance.settings.direction == 'rtl' ? $(this).attr('data-level') > level && parseInt($(this).css('margin-right')) >= 0 && $(this).position().left < instance.settings.container.width() - instance.settings.overlapWidth : $(this).attr('data-level') > level && parseInt($(this).css('margin-left')) >= 0 && $(this).position().left >= 0;
					return retObjs;                                                                                                   // 666
				}),                                                                                                                //
				    $prevLevelHolders = instance.settings.container.find('#' + instance.settings.menuID + ' div.levelHolderClass').filter(function () {
					var retObjs = instance.settings.direction == 'rtl' ? $(this).attr('data-level') <= level && parseInt($(this).css('margin-right')) >= 0 && $(this).position().left < instance.settings.container.width() - instance.settings.overlapWidth : $(this).attr('data-level') <= level && parseInt($(this).css('margin-left')) >= 0 && $(this).position().left >= 0;
					return retObjs;                                                                                                   // 675
				});                                                                                                                //
				if ($prevLevelHolders.length > 0) {                                                                                // 677
					collapingObjects['prevAnimEnded'] = false;                                                                        // 678
					$nextLevelHolders.each(function (key, val) {                                                                      // 679
						ieShadowFilterDistortion = $(val).css('filter').match(/DXImageTransform\.Microsoft\.Shadow/) ? $(val).get(0).filters.item("DXImageTransform.Microsoft.Shadow").strength : 0;
						lwidth = instance.settings.mode == 'overlap' ? $(val).width() - ($nextLevelHolders.length + $prevLevelHolders.length - $(val).attr('data-level') - 1) * (instance.settings.overlapWidth + ieShadowFilterDistortion) - ieShadowFilterDistortion : $(val).width() - ieShadowFilterDistortion;
						if (instance.settings.direction == 'rtl') {                                                                      // 682
							$(val).stop().animate({                                                                                         // 683
								marginRight: -1 * lwidth,                                                                                      // 684
								width: lwidth                                                                                                  // 685
							}, instance.settings.durationTransition);                                                                       //
						} else {                                                                                                         //
							$(val).stop().animate({                                                                                         // 689
								marginLeft: -1 * lwidth,                                                                                       // 690
								width: lwidth                                                                                                  // 691
							}, instance.settings.durationTransition);                                                                       //
						}                                                                                                                //
					});                                                                                                               //
					collapingObjects['nextAnimEnded'] = $nextLevelHolders.length > 0 ? false : true;                                  // 695
					$nextLevelHolders.last().queue(function () {                                                                      // 696
						collapingObjects['nextAnimEnded'] = true;                                                                        // 697
						animatedEventCallback(collapingObjects, callbacks);                                                              // 698
					});                                                                                                               //
					$prevLevelHolders.each(function (key, val) {                                                                      // 700
						ieShadowFilterDistortion = $(val).css('filter').match(/DXImageTransform\.Microsoft\.Shadow/) ? $(val).get(0).filters.item("DXImageTransform.Microsoft.Shadow").strength : 0;
						var $makeLevelHolderVisible = $prevLevelHolders.filter(function () {                                             // 702
							return $(this).attr('data-level') == level;                                                                     // 703
						});                                                                                                              //
						$makeLevelHolderVisible.css('visibility', 'visible');                                                            // 705
						$makeLevelHolderVisible.find('.' + instance.settings.backItemClass).css('visibility', 'visible');                // 706
						$makeLevelHolderVisible.find('ul').css('visibility', 'visible');                                                 // 707
						$makeLevelHolderVisible.removeClass(instance.settings.menuInactiveClass);                                        // 708
						lwidth = instance.settings.mode == 'overlap' ? $(val).width() - $nextLevelHolders.length * (instance.settings.overlapWidth + ieShadowFilterDistortion) - ieShadowFilterDistortion : $(val).width() - ieShadowFilterDistortion;
						if (instance.settings.direction == 'rtl') {                                                                      // 710
							$(val).stop().animate({                                                                                         // 711
								width: lwidth,                                                                                                 // 712
								marginRight: $(val).attr('data-level') == $baseLevelHolder.attr('data-level') && collapseAll ? instance.settings.fullCollapse ? -1 * $(val).width() : -1 * $(val).width() + (instance.settings.mode == 'overlap' ? $nextLevelHolders.length + 1 : 1) * instance.settings.overlapWidth : 0
							}, instance.settings.durationSlideOut, function () {                                                            //
								if ($(val).attr('data-level') == $baseLevelHolder.attr('data-level') && collapseAll) {                         // 721
									$baseLevelHolder.children('ul').first().hide(instance.settings.durationSlideDown, function () {               // 722
										$baseLevelHolder.addClass(instance.settings.menuInactiveClass);                                              // 723
									});                                                                                                           //
								}                                                                                                              //
								currWidth = $baseLevelHolder.width() + parseInt($baseLevelHolder.css('margin-right'), 10);                     // 726
								sizeElementWidth(instance.settings.container, currWidth);                                                      // 727
							});                                                                                                             //
						} else {                                                                                                         //
							$(val).stop().animate({                                                                                         // 731
								width: lwidth,                                                                                                 // 732
								marginLeft: $(val).attr('data-level') == $baseLevelHolder.attr('data-level') && collapseAll ? instance.settings.fullCollapse ? -1 * $(val).width() : -1 * $(val).width() + (instance.settings.mode == 'overlap' ? $nextLevelHolders.length + 1 : 1) * instance.settings.overlapWidth : 0
							}, instance.settings.durationSlideOut, function () {                                                            //
								if ($(val).attr('data-level') == $baseLevelHolder.attr('data-level') && collapseAll) {                         // 741
									$baseLevelHolder.children('ul').first().hide(instance.settings.durationSlideDown, function () {               // 742
										$baseLevelHolder.addClass(instance.settings.menuInactiveClass);                                              // 743
									});                                                                                                           //
								}                                                                                                              //
								currWidth = $baseLevelHolder.width() + parseInt($baseLevelHolder.css('margin-left'), 10);                      // 746
								sizeElementWidth(instance.settings.container, currWidth);                                                      // 747
							});                                                                                                             //
						}                                                                                                                //
						lpush = instance.settings.mode == 'overlap' ? -1 * ($nextLevelHolders.length * (instance.settings.overlapWidth + ieShadowFilterDistortion)) : 0;
						if ($(val).attr('data-level') == $baseLevelHolder.attr('data-level') && collapseAll) {                           // 751
							var blpush = instance.settings.fullCollapse ? -1 * ($baseLevelHolder.width() - ieShadowFilterDistortion) : -1 * ($baseLevelHolder.width() - ieShadowFilterDistortion) + instance.settings.overlapWidth;
							pushContainers(blpush);                                                                                         // 753
						} else {                                                                                                         //
							pushContainers(lpush);                                                                                          // 756
						}                                                                                                                //
					});                                                                                                               //
					$prevLevelHolders.last().queue(function () {                                                                      // 759
						collapingObjects['prevAnimEnded'] = true;                                                                        // 760
						animatedEventCallback(collapingObjects, callbacks);                                                              // 761
					});                                                                                                               //
				}                                                                                                                  //
				collapingObjects['collapsingEnded'] = true;                                                                        // 764
				animatedEventCallback(collapingObjects, callbacks);                                                                // 765
				return $this;                                                                                                      // 766
			}                                                                                                                   //
                                                                                                                       //
			// Expand Menu helper                                                                                               //
			function expandMenuActions() {                                                                                      // 17
				if ($(instance).find('div.levelHolderClass').is(':animated')) return false;                                        // 771
				instance.settings.onExpandMenuStart.apply(this, Array.prototype.slice.call([instance.settings]));                  // 772
				var menuTitle = arguments[0],                                                                                      // 773
				    callbacks = arguments[1],                                                                                      //
				    ieShadowFilterDistortion,                                                                                      //
				    lwidth,                                                                                                        //
				    lpush,                                                                                                         //
				    blpush,                                                                                                        //
				    currWidth,                                                                                                     //
				    expandingObjects = {},                                                                                         //
				    $baseLevelHolder = $('#' + instance.settings.menuID + ' div.levelHolderClass:first'),                          //
				    baseExpand = menuTitle == undefined ? true : false,                                                            //
				    baseLevelHolderCollapsed = instance.settings.direction == 'rtl' ? parseInt($baseLevelHolder.css('margin-right'), 10) < 0 || $baseLevelHolder.position().left >= instance.settings.container.width() - instance.settings.overlapWidth : parseInt($baseLevelHolder.css('margin-left'), 10) < 0 || $baseLevelHolder.position().left < 0;
				expandingObjects['expandingEnded'] = false;                                                                        // 783
				if (callbacks == undefined && (typeof callbacks === 'undefined' ? 'undefined' : (0, _typeof3['default'])(callbacks)) != 'object') {
					callbacks = [{ 'method': instance.settings.onExpandMenuEnd, 'args': [instance.settings] }];                       // 785
				} else {                                                                                                           //
					$.merge(callbacks, [{ 'method': instance.settings.onExpandMenuEnd, 'args': [instance.settings] }]);               // 787
				}                                                                                                                  //
				if (baseExpand) {                                                                                                  // 789
					expandingObjects['baseAnimEnded'] = false;                                                                        // 790
					$baseLevelHolder.removeClass(instance.settings.menuInactiveClass);                                                // 791
					currWidth = $baseLevelHolder.width();                                                                             // 792
					sizeElementWidth(instance.settings.container, currWidth);                                                         // 793
					if (instance.settings.direction == 'rtl') {                                                                       // 794
						$baseLevelHolder.stop().animate({                                                                                // 795
							marginRight: 0                                                                                                  // 796
						}, instance.settings.durationSlideOut, function () {                                                             //
							$baseLevelHolder.children('ul').first().show(instance.settings.durationSlideDown, function () {                 // 798
								expandingObjects['baseAnimEnded'] = true;                                                                      // 799
								animatedEventCallback(expandingObjects, callbacks);                                                            // 800
							});                                                                                                             //
						});                                                                                                              //
					} else {                                                                                                          //
						$baseLevelHolder.stop().animate({                                                                                // 805
							marginLeft: 0                                                                                                   // 806
						}, instance.settings.durationSlideOut, function () {                                                             //
							$baseLevelHolder.children('ul').first().show(instance.settings.durationSlideDown, function () {                 // 808
								expandingObjects['baseAnimEnded'] = true;                                                                      // 809
								animatedEventCallback(expandingObjects, callbacks);                                                            // 810
							});                                                                                                             //
						});                                                                                                              //
					}                                                                                                                 //
					blpush = instance.settings.fullCollapse ? $baseLevelHolder.width() : $baseLevelHolder.width() - instance.settings.overlapWidth;
					var pushbm = !menuExpanded($baseLevelHolder) ? pushContainers(blpush) : null;                                     // 815
				} else {                                                                                                           //
					var $selectedLevelHolder;                                                                                         // 817
					if ((typeof menuTitle === 'undefined' ? 'undefined' : (0, _typeof3['default'])(menuTitle)) == 'object') {         // 818
						$selectedLevelHolder = menuTitle;                                                                                // 819
					} else if (typeof menuTitle == 'string') {                                                                        //
						$selectedLevelHolder = findMenusByTitle(menuTitle);                                                              // 822
					} else {                                                                                                          //
						$selectedLevelHolder = null;                                                                                     // 825
						$.error('Provided menu selector is not valid');                                                                  // 826
					}                                                                                                                 //
					if ($selectedLevelHolder && $selectedLevelHolder.length == 1) {                                                   // 828
						var $activeLevelHolder = activeMenu(),                                                                           // 829
						    activeLevel = $activeLevelHolder.length == 1 ? $activeLevelHolder.attr('data-level') : 0,                    //
						    baseWidth = $selectedLevelHolder.width(),                                                                    //
						    setToOpenHolders = pathToRoot($selectedLevelHolder);                                                         //
						expandingObjects['setToOpenAnimEnded'] = false;                                                                  // 833
						if (setToOpenHolders) {                                                                                          // 834
							var parentLevelHoldersLen = $(setToOpenHolders).length - 1;                                                     // 835
							$baseLevelHolder.find('ul').each(function () {                                                                  // 836
								$(this).show(0);                                                                                               // 837
							});                                                                                                             //
							$(setToOpenHolders).find('ul').css('visibility', 'hidden');                                                     // 839
							$(setToOpenHolders).find('div').css('visibility', 'visible');                                                   // 840
							$(setToOpenHolders).find('.' + instance.settings.backItemClass).css('visibility', 'hidden');                    // 841
							$(setToOpenHolders).each(function (key, val) {                                                                  // 842
								ieShadowFilterDistortion = $(val).css('filter').match(/DXImageTransform\.Microsoft\.Shadow/) ? $(val).get(0).filters.item("DXImageTransform.Microsoft.Shadow").strength : 0;
								lwidth = baseWidth - ieShadowFilterDistortion + (parentLevelHoldersLen - $(val).attr('data-level')) * (instance.settings.overlapWidth + ieShadowFilterDistortion);
								if (instance.settings.container.width() < lwidth && instance.settings.mode == 'overlap') sizeElementWidth(instance.settings.container, lwidth);
								if (instance.settings.direction == 'rtl') {                                                                    // 847
									$(val).stop().animate({                                                                                       // 848
										marginRight: 0,                                                                                              // 849
										width: instance.settings.mode == 'overlap' ? lwidth : baseWidth - ieShadowFilterDistortion                   // 850
									}, instance.settings.durationTransition, function () {                                                        //
										$(val).addClass(instance.settings.menuInactiveClass);                                                        // 852
									});                                                                                                           //
								} else {                                                                                                       //
									$(val).stop().animate({                                                                                       // 856
										marginLeft: 0,                                                                                               // 857
										width: instance.settings.mode == 'overlap' ? lwidth : baseWidth - ieShadowFilterDistortion                   // 858
									}, instance.settings.durationTransition, function () {                                                        //
										$(val).addClass(instance.settings.menuInactiveClass);                                                        // 860
									});                                                                                                           //
								}                                                                                                              //
							});                                                                                                             //
							$(setToOpenHolders).last().queue(function () {                                                                  // 864
								$(this).removeClass(instance.settings.menuInactiveClass);                                                      // 865
								expandingObjects['setToOpenAnimEnded'] = true;                                                                 // 866
								animatedEventCallback(expandingObjects, callbacks);                                                            // 867
							});                                                                                                             //
							if (baseLevelHolderCollapsed) {                                                                                 // 869
								blpush = instance.settings.fullCollapse ? $baseLevelHolder.width() : $baseLevelHolder.width() - instance.settings.overlapWidth;
								pushContainers(blpush);                                                                                        // 871
							}                                                                                                               //
							if (instance.settings.mode == 'overlap') {                                                                      // 873
								lpush = baseLevelHolderCollapsed ? baseWidth + (parentLevelHoldersLen - (instance.settings.fullCollapse ? 0 : 1)) * (instance.settings.overlapWidth + ieShadowFilterDistortion) : (parentLevelHoldersLen - activeLevel) * (instance.settings.overlapWidth + ieShadowFilterDistortion);
								pushContainers(lpush);                                                                                         // 875
							}                                                                                                               //
							$selectedLevelHolder.css('visibility', 'visible');                                                              // 877
							$selectedLevelHolder.find('.' + instance.settings.backItemClass).css('visibility', 'visible');                  // 878
							$selectedLevelHolder.find('ul').css('visibility', 'visible');                                                   // 879
							$selectedLevelHolder.removeClass(instance.settings.menuInactiveClass);                                          // 880
						} else {                                                                                                         //
							$.error('Invalid menu object provided');                                                                        // 883
						}                                                                                                                //
					} else {                                                                                                          //
						$.error('No or too many menus named ' + menuTitle);                                                              // 887
					}                                                                                                                 //
				}                                                                                                                  //
				expandingObjects['expandingEnded'] = true;                                                                         // 890
				animatedEventCallback(expandingObjects, callbacks);                                                                // 891
			}                                                                                                                   //
                                                                                                                       //
			// Expand menu                                                                                                      //
			function expandMenu() {                                                                                             // 17
				var menu = arguments[0],                                                                                           // 896
				    $expandLevelHolder,                                                                                            //
				    $activeLevelHolder = activeMenu(),                                                                             //
				    $sharedLevelHolders,                                                                                           //
				    collapseLevel,                                                                                                 //
				    $searchRes;                                                                                                    //
				if ((typeof menu === 'undefined' ? 'undefined' : (0, _typeof3['default'])(menu)) == 'object') {                    // 900
					$expandLevelHolder = menu;                                                                                        // 901
				} else if (typeof menu == 'string') {                                                                              //
					$searchRes = findMenusByTitle(menu);                                                                              // 904
					if ($searchRes) {                                                                                                 // 905
						$expandLevelHolder = $searchRes.eq(0);                                                                           // 906
					} else {                                                                                                          //
						$.error(menu + ' menu level does not exist!');                                                                   // 909
					}                                                                                                                 //
				} else {                                                                                                           //
					$expandLevelHolder = $('#' + instance.settings.menuID + ' div.levelHolderClass:first');                           // 913
				}                                                                                                                  //
				$sharedLevelHolders = comparePaths($expandLevelHolder, $activeLevelHolder, true);                                  // 915
				collapseLevel = $sharedLevelHolders.length > 0 ? Math.max.apply(null, $sharedLevelHolders.map(function () {        // 916
					return $(this).attr('data-level');                                                                                // 917
				}).get()) : 0;                                                                                                     //
				if (collapseLevel < $activeLevelHolder.attr('data-level')) {                                                       // 918
					collapseMenu(collapseLevel, [{ 'method': expandMenuActions, 'args': arguments }]);                                // 919
				} else {                                                                                                           //
					expandMenuActions.apply(this, Array.prototype.slice.call(arguments));                                             // 922
				}                                                                                                                  //
				return $this;                                                                                                      // 924
			}                                                                                                                   //
                                                                                                                       //
			// Find menu(s) by Title text                                                                                       //
			function findMenusByTitle() {                                                                                       // 17
				var menuTitle = arguments[0],                                                                                      // 929
				    response,                                                                                                      //
				    $selectedLevelHolders = instance.settings.container.find('#' + instance.settings.menuID + ' div.levelHolderClass').filter(function () {
					return $(this).children('h2').text() == menuTitle;                                                                // 934
				});                                                                                                                //
				if ($selectedLevelHolders.length > 0) {                                                                            // 936
					returnValue = $selectedLevelHolders;                                                                              // 937
					response = returnValue;                                                                                           // 938
				} else {                                                                                                           //
					returnValue = false;                                                                                              // 941
					response = returnValue;                                                                                           // 942
				}                                                                                                                  //
				return response;                                                                                                   // 944
			}                                                                                                                   //
                                                                                                                       //
			// Find item(s) by Name                                                                                             //
			function findItemsByName() {                                                                                        // 17
				var itemName = arguments[0],                                                                                       // 949
				    response,                                                                                                      //
				    $selectedItems = instance.settings.container.find('#' + instance.settings.menuID + ' div.levelHolderClass li').filter(function () {
					return $(this).children('a').text() == itemName;                                                                  // 954
				});                                                                                                                //
				if ($selectedItems.length > 0) {                                                                                   // 956
					returnValue = $selectedItems;                                                                                     // 957
					response = returnValue;                                                                                           // 958
				} else {                                                                                                           //
					returnValue = false;                                                                                              // 961
					response = returnValue;                                                                                           // 962
				}                                                                                                                  //
				return response;                                                                                                   // 964
			}                                                                                                                   //
                                                                                                                       //
			// Find pathToRoot for provided menu                                                                                //
			function pathToRoot() {                                                                                             // 17
				var $selectedLevelHolder = arguments[0],                                                                           // 969
				    $parentLevelHolders,                                                                                           //
				    setToOpenHolders,                                                                                              //
				    response;                                                                                                      //
				if ($selectedLevelHolder == undefined || $selectedLevelHolder.length != 1) {                                       // 971
					returnValue = false;                                                                                              // 972
					return returnValue;                                                                                               // 973
				};                                                                                                                 //
				$parentLevelHolders = $selectedLevelHolder.parents('div.levelHolderClass');                                        // 975
				setToOpenHolders = $.merge($parentLevelHolders.get().reverse(), $selectedLevelHolder.get());                       // 976
				returnValue = setToOpenHolders;                                                                                    // 977
				return returnValue;                                                                                                // 978
			}                                                                                                                   //
                                                                                                                       //
			// Finds the same part of the path to root of two provided menus                                                    //
			function comparePaths() {                                                                                           // 17
				var $levelHolder0 = arguments[0],                                                                                  // 983
				    $levelHolder1 = arguments[1],                                                                                  //
				    mode = arguments[2] != undefined ? arguments[2] : false,                                                       //
				    $parentLevelHolders0,                                                                                          //
				    $parentLevelHolders1,                                                                                          //
				    setParents0,                                                                                                   //
				    setParents1,                                                                                                   //
				    lPath,                                                                                                         //
				    sPath,                                                                                                         //
				    comparePath,                                                                                                   //
				    response;                                                                                                      //
				if ($levelHolder0 == undefined || $levelHolder1 == undefined) {                                                    // 987
					returnValue = false;                                                                                              // 988
					return returnValue;                                                                                               // 989
				};                                                                                                                 //
				$parentLevelHolders0 = $levelHolder0.length == 1 ? $levelHolder0.parents('div.levelHolderClass') : null;           // 991
				$parentLevelHolders1 = $levelHolder1.length == 1 ? $levelHolder1.parents('div.levelHolderClass') : null;           // 992
				setParents0 = $parentLevelHolders0 != null ? $.merge($parentLevelHolders0.get().reverse(), $levelHolder0.get()) : [];
				setParents1 = $parentLevelHolders1 != null ? $.merge($parentLevelHolders1.get().reverse(), $levelHolder1.get()) : [];
				lPath = setParents0.length >= setParents1.length ? setParents0 : setParents1;                                      // 995
				sPath = lPath === setParents0 ? setParents1 : setParents0;                                                         // 996
				comparePath = $(lPath).filter(function () {                                                                        // 997
					return mode ? $.inArray(this, sPath) != -1 : $.inArray(this, sPath) == -1;                                        // 998
				});                                                                                                                //
				returnValue = comparePath;                                                                                         // 1000
				return returnValue;                                                                                                // 1001
			}                                                                                                                   //
                                                                                                                       //
			// Active menu                                                                                                      //
			function activeMenu() {                                                                                             // 17
				var $activeLevelHolders = instance.settings.container.find('#' + instance.settings.menuID + ' div.levelHolderClass').filter(function () {
					var retObjs = instance.settings.direction == 'rtl' ? parseInt($(this).css('margin-right')) >= 0 && $(this).position().left < instance.settings.container.width() - instance.settings.overlapWidth : parseInt($(this).css('margin-left')) >= 0 && $(this).position().left >= 0;
					return retObjs;                                                                                                   // 1013
				}),                                                                                                                //
				    maxLevel = Math.max.apply(null, $activeLevelHolders.map(function () {                                          //
					return $(this).attr('data-level');                                                                                // 1016
				}).get()),                                                                                                         //
				    $activeLevelHolder = $activeLevelHolders.filter(function () {                                                  //
					return $(this).attr('data-level') == maxLevel;                                                                    // 1018
				});                                                                                                                //
				returnValue = $activeLevelHolder;                                                                                  // 1020
				return returnValue;                                                                                                // 1021
			}                                                                                                                   //
                                                                                                                       //
			// Menu expanded                                                                                                    //
			function menuExpanded() {                                                                                           // 17
				var $levelHolder = arguments[0],                                                                                   // 1026
				    returnValue = false;                                                                                           //
				if ($levelHolder == undefined) return returnValue;                                                                 // 1028
                                                                                                                       //
				var check = instance.settings.direction == 'rtl' ? parseInt($levelHolder.css('margin-right')) >= 0 && $levelHolder.position().left < instance.settings.container.width() - instance.settings.overlapWidth : parseInt($levelHolder.css('margin-left')) >= 0 && $levelHolder.position().left >= 0;
				return check;                                                                                                      // 1034
			}                                                                                                                   //
                                                                                                                       //
			// Add item(s)                                                                                                      //
			function addItems() {                                                                                               // 17
				var items = arguments[0],                                                                                          // 1039
				    $levelHolder = arguments[1],                                                                                   //
				    position = arguments[2];                                                                                       //
				if ($levelHolder == undefined || (typeof items === 'undefined' ? 'undefined' : (0, _typeof3['default'])(items)) != 'object' || !$levelHolder) return false;
				if (items.level == undefined) items.level = parseInt($levelHolder.attr('data-level'), 10);                         // 1043
				if (position == undefined) position = 0;                                                                           // 1044
				var $itemGroup = $levelHolder.find('ul:first');                                                                    // 1045
				$.each(items, function () {                                                                                        // 1046
					if (this.name != undefined) createItem(this, $levelHolder, position);                                             // 1047
				});                                                                                                                //
				sizeDOMelements(instance.menuWidth);                                                                               // 1050
				return $this;                                                                                                      // 1051
			}                                                                                                                   //
                                                                                                                       //
			// Remove item(s)                                                                                                   //
			function removeItems() {                                                                                            // 17
				var $items = arguments[0];                                                                                         // 1056
				if ($items == undefined || (typeof $items === 'undefined' ? 'undefined' : (0, _typeof3['default'])($items)) != 'object' || $items.length == 0) return false;
				$items.remove();                                                                                                   // 1058
				var $activeMenu = activeMenu();                                                                                    // 1059
				if ($activeMenu.length == 1) {                                                                                     // 1060
					$activeMenu.css('visibility', 'visible');                                                                         // 1061
					$activeMenu.find('.' + instance.settings.backItemClass).css('visibility', 'visible');                             // 1062
					$activeMenu.find('ul').css('visibility', 'visible');                                                              // 1063
					$activeMenu.removeClass(instance.settings.menuInactiveClass);                                                     // 1064
					var widthDiff = $activeMenu.width() - instance.menuWidth;                                                         // 1065
					if (widthDiff != 0) {                                                                                             // 1066
						var $visibleLevelHolders = visibleLevelHolders();                                                                // 1067
						if ($visibleLevelHolders) $visibleLevelHolders.each(function () {                                                // 1068
							$(this).width($(this).width() - widthDiff);                                                                     // 1070
						});                                                                                                              //
					}                                                                                                                 //
				}                                                                                                                  //
				sizeDOMelements(instance.menuWidth);                                                                               // 1074
				return $this;                                                                                                      // 1075
			}                                                                                                                   //
                                                                                                                       //
			// Manage multiple animated events and associated callbacks                                                         //
			function animatedEventCallback(animatedObjects, callbacks) {                                                        // 17
				var doCallBack = true;                                                                                             // 1080
				$.each(animatedObjects, function (key, val) {                                                                      // 1081
					doCallBack = doCallBack && val;                                                                                   // 1082
				});                                                                                                                //
				if (doCallBack) window.setTimeout(function () {                                                                    // 1084
					$.each(callbacks, function (key, val) {                                                                           // 1086
						val['method'].apply(this, Array.prototype.slice.call(val['args']));                                              // 1087
					});                                                                                                               //
				}, 1);                                                                                                             //
			}                                                                                                                   //
                                                                                                                       //
			// Get/set settings options                                                                                         //
			function manageOptions() {                                                                                          // 17
				var response = false;                                                                                              // 1094
				if (instance.settings[arguments[0]] != undefined) {                                                                // 1095
					if (arguments[1] != undefined) instance.settings[arguments[0]] = arguments[1];                                    // 1096
					response = instance.settings[arguments[0]];                                                                       // 1098
				} else {                                                                                                           //
					$.error('No option ' + arguments[0] + ' found in jQuery.multilevelpushmenu');                                     // 1100
				}                                                                                                                  //
				return response;                                                                                                   // 1102
			}                                                                                                                   //
                                                                                                                       //
			// Mobile check                                                                                                     //
			// http://coveroverflow.com/a/11381730/989439                                                                       //
			function mobileCheck() {                                                                                            // 17
				var check = false;                                                                                                 // 1108
				(function (a) {                                                                                                    // 1109
					if (/(android|ipad|playbook|silk|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(a) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0, 4))) check = true;
				})(navigator.userAgent || navigator.vendor || window.opera);                                                       //
				return check;                                                                                                      // 1110
			}                                                                                                                   //
                                                                                                                       //
			if (mobileCheck()) {                                                                                                // 1113
				clickEventType = 'touchend';                                                                                       // 1114
				dragEventType = 'touchmove';                                                                                       // 1115
			} else {                                                                                                            //
				clickEventType = 'click';                                                                                          // 1118
				dragEventType = 'mousedown';                                                                                       // 1119
			}                                                                                                                   //
                                                                                                                       //
			// Invoke called method or init                                                                                     //
			if (methods[options]) {                                                                                             // 17
				returnValue = methods[options].apply(this, Array.prototype.slice.call(args, 1));                                   // 1124
				return returnValue;                                                                                                // 1125
			} else if ((typeof options === 'undefined' ? 'undefined' : (0, _typeof3['default'])(options)) === 'object' || !options) {
				returnValue = methods.init.apply(this, arguments);                                                                 // 1127
				return returnValue;                                                                                                // 1128
			} else {                                                                                                            //
				$.error('No ' + options + ' method found in jQuery.multilevelpushmenu');                                           // 1130
			}                                                                                                                   //
                                                                                                                       //
			// Return object instance or option value                                                                           //
			if (!returnValue) {                                                                                                 // 17
				returnValue = this;                                                                                                // 1135
			}                                                                                                                   //
		});                                                                                                                  //
		return returnValue;                                                                                                  // 1138
	};                                                                                                                    //
})(jQuery);                                                                                                            //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}],"threeTestData.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/lib/threeTestData.js                                                                                         //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
threeTestData = {                                                                                                      // 1
    "nodes": [{ "name": "Myriel", "group": 1 }, { "name": "Napoleon", "group": 1 }, { "name": "Mlle.Baptistine", "group": 1 }, { "name": "Mme.Magloire", "group": 1 }, { "name": "CountessdeLo", "group": 1 }, { "name": "Geborand", "group": 1 }, { "name": "Champtercier", "group": 1 }, { "name": "Cravatte", "group": 1 }, { "name": "Count", "group": 1 }, { "name": "OldMan", "group": 1 }, { "name": "Labarre", "group": 2 }, { "name": "Valjean", "group": 2 }, { "name": "Marguerite", "group": 3 }, { "name": "Mme.deR", "group": 2 }, { "name": "Isabeau", "group": 2 }, { "name": "Gervais", "group": 2 }, { "name": "Tholomyes", "group": 3 }, { "name": "Listolier", "group": 3 }, { "name": "Fameuil", "group": 3 }, { "name": "Blacheville", "group": 3 }, { "name": "Favourite", "group": 3 }, { "name": "Dahlia", "group": 3 }, { "name": "Zephine", "group": 3 }, { "name": "Fantine", "group": 3 }, { "name": "Mme.Thenardier", "group": 4 }, { "name": "Thenardier", "group": 4 }, { "name": "Cosette", "group": 5 }, { "name": "Javert", "group": 4 }, { "name": "Fauchelevent", "group": 0 }, { "name": "Bamatabois", "group": 2 }, { "name": "Perpetue", "group": 3 }, { "name": "Simplice", "group": 2 }, { "name": "Scaufflaire", "group": 2 }, { "name": "Woman1", "group": 2 }, { "name": "Judge", "group": 2 }, { "name": "Champmathieu", "group": 2 }, { "name": "Brevet", "group": 2 }, { "name": "Chenildieu", "group": 2 }, { "name": "Cochepaille", "group": 2 }, { "name": "Pontmercy", "group": 4 }, { "name": "Boulatruelle", "group": 6 }, { "name": "Eponine", "group": 4 }, { "name": "Anzelma", "group": 4 }, { "name": "Woman2", "group": 5 }, { "name": "MotherInnocent", "group": 0 }, { "name": "Gribier", "group": 0 }, { "name": "Jondrette", "group": 7 }, { "name": "Mme.Burgon", "group": 7 }, { "name": "Gavroche", "group": 8 }, { "name": "Gillenormand", "group": 5 }, { "name": "Magnon", "group": 5 }, { "name": "Mlle.Gillenormand", "group": 5 }, { "name": "Mme.Pontmercy", "group": 5 }, { "name": "Mlle.Vaubois", "group": 5 }, { "name": "Lt.Gillenormand", "group": 5 }, { "name": "Marius", "group": 8 }, { "name": "BaronessT", "group": 5 }, { "name": "Mabeuf", "group": 8 }, { "name": "Enjolras", "group": 8 }, { "name": "Combeferre", "group": 8 }, { "name": "Prouvaire", "group": 8 }, { "name": "Feuilly", "group": 8 }, { "name": "Courfeyrac", "group": 8 }, { "name": "Bahorel", "group": 8 }, { "name": "Bossuet", "group": 8 }, { "name": "Joly", "group": 8 }, { "name": "Grantaire", "group": 8 }, { "name": "MotherPlutarch", "group": 9 }, { "name": "Gueulemer", "group": 4 }, { "name": "Babet", "group": 4 }, { "name": "Claquesous", "group": 4 }, { "name": "Montparnasse", "group": 4 }, { "name": "Toussaint", "group": 5 }, { "name": "Child1", "group": 10 }, { "name": "Child2", "group": 10 }, { "name": "Brujon", "group": 4 }, { "name": "Mme.Hucheloup", "group": 8 }],
    "links": [{ "source": 1, "target": 0, "value": 1 }, { "source": 2, "target": 0, "value": 8 }, { "source": 3, "target": 0, "value": 10 }, { "source": 3, "target": 2, "value": 6 }, { "source": 4, "target": 0, "value": 1 }, { "source": 5, "target": 0, "value": 1 }, { "source": 6, "target": 0, "value": 1 }, { "source": 7, "target": 0, "value": 1 }, { "source": 8, "target": 0, "value": 2 }, { "source": 9, "target": 0, "value": 1 }, { "source": 11, "target": 10, "value": 1 }, { "source": 11, "target": 3, "value": 3 }, { "source": 11, "target": 2, "value": 3 }, { "source": 11, "target": 0, "value": 5 }, { "source": 12, "target": 11, "value": 1 }, { "source": 13, "target": 11, "value": 1 }, { "source": 14, "target": 11, "value": 1 }, { "source": 15, "target": 11, "value": 1 }, { "source": 17, "target": 16, "value": 4 }, { "source": 18, "target": 16, "value": 4 }, { "source": 18, "target": 17, "value": 4 }, { "source": 19, "target": 16, "value": 4 }, { "source": 19, "target": 17, "value": 4 }, { "source": 19, "target": 18, "value": 4 }, { "source": 20, "target": 16, "value": 3 }, { "source": 20, "target": 17, "value": 3 }, { "source": 20, "target": 18, "value": 3 }, { "source": 20, "target": 19, "value": 4 }, { "source": 21, "target": 16, "value": 3 }, { "source": 21, "target": 17, "value": 3 }, { "source": 21, "target": 18, "value": 3 }, { "source": 21, "target": 19, "value": 3 }, { "source": 21, "target": 20, "value": 5 }, { "source": 22, "target": 16, "value": 3 }, { "source": 22, "target": 17, "value": 3 }, { "source": 22, "target": 18, "value": 3 }, { "source": 22, "target": 19, "value": 3 }, { "source": 22, "target": 20, "value": 4 }, { "source": 22, "target": 21, "value": 4 }, { "source": 23, "target": 16, "value": 3 }, { "source": 23, "target": 17, "value": 3 }, { "source": 23, "target": 18, "value": 3 }, { "source": 23, "target": 19, "value": 3 }, { "source": 23, "target": 20, "value": 4 }, { "source": 23, "target": 21, "value": 4 }, { "source": 23, "target": 22, "value": 4 }, { "source": 23, "target": 12, "value": 2 }, { "source": 23, "target": 11, "value": 9 }, { "source": 24, "target": 23, "value": 2 }, { "source": 24, "target": 11, "value": 7 }, { "source": 25, "target": 24, "value": 13 }, { "source": 25, "target": 23, "value": 1 }, { "source": 25, "target": 11, "value": 12 }, { "source": 26, "target": 24, "value": 4 }, { "source": 26, "target": 11, "value": 31 }, { "source": 26, "target": 16, "value": 1 }, { "source": 26, "target": 25, "value": 1 }, { "source": 27, "target": 11, "value": 17 }, { "source": 27, "target": 23, "value": 5 }, { "source": 27, "target": 25, "value": 5 }, { "source": 27, "target": 24, "value": 1 }, { "source": 27, "target": 26, "value": 1 }, { "source": 28, "target": 11, "value": 8 }, { "source": 28, "target": 27, "value": 1 }, { "source": 29, "target": 23, "value": 1 }, { "source": 29, "target": 27, "value": 1 }, { "source": 29, "target": 11, "value": 2 }, { "source": 30, "target": 23, "value": 1 }, { "source": 31, "target": 30, "value": 2 }, { "source": 31, "target": 11, "value": 3 }, { "source": 31, "target": 23, "value": 2 }, { "source": 31, "target": 27, "value": 1 }, { "source": 32, "target": 11, "value": 1 }, { "source": 33, "target": 11, "value": 2 }, { "source": 33, "target": 27, "value": 1 }, { "source": 34, "target": 11, "value": 3 }, { "source": 34, "target": 29, "value": 2 }, { "source": 35, "target": 11, "value": 3 }, { "source": 35, "target": 34, "value": 3 }, { "source": 35, "target": 29, "value": 2 }, { "source": 36, "target": 34, "value": 2 }, { "source": 36, "target": 35, "value": 2 }, { "source": 36, "target": 11, "value": 2 }, { "source": 36, "target": 29, "value": 1 }, { "source": 37, "target": 34, "value": 2 }, { "source": 37, "target": 35, "value": 2 }, { "source": 37, "target": 36, "value": 2 }, { "source": 37, "target": 11, "value": 2 }, { "source": 37, "target": 29, "value": 1 }, { "source": 38, "target": 34, "value": 2 }, { "source": 38, "target": 35, "value": 2 }, { "source": 38, "target": 36, "value": 2 }, { "source": 38, "target": 37, "value": 2 }, { "source": 38, "target": 11, "value": 2 }, { "source": 38, "target": 29, "value": 1 }, { "source": 39, "target": 25, "value": 1 }, { "source": 40, "target": 25, "value": 1 }, { "source": 41, "target": 24, "value": 2 }, { "source": 41, "target": 25, "value": 3 }, { "source": 42, "target": 41, "value": 2 }, { "source": 42, "target": 25, "value": 2 }, { "source": 42, "target": 24, "value": 1 }, { "source": 43, "target": 11, "value": 3 }, { "source": 43, "target": 26, "value": 1 }, { "source": 43, "target": 27, "value": 1 }, { "source": 44, "target": 28, "value": 3 }, { "source": 44, "target": 11, "value": 1 }, { "source": 45, "target": 28, "value": 2 }, { "source": 47, "target": 46, "value": 1 }, { "source": 48, "target": 47, "value": 2 }, { "source": 48, "target": 25, "value": 1 }, { "source": 48, "target": 27, "value": 1 }, { "source": 48, "target": 11, "value": 1 }, { "source": 49, "target": 26, "value": 3 }, { "source": 49, "target": 11, "value": 2 }, { "source": 50, "target": 49, "value": 1 }, { "source": 50, "target": 24, "value": 1 }, { "source": 51, "target": 49, "value": 9 }, { "source": 51, "target": 26, "value": 2 }, { "source": 51, "target": 11, "value": 2 }, { "source": 52, "target": 51, "value": 1 }, { "source": 52, "target": 39, "value": 1 }, { "source": 53, "target": 51, "value": 1 }, { "source": 54, "target": 51, "value": 2 }, { "source": 54, "target": 49, "value": 1 }, { "source": 54, "target": 26, "value": 1 }, { "source": 55, "target": 51, "value": 6 }, { "source": 55, "target": 49, "value": 12 }, { "source": 55, "target": 39, "value": 1 }, { "source": 55, "target": 54, "value": 1 }, { "source": 55, "target": 26, "value": 21 }, { "source": 55, "target": 11, "value": 19 }, { "source": 55, "target": 16, "value": 1 }, { "source": 55, "target": 25, "value": 2 }, { "source": 55, "target": 41, "value": 5 }, { "source": 55, "target": 48, "value": 4 }, { "source": 56, "target": 49, "value": 1 }, { "source": 56, "target": 55, "value": 1 }, { "source": 57, "target": 55, "value": 1 }, { "source": 57, "target": 41, "value": 1 }, { "source": 57, "target": 48, "value": 1 }, { "source": 58, "target": 55, "value": 7 }, { "source": 58, "target": 48, "value": 7 }, { "source": 58, "target": 27, "value": 6 }, { "source": 58, "target": 57, "value": 1 }, { "source": 58, "target": 11, "value": 4 }, { "source": 59, "target": 58, "value": 15 }, { "source": 59, "target": 55, "value": 5 }, { "source": 59, "target": 48, "value": 6 }, { "source": 59, "target": 57, "value": 2 }, { "source": 60, "target": 48, "value": 1 }, { "source": 60, "target": 58, "value": 4 }, { "source": 60, "target": 59, "value": 2 }, { "source": 61, "target": 48, "value": 2 }, { "source": 61, "target": 58, "value": 6 }, { "source": 61, "target": 60, "value": 2 }, { "source": 61, "target": 59, "value": 5 }, { "source": 61, "target": 57, "value": 1 }, { "source": 61, "target": 55, "value": 1 }, { "source": 62, "target": 55, "value": 9 }, { "source": 62, "target": 58, "value": 17 }, { "source": 62, "target": 59, "value": 13 }, { "source": 62, "target": 48, "value": 7 }, { "source": 62, "target": 57, "value": 2 }, { "source": 62, "target": 41, "value": 1 }, { "source": 62, "target": 61, "value": 6 }, { "source": 62, "target": 60, "value": 3 }, { "source": 63, "target": 59, "value": 5 }, { "source": 63, "target": 48, "value": 5 }, { "source": 63, "target": 62, "value": 6 }, { "source": 63, "target": 57, "value": 2 }, { "source": 63, "target": 58, "value": 4 }, { "source": 63, "target": 61, "value": 3 }, { "source": 63, "target": 60, "value": 2 }, { "source": 63, "target": 55, "value": 1 }, { "source": 64, "target": 55, "value": 5 }, { "source": 64, "target": 62, "value": 12 }, { "source": 64, "target": 48, "value": 5 }, { "source": 64, "target": 63, "value": 4 }, { "source": 64, "target": 58, "value": 10 }, { "source": 64, "target": 61, "value": 6 }, { "source": 64, "target": 60, "value": 2 }, { "source": 64, "target": 59, "value": 9 }, { "source": 64, "target": 57, "value": 1 }, { "source": 64, "target": 11, "value": 1 }, { "source": 65, "target": 63, "value": 5 }, { "source": 65, "target": 64, "value": 7 }, { "source": 65, "target": 48, "value": 3 }, { "source": 65, "target": 62, "value": 5 }, { "source": 65, "target": 58, "value": 5 }, { "source": 65, "target": 61, "value": 5 }, { "source": 65, "target": 60, "value": 2 }, { "source": 65, "target": 59, "value": 5 }, { "source": 65, "target": 57, "value": 1 }, { "source": 65, "target": 55, "value": 2 }, { "source": 66, "target": 64, "value": 3 }, { "source": 66, "target": 58, "value": 3 }, { "source": 66, "target": 59, "value": 1 }, { "source": 66, "target": 62, "value": 2 }, { "source": 66, "target": 65, "value": 2 }, { "source": 66, "target": 48, "value": 1 }, { "source": 66, "target": 63, "value": 1 }, { "source": 66, "target": 61, "value": 1 }, { "source": 66, "target": 60, "value": 1 }, { "source": 67, "target": 57, "value": 3 }, { "source": 68, "target": 25, "value": 5 }, { "source": 68, "target": 11, "value": 1 }, { "source": 68, "target": 24, "value": 1 }, { "source": 68, "target": 27, "value": 1 }, { "source": 68, "target": 48, "value": 1 }, { "source": 68, "target": 41, "value": 1 }, { "source": 69, "target": 25, "value": 6 }, { "source": 69, "target": 68, "value": 6 }, { "source": 69, "target": 11, "value": 1 }, { "source": 69, "target": 24, "value": 1 }, { "source": 69, "target": 27, "value": 2 }, { "source": 69, "target": 48, "value": 1 }, { "source": 69, "target": 41, "value": 1 }, { "source": 70, "target": 25, "value": 4 }, { "source": 70, "target": 69, "value": 4 }, { "source": 70, "target": 68, "value": 4 }, { "source": 70, "target": 11, "value": 1 }, { "source": 70, "target": 24, "value": 1 }, { "source": 70, "target": 27, "value": 1 }, { "source": 70, "target": 41, "value": 1 }, { "source": 70, "target": 58, "value": 1 }, { "source": 71, "target": 27, "value": 1 }, { "source": 71, "target": 69, "value": 2 }, { "source": 71, "target": 68, "value": 2 }, { "source": 71, "target": 70, "value": 2 }, { "source": 71, "target": 11, "value": 1 }, { "source": 71, "target": 48, "value": 1 }, { "source": 71, "target": 41, "value": 1 }, { "source": 71, "target": 25, "value": 1 }, { "source": 72, "target": 26, "value": 2 }, { "source": 72, "target": 27, "value": 1 }, { "source": 72, "target": 11, "value": 1 }, { "source": 73, "target": 48, "value": 2 }, { "source": 74, "target": 48, "value": 2 }, { "source": 74, "target": 73, "value": 3 }, { "source": 75, "target": 69, "value": 3 }, { "source": 75, "target": 68, "value": 3 }, { "source": 75, "target": 25, "value": 3 }, { "source": 75, "target": 48, "value": 1 }, { "source": 75, "target": 41, "value": 1 }, { "source": 75, "target": 70, "value": 1 }, { "source": 75, "target": 71, "value": 1 }, { "source": 76, "target": 64, "value": 1 }, { "source": 76, "target": 65, "value": 1 }, { "source": 76, "target": 66, "value": 1 }, { "source": 76, "target": 63, "value": 1 }, { "source": 76, "target": 62, "value": 1 }, { "source": 76, "target": 48, "value": 1 }, { "source": 76, "target": 58, "value": 1 }]
};                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"main.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/lib/main.js                                                                                                  //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
d3Graph = {                                                                                                            // 1
    color: '',                                                                                                         // 2
    zoomer: function () {                                                                                              // 3
        function zoomer() {                                                                                            // 3
            var width = 500,                                                                                           // 4
                height = 500;                                                                                          //
            var xScale = d3.scale.linear().domain([0, width]).range([0, width]);                                       // 6
            var yScale = d3.scale.linear().domain([0, height]).range([0, height]);                                     // 8
            return d3.behavior.zoom().scaleExtent([0.1, 10]).x(xScale).y(yScale).on("zoomstart", zoomstart).on("zoom", redraw);
        }                                                                                                              //
                                                                                                                       //
        return zoomer;                                                                                                 //
    }(),                                                                                                               //
    svg: '',                                                                                                           // 17
    force: '',                                                                                                         // 18
    link: '',                                                                                                          // 19
    node: '',                                                                                                          // 20
    linkText: '',                                                                                                      // 21
    graph: {                                                                                                           // 22
        nodes: [],                                                                                                     // 23
        links: []                                                                                                      // 24
    },                                                                                                                 //
    zoomstart: function () {                                                                                           // 26
        function zoomstart() {                                                                                         // 26
            node.each(function (d) {                                                                                   // 27
                d.selected = false;                                                                                    // 28
                d.previouslySelected = false;                                                                          // 29
            });                                                                                                        //
            node.classed("selected", false);                                                                           // 31
        }                                                                                                              //
                                                                                                                       //
        return zoomstart;                                                                                              //
    }(),                                                                                                               //
    getGraphData: function () {                                                                                        // 33
        function getGraphData(nodeId) {                                                                                // 33
                                                                                                                       //
            var invNodes = Inventory.find({ "type": "instance", $and: [{ "host": nodeId }] });                         // 35
                                                                                                                       //
            var edges = [];                                                                                            // 37
            var nodes = [];                                                                                            // 38
                                                                                                                       //
            invNodes.forEach(function (n) {                                                                            // 40
                nodes = n["Entities"];                                                                                 // 41
                edges = n["Relations"];                                                                                // 42
            });                                                                                                        //
                                                                                                                       //
            nodes.forEach(function (n) {                                                                               // 45
                n.name = n.label;                                                                                      // 46
            });                                                                                                        //
                                                                                                                       //
            var edges_new = [];                                                                                        // 49
            edges.forEach(function (e) {                                                                               // 50
                var sourceNode = nodes.filter(function (n) {                                                           // 51
                    return n.id === e.from;                                                                            // 51
                })[0],                                                                                                 //
                    targetNode = nodes.filter(function (n) {                                                           //
                    return n.id === e.to;                                                                              // 52
                })[0];                                                                                                 //
                                                                                                                       //
                edges_new.push({ source: sourceNode, target: targetNode, value: 1, label: e.label, attributes: e.attributes });
            });                                                                                                        //
            //any links with duplicate source and target get an incremented 'linknum'                                  //
            for (var i = 0; i < edges_new.length; i++) {                                                               // 33
                if (i != 0 && edges_new[i].source == edges_new[i - 1].source && edges_new[i].target == edges_new[i - 1].target) {
                    edges_new[i].linknum = edges_new[i - 1].linknum + 1;                                               // 61
                } else {                                                                                               //
                    edges_new[i].linknum = 1;                                                                          // 63
                };                                                                                                     //
            };                                                                                                         //
            //var graph = {};                                                                                          //
            this.graph.nodes = nodes;                                                                                  // 33
            this.graph.links = edges_new;                                                                              // 67
        }                                                                                                              //
                                                                                                                       //
        return getGraphData;                                                                                           //
    }(),                                                                                                               //
    getGraphDataByClique: function () {                                                                                // 70
        function getGraphDataByClique(nodeObjId) {                                                                     // 70
            var cliques = Cliques.find({ focal_point: new Mongo.ObjectID(nodeObjId) }).fetch();                        // 71
            var cliquesLinks = [];                                                                                     // 72
            var nodes = [];                                                                                            // 73
            var edges_new = [];                                                                                        // 74
                                                                                                                       //
            cliques.forEach(function (n) {                                                                             // 76
                cliquesLinks.push(n["link_id"]);                                                                       // 77
            });                                                                                                        //
            var linksList = Links.find({ _id: { $in: cliquesLinks } }).fetch();                                        // 79
            console.log(linksList);                                                                                    // 80
                                                                                                                       //
            linksList.forEach(function (linkItem) {                                                                    // 82
                nodes.push(linkItem["source"]);                                                                        // 83
                nodes.push(linkItem["target"]);                                                                        // 84
            });                                                                                                        //
            var nodesList = Inventory.find({ _id: { $in: nodes } }).fetch();                                           // 86
            linksList.forEach(function (linkItem) {                                                                    // 87
                var sourceNode = nodesList.filter(function (n) {                                                       // 88
                    return n._id._str === linkItem.source._str;                                                        // 88
                })[0],                                                                                                 //
                    targetNode = nodesList.filter(function (n) {                                                       //
                    return n._id._str === linkItem.target._str;                                                        // 89
                })[0];                                                                                                 //
                                                                                                                       //
                edges_new.push({ source: sourceNode, target: targetNode, value: 1, label: linkItem.link_name, attributes: linkItem });
            });                                                                                                        //
            nodesList.forEach(function (nodeItem) {                                                                    // 94
                nodeItem.attributes = [];                                                                              // 95
                var attrHoverFields = NodeHoverAttr.find({ "type": nodeItem["type"] }).fetch();                        // 96
                if (attrHoverFields.length) {                                                                          // 97
                    attrHoverFields[0].attributes.forEach(function (field) {                                           // 98
                        if (nodeItem[field]) {                                                                         // 99
                            var object = {};                                                                           // 100
                            object[field] = nodeItem[field];                                                           // 101
                            nodeItem.attributes.push(object);                                                          // 102
                        }                                                                                              //
                    });                                                                                                //
                }                                                                                                      //
            });                                                                                                        //
                                                                                                                       //
            this.graph.nodes = nodesList;                                                                              // 108
            this.graph.links = edges_new;                                                                              // 109
        }                                                                                                              //
                                                                                                                       //
        return getGraphDataByClique;                                                                                   //
    }(),                                                                                                               //
    creategraphdata: function () {                                                                                     // 112
        function creategraphdata() {                                                                                   // 112
            var self = this;                                                                                           // 113
            var width = 500,                                                                                           // 114
                height = 500;                                                                                          //
                                                                                                                       //
            this.color = d3.scale.category20();                                                                        // 117
            /*                                                                                                         //
                    this.svg = d3.select("#dgraphid").append("svg")                                                    //
                        .attr("width", "100%")                                                                         //
                        .attr("height", "100%")                                                                        //
                        .attr("pointer-events", "all")                                                                 //
                        //.attr('transform', 'translate(250,250) scale(0.3)')                                          //
                        .call(d3.behavior.zoom().on("zoom", this.redraw))                                              //
                        .append('svg:g');                                                                              //
                                                                                                                       //
                    //.append("g");                                                                                    //
                                                                                                                       //
                    this.force = cola.d3adaptor().convergenceThreshold(0.1)                                            //
                        //.linkDistance(200)                                                                           //
                        .size([width, height]);                                                                        //
            */                                                                                                         //
            var focused = null;                                                                                        // 112
                                                                                                                       //
            this.force = cola.d3adaptor().convergenceThreshold(0.1)                                                    // 135
            //.linkDistance(200)                                                                                       //
            .size([width, height]);                                                                                    //
                                                                                                                       //
            var outer = d3.select("#dgraphid").append("svg").attr({ width: "100%", height: "100%", "pointer-events": "all" });
                                                                                                                       //
            outer.append('rect').attr({ "class": 'background', width: "100%", height: "100%" }).call(d3.behavior.zoom().on("zoom", function (d) {
                d3Graph.svg.attr("transform", "translate(" + d3.event.translate + ")" + " scale(" + d3.event.scale + ")");
            })).on("mouseover", function () {                                                                          //
                focused = this;                                                                                        // 148
            });                                                                                                        //
                                                                                                                       //
            d3.select("body").on("keydown", function () {                                                              // 150
                d3.select(focused); /* then do something with it here */                                               // 150
            });                                                                                                        //
                                                                                                                       //
            this.svg = outer.append('g').attr('transform', 'translate(250,250) scale(0.3)');                           // 152
        }                                                                                                              //
                                                                                                                       //
        return creategraphdata;                                                                                        //
    }(),                                                                                                               //
    redraw: function () {                                                                                              // 157
        function redraw() {                                                                                            // 157
            console.log("here", d3.event.translate, d3.event.scale);                                                   // 158
                                                                                                                       //
            d3Graph.svg.attr("transform", "translate(" + d3.event.translate + ")" + " scale(" + d3.event.scale + ")");
        }                                                                                                              //
                                                                                                                       //
        return redraw;                                                                                                 //
    }(),                                                                                                               //
                                                                                                                       //
    updateNetworkGraph: function () {                                                                                  // 166
        function updateNetworkGraph() {                                                                                // 166
            var self = this;                                                                                           // 167
                                                                                                                       //
            this.svg.selectAll('g').remove();                                                                          // 169
            //this.svg.exit().remove();                                                                                //
                                                                                                                       //
            var div = d3.select("body").append("div").attr("class", "tooltip").style("opacity", 0);                    // 166
                                                                                                                       //
            this.force.nodes(this.graph.nodes).links(this.graph.links).symmetricDiffLinkLengths(250)                   // 176
            //.jaccardLinkLengths(300)                                                                                 //
            //.jaccardLinkLengths(80,0.7)                                                                              //
            .handleDisconnected(true).avoidOverlaps(true).start(50, 100, 200);                                         //
                                                                                                                       //
            /*                                                                                                         //
                        this.force                                                                                     //
                        .on("dragstart", function (d) { d3.event.sourceEvent.stopPropagation(); d3.select(this).classed("dragging", true); } )
                        .on("drag", function (d) { d3.select(this).attr("cx", d.x = d3.event.x).attr("cy", d.y = d3.event.y); } )
                        .on("dragend", function (d) { d3.select(this).classed("dragging", false); });                  //
            */                                                                                                         //
                                                                                                                       //
            // Define the div for the tooltip                                                                          //
                                                                                                                       //
            //svg.exit().remove();                                                                                     //
            //graph.constraints = [{"axis":"y", "left":0, "right":1, "gap":25},];                                      //
                                                                                                                       //
            //.start(10,15,20);                                                                                        //
            /*var path = svg.append("svg:g")                                                                           //
                .selectAll("path")                                                                                     //
                .data(force.links())                                                                                   //
                .enter().append("svg:path")                                                                            //
                .attr("class", "link");;                                                                               //
            */                                                                                                         //
            var link = this.svg.selectAll(".link").data(this.force.links()).enter().append("g").attr("class", "link-group").append("line").attr("class", "link").style("stroke-width", function (d) {
                return Math.sqrt(d.stroke);                                                                            // 213
            }).style("stroke", function (d) {                                                                          //
                if (d.label == 'net-103') {                                                                            // 215
                    self.blinkLink(d);                                                                                 // 216
                    return "red";                                                                                      // 217
                }                                                                                                      //
                //return self.color(d.level);                                                                          //
            });                                                                                                        // 214
                                                                                                                       //
            var linkText = this.svg.selectAll(".link-group").append("text").data(this.force.links()).text(function (d) {
                return d.label;                                                                                        // 225
            }).attr("x", function (d) {                                                                                //
                return d.source.x + (d.target.x - d.source.x) * 0.5;                                                   // 226
            }).attr("y", function (d) {                                                                                //
                return d.source.y + (d.target.y - d.source.y) * 0.5;                                                   // 227
            }).attr("dy", ".25em").attr("text-anchor", "right").on("mouseover", function (d) {                         //
                div.transition().duration(200).style("opacity", .9);                                                   // 231
                d.title = "";                                                                                          // 234
                if (d.attributes != undefined) {                                                                       // 235
                    d.title = JSON.stringify(d.attributes, null, 4).toString().replace(/\,/g, '<BR>').replace(/\[/g, '').replace(/\]/g, '').replace(/\{/g, '').replace(/\}/g, '').replace(/"/g, '');
                }                                                                                                      //
                div.html("<p><u>" + d.label + "</u><br/>" + d.title + "<p/>").style("left", d3.event.pageX + "px").style("top", d3.event.pageY - 28 + "px");
            }).on("mouseout", function (d) {                                                                           //
                div.transition().duration(500).style("opacity", 0);                                                    // 243
            });                                                                                                        //
                                                                                                                       //
            var node = this.svg.selectAll(".node").data(this.force.nodes()).enter().append("g").attr("class", "node").call(this.force.drag);
                                                                                                                       //
            node.append("circle").attr("class", "node").attr("r", function (d) {                                       // 257
                return 13;                                                                                             // 259
            }).on("mouseover", function (d) {                                                                          //
                div.transition().duration(200).style("opacity", .9);                                                   // 261
                d.title = "";                                                                                          // 264
                if (d.attributes != undefined) {                                                                       // 265
                    d.title = JSON.stringify(d.attributes, null, 4).toString().replace(/\,/g, '<BR>').replace(/\[/g, '').replace(/\]/g, '').replace(/\{/g, '').replace(/\}/g, '').replace(/"/g, '');
                }                                                                                                      //
                                                                                                                       //
                div.html("<p><u>" + d.name + "</u><br/>" + d.title + "<p/>").style("left", d3.event.pageX + "px").style("top", d3.event.pageY - 28 + "px");
            }).on("mouseout", function (d) {                                                                           //
                div.transition().duration(500).style("opacity", 0);                                                    // 274
            }).style("fill", function (d) {                                                                            //
                if (d.level == 2) {                                                                                    // 279
                    self.blinkNode(d);                                                                                 // 280
                    return "red";                                                                                      // 281
                }                                                                                                      //
                                                                                                                       //
                return self.color(d.group);                                                                            // 284
            }).call(this.force.drag);                                                                                  //
                                                                                                                       //
            /*                                                                                                         //
                        .each(function() {                                                                             //
                            var sel = d3.select(this);                                                                 //
                            var state = false;                                                                         //
                            sel.on('dblclick', function () {                                                           //
                                state = !state;                                                                        //
                                if (state) {                                                                           //
                                    sel.style('fill', 'black');                                                        //
                                } else {                                                                               //
                                    sel.style('fill', function (d) {                                                   //
                                        return d.colr;                                                                 //
                                    });                                                                                //
                                }                                                                                      //
                            });                                                                                        //
                        });                                                                                            //
            */                                                                                                         //
                                                                                                                       //
            node.append("text").attr("dx", 14).attr("dy", ".35em").text(function (d) {                                 // 166
                return d.object_name;                                                                                  // 309
            });                                                                                                        //
                                                                                                                       //
            this.force.on("tick", function () {                                                                        // 312
                link.attr("x1", function (d) {                                                                         // 313
                    return d.source.x;                                                                                 // 313
                }).attr("y1", function (d) {                                                                           //
                    return d.source.y;                                                                                 // 314
                }).attr("x2", function (d) {                                                                           //
                    return d.target.x;                                                                                 // 315
                }).attr("y2", function (d) {                                                                           //
                    return d.target.y;                                                                                 // 316
                });                                                                                                    //
                /*                                                                                                     //
                                .attr("dr1", function(d) { return 75/d.source.linknum; })                              //
                                .attr("dr2", function(d) { return 75/d.target.linknum; });                             //
                */                                                                                                     //
                                                                                                                       //
                node.attr("transform", function (d) {                                                                  // 312
                    return "translate(" + d.x + "," + d.y + ")";                                                       // 322
                });                                                                                                    //
                                                                                                                       //
                linkText.attr("x", function (d) {                                                                      // 324
                    return d.source.x + (d.target.x - d.source.x) * 0.5;                                               // 325
                }).attr("y", function (d) {                                                                            //
                    return d.source.y + (d.target.y - d.source.y) * 0.5;                                               // 326
                });                                                                                                    //
            });                                                                                                        //
        }                                                                                                              //
                                                                                                                       //
        return updateNetworkGraph;                                                                                     //
    }(),                                                                                                               //
    centerview: function () {                                                                                          // 331
        function centerview() {                                                                                        // 331
            // Center the view on the molecule(s) and scale it so that everything                                      //
            // fits in the window                                                                                      //
            var width = 500,                                                                                           // 334
                height = 500;                                                                                          //
                                                                                                                       //
            if (nodeGraph === null) return;                                                                            // 337
                                                                                                                       //
            var nodes = nodeGraph.nodes;                                                                               // 340
                                                                                                                       //
            //no molecules, nothing to do                                                                              //
            if (nodes.length === 0) return;                                                                            // 331
                                                                                                                       //
            // Get the bounding box                                                                                    //
            min_x = d3.min(nodes.map(function (d) {                                                                    // 331
                return d.x;                                                                                            // 347
            }));                                                                                                       //
            min_y = d3.min(nodes.map(function (d) {                                                                    // 348
                return d.y;                                                                                            // 348
            }));                                                                                                       //
                                                                                                                       //
            max_x = d3.max(nodes.map(function (d) {                                                                    // 350
                return d.x;                                                                                            // 350
            }));                                                                                                       //
            max_y = d3.max(nodes.map(function (d) {                                                                    // 351
                return d.y;                                                                                            // 351
            }));                                                                                                       //
                                                                                                                       //
            // The width and the height of the graph                                                                   //
            mol_width = max_x - min_x;                                                                                 // 331
            mol_height = max_y - min_y;                                                                                // 356
                                                                                                                       //
            // how much larger the drawing area is than the width and the height                                       //
            width_ratio = width / mol_width;                                                                           // 331
            height_ratio = height / mol_height;                                                                        // 360
                                                                                                                       //
            // we need to fit it in both directions, so we scale according to                                          //
            // the direction in which we need to shrink the most                                                       //
            min_ratio = Math.min(width_ratio, height_ratio) * 0.8;                                                     // 331
                                                                                                                       //
            // the new dimensions of the molecule                                                                      //
            new_mol_width = mol_width * min_ratio;                                                                     // 331
            new_mol_height = mol_height * min_ratio;                                                                   // 368
                                                                                                                       //
            // translate so that it's in the center of the window                                                      //
            x_trans = -min_x * min_ratio + (width - new_mol_width) / 2;                                                // 331
            y_trans = -min_y * min_ratio + (height - new_mol_height) / 2;                                              // 372
                                                                                                                       //
            // do the actual moving                                                                                    //
            this.svg.attr("transform", "translate(" + [x_trans, y_trans] + ")" + " scale(" + min_ratio + ")");         // 331
                                                                                                                       //
            // tell the zoomer what we did so that next we zoom, it uses the                                           //
            // transformation we entered here                                                                          //
            this.zoomer.translate([x_trans, y_trans]);                                                                 // 331
            this.zoomer.scale(min_ratio);                                                                              // 382
        }                                                                                                              //
                                                                                                                       //
        return centerview;                                                                                             //
    }(),                                                                                                               //
    keydown: function () {                                                                                             // 384
        function keydown() {                                                                                           // 384
            shiftKey = d3.event.shiftKey || d3.event.metaKey;                                                          // 385
            ctrlKey = d3.event.ctrlKey;                                                                                // 386
                                                                                                                       //
            console.log('d3.event', d3.event);                                                                         // 388
                                                                                                                       //
            if (d3.event.keyCode == 67) {                                                                              // 390
                //the 'c' key                                                                                          //
                this.centerview();                                                                                     // 391
            }                                                                                                          //
        }                                                                                                              //
                                                                                                                       //
        return keydown;                                                                                                //
    }(),                                                                                                               //
    blinkNode: function () {                                                                                           // 395
        function blinkNode(node) {                                                                                     // 395
            var nodeList = this.svg.selectAll(".node");                                                                // 396
            var selected = nodeList.filter(function (d, i) {                                                           // 397
                return d.id == node.id;                                                                                // 398
                //return d.name != findFromParent;                                                                     //
            });                                                                                                        // 397
            selected.forEach(function (n) {                                                                            // 401
                for (i = 0; i != 30; i++) {                                                                            // 402
                    $(n[1]).fadeTo('slow', 0.1).fadeTo('slow', 5.0);                                                   // 403
                };                                                                                                     //
            });                                                                                                        //
        }                                                                                                              //
                                                                                                                       //
        return blinkNode;                                                                                              //
    }(),                                                                                                               //
    blinkLink: function () {                                                                                           // 407
        function blinkLink(link) {                                                                                     // 407
            var linkList = this.svg.selectAll(".link");                                                                // 408
            var selected = linkList.filter(function (d, i) {                                                           // 409
                return d.id == link.id;                                                                                // 410
                //return d.name != findFromParent;                                                                     //
            });                                                                                                        // 409
            selected.forEach(function (n) {                                                                            // 413
                for (i = 0; i != 30; i++) {                                                                            // 414
                    $(n[1]).fadeTo('slow', 0.1).fadeTo('slow', 5.0);                                                   // 415
                };                                                                                                     //
            });                                                                                                        //
        }                                                                                                              //
                                                                                                                       //
        return blinkLink;                                                                                              //
    }(),                                                                                                               //
    tick: function () {                                                                                                // 419
        function tick(obj) {                                                                                           // 419
                                                                                                                       //
            obj.link.attr("x1", function (d) {                                                                         // 421
                return d.source.x;                                                                                     // 421
            }).attr("y1", function (d) {                                                                               //
                return d.source.y;                                                                                     // 422
            }).attr("x2", function (d) {                                                                               //
                return d.target.x;                                                                                     // 423
            }).attr("y2", function (d) {                                                                               //
                return d.target.y;                                                                                     // 424
            });                                                                                                        //
                                                                                                                       //
            obj.node.attr("transform", function (d) {                                                                  // 426
                return "translate(" + d.x + "," + d.y + ")";                                                           // 426
            });                                                                                                        //
                                                                                                                       //
            obj.linkText.attr("x", function (d) {                                                                      // 428
                return d.source.x + (d.target.x - d.source.x) * 0.5;                                                   // 429
            }).attr("y", function (d) {                                                                                //
                return d.source.y + (d.target.y - d.source.y) * 0.5;                                                   // 430
            });                                                                                                        //
        }                                                                                                              //
                                                                                                                       //
        return tick;                                                                                                   //
    }()                                                                                                                //
};                                                                                                                     //
menuTree = {                                                                                                           // 433
    menu: {},                                                                                                          // 434
    init: function () {                                                                                                // 435
        function init() {                                                                                              // 435
            this.memu = $('#menu').multilevelpushmenu({                                                                // 436
                menuWidth: '20%',                                                                                      // 437
                menuHeight: '94%',                                                                                     // 438
                containersToPush: [$('#pushobj')],                                                                     // 439
                overlapWidth: 40,                                                                                      // 440
                backItemIcon: 'fa fa-angle-left',                                                                      // 441
                groupIcon: 'fa fa-angle-right',                                                                        // 442
                onItemClick: function () {                                                                             // 443
                    function onItemClick() {                                                                           // 443
                        var event = arguments[0],                                                                      // 444
                            $menuLevelHolder = arguments[1],                                                           //
                            $item = arguments[2],                                                                      //
                            options = arguments[3],                                                                    //
                            title = $menuLevelHolder.find('h2:first').text(),                                          //
                            itemName = $item.find('a:first').text();                                                   //
                        console.log(arguments);                                                                        // 450
                        console.log($item[0]);                                                                         // 451
                        if ($item[0].type == "host_ref" && $item[0].title == 'node-24') {                              // 452
                            if ($item.level > 1) {                                                                     // 453
                                var itemList = $('#menu').multilevelpushmenu('pathtoroot', $item);                     // 454
                                $('.breadcrumb li').remove();                                                          // 455
                                itemList.forEach(function (e) {                                                        // 456
                                    if (e.firstChild.innerText != '' && e.firstChild.innerText != undefined) {         // 457
                                        $('.breadcrumb').append('<li><a href="#">' + e.firstChild.innerText + '</a></li>');
                                    }                                                                                  //
                                });                                                                                    //
                                $('.breadcrumb').append('<li class="active">' + itemName + '</li>');                   // 462
                            }                                                                                          //
                                                                                                                       //
                            Session.set('currNodeId', $item[0].id);                                                    // 465
                            var graphData = d3Graph.getGraphData($item[0].id);                                         // 466
                            d3Graph.updateNetworkGraph(graphData);                                                     // 467
                            /*                                                                                         //
                             myfunc = Template.multilevelorig.__helpers.get("getNodeItems");                           //
                             myfunc($item[0].id);                                                                      //
                             */                                                                                        //
                        } else if ($item.attr("clique") == "true") {                                                   //
                                var graphData = d3Graph.getGraphDataByClique($item.attr("objId"));                     // 452
                                //console.log($item[0].objId);                                                         //
                            }                                                                                          // 474
                        //console.log($item.find( 'a:first' ));                                                        //
                    }                                                                                                  // 443
                                                                                                                       //
                    return onItemClick;                                                                                //
                }(),                                                                                                   //
                onGroupItemClick: function () {                                                                        // 480
                    function onGroupItemClick() {                                                                      // 480
                        var event = arguments[0],                                                                      // 481
                            $menuLevelHolder = arguments[1],                                                           //
                            $item = arguments[2],                                                                      //
                            options = arguments[3],                                                                    //
                            title = $menuLevelHolder.find('h2:first').text(),                                          //
                            itemName = $item.find('a:first').text();                                                   //
                                                                                                                       //
                        console.log($item);                                                                            // 488
                        if ($item.attr("clique") == "true") {                                                          // 489
                            var graphData = d3Graph.getGraphDataByClique($item.attr("objId"));                         // 490
                            d3Graph.updateNetworkGraph(graphData);                                                     // 491
                            console.log($item.attr("objId"));                                                          // 492
                        }                                                                                              //
                    }                                                                                                  //
                                                                                                                       //
                    return onGroupItemClick;                                                                           //
                }()                                                                                                    //
            });                                                                                                        //
        }                                                                                                              //
                                                                                                                       //
        return init;                                                                                                   //
    }()                                                                                                                //
};                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}},"accounts-config.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/accounts-config.js                                                                                           //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
Accounts.ui.config({                                                                                                   // 1
    passwordSignupFields: 'USERNAME_ONLY'                                                                              // 2
});                                                                                                                    //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"d3plusgraph.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/d3plusgraph.js                                                                                               //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
Template.d3plusgraph.rendered = function () {                                                                          // 1
    var sample_data = [{ "name": "alpha", "size": 10 }, { "name": "beta", "size": 12 }, { "name": "gamma", "size": 30 }, { "name": "delta", "size": 26 }, { "name": "epsilon", "size": 12 }, { "name": "zeta", "size": 26 }, { "name": "theta", "size": 11 }, { "name": "eta", "size": 24 }];
    var connections = [{ "source": "alpha", "target": "beta" }, { "source": "alpha", "target": "gamma" }, { "source": "beta", "target": "delta" }, { "source": "beta", "target": "epsilon" }, { "source": "zeta", "target": "gamma" }, { "source": "theta", "target": "gamma" }, { "source": "eta", "target": "gamma" }];
    var invNodes = Inventory.find({ "type": "instance", $and: [{ "host": 'node-25' }] }).fetch();                      // 21
                                                                                                                       //
    var edges = [];                                                                                                    // 23
    var nodes = [];                                                                                                    // 24
                                                                                                                       //
    invNodes.forEach(function (n) {                                                                                    // 26
        nodes = n["Entities"];                                                                                         // 27
        edges = n["Relations"];                                                                                        // 28
    });                                                                                                                //
    nodes.forEach(function (n) {                                                                                       // 30
        n.name = n.label;                                                                                              // 31
    });                                                                                                                //
    var edges_new = [];                                                                                                // 33
    edges.forEach(function (e) {                                                                                       // 34
        var sourceNode = nodes.filter(function (n) {                                                                   // 35
            return n.id === e.from;                                                                                    // 35
        })[0],                                                                                                         //
            targetNode = nodes.filter(function (n) {                                                                   //
            return n.id === e.to;                                                                                      // 36
        })[0];                                                                                                         //
                                                                                                                       //
        edges_new.push({ source: sourceNode, target: targetNode, value: 1, label: e.label });                          // 38
    });                                                                                                                //
                                                                                                                       //
    var visualization = d3plus.viz().container("#viz").type("network").data(nodes).edges(edges_new).size("level").id("id").draw();
};                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"envdialog.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/envdialog.js                                                                                                 //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
Template.envdialog.rendered = function () {                                                                            // 1
    new WOW().init();                                                                                                  // 2
    var dialog = document.querySelector('dialog');                                                                     // 3
    var showDialogButton = document.querySelector('#show-dialog');                                                     // 4
    if (!dialog.showModal) {                                                                                           // 5
        dialogPolyfill.registerDialog(dialog);                                                                         // 6
    }                                                                                                                  //
    showDialogButton.addEventListener('click', function () {                                                           // 8
        dialog.showModal();                                                                                            // 9
    });                                                                                                                //
    dialog.querySelector('.close').addEventListener('click', function () {                                             // 11
        dialog.close();                                                                                                // 12
    });                                                                                                                //
};                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"header.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/header.js                                                                                                    //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
Template.header.events = {};                                                                                           // 1
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"home.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/home.js                                                                                                      //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
Template.home.rendered = function () {                                                                                 // 1
    console.log("Home Render");                                                                                        // 2
    //Router.current().render().data();                                                                                //
};                                                                                                                     // 1
Template.topnavbarmenu.helpers({});                                                                                    // 5
Template.topnavbarmenu.rendered = function () {};                                                                      // 7
Template.topnavbarmenu.events = {                                                                                      // 10
    /*                                                                                                                 //
        "autocompleteselect input": function(event, template, doc) {                                                   //
            console.log("selected ", doc);                                                                             //
        },                                                                                                             //
    */                                                                                                                 //
    /*                                                                                                                 //
        'keyup input#search': function () {                                                                            //
                                                                                                                       //
            /!*AutoCompletion.autocomplete({                                                                           //
                element: 'input#search',       // DOM identifier for the element                                       //
                collection: Inventory,// MeteorJS collection object                                                    //
                field: 'Entities',                    // Document field name to search for                             //
                limit: 10,                         // Max number of elements to show                                   //
                sort: { id: 1 },              // Sort object to filter results with                                    //
                filter: { "host": "node-25","type": "instance" }});                                                    //
            //filter: { 'gender': 'female' }}); // Additional filtering*!/                                             //
        },                                                                                                             //
    */                                                                                                                 //
    "keypress #search": function () {                                                                                  // 29
        function keypressSearch(event, template) {                                                                     // 29
            if (event.which === 13) {                                                                                  // 30
                var instance = Template.instance(),                                                                    // 31
                    findFromParent = instance.$(event.target).val();                                                   //
                console.log("temp val is " + findFromParent);                                                          // 33
                                                                                                                       //
                //var selectedVal = $('#search').val();                                                                //
                var node = svg.selectAll(".node");                                                                     // 30
                if (findFromParent == "none") {                                                                        // 37
                    node.style("stroke", "white").style("stroke-width", "1");                                          // 38
                } else {                                                                                               //
                    var selected = node.filter(function (d, i) {                                                       // 40
                        return d.label.indexOf(findFromParent) < 0;                                                    // 41
                        //return d.name != findFromParent;                                                             //
                    });                                                                                                // 40
                    selected.style("opacity", "0");                                                                    // 44
                    var link = svg.selectAll(".link");                                                                 // 45
                    link.style("opacity", "0");                                                                        // 46
                    d3.selectAll(".node, .link").transition().duration(5000).style("opacity", 1);                      // 47
                }                                                                                                      //
            }                                                                                                          //
                                                                                                                       //
            //return Inventory.find({ "type": "instance", $and: [ { "host": Session.get('currNodeId')} ] }).fetch().map(function(it){ return it.name; });
        }                                                                                                              // 29
                                                                                                                       //
        return keypressSearch;                                                                                         //
    }()                                                                                                                //
};                                                                                                                     //
                                                                                                                       //
Template.d3graph.rendered = function () {                                                                              // 60
    d3Graph.creategraphdata();                                                                                         // 61
    //var graphData = getGraphData("node-25");                                                                         //
    //updateNetworkGraph(graphData);                                                                                   //
    var initgraph = true;                                                                                              // 60
    Tracker.autorun(function () {                                                                                      // 65
        var nodeId = Session.get('currNodeId');                                                                        // 66
        var nodesXY = [];                                                                                              // 67
        if (nodeId) {                                                                                                  // 68
            d3Graph.getGraphData(nodeId);                                                                              // 69
            /*                                                                                                         //
                        d3Graph.force.nodes().forEach(function(e){                                                     //
                            nodesXY.push({id:e.id,x:e.x,y:e.y});                                                       //
                            //graphData.nodes[e] = e.x;                                                                //
                            //graphData.nodes[] = e.y;                                                                 //
                        });                                                                                            //
                        var i=0;                                                                                       //
                        graphData.nodes.forEach(function(e){                                                           //
                            if(e.id==nodesXY[i].id){                                                                   //
                                e.x = nodesXY[i].x;                                                                    //
                                e.y = nodesXY[i].y;                                                                    //
                            }                                                                                          //
                            i++;                                                                                       //
                        });                                                                                            //
                        var j=0;                                                                                       //
                        graphData.links.forEach(function(e){                                                           //
                            if(e.source.id==nodesXY[j].id){                                                            //
                                e.source.x = nodesXY[j].x;                                                             //
                                e.source.y = nodesXY[j].y;                                                             //
                            }                                                                                          //
                            else if(e.target.id==nodesXY[j].id){                                                       //
                                e.target.x = nodesXY[j].x;                                                             //
                                e.target.y = nodesXY[j].y;                                                             //
                            }                                                                                          //
                            j++;                                                                                       //
                        });                                                                                            //
                        console.log(graphData.nodes);                                                                  //
            */                                                                                                         //
            //d3Graph.updateNetworkGraph(graphData);                                                                   //
            if (!initgraph) {                                                                                          // 68
                //d3Graph.start();                                                                                     //
                d3Graph.updateNetworkGraph();                                                                          // 101
            }                                                                                                          //
        }                                                                                                              //
        initgraph = false;                                                                                             // 106
    });                                                                                                                //
};                                                                                                                     //
Template.multilevelorig.events = {                                                                                     // 110
    "click a": function () {                                                                                           // 111
        function clickA(event, template) {                                                                             // 111
            //console.log(event.target.innerText);                                                                     //
            $('#menu').multilevelpushmenu('expand', event.target.innerText);                                           // 113
        }                                                                                                              //
                                                                                                                       //
        return clickA;                                                                                                 //
    }()                                                                                                                //
};                                                                                                                     //
                                                                                                                       //
Template.multilevelorig.rendered = function () {                                                                       // 118
    console.log("multilevelorig Render");                                                                              // 119
                                                                                                                       //
    //Router.current().render().data();                                                                                //
    //Session.set("currEnv","WebEX-Mirantis@Cisco");                                                                   //
    menuTree.init();                                                                                                   // 118
                                                                                                                       //
    //Session.set("currEnv","WebEX-Mirantis@Cisco");                                                                   //
                                                                                                                       //
    /*$('#menu').multilevelpushmenu('option', 'menuHeight', $(document).height());                                     //
    $('#menu').multilevelpushmenu('redraw');                                                                           //
    $(window).resize(function () {                                                                                     //
        $('#menu').multilevelpushmenu('option', 'menuHeight', $(document).height());                                   //
        $('#menu').multilevelpushmenu('redraw');                                                                       //
    });                                                                                                                //
    */                                                                                                                 //
    /*                                                                                                                 //
        Meteor.setTimeout( function(){                                                                                 //
        },1000);                                                                                                       //
    */                                                                                                                 //
                                                                                                                       //
    $(document).ready(function () {                                                                                    // 118
        // HTML markup implementation, overlap mode                                                                    //
        /*                                                                                                             //
                var nodesList = getGraphData("node-25").nodes;                                                         //
                var nodesNames = [];                                                                                   //
                nodesList.forEach(function(n){                                                                         //
                    nodesNames.push(n.label);                                                                          //
                });                                                                                                    //
                nodesNames = nodesNames.sort();                                                                        //
                console.log(nodesNames);                                                                               //
                $('#search').autocomplete({                                                                            //
                    minLength: 0,                                                                                      //
                    source: nodesNames                                                                                 //
                });                                                                                                    //
        */                                                                                                             //
                                                                                                                       //
    });                                                                                                                //
};                                                                                                                     //
Template.envForm.events = {                                                                                            // 158
    "change #envList": function () {                                                                                   // 159
        function changeEnvList(event, template) {                                                                      // 159
            //console.log(event.target.value);                                                                         //
            //Session.set("currEnv",event.target.value);                                                               //
            event.preventDefault();                                                                                    // 162
            menuTree.init();                                                                                           // 163
            Router.go('home', { _id: 1 }, { query: 'env=' + event.target.value });                                     // 164
            Meteor.setTimeout(function () {                                                                            // 165
                window.location.reload();                                                                              // 166
            }, 100);                                                                                                   //
                                                                                                                       //
            //Router.go('/home?'+'env='+event.target.value);                                                           //
            //window.location.reload();                                                                                //
            //$( '#menu' ).multilevelpushmenu( 'redraw' );                                                             //
            //menuTree.init();                                                                                         //
        }                                                                                                              // 159
                                                                                                                       //
        return changeEnvList;                                                                                          //
    }()                                                                                                                //
};                                                                                                                     //
Template.envForm.helpers({                                                                                             // 176
    selected: function () {                                                                                            // 177
        function selected() {                                                                                          // 177
            var controller = Iron.controller();                                                                        // 178
            var envName = controller.state.get('envName');                                                             // 179
            if (envName == this.name) {                                                                                // 180
                console.log(this.name + 'selected');                                                                   // 181
                return 'selected';                                                                                     // 182
            }                                                                                                          //
        }                                                                                                              //
                                                                                                                       //
        return selected;                                                                                               //
    }(),                                                                                                               //
    envList: function () {                                                                                             // 185
        function envList() {                                                                                           // 185
            //return Environments.find({type:"environment"});                                                          //
            return Environments.find({});                                                                              // 187
        }                                                                                                              //
                                                                                                                       //
        return envList;                                                                                                //
    }()                                                                                                                //
});                                                                                                                    //
                                                                                                                       //
Template.multilevelorig.helpers({                                                                                      // 191
    treeItems: function () {                                                                                           // 192
        function treeItems() {                                                                                         // 192
            //console.log(Inventory.find({parent_id: "WebEX-Mirantis@Cisco"}));                                        //
            //return Inventory.find({parent_id: "WebEX-Mirantis@Cisco"});                                              //
            /*                                                                                                         //
                    var currEnv = Router.current().route.getName();                                                    //
                    console.log("*****"+currEnv+"*****");                                                              //
            */                                                                                                         //
            var controller = Iron.controller();                                                                        // 199
            var envName = controller.state.get('envName');                                                             // 200
            return Inventory.find({ environment: envName, parent_id: envName });                                       // 201
        }                                                                                                              //
                                                                                                                       //
        return treeItems;                                                                                              //
    }(),                                                                                                               //
    getNodeItems: function () {                                                                                        // 203
        function getNodeItems(nodeId) {                                                                                // 203
            //console.log(nodeId);                                                                                     //
            //console.log(Inventory.find({parent_id: nodeId}));                                                        //
            return Inventory.find({ parent_id: nodeId });                                                              // 206
        }                                                                                                              //
                                                                                                                       //
        return getNodeItems;                                                                                           //
    }()                                                                                                                //
});                                                                                                                    //
Template.multilevelorigNodeTemplate.helpers({                                                                          // 209
    hasClique: function () {                                                                                           // 210
        function hasClique() {                                                                                         // 210
            var controller = Iron.controller();                                                                        // 211
            var envName = controller.state.get('envName');                                                             // 212
            if (Inventory.find({ parent_id: this.id, parent_type: this.type, environment: envName, clique: true, show_in_tree: true }).count() > 0) {
                console.log("clique=True");                                                                            // 214
                return "true";                                                                                         // 215
            } else {                                                                                                   //
                return "false";                                                                                        // 218
            }                                                                                                          //
        }                                                                                                              //
                                                                                                                       //
        return hasClique;                                                                                              //
    }(),                                                                                                               //
    hasChildren: function () {                                                                                         // 222
        function hasChildren() {                                                                                       // 222
            var controller = Iron.controller();                                                                        // 223
            var envName = controller.state.get('envName');                                                             // 224
            return Inventory.find({ parent_id: this.id, parent_type: this.type, environment: envName, show_in_tree: true }).count() > 0;
        }                                                                                                              //
                                                                                                                       //
        return hasChildren;                                                                                            //
    }(),                                                                                                               //
    children: function () {                                                                                            // 227
        function children() {                                                                                          // 227
            var controller = Iron.controller();                                                                        // 228
            var envName = controller.state.get('envName');                                                             // 229
            return Inventory.find({ parent_id: this.id, parent_type: this.type, environment: envName, show_in_tree: true });
        }                                                                                                              //
                                                                                                                       //
        return children;                                                                                               //
    }()                                                                                                                //
});                                                                                                                    //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"landingpage.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/landingpage.js                                                                                               //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
Template.landingpage.rendered = function () {                                                                          // 1
  new WOW().init();                                                                                                    // 2
};                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"mainInit.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/mainInit.js                                                                                                  //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
Template.mainPage.rendered = function () {                                                                             // 1
    $(window).scroll(function () {                                                                                     // 2
        var windowWidth = $(this).width();                                                                             // 3
        var windowHeight = $(this).height();                                                                           // 4
        var windowScrollTop = $(this).scrollTop();                                                                     // 5
                                                                                                                       //
        // effect - No1                                                                                                //
        if (windowScrollTop > 60) {                                                                                    // 2
            $('.banner h2').css('display', 'none');                                                                    // 9
            $('.banner .info').css('display', 'block');                                                                // 10
        } else {                                                                                                       //
            $('.banner h2').css('display', 'block');                                                                   // 12
            $('.banner .info').css('display', 'none');                                                                 // 13
        }                                                                                                              //
                                                                                                                       //
        // effect - No2                                                                                                //
        var firstAnimation = function firstAnimation() {                                                               // 2
            $('.clients .clients-info').each(function () {                                                             // 18
                $(this).delay(500).animate({ opacity: 1, height: '180', width: '250' }, 2000);                         // 20
            });                                                                                                        //
        };                                                                                                             //
                                                                                                                       //
        // effect - No3                                                                                                //
        var secondAnimation = function secondAnimation() {                                                             // 2
            $('.method:eq(0)').delay(1000).animate({ opacity: 1 }, 'slow', function () {                               // 27
                $(this).find('h4').css('background-color', '#B5C3D5');                                                 // 28
            });                                                                                                        //
            $('.method:eq(1)').delay(2000).animate({ opacity: 1 }, 'slow', function () {                               // 30
                $(this).find('h4').css('background-color', '#B5C3D5');                                                 // 31
            });                                                                                                        //
            $('.method:eq(2)').delay(3000).animate({ opacity: 1 }, 'slow', function () {                               // 33
                $(this).find('h4').css('background-color', '#B5C3D5');                                                 // 34
            });                                                                                                        //
            $('.method:eq(3)').delay(4000).animate({ opacity: 1 }, 'slow', function () {                               // 36
                $(this).find('h4').css('background-color', '#B5C3D5');                                                 // 37
            });                                                                                                        //
        };                                                                                                             //
                                                                                                                       //
        // effect - No4                                                                                                //
        var thirdAnimation = function thirdAnimation() {                                                               // 2
            $('.blogs').find('p').delay(1400).animate({ opacity: 1, left: 0 }, 'slow');                                // 43
            $('.blogs').find('img').delay(2000).animate({ opacity: 1, right: 0 }, 'slow');                             // 44
            $('.blogs').find('button').delay(2500).animate({ opacity: 1, bottom: 0 }, 'slow');                         // 45
        };                                                                                                             //
                                                                                                                       //
        if (windowWidth <= 549) {                                                                                      // 49
            if (windowScrollTop > 600) {                                                                               // 50
                $('.clients').css('background', 'tomato');                                                             // 51
                firstAnimation();                                                                                      // 52
            }                                                                                                          //
            if (windowScrollTop > 1750) {                                                                              // 54
                $('.process').css('background', 'tomato');                                                             // 55
                secondAnimation();                                                                                     // 56
            }                                                                                                          //
            if (windowScrollTop > 3500) {                                                                              // 58
                $('.blogs').css('background', 'tomato');                                                               // 59
                thirdAnimation();                                                                                      // 60
            }                                                                                                          //
        } else if (windowWidth > 549 && windowWidth <= 991) {                                                          //
            if (windowScrollTop > 480) {                                                                               // 63
                $('.clients').css('background', 'tomato');                                                             // 64
                firstAnimation();                                                                                      // 65
            }if (windowScrollTop > 1150) {                                                                             //
                $('.process').css('background', 'tomato');                                                             // 67
                secondAnimation();                                                                                     // 68
            }if (windowScrollTop > 2200) {                                                                             //
                $('.blogs').css('background', 'tomato');                                                               // 70
                thirdAnimation();                                                                                      // 71
            }                                                                                                          //
        } else {                                                                                                       //
            if (windowScrollTop > 450) {                                                                               // 74
                $('.clients').css('background', 'tomato');                                                             // 75
                firstAnimation();                                                                                      // 76
            }if (windowScrollTop > 850) {                                                                              //
                $('.process').css('background', 'tomato');                                                             // 78
                secondAnimation();                                                                                     // 79
            }                                                                                                          //
            if (windowScrollTop > 1600) {                                                                              // 81
                $('.blogs').css('background', 'tomato');                                                               // 82
                thirdAnimation();                                                                                      // 83
            }                                                                                                          //
        }                                                                                                              //
    });                                                                                                                //
};                                                                                                                     //
Template.loading.rendered = function () {                                                                              // 88
    if (!Session.get('loadingSplash')) {                                                                               // 89
        this.loading = window.pleaseWait({                                                                             // 90
            //logo: '/images/Meteor-logo.png',                                                                         //
            logo: '',                                                                                                  // 92
            backgroundColor: '#7f8c8d',                                                                                // 93
            loadingHtml: message + spinner                                                                             // 94
        });                                                                                                            //
        Session.set('loadingSplash', true); // just show loading splash once                                           // 96
    }                                                                                                                  // 89
};                                                                                                                     //
                                                                                                                       //
Template.loading.destroyed = function () {                                                                             // 100
    if (this.loading) {                                                                                                // 101
        this.loading.finish();                                                                                         // 102
    }                                                                                                                  //
};                                                                                                                     //
                                                                                                                       //
var message = '<p class="loading-message">Loading OSDNA</p>';                                                          // 106
var spinner = '<div class="sk-spinner sk-spinner-rotating-plane"></div>';                                              // 107
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"subscriptions.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/subscriptions.js                                                                                             //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
//Meteor.subscribe("inventory");                                                                                       //
//Session.set("currEnv","WebEX-Mirantis@Cisco");                                                                       //
Meteor.subscribe("environments_config");                                                                               // 3
Meteor.subscribe("cliques");                                                                                           // 4
Meteor.subscribe("links");                                                                                             // 5
Meteor.subscribe("attributes_for_hover_on_data");                                                                      // 6
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"threeTest2.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/threeTest2.js                                                                                                //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
var cola3;                                                                                                             // 1
(function (cola3) {                                                                                                    // 2
    var Graph = function () {                                                                                          // 3
        function Graph(parentObject, n, edges, nodeColour) {                                                           // 4
            var _this = this;                                                                                          // 5
            this.edgeList = [];                                                                                        // 6
            this.parentObject = parentObject;                                                                          // 7
            this.rootObject = new THREE.Object3D();                                                                    // 8
            parentObject.add(this.rootObject);                                                                         // 9
            // Create all the node meshes                                                                              //
            this.nodeMeshes = Array(n);                                                                                // 4
            for (var i = 0; i < n; ++i) {                                                                              // 12
                var sphere = this.nodeMeshes[i] = new THREE.Mesh(new THREE.SphereGeometry(1, 10, 10), new THREE.MeshLambertMaterial({ color: nodeColour[i] }));
                this.rootObject.add(sphere);                                                                           // 14
            }                                                                                                          //
            // Create all the edges                                                                                    //
            edges.forEach(function (e) {                                                                               // 4
                _this.edgeList.push(new Edge(_this.rootObject, _this.nodeMeshes[e.source].position, _this.nodeMeshes[e.target].position));
            });                                                                                                        //
        }                                                                                                              //
        Graph.prototype.setNodePositions = function (colaCoords) {                                                     // 21
            var x = colaCoords[0],                                                                                     // 22
                y = colaCoords[1],                                                                                     //
                z = colaCoords[2];                                                                                     //
            for (var i = 0; i < this.nodeMeshes.length; ++i) {                                                         // 23
                var p = this.nodeMeshes[i].position;                                                                   // 24
                p.x = x[i];                                                                                            // 25
                p.y = y[i];                                                                                            // 26
                p.z = z[i];                                                                                            // 27
            }                                                                                                          //
        };                                                                                                             //
        Graph.prototype.update = function () {                                                                         // 30
            this.edgeList.forEach(function (e) {                                                                       // 31
                return e.update();                                                                                     // 31
            });                                                                                                        //
        };                                                                                                             //
        // Remove self from the scene so that the object can be GC'ed                                                  //
        Graph.prototype.destroy = function () {                                                                        // 3
            this.parentObject.remove(this.rootObject);                                                                 // 35
        };                                                                                                             //
        return Graph;                                                                                                  // 37
    }();                                                                                                               //
    cola3.Graph = Graph;                                                                                               // 39
    var Edge = function () {                                                                                           // 40
        function Edge(parentObject, sourcePoint, targetPoint) {                                                        // 41
            this.parentObject = parentObject;                                                                          // 42
            this.sourcePoint = sourcePoint;                                                                            // 43
            this.targetPoint = targetPoint;                                                                            // 44
            this.shape = this.makeCylinder();                                                                          // 45
            parentObject.add(this.shape);                                                                              // 46
        }                                                                                                              //
        Edge.prototype.makeCylinder = function () {                                                                    // 48
            var n = 12,                                                                                                // 49
                points = [],                                                                                           //
                cosh = function cosh(v) {                                                                              //
                return (Math.pow(Math.E, v) + Math.pow(Math.E, -v)) / 2;                                               // 49
            };                                                                                                         //
            var xmax = 2,                                                                                              // 50
                m = 2 * cosh(xmax);                                                                                    //
            for (var i = 0; i < n + 1; i++) {                                                                          // 51
                var x = 2 * xmax * (i - n / 2) / n;                                                                    // 52
                points.push(new THREE.Vector3(cosh(x) / m, 0, (i - n / 2) / n));                                       // 53
            }                                                                                                          //
            var material = new THREE.MeshLambertMaterial({ color: 0xcfcfcf }),                                         // 55
                geometry = new THREE.LatheGeometry(points, 12),                                                        //
                cylinder = new THREE.Mesh(geometry, material);                                                         //
            return cylinder;                                                                                           // 56
        };                                                                                                             //
        Edge.prototype.update = function () {                                                                          // 58
            var a = this.sourcePoint,                                                                                  // 59
                b = this.targetPoint;                                                                                  //
            var m = new THREE.Vector3();                                                                               // 60
            m.addVectors(a, b).divideScalar(2);                                                                        // 61
            this.shape.position = m;                                                                                   // 62
            var origVec = new THREE.Vector3(0, 0, 1); //vector of cylinder                                             // 63
            var targetVec = new THREE.Vector3();                                                                       // 58
            targetVec.subVectors(b, a);                                                                                // 65
            var l = targetVec.length();                                                                                // 66
            this.shape.scale.set(1, 1, l);                                                                             // 67
            targetVec.normalize();                                                                                     // 68
            var angle = Math.acos(origVec.dot(targetVec));                                                             // 69
            var axis = new THREE.Vector3();                                                                            // 70
            axis.crossVectors(origVec, targetVec);                                                                     // 71
            axis.normalize();                                                                                          // 72
            var quaternion = new THREE.Quaternion();                                                                   // 73
            quaternion.setFromAxisAngle(axis, angle);                                                                  // 74
            this.shape.quaternion = quaternion;                                                                        // 75
        };                                                                                                             //
        return Edge;                                                                                                   // 77
    }();                                                                                                               //
    cola3.Edge = Edge;                                                                                                 // 79
})(cola3 || (cola3 = {}));                                                                                             //
                                                                                                                       //
Template.threeTest2.rendered = function () {                                                                           // 82
    var graph = {                                                                                                      // 83
        "nodes": [{ "name": "Myriel", "group": 1 }, { "name": "Napoleon", "group": 1 }, { "name": "Mlle.Baptistine", "group": 1 }, { "name": "Mme.Magloire", "group": 1 }, { "name": "CountessdeLo", "group": 1 }, { "name": "Geborand", "group": 1 }, { "name": "Champtercier", "group": 1 }, { "name": "Cravatte", "group": 1 }, { "name": "Count", "group": 1 }, { "name": "OldMan", "group": 1 }, { "name": "Labarre", "group": 2 }, { "name": "Valjean", "group": 2 }, { "name": "Marguerite", "group": 3 }, { "name": "Mme.deR", "group": 2 }, { "name": "Isabeau", "group": 2 }, { "name": "Gervais", "group": 2 }, { "name": "Tholomyes", "group": 3 }, { "name": "Listolier", "group": 3 }, { "name": "Fameuil", "group": 3 }, { "name": "Blacheville", "group": 3 }, { "name": "Favourite", "group": 3 }, { "name": "Dahlia", "group": 3 }, { "name": "Zephine", "group": 3 }, { "name": "Fantine", "group": 3 }, { "name": "Mme.Thenardier", "group": 4 }, { "name": "Thenardier", "group": 4 }, { "name": "Cosette", "group": 5 }, { "name": "Javert", "group": 4 }, { "name": "Fauchelevent", "group": 0 }, { "name": "Bamatabois", "group": 2 }, { "name": "Perpetue", "group": 3 }, { "name": "Simplice", "group": 2 }, { "name": "Scaufflaire", "group": 2 }, { "name": "Woman1", "group": 2 }, { "name": "Judge", "group": 2 }, { "name": "Champmathieu", "group": 2 }, { "name": "Brevet", "group": 2 }, { "name": "Chenildieu", "group": 2 }, { "name": "Cochepaille", "group": 2 }, { "name": "Pontmercy", "group": 4 }, { "name": "Boulatruelle", "group": 6 }, { "name": "Eponine", "group": 4 }, { "name": "Anzelma", "group": 4 }, { "name": "Woman2", "group": 5 }, { "name": "MotherInnocent", "group": 0 }, { "name": "Gribier", "group": 0 }, { "name": "Jondrette", "group": 7 }, { "name": "Mme.Burgon", "group": 7 }, { "name": "Gavroche", "group": 8 }, { "name": "Gillenormand", "group": 5 }, { "name": "Magnon", "group": 5 }, { "name": "Mlle.Gillenormand", "group": 5 }, { "name": "Mme.Pontmercy", "group": 5 }, { "name": "Mlle.Vaubois", "group": 5 }, { "name": "Lt.Gillenormand", "group": 5 }, { "name": "Marius", "group": 8 }, { "name": "BaronessT", "group": 5 }, { "name": "Mabeuf", "group": 8 }, { "name": "Enjolras", "group": 8 }, { "name": "Combeferre", "group": 8 }, { "name": "Prouvaire", "group": 8 }, { "name": "Feuilly", "group": 8 }, { "name": "Courfeyrac", "group": 8 }, { "name": "Bahorel", "group": 8 }, { "name": "Bossuet", "group": 8 }, { "name": "Joly", "group": 8 }, { "name": "Grantaire", "group": 8 }, { "name": "MotherPlutarch", "group": 9 }, { "name": "Gueulemer", "group": 4 }, { "name": "Babet", "group": 4 }, { "name": "Claquesous", "group": 4 }, { "name": "Montparnasse", "group": 4 }, { "name": "Toussaint", "group": 5 }, { "name": "Child1", "group": 10 }, { "name": "Child2", "group": 10 }, { "name": "Brujon", "group": 4 }, { "name": "Mme.Hucheloup", "group": 8 }],
        "links": [{ "source": 1, "target": 0, "value": 1 }, { "source": 2, "target": 0, "value": 8 }, { "source": 3, "target": 0, "value": 10 }, { "source": 3, "target": 2, "value": 6 }, { "source": 4, "target": 0, "value": 1 }, { "source": 5, "target": 0, "value": 1 }, { "source": 6, "target": 0, "value": 1 }, { "source": 7, "target": 0, "value": 1 }, { "source": 8, "target": 0, "value": 2 }, { "source": 9, "target": 0, "value": 1 }, { "source": 11, "target": 10, "value": 1 }, { "source": 11, "target": 3, "value": 3 }, { "source": 11, "target": 2, "value": 3 }, { "source": 11, "target": 0, "value": 5 }, { "source": 12, "target": 11, "value": 1 }, { "source": 13, "target": 11, "value": 1 }, { "source": 14, "target": 11, "value": 1 }, { "source": 15, "target": 11, "value": 1 }, { "source": 17, "target": 16, "value": 4 }, { "source": 18, "target": 16, "value": 4 }, { "source": 18, "target": 17, "value": 4 }, { "source": 19, "target": 16, "value": 4 }, { "source": 19, "target": 17, "value": 4 }, { "source": 19, "target": 18, "value": 4 }, { "source": 20, "target": 16, "value": 3 }, { "source": 20, "target": 17, "value": 3 }, { "source": 20, "target": 18, "value": 3 }, { "source": 20, "target": 19, "value": 4 }, { "source": 21, "target": 16, "value": 3 }, { "source": 21, "target": 17, "value": 3 }, { "source": 21, "target": 18, "value": 3 }, { "source": 21, "target": 19, "value": 3 }, { "source": 21, "target": 20, "value": 5 }, { "source": 22, "target": 16, "value": 3 }, { "source": 22, "target": 17, "value": 3 }, { "source": 22, "target": 18, "value": 3 }, { "source": 22, "target": 19, "value": 3 }, { "source": 22, "target": 20, "value": 4 }, { "source": 22, "target": 21, "value": 4 }, { "source": 23, "target": 16, "value": 3 }, { "source": 23, "target": 17, "value": 3 }, { "source": 23, "target": 18, "value": 3 }, { "source": 23, "target": 19, "value": 3 }, { "source": 23, "target": 20, "value": 4 }, { "source": 23, "target": 21, "value": 4 }, { "source": 23, "target": 22, "value": 4 }, { "source": 23, "target": 12, "value": 2 }, { "source": 23, "target": 11, "value": 9 }, { "source": 24, "target": 23, "value": 2 }, { "source": 24, "target": 11, "value": 7 }, { "source": 25, "target": 24, "value": 13 }, { "source": 25, "target": 23, "value": 1 }, { "source": 25, "target": 11, "value": 12 }, { "source": 26, "target": 24, "value": 4 }, { "source": 26, "target": 11, "value": 31 }, { "source": 26, "target": 16, "value": 1 }, { "source": 26, "target": 25, "value": 1 }, { "source": 27, "target": 11, "value": 17 }, { "source": 27, "target": 23, "value": 5 }, { "source": 27, "target": 25, "value": 5 }, { "source": 27, "target": 24, "value": 1 }, { "source": 27, "target": 26, "value": 1 }, { "source": 28, "target": 11, "value": 8 }, { "source": 28, "target": 27, "value": 1 }, { "source": 29, "target": 23, "value": 1 }, { "source": 29, "target": 27, "value": 1 }, { "source": 29, "target": 11, "value": 2 }, { "source": 30, "target": 23, "value": 1 }, { "source": 31, "target": 30, "value": 2 }, { "source": 31, "target": 11, "value": 3 }, { "source": 31, "target": 23, "value": 2 }, { "source": 31, "target": 27, "value": 1 }, { "source": 32, "target": 11, "value": 1 }, { "source": 33, "target": 11, "value": 2 }, { "source": 33, "target": 27, "value": 1 }, { "source": 34, "target": 11, "value": 3 }, { "source": 34, "target": 29, "value": 2 }, { "source": 35, "target": 11, "value": 3 }, { "source": 35, "target": 34, "value": 3 }, { "source": 35, "target": 29, "value": 2 }, { "source": 36, "target": 34, "value": 2 }, { "source": 36, "target": 35, "value": 2 }, { "source": 36, "target": 11, "value": 2 }, { "source": 36, "target": 29, "value": 1 }, { "source": 37, "target": 34, "value": 2 }, { "source": 37, "target": 35, "value": 2 }, { "source": 37, "target": 36, "value": 2 }, { "source": 37, "target": 11, "value": 2 }, { "source": 37, "target": 29, "value": 1 }, { "source": 38, "target": 34, "value": 2 }, { "source": 38, "target": 35, "value": 2 }, { "source": 38, "target": 36, "value": 2 }, { "source": 38, "target": 37, "value": 2 }, { "source": 38, "target": 11, "value": 2 }, { "source": 38, "target": 29, "value": 1 }, { "source": 39, "target": 25, "value": 1 }, { "source": 40, "target": 25, "value": 1 }, { "source": 41, "target": 24, "value": 2 }, { "source": 41, "target": 25, "value": 3 }, { "source": 42, "target": 41, "value": 2 }, { "source": 42, "target": 25, "value": 2 }, { "source": 42, "target": 24, "value": 1 }, { "source": 43, "target": 11, "value": 3 }, { "source": 43, "target": 26, "value": 1 }, { "source": 43, "target": 27, "value": 1 }, { "source": 44, "target": 28, "value": 3 }, { "source": 44, "target": 11, "value": 1 }, { "source": 45, "target": 28, "value": 2 }, { "source": 47, "target": 46, "value": 1 }, { "source": 48, "target": 47, "value": 2 }, { "source": 48, "target": 25, "value": 1 }, { "source": 48, "target": 27, "value": 1 }, { "source": 48, "target": 11, "value": 1 }, { "source": 49, "target": 26, "value": 3 }, { "source": 49, "target": 11, "value": 2 }, { "source": 50, "target": 49, "value": 1 }, { "source": 50, "target": 24, "value": 1 }, { "source": 51, "target": 49, "value": 9 }, { "source": 51, "target": 26, "value": 2 }, { "source": 51, "target": 11, "value": 2 }, { "source": 52, "target": 51, "value": 1 }, { "source": 52, "target": 39, "value": 1 }, { "source": 53, "target": 51, "value": 1 }, { "source": 54, "target": 51, "value": 2 }, { "source": 54, "target": 49, "value": 1 }, { "source": 54, "target": 26, "value": 1 }, { "source": 55, "target": 51, "value": 6 }, { "source": 55, "target": 49, "value": 12 }, { "source": 55, "target": 39, "value": 1 }, { "source": 55, "target": 54, "value": 1 }, { "source": 55, "target": 26, "value": 21 }, { "source": 55, "target": 11, "value": 19 }, { "source": 55, "target": 16, "value": 1 }, { "source": 55, "target": 25, "value": 2 }, { "source": 55, "target": 41, "value": 5 }, { "source": 55, "target": 48, "value": 4 }, { "source": 56, "target": 49, "value": 1 }, { "source": 56, "target": 55, "value": 1 }, { "source": 57, "target": 55, "value": 1 }, { "source": 57, "target": 41, "value": 1 }, { "source": 57, "target": 48, "value": 1 }, { "source": 58, "target": 55, "value": 7 }, { "source": 58, "target": 48, "value": 7 }, { "source": 58, "target": 27, "value": 6 }, { "source": 58, "target": 57, "value": 1 }, { "source": 58, "target": 11, "value": 4 }, { "source": 59, "target": 58, "value": 15 }, { "source": 59, "target": 55, "value": 5 }, { "source": 59, "target": 48, "value": 6 }, { "source": 59, "target": 57, "value": 2 }, { "source": 60, "target": 48, "value": 1 }, { "source": 60, "target": 58, "value": 4 }, { "source": 60, "target": 59, "value": 2 }, { "source": 61, "target": 48, "value": 2 }, { "source": 61, "target": 58, "value": 6 }, { "source": 61, "target": 60, "value": 2 }, { "source": 61, "target": 59, "value": 5 }, { "source": 61, "target": 57, "value": 1 }, { "source": 61, "target": 55, "value": 1 }, { "source": 62, "target": 55, "value": 9 }, { "source": 62, "target": 58, "value": 17 }, { "source": 62, "target": 59, "value": 13 }, { "source": 62, "target": 48, "value": 7 }, { "source": 62, "target": 57, "value": 2 }, { "source": 62, "target": 41, "value": 1 }, { "source": 62, "target": 61, "value": 6 }, { "source": 62, "target": 60, "value": 3 }, { "source": 63, "target": 59, "value": 5 }, { "source": 63, "target": 48, "value": 5 }, { "source": 63, "target": 62, "value": 6 }, { "source": 63, "target": 57, "value": 2 }, { "source": 63, "target": 58, "value": 4 }, { "source": 63, "target": 61, "value": 3 }, { "source": 63, "target": 60, "value": 2 }, { "source": 63, "target": 55, "value": 1 }, { "source": 64, "target": 55, "value": 5 }, { "source": 64, "target": 62, "value": 12 }, { "source": 64, "target": 48, "value": 5 }, { "source": 64, "target": 63, "value": 4 }, { "source": 64, "target": 58, "value": 10 }, { "source": 64, "target": 61, "value": 6 }, { "source": 64, "target": 60, "value": 2 }, { "source": 64, "target": 59, "value": 9 }, { "source": 64, "target": 57, "value": 1 }, { "source": 64, "target": 11, "value": 1 }, { "source": 65, "target": 63, "value": 5 }, { "source": 65, "target": 64, "value": 7 }, { "source": 65, "target": 48, "value": 3 }, { "source": 65, "target": 62, "value": 5 }, { "source": 65, "target": 58, "value": 5 }, { "source": 65, "target": 61, "value": 5 }, { "source": 65, "target": 60, "value": 2 }, { "source": 65, "target": 59, "value": 5 }, { "source": 65, "target": 57, "value": 1 }, { "source": 65, "target": 55, "value": 2 }, { "source": 66, "target": 64, "value": 3 }, { "source": 66, "target": 58, "value": 3 }, { "source": 66, "target": 59, "value": 1 }, { "source": 66, "target": 62, "value": 2 }, { "source": 66, "target": 65, "value": 2 }, { "source": 66, "target": 48, "value": 1 }, { "source": 66, "target": 63, "value": 1 }, { "source": 66, "target": 61, "value": 1 }, { "source": 66, "target": 60, "value": 1 }, { "source": 67, "target": 57, "value": 3 }, { "source": 68, "target": 25, "value": 5 }, { "source": 68, "target": 11, "value": 1 }, { "source": 68, "target": 24, "value": 1 }, { "source": 68, "target": 27, "value": 1 }, { "source": 68, "target": 48, "value": 1 }, { "source": 68, "target": 41, "value": 1 }, { "source": 69, "target": 25, "value": 6 }, { "source": 69, "target": 68, "value": 6 }, { "source": 69, "target": 11, "value": 1 }, { "source": 69, "target": 24, "value": 1 }, { "source": 69, "target": 27, "value": 2 }, { "source": 69, "target": 48, "value": 1 }, { "source": 69, "target": 41, "value": 1 }, { "source": 70, "target": 25, "value": 4 }, { "source": 70, "target": 69, "value": 4 }, { "source": 70, "target": 68, "value": 4 }, { "source": 70, "target": 11, "value": 1 }, { "source": 70, "target": 24, "value": 1 }, { "source": 70, "target": 27, "value": 1 }, { "source": 70, "target": 41, "value": 1 }, { "source": 70, "target": 58, "value": 1 }, { "source": 71, "target": 27, "value": 1 }, { "source": 71, "target": 69, "value": 2 }, { "source": 71, "target": 68, "value": 2 }, { "source": 71, "target": 70, "value": 2 }, { "source": 71, "target": 11, "value": 1 }, { "source": 71, "target": 48, "value": 1 }, { "source": 71, "target": 41, "value": 1 }, { "source": 71, "target": 25, "value": 1 }, { "source": 72, "target": 26, "value": 2 }, { "source": 72, "target": 27, "value": 1 }, { "source": 72, "target": 11, "value": 1 }, { "source": 73, "target": 48, "value": 2 }, { "source": 74, "target": 48, "value": 2 }, { "source": 74, "target": 73, "value": 3 }, { "source": 75, "target": 69, "value": 3 }, { "source": 75, "target": 68, "value": 3 }, { "source": 75, "target": 25, "value": 3 }, { "source": 75, "target": 48, "value": 1 }, { "source": 75, "target": 41, "value": 1 }, { "source": 75, "target": 70, "value": 1 }, { "source": 75, "target": 71, "value": 1 }, { "source": 76, "target": 64, "value": 1 }, { "source": 76, "target": 65, "value": 1 }, { "source": 76, "target": 66, "value": 1 }, { "source": 76, "target": 63, "value": 1 }, { "source": 76, "target": 62, "value": 1 }, { "source": 76, "target": 48, "value": 1 }, { "source": 76, "target": 58, "value": 1 }]
    };                                                                                                                 //
    var scene = new THREE.Scene();                                                                                     // 420
    var camera = new THREE.PerspectiveCamera(80, window.innerWidth / window.innerHeight, 0.1, 1000);                   // 421
    var renderer = new THREE.WebGLRenderer({ antialias: true });                                                       // 422
    var sizeRatio = 1;                                                                                                 // 423
    var div = document.getElementById("canvas-force");                                                                 // 424
    renderer.setSize(window.innerWidth * sizeRatio, window.innerHeight * sizeRatio - div.offsetTop);                   // 425
    div.appendChild(renderer.domElement);                                                                              // 426
    var colaObject = new THREE.Object3D();                                                                             // 427
    colaObject.position = new THREE.Vector3();                                                                         // 428
    scene.add(colaObject);                                                                                             // 429
    var ambient = new THREE.AmbientLight(0x1f1f1f);                                                                    // 430
    scene.add(ambient);                                                                                                // 431
    var directionalLight = new THREE.DirectionalLight(0xffeedd);                                                       // 432
    directionalLight.position.set(0, 0, 1);                                                                            // 433
    scene.add(directionalLight);                                                                                       // 434
    var n = graph.nodes.length;                                                                                        // 435
    var color = d3.scale.category20();                                                                                 // 436
    var nodeColourings = graph.nodes.map(function (v) {                                                                // 437
        var str = color(v.group).replace("#", "0x");                                                                   // 438
        return parseInt(str);                                                                                          // 439
    });                                                                                                                //
    var colaGraph = new cola3.Graph(colaObject, n, graph.links, nodeColourings);                                       // 441
    var layout = new cola.Layout3D(graph.nodes, graph.links, 6);                                                       // 442
    layout.start(10);                                                                                                  // 443
    camera.position.z = 50;                                                                                            // 444
    var xAngle = 0;                                                                                                    // 445
    var yAngle = 0;                                                                                                    // 446
    document.onmousedown = mousedownhandler;                                                                           // 447
    document.onmouseup = mouseuphandler;                                                                               // 448
    document.onmousemove = mousemovehandler;                                                                           // 449
    var mouse = {                                                                                                      // 450
        down: false,                                                                                                   // 451
        x: 0, y: 0,                                                                                                    // 452
        dx: 0, dy: 0                                                                                                   // 453
    };                                                                                                                 //
    function mousedownhandler(e) {                                                                                     // 455
        mouse.down = true;                                                                                             // 456
        mouse.x = e.clientX;                                                                                           // 457
        mouse.y = e.clientY;                                                                                           // 458
    }                                                                                                                  //
    function mouseuphandler(e) {                                                                                       // 460
        mouse.down = false;                                                                                            // 461
    }                                                                                                                  //
    function mousemovehandler(e) {                                                                                     // 463
        if (mouse.down) {                                                                                              // 464
            mouse.dx = e.clientX - mouse.x;                                                                            // 465
            mouse.x = e.clientX;                                                                                       // 466
            mouse.dy = e.clientY - mouse.y;                                                                            // 467
            mouse.y = e.clientY;                                                                                       // 468
        }                                                                                                              //
    }                                                                                                                  //
    var delta = Number.POSITIVE_INFINITY;                                                                              // 471
    var converged = false;                                                                                             // 472
    var render = function render() {                                                                                   // 473
        xAngle += mouse.dx / 100;                                                                                      // 474
        yAngle += mouse.dy / 100;                                                                                      // 475
        colaObject.rotation.set(yAngle, xAngle, 0);                                                                    // 476
        var s = converged ? 0 : layout.tick();                                                                         // 477
        if (s != 0 && Math.abs(Math.abs(delta / s) - 1) > 1e-7) {                                                      // 478
            delta = s;                                                                                                 // 479
            colaGraph.setNodePositions(layout.result);                                                                 // 480
            colaGraph.update(); // Update all the edge positions                                                       // 481
        } else {                                                                                                       // 478
                converged = true;                                                                                      // 484
            }                                                                                                          //
        renderer.render(scene, camera);                                                                                // 486
        requestAnimationFrame(render);                                                                                 // 487
    };                                                                                                                 //
    render();                                                                                                          // 489
                                                                                                                       //
    /*                                                                                                                 //
    var config={};                                                                                                     //
    config.gravity = 0.3;                                                                                              //
    config.charge = -400;                                                                                              //
    var data = threeTestData;                                                                                          //
          var forceTHREE = new D3THREE();                                                                              //
        forceTHREE.init('canvas-force');                                                                               //
        var forceViz = new D3THREE.Force(forceTHREE);                                                                  //
          var threeData = data;                                                                                        //
          var color = d3.scale.category20();                                                                           //
          var spheres = [], three_links = [];                                                                          //
        // Define the 3d force                                                                                         //
        var force = d3.layout.force3d()                                                                                //
            .nodes(sort_data=[])                                                                                       //
            .links(links=[])                                                                                           //
            .size([50, 50])                                                                                            //
            .gravity(config.gravity)                                                                                   //
            .charge(config.charge);                                                                                    //
          var DISTANCE = 1;                                                                                            //
          for (var i = 0; i < threeData.nodes.length; i++) {                                                           //
            sort_data.push({x:threeData.nodes[i].x + DISTANCE,y:threeData.nodes[i].y + DISTANCE,z:0});                 //
              // set up the sphere vars                                                                                //
            var radius = 5,                                                                                            //
                segments = 16,                                                                                         //
                rings = 16;                                                                                            //
              // create the sphere's material                                                                          //
            var nodeColor = +color(threeData.nodes[i].group).replace("#", "0x");                                       //
            var sphereMaterial = new THREE.MeshBasicMaterial({ color: nodeColor });                                    //
              var sphere = new THREE.Mesh(                                                                             //
                new THREE.SphereGeometry(                                                                              //
                    radius,                                                                                            //
                    segments,                                                                                          //
                    rings),                                                                                            //
                sphereMaterial);                                                                                       //
              spheres.push(sphere);                                                                                    //
              // add the sphere to the scene                                                                           //
            forceViz._dt.scene.add(sphere);                                                                            //
        }                                                                                                              //
          for (var i = 0; i < threeData.links.length; i++) {                                                           //
            links.push({target:sort_data[threeData.links[i].target],source:sort_data[threeData.links[i].source]});     //
              var material = new THREE.LineBasicMaterial({ color: forceViz._config.linkColor,                          //
                linewidth: forceViz._config.linkWidth});                                                               //
            var geometry = new THREE.Geometry();                                                                       //
              geometry.vertices.push( new THREE.Vector3( 0, 0, 0 ) );                                                  //
            geometry.vertices.push( new THREE.Vector3( 0, 0, 0 ) );                                                    //
            var line = new THREE.Line( geometry, material );                                                           //
            line.userData = { source: threeData.links[i].source,                                                       //
                target: threeData.links[i].target };                                                                   //
            three_links.push(line);                                                                                    //
            forceViz._dt.scene.add(line);                                                                              //
        }                                                                                                              //
          force.start();                                                                                               //
          // set up the axes                                                                                           //
        var x = d3.scale.linear().domain([0, 350]).range([0, 10]),                                                     //
            y = d3.scale.linear().domain([0, 350]).range([0, 10]),                                                     //
            z = d3.scale.linear().domain([0, 350]).range([0, 10]);                                                     //
          var self = forceViz;                                                                                         //
        force.on("tick", function(e) {                                                                                 //
            for (var i = 0; i < sort_data.length; i++) {                                                               //
                spheres[i].position.set(x(sort_data[i].x) * 40 - 40, y(sort_data[i].y) * 40 - 40,z(sort_data[i].z) * 40 - 40);
                  for (var j = 0; j < three_links.length; j++) {                                                       //
                    var line = three_links[j];                                                                         //
                    var vi = -1;                                                                                       //
                    if (line.userData.source === i) {                                                                  //
                        vi = 0;                                                                                        //
                    }                                                                                                  //
                    if (line.userData.target === i) {                                                                  //
                        vi = 1;                                                                                        //
                    }                                                                                                  //
                        if (vi >= 0) {                                                                                 //
                        line.geometry.vertices[vi].x = x(sort_data[i].x) * 40 - 40;                                    //
                        line.geometry.vertices[vi].y = y(sort_data[i].y) * 40 - 40;                                    //
                        line.geometry.vertices[vi].z = y(sort_data[i].z) * 40 - 40;                                    //
                        line.geometry.verticesNeedUpdate = true;                                                       //
                    }                                                                                                  //
                }                                                                                                      //
            }                                                                                                          //
        });                                                                                                            //
          // call animate loop                                                                                         //
        forceTHREE.animate();                                                                                          //
    */                                                                                                                 //
};                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"threejsTest.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// client/threejsTest.js                                                                                               //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
/*(function() {                                                                                                        //
// D3.layout.force3d.js                                                                                                //
// (C) 2012 ziggy.jonsson.nyc@gmail.com                                                                                //
// BSD license (http://opensource.org/licenses/BSD-3-Clause)                                                           //
                                                                                                                       //
    d3.layout.force3d = function() {                                                                                   //
        var  forceXY = d3.layout.force()                                                                               //
            ,forceZ = d3.layout.force()                                                                                //
            ,zNodes = {}                                                                                               //
            ,zLinks = {}                                                                                               //
            ,nodeID = 1                                                                                                //
            ,linkID = 1                                                                                                //
            ,tickFunction = Object                                                                                     //
                                                                                                                       //
        var force3d = {}                                                                                               //
                                                                                                                       //
        Object.keys(forceXY).forEach(function(d) {                                                                     //
            force3d[d] = function() {                                                                                  //
                var result = forceXY[d].apply(this,arguments)                                                          //
                if (d !="nodes" && d!="links")  forceZ[d].apply(this,arguments)                                        //
                return (result == forceXY) ? force3d : result                                                          //
            }                                                                                                          //
        })                                                                                                             //
                                                                                                                       //
                                                                                                                       //
        force3d.on = function(name,fn) {                                                                               //
            tickFunction = fn                                                                                          //
            return force3d                                                                                             //
        }                                                                                                              //
                                                                                                                       //
                                                                                                                       //
        forceXY.on("tick",function() {                                                                                 //
                                                                                                                       //
            // Refresh zNodes add new, delete removed                                                                  //
            var _zNodes = {}                                                                                           //
            forceXY.nodes().forEach(function(d,i) {                                                                    //
                if (!d.id) d.id = nodeID++                                                                             //
                _zNodes[d.id] = zNodes[d.id] ||  {x:d.z,px:d.z,py:d.z,y:d.z,id:d.id}                                   //
                d.z =  _zNodes[d.id].x                                                                                 //
            })                                                                                                         //
            zNodes = _zNodes                                                                                           //
                                                                                                                       //
            // Refresh zLinks add new, delete removed                                                                  //
            var _zLinks = {}                                                                                           //
            forceXY.links().forEach(function(d) {                                                                      //
                var nytt = false                                                                                       //
                if (!d.linkID) { d.linkID = linkID++;nytt=true}                                                        //
                _zLinks[d.linkID] = zLinks[d.linkID]  || {target:zNodes[d.target.id],source:zNodes[d.source.id]}       //
                                                                                                                       //
            })                                                                                                         //
            zLinks = _zLinks                                                                                           //
                                                                                                                       //
            // Update the nodes/links in forceZ                                                                        //
            forceZ.nodes(d3.values(zNodes))                                                                            //
            forceZ.links(d3.values(zLinks))                                                                            //
            forceZ.start() // Need to kick forceZ so we don't lose the update mechanism                                //
                                                                                                                       //
            // And run the user defined function, if defined                                                           //
            tickFunction()                                                                                             //
        })                                                                                                             //
                                                                                                                       //
        // Expose the sub-forces for debugging purposes                                                                //
        force3d.xy = forceXY                                                                                           //
        force3d.z = forceZ                                                                                             //
                                                                                                                       //
        return force3d                                                                                                 //
    }                                                                                                                  //
})()*/                                                                                                                 //
Template.threeTest.rendered = function () {                                                                            // 69
    function getGraphData() {                                                                                          // 70
        nodeId = 'node-24';                                                                                            // 71
        //d3.json("miserables.json", function(error, graph) {                                                          //
                                                                                                                       //
        //var invNodes = Inventory.find({ "type": "instance", $and: [ { "id": nodeId } ] });                           //
        var invNodes = Inventory.find({ "type": "instance", $and: [{ "host": nodeId }] });                             // 70
                                                                                                                       //
        var edges = [];                                                                                                // 77
        var nodes = [];                                                                                                // 78
                                                                                                                       //
        invNodes.forEach(function (n) {                                                                                // 80
            nodes = n["Entities"];                                                                                     // 81
            edges = n["Relations"];                                                                                    // 82
        });                                                                                                            //
        //console.log(testNodes);                                                                                      //
        //var invEdges = Inventory.find({ "type": "instance", $and: [ { "id": nodeId } ] }["Edges"]);                  //
                                                                                                                       //
        //var invEdges = EdgesList.find(nodeId).fetch();                                                               //
        //var invNodes = NodesList.find(nodeId).fetch();                                                               //
        //console.log(invEdges);                                                                                       //
                                                                                                                       //
        /*                                                                                                             //
         var edges = Edges.find().fetch();                                                                             //
         var nodes = Nodes.find().fetch();                                                                             //
         */                                                                                                            //
                                                                                                                       //
        nodes.forEach(function (n) {                                                                                   // 70
            n.name = n.label;                                                                                          // 98
            n.x = Math.random();                                                                                       // 99
            n.y = Math.random();                                                                                       // 100
        });                                                                                                            //
        var edges_new = [];                                                                                            // 102
        edges.forEach(function (e) {                                                                                   // 103
            var sourceNode = nodes.filter(function (n) {                                                               // 104
                return n.id === e.from;                                                                                // 104
            })[0],                                                                                                     //
                targetNode = nodes.filter(function (n) {                                                               //
                return n.id === e.to;                                                                                  // 105
            })[0];                                                                                                     //
                                                                                                                       //
            edges_new.push({ source: sourceNode, target: targetNode, value: 1, label: e.label, attributes: e.attributes });
        });                                                                                                            //
                                                                                                                       //
        var graph = {};                                                                                                // 110
        graph.nodes = nodes;                                                                                           // 111
        graph.links = edges_new;                                                                                       // 112
                                                                                                                       //
        //console.log(graph);                                                                                          //
                                                                                                                       //
        return graph;                                                                                                  // 70
    }                                                                                                                  //
                                                                                                                       //
    var graph = getGraphData();                                                                                        // 120
                                                                                                                       //
    var color = d3.scale.category20();                                                                                 // 122
                                                                                                                       //
    var WIDTH = 700,                                                                                                   // 125
        HEIGHT = 700;                                                                                                  //
                                                                                                                       //
    var COLOR = "#0f608b";                                                                                             // 127
    var LINK_COLOR = "#999999";                                                                                        // 128
                                                                                                                       //
    var scene = new THREE.Scene();                                                                                     // 130
                                                                                                                       //
    // set some camera attributes                                                                                      //
    var VIEW_ANGLE = 45,                                                                                               // 69
        ASPECT = WIDTH / HEIGHT,                                                                                       //
        NEAR = 0.1,                                                                                                    //
        FAR = 10000;                                                                                                   //
                                                                                                                       //
    // get the DOM element to attach to                                                                                //
    // - assume we've got jQuery to hand                                                                               //
    var $container = $('#threeGraph');                                                                                 // 69
                                                                                                                       //
    // create a WebGL renderer, camera                                                                                 //
    // and a scene                                                                                                     //
    var renderer = new THREE.WebGLRenderer({ alpha: true,                                                              // 69
        antialiasing: true });                                                                                         // 145
                                                                                                                       //
    renderer.setClearColor(0x000000, 0);                                                                               // 147
                                                                                                                       //
    var camera = new THREE.PerspectiveCamera(VIEW_ANGLE, ASPECT, NEAR, FAR);                                           // 149
                                                                                                                       //
    var scene = new THREE.Scene();                                                                                     // 156
                                                                                                                       //
    // add the camera to the scene                                                                                     //
    scene.add(camera);                                                                                                 // 69
                                                                                                                       //
    // the camera starts at 0,0,0                                                                                      //
    // so pull it back                                                                                                 //
    camera.position.z = 300;                                                                                           // 69
                                                                                                                       //
    // start the renderer                                                                                              //
    renderer.setSize(WIDTH, HEIGHT);                                                                                   // 69
                                                                                                                       //
    // attach the render-supplied DOM element                                                                          //
    $container.append(renderer.domElement);                                                                            // 69
                                                                                                                       //
    var spheres = [],                                                                                                  // 171
        three_links = [];                                                                                              //
                                                                                                                       //
    // Define the 3d force                                                                                             //
    var force = d3.layout.force3d().nodes(sort_data = []).links(links = []).size([50, 50]).gravity(0.3).charge(-400);  // 69
                                                                                                                       //
    var DISTANCE = 1;                                                                                                  // 181
    //    var data = graph;                                                                                            //
    var data = {                                                                                                       // 69
        "nodes": [{                                                                                                    // 184
            "x": 469,                                                                                                  // 186
            "y": 410                                                                                                   // 187
        }, {                                                                                                           //
            "x": 493,                                                                                                  // 190
            "y": 364                                                                                                   // 191
        }, {                                                                                                           //
            "x": 442,                                                                                                  // 194
            "y": 365                                                                                                   // 195
        }, {                                                                                                           //
            "x": 467,                                                                                                  // 198
            "y": 314                                                                                                   // 199
        }, {                                                                                                           //
            "x": 477,                                                                                                  // 202
            "y": 248                                                                                                   // 203
        }, {                                                                                                           //
            "x": 425,                                                                                                  // 206
            "y": 207                                                                                                   // 207
        }, {                                                                                                           //
            "x": 402,                                                                                                  // 210
            "y": 155                                                                                                   // 211
        }, {                                                                                                           //
            "x": 369,                                                                                                  // 214
            "y": 196                                                                                                   // 215
        }, {                                                                                                           //
            "x": 350,                                                                                                  // 218
            "y": 148                                                                                                   // 219
        }, {                                                                                                           //
            "x": 539,                                                                                                  // 222
            "y": 222                                                                                                   // 223
        }, {                                                                                                           //
            "x": 594,                                                                                                  // 226
            "y": 235                                                                                                   // 227
        }, {                                                                                                           //
            "x": 582,                                                                                                  // 230
            "y": 185                                                                                                   // 231
        }, {                                                                                                           //
            "x": 633,                                                                                                  // 234
            "y": 200                                                                                                   // 235
        }],                                                                                                            //
        "links": [{                                                                                                    // 238
            "source": 0,                                                                                               // 240
            "target": 1                                                                                                // 241
        }, {                                                                                                           //
            "source": 1,                                                                                               // 244
            "target": 2                                                                                                // 245
        }, {                                                                                                           //
            "source": 2,                                                                                               // 248
            "target": 0                                                                                                // 249
        }, {                                                                                                           //
            "source": 1,                                                                                               // 252
            "target": 3                                                                                                // 253
        }, {                                                                                                           //
            "source": 3,                                                                                               // 256
            "target": 2                                                                                                // 257
        }, {                                                                                                           //
            "source": 3,                                                                                               // 260
            "target": 4                                                                                                // 261
        }, {                                                                                                           //
            "source": 4,                                                                                               // 264
            "target": 5                                                                                                // 265
        }, {                                                                                                           //
            "source": 5,                                                                                               // 268
            "target": 6                                                                                                // 269
        }, {                                                                                                           //
            "source": 5,                                                                                               // 272
            "target": 7                                                                                                // 273
        }, {                                                                                                           //
            "source": 6,                                                                                               // 276
            "target": 7                                                                                                // 277
        }, {                                                                                                           //
            "source": 6,                                                                                               // 280
            "target": 8                                                                                                // 281
        }, {                                                                                                           //
            "source": 7,                                                                                               // 284
            "target": 8                                                                                                // 285
        }, {                                                                                                           //
            "source": 9,                                                                                               // 288
            "target": 4                                                                                                // 289
        }, {                                                                                                           //
            "source": 9,                                                                                               // 292
            "target": 11                                                                                               // 293
        }, {                                                                                                           //
            "source": 9,                                                                                               // 296
            "target": 10                                                                                               // 297
        }, {                                                                                                           //
            "source": 10,                                                                                              // 300
            "target": 11                                                                                               // 301
        }, {                                                                                                           //
            "source": 11,                                                                                              // 304
            "target": 12                                                                                               // 305
        }, {                                                                                                           //
            "source": 12,                                                                                              // 308
            "target": 10                                                                                               // 309
        }]                                                                                                             //
    };                                                                                                                 //
                                                                                                                       //
    for (var i = 0; i < data.nodes.length; i++) {                                                                      // 314
        sort_data.push({ x: data.nodes.x + DISTANCE, y: data.nodes.y + DISTANCE, z: 0 });                              // 315
                                                                                                                       //
        // set up the sphere vars                                                                                      //
        var radius = 5,                                                                                                // 314
            segments = 16,                                                                                             //
            rings = 16;                                                                                                //
                                                                                                                       //
        // create the sphere's material                                                                                //
        var sphereMaterial = new THREE.MeshLambertMaterial({                                                           // 314
            color: COLOR                                                                                               // 325
        });                                                                                                            //
                                                                                                                       //
        var sphere = new THREE.Mesh(new THREE.SphereGeometry(radius, segments, rings), sphereMaterial);                // 328
                                                                                                                       //
        spheres.push(sphere);                                                                                          // 335
                                                                                                                       //
        // add the sphere to the scene                                                                                 //
        scene.add(sphere);                                                                                             // 314
    }                                                                                                                  //
                                                                                                                       //
    for (var i = 0; i < data.links.length; i++) {                                                                      // 341
        links.push({ target: data.links[i].target, source: data.links[i].source });                                    // 342
                                                                                                                       //
        var material = new THREE.LineBasicMaterial({ color: LINK_COLOR,                                                // 344
            linewidth: 2 });                                                                                           // 345
        var geometry = new THREE.Geometry();                                                                           // 346
                                                                                                                       //
        geometry.vertices.push(new THREE.Vector3(0, 0, 0));                                                            // 348
        geometry.vertices.push(new THREE.Vector3(0, 0, 0));                                                            // 349
        var line = new THREE.Line(geometry, material);                                                                 // 350
        line.userData = { source: data.links[i].source,                                                                // 351
            target: data.links[i].target };                                                                            // 352
        three_links.push(line);                                                                                        // 353
        scene.add(line);                                                                                               // 354
                                                                                                                       //
        force.start();                                                                                                 // 356
    }                                                                                                                  //
                                                                                                                       //
    // set up the axes                                                                                                 //
    var x = d3.scale.linear().domain([0, 350]).range([0, 10]),                                                         // 69
        y = d3.scale.linear().domain([0, 350]).range([0, 10]),                                                         //
        z = d3.scale.linear().domain([0, 350]).range([0, 10]);                                                         //
                                                                                                                       //
    force.on("tick", function (e) {                                                                                    // 364
        for (var i = 0; i < sort_data.length; i++) {                                                                   // 365
            spheres[i].position.set(x(sort_data[i].x) * 40 - 40, y(sort_data[i].y) * 40 - 40, 0);                      // 366
                                                                                                                       //
            for (var j = 0; j < three_links.length; j++) {                                                             // 368
                var line = three_links[j];                                                                             // 369
                var vi = -1;                                                                                           // 370
                if (line.userData.source === i) {                                                                      // 371
                    vi = 0;                                                                                            // 372
                }                                                                                                      //
                if (line.userData.target === i) {                                                                      // 374
                    vi = 1;                                                                                            // 375
                }                                                                                                      //
                                                                                                                       //
                if (vi >= 0) {                                                                                         // 378
                    line.geometry.vertices[vi].x = x(sort_data[i].x) * 40 - 40;                                        // 379
                    line.geometry.vertices[vi].y = y(sort_data[i].y) * 40 - 40;                                        // 380
                    line.geometry.verticesNeedUpdate = true;                                                           // 381
                }                                                                                                      //
            }                                                                                                          //
        }                                                                                                              //
                                                                                                                       //
        renderer.render(scene, camera);                                                                                // 386
    });                                                                                                                //
                                                                                                                       //
    // create a point light                                                                                            //
    var pointLight = new THREE.PointLight(0xFFFFFF);                                                                   // 69
                                                                                                                       //
    // set its position                                                                                                //
    pointLight.position.x = 10;                                                                                        // 69
    pointLight.position.y = 50;                                                                                        // 394
    pointLight.position.z = 130;                                                                                       // 395
                                                                                                                       //
    // add to the scene                                                                                                //
    scene.add(pointLight);                                                                                             // 69
                                                                                                                       //
    var rotSpeed = 0.01;                                                                                               // 400
    function checkRotation() {                                                                                         // 401
                                                                                                                       //
        var x = camera.position.x,                                                                                     // 403
            y = camera.position.y,                                                                                     //
            z = camera.position.z;                                                                                     //
                                                                                                                       //
        camera.position.x = x * Math.cos(rotSpeed) - z * Math.sin(rotSpeed);                                           // 407
        camera.position.z = z * Math.cos(rotSpeed) + x * Math.sin(rotSpeed);                                           // 408
                                                                                                                       //
        camera.lookAt(scene.position);                                                                                 // 410
    }                                                                                                                  //
                                                                                                                       //
    function animate() {                                                                                               // 414
        requestAnimationFrame(animate);                                                                                // 415
                                                                                                                       //
        checkRotation();                                                                                               // 417
                                                                                                                       //
        renderer.render(scene, camera);                                                                                // 419
    }                                                                                                                  //
                                                                                                                       //
    animate();                                                                                                         // 422
    /*   var data = [4, 8, 15, 16, 23, 42];                                                                            //
                                                                                                                       //
    // these are, as before, to make D3's .append() and .selectAll() work                                              //
       THREE.Object3D.prototype.appendChild = function (c) { this.add(c); return c; };                                 //
       THREE.Object3D.prototype.querySelectorAll = function () { return []; };                                         //
                                                                                                                       //
    // this one is to use D3's .attr() on THREE's objects                                                              //
       THREE.Object3D.prototype.setAttribute = function (name, value) {                                                //
           var chain = name.split('.');                                                                                //
           var object = this;                                                                                          //
           for (var i = 0; i < chain.length - 1; i++) {                                                                //
               object = object[chain[i]];                                                                              //
           }                                                                                                           //
           object[chain[chain.length - 1]] = value;                                                                    //
       }                                                                                                               //
                                                                                                                       //
       var camera, scene, renderer, chart3d;                                                                           //
                                                                                                                       //
       init();                                                                                                         //
       animate();                                                                                                      //
                                                                                                                       //
       function init () {                                                                                              //
           // standard THREE stuff, straight from examples                                                             //
           renderer = new THREE.WebGLRenderer();                                                                       //
           renderer.setSize( window.innerWidth, window.innerHeight );                                                  //
           document.body.appendChild( renderer.domElement );                                                           //
                                                                                                                       //
           camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 1000 );                //
           camera.position.z = 400;                                                                                    //
                                                                                                                       //
           scene = new THREE.Scene();                                                                                  //
                                                                                                                       //
           var light = new THREE.DirectionalLight( 0xffffff );                                                         //
           light.position.set( 0, 0, 1 );                                                                              //
           scene.add( light );                                                                                         //
                                                                                                                       //
           var geometry = new THREE.CubeGeometry( 20, 20, 20 );                                                        //
           var material = new THREE.MeshLambertMaterial( {                                                             //
               color: 0x4682B4, shading: THREE.FlatShading, vertexColors: THREE.VertexColors } );                      //
                                                                                                                       //
           // create container for our 3D chart                                                                        //
           chart3d = new THREE.Object3D();                                                                             //
           chart3d.rotation.x = 0.6;                                                                                   //
           scene.add( chart3d );                                                                                       //
                                                                                                                       //
           // use D3 to set up 3D bars                                                                                 //
           d3.select( chart3d )                                                                                        //
               .selectAll()                                                                                            //
               .data(data)                                                                                             //
               .enter().append( function() { return new THREE.Mesh( geometry, material ); } )                          //
               .attr("position.x", function(d, i) { return 30 * i; })                                                  //
               .attr("position.y", function(d, i) { return d; })                                                       //
               .attr("scale.y", function(d, i) { return d / 10; })                                                     //
                                                                                                                       //
           // continue with THREE stuff                                                                                //
           window.addEventListener( 'resize', onWindowResize, false );                                                 //
       }                                                                                                               //
                                                                                                                       //
       function onWindowResize() {                                                                                     //
                                                                                                                       //
           camera.aspect = window.innerWidth / window.innerHeight;                                                     //
           camera.updateProjectionMatrix();                                                                            //
                                                                                                                       //
           renderer.setSize( window.innerWidth, window.innerHeight );                                                  //
                                                                                                                       //
       }                                                                                                               //
                                                                                                                       //
       function animate() {                                                                                            //
                                                                                                                       //
           requestAnimationFrame( animate );                                                                           //
                                                                                                                       //
           chart3d.rotation.y += 0.01;                                                                                 //
                                                                                                                       //
           renderer.render( scene, camera );                                                                           //
                                                                                                                       //
       }                                                                                                               //
    */                                                                                                                 //
                                                                                                                       //
    /*                                                                                                                 //
                                                                                                                       //
        var d3obj = d3.select("#threeGraph").append("svg")                                                             //
            .attr("width", "100%")                                                                                     //
            .attr("height", "100%");                                                                                   //
                                                                                                                       //
        var force = d3.layout.force()                                                                                  //
            .charge(-120)                                                                                              //
            .linkDistance(30)                                                                                          //
            .size([700, 700]);                                                                                         //
                                                                                                                       //
        force                                                                                                          //
            .nodes(graph.nodes)                                                                                        //
            .links(graph.links)                                                                                        //
            .start(10,15,20);                                                                                          //
    */                                                                                                                 //
                                                                                                                       //
    /*                                                                                                                 //
        var d3obj = d3.select( chart )                                                                                 //
            .selectAll()                                                                                               //
            //.data(graph.nodes)                                                                                       //
            //.enter()                                                                                                 //
            .append( createDiv )                                                                                       //
            .style("width", function(d) { return d * 10 + "px"; })                                                     //
            .text(function(d) { return d; });                                                                          //
    */                                                                                                                 //
    /*                                                                                                                 //
                                                                                                                       //
        var link = d3obj.selectAll(".link")                                                                            //
            .data(graph.links)                                                                                         //
            .enter()                                                                                                   //
            .append("g")                                                                                               //
            .attr("class", "link-group")                                                                               //
            .append("line")                                                                                            //
            .attr("class", "link")                                                                                     //
            .style("stroke-width", function(d) { return Math.sqrt(d.stroke); });                                       //
                                                                                                                       //
        var node = d3obj.selectAll(".node")                                                                            //
            .data(graph.nodes)                                                                                         //
            .enter().append("g")                                                                                       //
            .attr("class", "node")                                                                                     //
            .call(force.drag);                                                                                         //
                                                                                                                       //
                                                                                                                       //
        node.append("circle")                                                                                          //
            .attr("class", "node")                                                                                     //
            .attr("r", function(d){return 13;})                                                                        //
            .on("mouseover", function(d) {                                                                             //
                d3obj.transition()                                                                                     //
                    .duration(200)                                                                                     //
                    .style("opacity", .9);                                                                             //
                d.title = "";                                                                                          //
                if(d.attributes != undefined){                                                                         //
                    d.title = JSON.stringify(d.attributes, null, 4).toString().replace(/\,/g,'<BR>').replace(/\[/g,'').replace(/\]/g,'').replace(/\{/g,'').replace(/\}/g,'').replace(/"/g,'');
                }                                                                                                      //
                                                                                                                       //
                d3obj.html("<p><u>" + d.name + "</u><br/>"  + d.title + "<p/>")                                        //
                    .style("left", (d3.event.pageX) + "px")                                                            //
                    .style("top", (d3.event.pageY - 28) + "px");                                                       //
            })                                                                                                         //
            .on("mouseout", function(d) {                                                                              //
                d3obj.transition()                                                                                     //
                    .duration(500)                                                                                     //
                    .style("opacity", 0);                                                                              //
            })                                                                                                         //
            .style("fill", function(d) { return color(d.level); })                                                     //
            .call(force.drag);                                                                                         //
                                                                                                                       //
        node.append("text")                                                                                            //
            .attr("dx", 14)                                                                                            //
            .attr("dy", ".35em")                                                                                       //
            .text(function(d) { return d.label});                                                                      //
                                                                                                                       //
                                                                                                                       //
        force.on("tick", function() {                                                                                  //
            link.attr("x1", function(d) { return d.source.x; })                                                        //
                .attr("y1", function(d) { return d.source.y; })                                                        //
                .attr("x2", function(d) { return d.target.x; })                                                        //
                .attr("y2", function(d) { return d.target.y; });                                                       //
                                                                                                                       //
            node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });                      //
                                                                                                                       //
        });                                                                                                            //
    */                                                                                                                 //
                                                                                                                       //
    /*                                                                                                                 //
    $(document).ready(function() {                                                                                     //
        var container, stats, valid;                                                                                   //
        var camera, scene, renderer, group, particle;                                                                  //
        var mouseX = 0, mouseY = 0;                                                                                    //
        var force, nodes = [], links = [];                                                                             //
          var part = new Image();                                                                                      //
        part.src = "/particle.png";                                                                                    //
        part.onload = function () {                                                                                    //
            init();                                                                                                    //
            animate();                                                                                                 //
        };                                                                                                             //
          var w2 = document.body.clientWidth / 2;                                                                      //
        var h2 = document.body.clientHeight / 2;                                                                       //
          function colorize(img, r, g, b, a) {                                                                         //
            if (!img)                                                                                                  //
                return img;                                                                                            //
              var tempFileCanvas = document.createElement("canvas");                                                   //
            tempFileCanvas.width = img.width;                                                                          //
            tempFileCanvas.height = img.height;                                                                        //
              var imgCtx = tempFileCanvas.getContext("2d"), imgdata, i;                                                //
            imgCtx.clearRect(0, 0, img.width, img.height);                                                             //
            imgCtx.save();                                                                                             //
            imgCtx.drawImage(img, 0, 0);                                                                               //
              imgdata = imgCtx.getImageData(0, 0, img.width, img.height);                                              //
              i = imgdata.data.length;                                                                                 //
            while ((i -= 4) > -1) {                                                                                    //
                imgdata.data[i + 3] = imgdata.data[i] * a;                                                             //
                if (imgdata.data[i + 3]) {                                                                             //
                    imgdata.data[i] = r;                                                                               //
                    imgdata.data[i + 1] = g;                                                                           //
                    imgdata.data[i + 2] = b;                                                                           //
                }                                                                                                      //
            }                                                                                                          //
              imgCtx.putImageData(imgdata, 0, 0);                                                                      //
            imgCtx.restore();                                                                                          //
            return tempFileCanvas;                                                                                     //
        }                                                                                                              //
          function init() {                                                                                            //
              //container = document.createElement('div');                                                             //
            container = $("#threeGraph");                                                                              //
            //document.body.appendChild(container);                                                                    //
              camera = new THREE.PerspectiveCamera(h2 * 2, w2 / h2, 99, 101);                                          //
            camera.position.z = 100;                                                                                   //
              scene = new THREE.Scene();                                                                               //
              var group = new THREE.Object3D();                                                                        //
              var PI2 = Math.PI * 2;                                                                                   //
            var program = function (ctx, color) {                                                                      //
                color = d3.rgb(ctx.fillStyle);                                                                         //
                ctx.drawImage(part, 0.5, 0.5, 1, 1);                                                                   //
            };                                                                                                         //
              var lineMaterial = new THREE.LineBasicMaterial({                                                         //
                color: 0xff0000,                                                                                       //
                opacity: .1                                                                                            //
            });                                                                                                        //
              var particleMaterial = new THREE.PointsMaterial({                                                        //
                size: 0.1,                                                                                             //
                blending: THREE.AdditiveBlending, // required                                                          //
                depthTest: false, // required                                                                          //
                transparent: true,                                                                                     //
                opacity: 0.7,                                                                                          //
                vertexColors: true // optional                                                                         //
            });                                                                                                        //
              /!*new THREE.ParticleCanvasMaterial( {                                                                   //
             color: Math.random() * 0x808008 + 0x808080,                                                               //
             program: program                                                                                          //
             } )*!/                                                                                                    //
              for (var i = 0, j; i < 500; i++) {                                                                       //
                  var pm = particleMaterial.clone();                                                                   //
                  pm.color = new THREE.Color();                                                                        //
                //pm.color.setHSV(Math.random(), 1, 1);                                                                //
                  var c = d3.rgb(pm.color.getStyle());                                                                 //
                pm.map = new THREE.Texture(colorize(part, c.r, c.g, c.b, 1));                                          //
                  particle = new THREE.Particle(pm);                                                                   //
                particle.position.x = (Math.random() * w2 * 4 - w2 * 2);                                               //
                particle.position.y = (Math.random() * h2 * 4 - h2 * 2);                                               //
                particle.position.z = 0;                                                                               //
                particle.scale.x = particle.scale.y = Math.random();                                                   //
                  j = nodes.push(particle.position);                                                                   //
                  j = links.push({source: j % 10, target: j - 1});                                                     //
                j = links[j - 1];                                                                                      //
                stats = new THREE.Geometry();                                                                          //
                stats.vertices.push(new THREE.Vector3(nodes[j.source]));                                               //
                stats.vertices.push(new THREE.Vector3(nodes[j.target]));                                               //
                  group.add(new THREE.Line(stats, lineMaterial));                                                      //
                  group.add(particle);                                                                                 //
            }                                                                                                          //
            scene.add(group);                                                                                          //
              renderer = new THREE.CanvasRenderer();                                                                   //
            renderer.setSize(w2 * 2, h2 * 2);                                                                          //
            //container.appendChild(renderer.domElement);                                                              //
            container.append(renderer.domElement);                                                                     //
              d3.select(renderer.domElement)                                                                           //
                .call(d3.behavior.zoom()                                                                               //
                    .scaleExtent([0.01, 8])                                                                            //
                    .scale(1)                                                                                          //
                    .translate([group.position.x, group.position.y])                                                   //
                    .on("zoom", function () {                                                                          //
                        group.scale.x = group.scale.y = d3.event.scale;                                                //
                        //camera.position.z = d3.event.scale;                                                          //
                        group.position.x = -d3.event.translate[0];                                                     //
                        group.position.y = d3.event.translate[1];                                                      //
                          valid = false;                                                                               //
                    }));                                                                                               //
              window.addEventListener('resize', onWindowResize, false);                                                //
              force = d3.layout.force()                                                                                //
                .nodes(nodes)                                                                                          //
                .links(links)                                                                                          //
                .on("tick", function () {                                                                              //
                    valid = false;                                                                                     //
                })                                                                                                     //
                .start();                                                                                              //
        }                                                                                                              //
          function onWindowResize() {                                                                                  //
              w2 = window.innerWidth / 2;                                                                              //
            h2 = window.innerHeight / 2;                                                                               //
              camera.aspect = w2 / h2;                                                                                 //
            camera.updateProjectionMatrix();                                                                           //
              renderer.setSize(w2 * 2, h2 * 2);                                                                        //
              valid = false;                                                                                           //
        }                                                                                                              //
          function animate() {                                                                                         //
              requestAnimationFrame(animate);                                                                          //
              if (!valid) {                                                                                            //
                valid = true;                                                                                          //
                render();                                                                                              //
            }                                                                                                          //
          }                                                                                                            //
          function render() {                                                                                          //
              camera.lookAt(scene.position);                                                                           //
              renderer.render(scene, camera);                                                                          //
          }                                                                                                            //
    });                                                                                                                //
    */                                                                                                                 //
};                                                                                                                     // 69
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}},"lib":{"collections.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// lib/collections.js                                                                                                  //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
Inventory = new Mongo.Collection("inventory");                                                                         // 1
Cliques = new Mongo.Collection("cliques");                                                                             // 2
Links = new Mongo.Collection("links");                                                                                 // 3
Environments = new Mongo.Collection("environments_config");                                                            // 4
NodeHoverAttr = new Mongo.Collection("attributes_for_hover_on_data");                                                  // 5
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"router.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// lib/router.js                                                                                                       //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
/**                                                                                                                    //
 * Created by oashery on 3/2/2016.                                                                                     //
 */                                                                                                                    //
Router.configure({                                                                                                     // 4
    layoutTemplate: 'main',                                                                                            // 5
    loadingTemplate: 'loading'                                                                                         // 6
});                                                                                                                    //
Router.route('/', {                                                                                                    // 8
    name: 'homePage',                                                                                                  // 9
    template: 'mainPage'                                                                                               // 10
});                                                                                                                    //
Router.route('home', {                                                                                                 // 12
    path: '/home',                                                                                                     // 13
    waitOn: function () {                                                                                              // 14
        function waitOn() {                                                                                            // 14
            return Meteor.subscribe('inventory');                                                                      // 15
        }                                                                                                              //
                                                                                                                       //
        return waitOn;                                                                                                 //
    }(),                                                                                                               //
    action: function () {                                                                                              // 17
        function action() {                                                                                            // 17
            if (this.ready()) {                                                                                        // 18
                                                                                                                       //
                this.state.set('envName', this.params.query.env);                                                      // 20
                /*                                                                                                     //
                            if(query){                                                                                 //
                                    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
                                    console.log(query);                                                                //
                                    this.render('home', {                                                              //
                                        data: function () {                                                            //
                                            return Inventory.find({environment: query, parent_id: query});             //
                                        }                                                                              //
                                    });                                                                                //
                                    //                                                                                 //
                            }                                                                                          //
                */                                                                                                     //
                                                                                                                       //
                // if the sub handle returned from waitOn ready() method returns                                       //
                // true then we're ready to go ahead and render the page.                                              //
                this.render('home');                                                                                   // 18
            } else {                                                                                                   //
                // otherwise render the loading template.                                                              //
                this.render('loading');                                                                                // 41
            }                                                                                                          //
        }                                                                                                              //
                                                                                                                       //
        return action;                                                                                                 //
    }()                                                                                                                //
                                                                                                                       //
});                                                                                                                    //
Router.route('landingpage', {                                                                                          // 46
    name: 'landingpage',                                                                                               // 47
    path: '/landing'                                                                                                   // 48
});                                                                                                                    //
Router.route('d3plusgraph', {                                                                                          // 50
    path: '/d3plus'                                                                                                    // 51
});                                                                                                                    //
Router.route('threeTest', {                                                                                            // 53
    path: '/three'                                                                                                     // 54
});                                                                                                                    //
Router.route('threeTest2', {                                                                                           // 56
    path: '/three2'                                                                                                    // 57
});                                                                                                                    //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}},"osdna_new.js":["webcola",function(require){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                     //
// osdna_new.js                                                                                                        //
//                                                                                                                     //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                       //
cola = require('webcola');                                                                                             // 1
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}]},{"extensions":[".js",".json",".html",".css"]});
require("./client/templates/template.d3plusgraph.js");
require("./client/templates/template.envdialog.js");
require("./client/templates/template.header.js");
require("./client/templates/template.home.js");
require("./client/templates/template.landingpage.js");
require("./client/templates/template.mainPage.js");
require("./client/templates/template.threeTest.js");
require("./client/templates/template.threeTest2.js");
require("./client/templates/template.main.js");
require("./client/lib/d3three.js");
require("./client/lib/jquery.multilevelpushmenu.js");
require("./client/lib/threeTestData.js");
require("./lib/collections.js");
require("./lib/router.js");
require("./client/accounts-config.js");
require("./client/d3plusgraph.js");
require("./client/envdialog.js");
require("./client/header.js");
require("./client/home.js");
require("./client/landingpage.js");
require("./client/mainInit.js");
require("./client/subscriptions.js");
require("./client/threeTest2.js");
require("./client/threejsTest.js");
require("./osdna_new.js");
require("./client/lib/main.js");