import { Mongo } from 'meteor/mongo';

export const SupportedEnvironments = new Mongo.Collection(
  'supported_environments', { idGeneration: 'MONGO' });

export const subsNameSupportedEnvs = 'supported-environments';

export function isMonitoringSupported(distribution, type_drivers, mechanism_drivers) {
  return SupportedEnvironments.find({
    'environment.distribution': distribution,
    'environment.type_drivers': type_drivers,
    'environment.mechanism_drivers': { $in: mechanism_drivers },
    'features.monitoring': true
  }).count() > 0;
}

export function isListeningSupported(distribution, type_drivers, mechanism_drivers) {
  return SupportedEnvironments.find({
    'environment.distribution': distribution,
    'environment.type_drivers': type_drivers,
    'environment.mechanism_drivers': { $in: mechanism_drivers },
    'features.listening': true
  }).count() > 0;
}
