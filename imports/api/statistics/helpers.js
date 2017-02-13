import * as R from 'ramda';

export function createGraphQuerySchema(
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
      //$lt: timeEnd
    }
  };

  if (! R.isNil(timeEnd)) {
    schema = R.assocPath(['averageArrivalNanoSeconds', '$lt'], timeEnd, schema);
  }

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
