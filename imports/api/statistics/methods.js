import * as R from 'ramda';
import { Statistics } from './statistics';

Meteor.methods({
  'statistics.flowTypes?env&object_id&type'({ env, object_id, type}) {
    console.log('subscribe: statistics.flowTypes?env&object_id&type');
    console.log(`- env: ${env}`);
    console.log(`- object_id: ${object_id}`);
    console.log(`- type: ${type}`);

    let pipeline = [{
      $match: {
        environment: env,
        object_id: object_id,
        type: type
      }
    }, {
      $group: {
        _id: { flowType: '$flowType' },
        flowType: { $first: '$flowType' }
      }
    }];
    
    return Statistics.aggregate(pipeline);
  },

  'statistics.srcMacAddresses?env&object_id&type&flowType'(
      { env, object_id, type, flowType }) {

    let pipeline = [{
      $match: {
        environment: env,
        object_id: object_id,
        type: type,
        flowType: flowType
      }
    }, {
      $group: {
        _id: { sourceMacAddress: '$sourceMacAddress' },
        sourceMacAddress: { $first: '$sourceMacAddress' }
      }
    }];
    
    return Statistics.aggregate(pipeline);
  },

  'statistics.dstMacAddresses?env&object_id&type&flowType'(
      { env, object_id, type, flowType }) {

    let pipeline = [{
      $match: {
        environment: env,
        object_id: object_id,
        type: type,
        flowType: flowType
      }
    }, {
      $group: {
        _id: { destinationMacAddress: 'destinationMacAddress' },
        destinationMacAddress: { $first: '$destinationMacAddress' }
      }
    }];
    
    return Statistics.aggregate(pipeline);
  },

  'statistics.srcIPv4Addresses?env&object_id&type&flow_typw'(
      { env, object_id, type, flowType }) {
    let pipeline = [{
      $match: {
        environment: env,
        object_id: object_id,
        type: type,
        flowType: flowType
      }
    }, {
      $group: {
        _id: { sourceIPv4Address: '$sourceIPv4Address' },
        sourceIPv4Address: { $first: '$sourceIPv4Address' }
      }
    }];
    
    return Statistics.aggregate(pipeline);
  },

  'statistics.dstIPv4Addresses?env&object_id&type&flowType'(
      { env, object_id, type, flowType }) {
    let pipeline = [{
      $match: {
        environment: env,
        object_id: object_id,
        type: type,
        flowType: flowType
      }
    }, {
      $group: {
        _id: { destinationIPv4Address: '$destinationIPv4Addres' },
        destinationIPv4Address: { $first: '$destinationIPv4Addres' }
      }
    }];
    
    return Statistics.aggregate(pipeline);
  },

  'statistics!graph-frames'({ 
    env, 
    object_id, 
    type,
    flowType, 
    timeStart,
    timeEnd,
    sourceMacAddress,
    destinationMacAddress,
    sourceIPv4Address,
    destinationIPv4Address
  }) {
    let schema = createGraphQuerySchema(
      env, 
      object_id,
      type,
      flowType, 
      timeStart,
      timeEnd,
      sourceMacAddress,
      destinationMacAddress,
      sourceIPv4Address,
      destinationIPv4Address);

    console.log('statistics!graph-frames');
    console.log(`- env: ${env}`);
    console.log(`- object_id: ${object_id}`);
    console.log(`- type: ${type}`);
    console.log(`- flowType: ${flowType}`);
    console.log(`- timeStart: ${timeStart}`);
    console.log(`- timeEnd: ${timeEnd}`);
    console.log(`- sourceMacAddress: ${sourceMacAddress}`);
    console.log(`- destinationMacAddress: ${destinationMacAddress}`);
    console.log(`- sourceIPv4Address: ${sourceIPv4Address}`);
    console.log(`- destinationIPv4Address: ${destinationIPv4Address}`);

    return Statistics.find(schema).fetch();
  }
});

function createGraphQuerySchema(
  env, 
  object_id, 
  type,
  flowType, 
  timeStart,
  timeEnd,
  sourceMacAddress,
  destinationMacAddress,
  sourceIPv4Address,
  destinationIPv4Address) {

  let schema = {
    environment: env, 
    object_id: object_id, 
    type: type,
    flowType: flowType, 
    averageArrivalNanoSeconds: {
      $gte: timeStart,
      $lt: timeEnd
    }
  };

  switch (flowType) {
  case 'L2':
    schema = R.merge(schema, {
      sourceMacAddress: sourceMacAddress,
      destinationMacAddress: destinationMacAddress  
    });
    break;

  case 'L3':
    schema = R.merge(schema, {
      sourceIPv4Address: sourceIPv4Address,
      destinationIPv4Address: destinationIPv4Address
    });
    break;

  default:
    break;
  }

  return schema;
}

