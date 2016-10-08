Meteor.publish("messages", function () {
    console.log("server subscribtion to: messages");
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    //return Inventory.find({ "show_in_tree": true });
    return Messages.find({});
});

Meteor.publish("messages?env+level", function (env, level) {
    var query = {
      environment: env,
      level: level
    };
    var counterName = "messages?env+level!counter?env=" +
      env + "&level=" + level;

    console.log("server subscription to: messages - counter");
    console.log(" - name: " + counterName);
    Counts.publish(this, counterName, Messages.find(query));

    console.log("server subscribtion to: messages");
    console.log("- env: " + env);
    console.log("- level: " + level);
    return Messages.find(query);
});

Meteor.publish("inventory", function () {
    console.log("server subscribtion to: inventory");
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    //return Inventory.find({ "show_in_tree": true });
    return Inventory.find({});
});

Meteor.publish("inventory?env+type", function (env, type) {
    var query = {
      environment: env,
      type: type
    }
    var counterName = "inventory?env+type!counter?env=" + env + "&type=" + type;

    console.log("server subscribing to counter: " + counterName);
    Counts.publish(this, counterName, Inventory.find(query));

    console.log("server subscribtion to: inventory-by-env-and-type");
    console.log("-env: " + env);
    console.log("-type: " + type);
    return Inventory.find(); 
});

Meteor.publish("inventory.children", function (nodeId) {
  console.log("server subscribtion to: inventory.children");
  console.log("node id: " + nodeId.toString());

  return Inventory.find({
    parent_id: nodeId
  });    
});

Meteor.publish("inventory.first-child", function (nodeId) {
    console.log("server subscribing to: inventory.first-child");
    console.log("node id: " + nodeId.toString());

    var counterName = "inventory.first-child!counter!id=" + nodeId;
    Counts.publish(this, counterName, 
      Inventory.find({
        parent_id: nodeId
      }, {
        limit: 1
      }));
    console.log("server subscribing to counter: " + counterName);

  // todo: eyaltask: all criteria
    return Inventory.find({
      parent_id: nodeId
    }, {
      limit: 1
    });
});

Meteor.publish("inventoryByEnv", function (env) {
    console.log("server subscribtion to: inventoryByEnv");
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    //return Inventory.find({ "show_in_tree": true });
    return Inventory.find({"environment":env});
});

Meteor.publish("environments_config", function () {
    console.log("server subscribtion to: environments_config");
    return Environments.find({type:"environment"});
});

Meteor.publish("cliques", function () {
    console.log("server subscribtion to: cliques");
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    return Cliques.find({});
});

Meteor.publish("links", function () {
    console.log("server subscribtion to: links");
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    return Links.find({});
});

Meteor.publish("attributes_for_hover_on_data", function () {
    console.log("server subscribtion to: attributes_for_hover_on_data");
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
