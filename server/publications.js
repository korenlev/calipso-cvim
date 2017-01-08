Meteor.publish("cliques", function () {
    console.log("server subscribtion to: cliques");
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    return Cliques.find({});
});

Meteor.publish("cliques?focal_point", function (objId) {
    var query = {
      focal_point: new Mongo.ObjectID(objId) 
    }
  /*
    var counterName = "inventory?env+type!counter?env=" + env + "&type=" + type;

    console.log("server subscribing to counter: " + counterName);
    Counts.publish(this, counterName, Inventory.find(query));
  */

    console.log("server subscribtion to: cliques?focal_point");
    console.log("- focal_point: " + objId);
    return Cliques.find(query); 
});

Meteor.publish("links", function () {
    console.log("server subscribtion to: links");
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    return Links.find({});
});

Meteor.publish("links?_id-in", function (idsList) {
    var query = {
      _id: { $in: idsList}
    }
  /*
    var counterName = "inventory?env+type!counter?env=" + env + "&type=" + type;

    console.log("server subscribing to counter: " + counterName);
    Counts.publish(this, counterName, Inventory.find(query));
  */

    console.log("server subscribtion to: links?_id-in");
    console.log("- _id-in: " + idsList);
    return Links.find(query); 
});

Meteor.publish("attributes_for_hover_on_data", function () {
    console.log("server subscribtion to: attributes_for_hover_on_data");
    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    return NodeHoverAttr.find({});
});

Meteor.publish("attributes_for_hover_on_data?type", function (type) {
    console.log("server subscribtion to: attributes_for_hover_on_data?type");
    console.log("- type: " + type);

    //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
    return NodeHoverAttr.find({ "type": type});
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
