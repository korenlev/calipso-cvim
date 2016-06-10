Meteor.publish("inventory", function () {
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    //return Inventory.find({ "show_in_tree": true });
    return Inventory.find({});
});
Meteor.publish("environments_config", function () {
    return Environments.find({type:"environment"});
});
Meteor.publish("cliques", function () {
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    return Cliques.find({});
});
Meteor.publish("links", function () {
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    return Links.find({});
});
Meteor.publish("attributes_for_hover_on_data", function () {
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    return NodeHoverAttr.find({});
});
/*
Meteor.publish("nodesList", function (nodeId) {
    return Inventory.find({ "type": "instance", $and: [ { "id": nodeId } ] }["Entities"]);
});
Meteor.publish("edgesList", function (nodeId) {
    return Inventory.find({ "type": "instance", $and: [ { "id": nodeId } ] }["Relations"]);
});
*/
Meteor.startup(function () {
    // code to run on server at startup
});
