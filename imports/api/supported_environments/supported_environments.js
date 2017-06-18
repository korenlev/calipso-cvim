import { Mongo } from 'meteor/mongo';
import * as R from 'ramda';

export const SupportedEnvironments = new Mongo.Collection(
  'supported_environments', { idGeneration: 'MONGO' });

export const subsNameSupportedEnvs = 'supported-environments';

export function isMonitoringSupported(distribution, type_drivers, mechanism_drivers) {
  console.log('isMonitoringSupported');
  console.log(`distribution: ${R.toString(distribution)}`);
  console.log(`type_drivers: ${R.toString(type_drivers)}`);
  console.log(`mechanism_drivers: ${R.toString(mechanism_drivers)}`);

  let result = SupportedEnvironments.find({
    'environment.distribution': distribution,
    'environment.type_drivers': type_drivers,
    'environment.mechanism_drivers': { $in: mechanism_drivers },
    'features.monitoring': true
  }).count() > 0;

  console.log(`result: ${R.toString(result)}`);
  return result;
}

export function isListeningSupported(distribution, type_drivers, mechanism_drivers) {
  console.log('isListeningSupported');
  console.log(`distribution: ${R.toString(distribution)}`);
  console.log(`type_drivers: ${R.toString(type_drivers)}`);
  console.log(`mechanism_drivers: ${R.toString(mechanism_drivers)}`);

  let result = SupportedEnvironments.find({
    'environment.distribution': distribution,
    'environment.type_drivers': type_drivers,
    'environment.mechanism_drivers': { $in: mechanism_drivers },
    'features.listening': true
  }).count() > 0;

  console.log(`result: ${R.toString(result)}`);
  return result;
}