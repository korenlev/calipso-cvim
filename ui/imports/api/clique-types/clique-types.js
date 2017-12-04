/////////////////////////////////////////////////////////////////////////////////////////
// Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems) and others /
//                                                                                      /
// All rights reserved. This program and the accompanying materials                     /
// are made available under the terms of the Apache License, Version 2.0                /
// which accompanies this distribution, and is available at                             /
// http://www.apache.org/licenses/LICENSE-2.0                                           /
/////////////////////////////////////////////////////////////////////////////////////////
import { Mongo } from 'meteor/mongo';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import * as R from 'ramda';
import { Constants } from '/imports/api/constants/constants';
import { Environments } from '/imports/api/environments/environments';
import { LinkTypes } from '/imports/api/link-types/link-types';

export const CliqueTypes = new Mongo.Collection(
  'clique_types', { idGeneration: 'MONGO' });

let schema = {
  _id: { type: { _str: { type: String, regEx: SimpleSchema.RegEx.Id } } },

  environment: {
    type: String,
    defaultValue: "",
    optional: true,
    custom: function () {
      let that = this;
      if (that.value !== that.definition.defaultValue) {
        let env = Environments.findOne({name: that.value});

        if (R.isNil(env)) {
          return 'notAllowed';
        }
      }

      // Document validators workaround
      return callValidators(that);
    }
  },

  focal_point_type: {
    type: String,
    custom: function () {
      let that = this;
      let values = Constants.findOne({ name: 'object_types_for_links' }).data;

      if (R.isNil(R.find(R.propEq('value', that.value), values))) {
        return 'notAllowed';
      }
    }
  },

  link_types: {
    type: [String],
    minCount: 1,
    defaultValue: [],
    custom: function () {
      let that = this;
      let findResult = R.all(function (pLinkType) {
        if (R.isNil(LinkTypes.findOne({ type: pLinkType }))) {
          return false;
        }

        return true;
      }, that.value);

      if (! findResult) { return 'notAllowed'; }

      return;
    },
  },

  name: {
    type: String
  },

  distribution: {
    type: String,
    defaultValue: "",
    optional: true,
  },

  distribution_version: {
    type: String,
    defaultValue: "",
    optional: true,
  },

  mechanism_drivers: {
    type: String,
    defaultValue: "",
    optional: true,
    custom: function () {
      let that = this;
      let values = Constants.findOne({ name: 'mechanism_drivers' }).data;

      if (this.value !== this.definition.defaultValue
          && R.isNil(R.find(R.propEq('value', that.value), values))) {
        return 'notAllowed';
      }
    }
  },

  type_drivers: {
    type: String,
    defaultValue: "",
    optional: true,
    custom: function () {
      let that = this;
      let values = Constants.findOne({ name: 'type_drivers' }).data;

      if (this.value !== this.definition.defaultValue
          && R.isNil(R.find(R.propEq('value', that.value), values))) {
        return 'notAllowed';
      }
    }
  },

  use_implicit_links: {
    type: Boolean
  },
};

let simpleSchema = new SimpleSchema(schema);
simpleSchema.messages({'insufficientData': 'Environment or configuration should be specified'});

// Document validators workaround
function callValidators(context) {
  if (R.isNil(context.docId)) {
    context.docId = context.field('_id').value;
  }

  let validators = [requiredFieldsValidator, focalPointValidator,
                    nameValidator, duplicateConfigurationValidator];

  for (let i=0; i<validators.length; i++) {
    let error = validators[i](context);
    if (!R.isNil(error)) {
      return error;
    }
  }
}

function focalPointValidator(that) {
  // Validate focal point uniqueness
  console.log("Validator: focal point uniqueness");

  let existing = CliqueTypes.findOne({
    environment: that.field('environment').value,
    focal_point_type: that.field('focal_point_type').value
  });

  if (R.allPass([
    R.pipe(R.isNil, R.not),
    R.pipe(R.propEq('_id', that.docId), R.not)
  ])(existing)) {
    console.warn("Duplicate focal point type in env");
    return 'alreadyExists';
  }
}

function nameValidator(that) {
  // Validate name uniqueness
  console.log("Validator: name uniqueness");

  let existing = CliqueTypes.findOne({
    environment: that.field('environment').value,
    name: that.field('name').value
  });

  if (R.allPass([
    R.pipe(R.isNil, R.not),
    R.pipe(R.propEq('_id', that.docId), R.not)
  ])(existing)) {
    console.warn("Duplicate name in env");
    return 'alreadyExists';
  }
}

export function isEmpty(obj) {
    return R.isEmpty(obj) || R.isNil(obj)
}

function requiredFieldsValidator(that) {
  // Validate all required fields
  console.log("Validator: required fields");

  let populated = R.filter((f) => !isEmpty(that.field(f).value))
                           (['environment', 'distribution', 'mechanism_drivers', 'type_drivers']);

  if (populated.length === 0) {
    console.warn("Insufficient data");
    return 'insufficientData'
  }
}

function duplicateConfigurationValidator(that) {
  // Validate that the clique type configuration is not a duplicate
  // Environment-specific duplicates are handled in other validators
  console.log("Validator: duplicate clique type configuration");
  if (!isEmpty(that.field('environment').value)) {
    return;
  }

  let fields = ['distribution', 'mechanism_drivers', 'type_drivers'];
  let search = {};
  for (let i = 0; i < fields.length; ++i) {
      let field = fields[i];
      let value = that.field(field).value;
      if (!isEmpty(value)) {
          search[field] = value;
          if (field === 'distribution') {
              let dv = that.field('distribution_version').value;
              if (!isEmpty(dv)) {
                  search['distribution_version'] = dv;
              }
          }
          break;
      }
  }

  let existing = CliqueTypes.findOne(search);
  if (R.allPass([
          R.pipe(R.isNil, R.not),
          R.pipe(R.propEq('_id', that.docId), R.not)
      ])(existing)) {
      console.warn("Duplicate clique type");
      return 'alreadyExists';
  }
}

CliqueTypes.schema = simpleSchema;
CliqueTypes.attachSchema(CliqueTypes.schema);
