//import * as R from 'ramda';

import { check } from 'meteor/check';
import { Inventory } from '../inventories';
import { regexEscape } from '/imports/lib/regex-utils';

const AUTO_COMPLETE_RESULTS_LIMIT = 5;



Meteor.methods({
  'inventorySearch': function(searchTerm, envName) {
    check(searchTerm, String);
    this.unblock();
    var searchExp = new RegExp(regexEscape(searchTerm), 'i');
    return Inventory.find(
      { environment: envName, name: searchExp }, {limit: AUTO_COMPLETE_RESULTS_LIMIT }
      ).fetch();
  }
});
