import { ValidatedMethod } from 'meteor/mdg:validated-method';
import * as R from 'ramda';

import { Scans } from './scans';

export const insert = new ValidatedMethod({
  name: 'scans.insert',
  validate: Scans.simpleSchema()
    .pick([
      'environment',
      'inventory',
      'object_id',
      'log_level',
      'clear',
      'loglevel',
      'scan_only_inventory',
      'scan_only_links',
      'scan_only_cliques',
    ]).validator({ clean: true, filter: false }),
  run({
    environment,
    inventory,
    object_id,
    log_level,
    clear,
    loglevel,
    scan_only_inventory,
    scan_only_links,
    scan_only_cliques,
  }) {
    let scan = Scans.schema.clean({
      status: 'pending'
    });
    scan = R.merge(scan, {
      environment,
      inventory,
      object_id,
      log_level,
      clear,
      loglevel,
      scan_only_inventory,
      scan_only_links,
      scan_only_cliques,
      submit_timestamp: Date.now()
    });

    Scans.insert(scan);
  },

});
