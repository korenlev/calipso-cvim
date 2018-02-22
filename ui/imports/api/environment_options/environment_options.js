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

export const EnvironmentOptions =
    new Mongo.Collection('environment_options', { idGeneration: 'MONGO' });

let schema = {
    _id: { type: { _str: { type: String, regEx: SimpleSchema.RegEx.Id } } },
    distributions: { type: [String] },
    distribution_versions: { type: [String] },
    mechanism_drivers: { type: [String] },
    type_drivers: { type: [String] },
};

EnvironmentOptions.schema = schema;
EnvironmentOptions.attachSchema(schema);

EnvironmentOptions.getByDistribution = function(distribution, field) {
    return R.ifElse(R.isNil, R.always([]), R.prop(field)) (
        EnvironmentOptions.findOne({ distributions: distribution })
    ).map(elem => ({'label': elem, 'value': elem}));
};