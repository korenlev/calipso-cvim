import { ValidatedMethod } from 'meteor/mdg:validated-method';
import * as R from 'ramda';

import { ScanningRequests } from './scanning_requests';

export const insert = new ValidatedMethod({
  name: 'scanning_reuests.insert',
  validate: ScanningRequests.simpleSchema()
    .pick([
      'environment_name',
      'cgi',
      'mongo_config',
      'type',
      'inventory',
      'scan_self',
      'id',
      'parent_id',
      'parent_type',
      'id_field',
      'loglevel',
      'inventory_only',
      'links_only',
      'cliques_only',
      'clear',
    ]).validator({ clean: true, filter: false }),
  run({
    environment_name,
    cgi,
    mongo_config,
    type,
    inventory,
    scan_self,
    id,
    parent_id,
    parent_type,
    id_field,
    loglevel,
    inventory_only,
    links_only,
    cliques_only,
    clear,
  }) {
    let scanning_request = ScanningRequests.schema.clean({});
    scanning_request = R.merge(scanning_request, {
      environment_name,
      cgi,
      mongo_config,
      type,
      inventory,
      scan_self,
      id,
      parent_id,
      parent_type,
      id_field,
      loglevel,
      inventory_only,
      links_only,
      cliques_only,
      clear,
    });

    ScanningRequests.insert(scanning_request);
  }
});
