//import * as R from 'ramda';

import { check } from 'meteor/check';
import * as R from 'ramda';
import { Inventory } from '../inventories';
import { Environments } from '/imports/api/environments/environments';
import { regexEscape } from '/imports/lib/regex-utils';

const AUTO_COMPLETE_RESULTS_LIMIT = 5;



Meteor.methods({
  'inventorySearch': function(searchTerm, envName) {
    check(searchTerm, String);
    this.unblock();
    let searchExp = new RegExp(regexEscape(searchTerm), 'i');
    let env = Environments.findOne({ name: envName });

    let results = Inventory.find({ 
      environment: envName, 
      name: searchExp 
    }, {
      limit: AUTO_COMPLETE_RESULTS_LIMIT 
    }).fetch();

    return R.map((inventory) => {
      return R.merge(inventory, {
        _envId: env._id
      });
    }, results);

  },

  'expandNodePath': function(nodeId) {
    console.log('method server: expandNodePath', R.toString(nodeId));

    //check(nodeId, MongoI);
    this.unblock();

    let node = Inventory.findOne({ _id: nodeId });
    if (R.isNil(node)) { 
      console.log('method server: expandNodePath - no node');
      return null; 
    }

    let idList = R.pipe(R.split('/'), R.drop(2))(node.id_path);
    let result = R.map((partId) => {
      return Inventory.findOne({ environment: node.environment, id: partId });
    }, idList);
    
    console.log('method server: expandNodePath - results', result);
    return result;
  },
});

