import * as R from 'ramda';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { pathRegEx } from '/imports/lib/general-regex';

export const CLISchema = new SimpleSchema({
  name: { type: String, autoValue: function () { return 'CLI'; } },
  host: { type: String },
  key: { 
    type: String,
    regEx: pathRegEx,
    optional: true
  },
  user: { type: String },
  pwd: { 
    type: String,
    optional: true
  },
});

CLISchema.addValidator(function () {
  let that = this;

  let conf = {};
  if (isConfEmpty(conf)) {
    return;
  }

  let validationResult = R.find((validationFn) => {
    return validationFn(that).isError;
  }, [ keyPasswordValidation ]);

  if (R.isNil(validationResult)) { return; }

  throw validationResult(that);
});

function keyPasswordValidation(schemaItem) {
  let password = schemaItem.field('pwd');
  let key = schemaItem.field('key');

  if (key.value || password.value) { return { isError: false }; }

  return {
    isError: true,
    type: 'subGroupError',
    data: [],
    message: 'Master Host Group: At least one required: key or password'
  }; 
}

function isConfEmpty(conf) {
  return R.find((key) => {
    return !(R.isNil(conf[key]));
  }, R.keys(conf));
}
