import * as R from 'ramda';
import * as utils from '/imports/lib/utilities';

Template.registerHelper('asHash', function (params) {
  return params.hash;
});

Template.registerHelper('idToStr', utils.idToStr);

Template.registerHelper('rPath', function (source, pathStr) {
  let path = R.split('.', pathStr);
  return R.path(path, source);
});
