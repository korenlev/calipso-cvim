import * as R from 'ramda';

export function idToStr(orgId) {
  return R.ifElse(R.is(Mongo.ObjectID),
    function (id) { return id.toHexString() + ':' + 'objectid'; },
    R.identity
  )(orgId); 
}

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
