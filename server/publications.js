Meteor.publish("messages", function () {
    console.log("subscribtion to: messages");
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    //return Inventory.find({ "show_in_tree": true });
    return Messages.find({});
});

Meteor.publish("inventory", function () {
    console.log("subscribtion to: inventory");
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    //return Inventory.find({ "show_in_tree": true });
    return Inventory.find({});
});

Meteor.publish("inventory.children", function (nodeId) {
  console.log("subscribtion to: inventory.children");
  console.log("node id: " + nodeId.toString());

  return Inventory.find({
    parent_id: nodeId
  });    
});

Meteor.publish("inventory.first-child", function (nodeId) {
    console.log("subscribing to: inventory.first-child");
    console.log("node id: " + nodeId.toString());

    var counterName = "inventory.first-child!counter!id=" + nodeId;
    Counts.publish(this, counterName, 
      Inventory.find({
        parent_id: nodeId
      }, {
        limit: 1
      }));
    console.log("subscribing to counter: " + counterName);

  // todo: eyaltask: all criteria
    return Inventory.find({
      parent_id: nodeId
    }, {
      limit: 1
    });
});

Meteor.publish("inventoryByEnv", function (env) {
    console.log("subscribtion to: inventoryByEnv");
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    //return Inventory.find({ "show_in_tree": true });
    return Inventory.find({"environment":env});
});

Meteor.publish("environments_config", function () {
    console.log("subscribtion to: environments_config");
    return Environments.find({type:"environment"});
});

Meteor.publish("cliques", function () {
    console.log("subscribtion to: cliques");
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    return Cliques.find({});
});

Meteor.publish("links", function () {
    console.log("subscribtion to: links");
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    return Links.find({});
});

Meteor.publish("attributes_for_hover_on_data", function () {
    console.log("subscribtion to: attributes_for_hover_on_data");
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
