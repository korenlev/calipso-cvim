import { ValidatedMethod } from 'meteor/mdg:validated-method';
import * as R from 'ramda';

import { ScheduledScans } from './scheduled-scans';

export const insert = new ValidatedMethod({
  name: 'scheduled-scans.insert',
  validate: ScheduledScans.simpleSchema()
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
      'freq',
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
    freq,
  }) {
    let scan = ScheduledScans.schema.clean({ });

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
      freq, 
    });

    ScheduledScans.insert(scan);
  },

});

export const update = new ValidatedMethod({
  name: 'scheduled_scans.update',
  validate: ScheduledScans.simpleSchema()
    .pick([
      '_id',
      'environment',
      'inventory',
      'object_id',
      'log_level',
      'clear',
      'loglevel',
      'scan_only_inventory',
      'scan_only_links',
      'scan_only_cliques',
      'freq',
    ]).validator({ clean: true, filter: false }),
  run({
    _id,
    environment,
    inventory,
    object_id,
    log_level,
    clear,
    loglevel,
    scan_only_inventory,
    scan_only_links,
    scan_only_cliques,
    freq,
  }) {
    let item = ScheduledScans.findOne({ _id: _id });
    console.log('scheduled scan for update: ', item);

    item = R.merge(R.pick([
      'environment',
      'inventory',
      'object_id',
      'log_level',
      'clear',
      'loglevel',
      'scan_only_inventory',
      'scan_only_links',
      'scan_only_cliques',
      'freq',
    ], item), {
      environment,
      inventory,
      object_id,
      log_level,
      clear,
      loglevel,
      scan_only_inventory,
      scan_only_links,
      scan_only_cliques,
      freq,
    });

    ScheduledScans.update({ _id: _id }, { $set: item });
  }
});

export const remove = new ValidatedMethod({
  name: 'scheduled_scans.remove',
  validate: ScheduledScans.simpleSchema()
    .pick([
      '_id',
    ]).validator({ clean: true, filter: false }),
  run({
    _id
  }) {
    let item = ScheduledScans.findOne({ _id: _id });
    console.log('scheduled scan for remove: ', item);

    ScheduledScans.remove({ _id: _id });
  }
});
