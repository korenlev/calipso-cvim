var require = meteorInstall({"lib":{"collections.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                         //
// lib/collections.js                                                                                      //
//                                                                                                         //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                           //
Inventory = new Mongo.Collection("inventory");                                                             // 1
Cliques = new Mongo.Collection("cliques");                                                                 // 2
Links = new Mongo.Collection("links");                                                                     // 3
Environments = new Mongo.Collection("environments_config");                                                // 4
NodeHoverAttr = new Mongo.Collection("attributes_for_hover_on_data");                                      // 5
/////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"router.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                         //
// lib/router.js                                                                                           //
//                                                                                                         //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                           //
/**                                                                                                        //
 * Created by oashery on 3/2/2016.                                                                         //
 */                                                                                                        //
Router.configure({                                                                                         // 4
    layoutTemplate: 'main',                                                                                // 5
    loadingTemplate: 'loading'                                                                             // 6
});                                                                                                        //
Router.route('/', {                                                                                        // 8
    name: 'homePage',                                                                                      // 9
    template: 'mainPage'                                                                                   // 10
});                                                                                                        //
Router.route('home', {                                                                                     // 12
    path: '/home',                                                                                         // 13
    waitOn: function () {                                                                                  // 14
        function waitOn() {                                                                                // 14
            return Meteor.subscribe('inventory');                                                          // 15
        }                                                                                                  //
                                                                                                           //
        return waitOn;                                                                                     //
    }(),                                                                                                   //
    action: function () {                                                                                  // 17
        function action() {                                                                                // 17
            if (this.ready()) {                                                                            // 18
                                                                                                           //
                this.state.set('envName', this.params.query.env);                                          // 20
                /*                                                                                         //
                            if(query){                                                                     //
                                    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
                                    console.log(query);                                                    //
                                    this.render('home', {                                                  //
                                        data: function () {                                                //
                                            return Inventory.find({environment: query, parent_id: query});
                                        }                                                                  //
                                    });                                                                    //
                                    //                                                                     //
                            }                                                                              //
                */                                                                                         //
                                                                                                           //
                // if the sub handle returned from waitOn ready() method returns                           //
                // true then we're ready to go ahead and render the page.                                  //
                this.render('home');                                                                       // 18
            } else {                                                                                       //
                // otherwise render the loading template.                                                  //
                this.render('loading');                                                                    // 41
            }                                                                                              //
        }                                                                                                  //
                                                                                                           //
        return action;                                                                                     //
    }()                                                                                                    //
                                                                                                           //
});                                                                                                        //
Router.route('landingpage', {                                                                              // 46
    name: 'landingpage',                                                                                   // 47
    path: '/landing'                                                                                       // 48
});                                                                                                        //
Router.route('d3plusgraph', {                                                                              // 50
    path: '/d3plus'                                                                                        // 51
});                                                                                                        //
Router.route('threeTest', {                                                                                // 53
    path: '/three'                                                                                         // 54
});                                                                                                        //
Router.route('threeTest2', {                                                                               // 56
    path: '/three2'                                                                                        // 57
});                                                                                                        //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////

}},"server":{"methods.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                         //
// server/methods.js                                                                                       //
//                                                                                                         //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                           //
Meteor.methods({});                                                                                        // 1
/////////////////////////////////////////////////////////////////////////////////////////////////////////////

},"publications.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                         //
// server/publications.js                                                                                  //
//                                                                                                         //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                           //
Meteor.publish("inventory", function () {                                                                  // 1
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});                    //
    //return Inventory.find({ "show_in_tree": true });                                                     //
    return Inventory.find({});                                                                             // 4
});                                                                                                        //
Meteor.publish("environments_config", function () {                                                        // 6
    return Environments.find({ type: "environment" });                                                     // 7
});                                                                                                        //
Meteor.publish("cliques", function () {                                                                    // 9
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});                    //
    return Cliques.find({});                                                                               // 11
});                                                                                                        //
Meteor.publish("links", function () {                                                                      // 13
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});                    //
    return Links.find({});                                                                                 // 15
});                                                                                                        //
Meteor.publish("attributes_for_hover_on_data", function () {                                               // 17
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});                    //
    return NodeHoverAttr.find({});                                                                         // 19
});                                                                                                        //
/*                                                                                                         //
Meteor.publish("nodesList", function (nodeId) {                                                            //
    return Inventory.find({ "type": "instance", $and: [ { "id": nodeId } ] }["Entities"]);                 //
});                                                                                                        //
Meteor.publish("edgesList", function (nodeId) {                                                            //
    return Inventory.find({ "type": "instance", $and: [ { "id": nodeId } ] }["Relations"]);                //
});                                                                                                        //
*/                                                                                                         //
Meteor.startup(function () {                                                                               // 29
                                                                                                           //
    // code to run on server at startup                                                                    //
});                                                                                                        //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////

}},"osdna_new.js":["webcola",function(require){

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                         //
// osdna_new.js                                                                                            //
//                                                                                                         //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                           //
cola = require('webcola');                                                                                 // 1
/////////////////////////////////////////////////////////////////////////////////////////////////////////////

}]},{"extensions":[".js",".json"]});
require("./lib/collections.js");
require("./lib/router.js");
require("./server/methods.js");
require("./server/publications.js");
require("./osdna_new.js");
//# sourceMappingURL=app.js.map
