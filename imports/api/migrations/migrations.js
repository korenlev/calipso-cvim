import { CliqueTypes } from '/imports/api/clique-types/clique-types';

Migrations.add({
  version: 1,
  up: () => {
    console.log('migrating: add clique type constaints for env+name, env+focal_point_type');
    CliqueTypes._ensureIndex({ environment: 1, name: 1 });
    CliqueTypes._ensureIndex({ environment: 1, focal_point_type: 1 });
  },
  down: () => {
  }
});
