import * as R from 'ramda';

export function parseReqId(pId) {
  let idMatch = R.match(/(.*):objectid$/, pId);
  if (idMatch.length === 0) {
    return {
      type: 'string',
      id: pId
    };
  } else {
    return { 
      type: 'objectid',
      id: new Mongo.ObjectID(idMatch[1])
    };
  }
}
