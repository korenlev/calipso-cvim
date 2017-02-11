import { Meteor } from 'meteor/meteor';

import { NodeHoverAttr } from '../attributes_for_hover_on_data.js';

Meteor.publish('attributes_for_hover_on_data', function () {
  console.log('server subscribtion to: attributes_for_hover_on_data');
  //return Inventory.find({$where: 'this.id_path.match('^/WebEX-Mirantis@Cisco/')'});
  return NodeHoverAttr.find({});
});

Meteor.publish('attributes_for_hover_on_data?type', function (type) {
  console.log('server subscribtion to: attributes_for_hover_on_data?type');
  console.log('- type: ' + type);

  //return Inventory.find({$where: 'this.id_path.match('^/WebEX-Mirantis@Cisco/')'});
  return NodeHoverAttr.find({ 'type': type});
});
