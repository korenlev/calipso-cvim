//import * as R from 'ramda';
import * as utils from '/imports/lib/utilities';

Template.registerHelper('asHash', function (params) {
  return params.hash;
});

Template.registerHelper('idToStr', utils.idToStr);
