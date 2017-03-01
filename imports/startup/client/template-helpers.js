import * as R from 'ramda';

Template.registerHelper('asHash', function (params) {
  return params.hash;
});

Template.registerHelper('idToStr', function (orgId) {
  return R.ifElse(R.is(Mongo.ObjectID),
    function (id) { return id.toHexString() + ':' + 'objectid'; },
    R.identity
  )(orgId); 
});
