/////////////////////////////////////////////////////////////////////////////////////////
// Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems) and others /
//                                                                                      /
// All rights reserved. This program and the accompanying materials                     /
// are made available under the terms of the Apache License, Version 2.0                /
// which accompanies this distribution, and is available at                             /
// http://www.apache.org/licenses/LICENSE-2.0                                           /
/////////////////////////////////////////////////////////////////////////////////////////
import { SimpleSchema } from 'meteor/aldeed:simple-schema';

export const AciSchema = new SimpleSchema({
  name: { 
    type: String, 
    autoValue: function () { return 'ACI'; } 
  },
  host: { 
    type: String,
    regEx: SimpleSchema.RegEx.IP,
    defaultValue: '10.56.0.104',
  },
  user: { 
    type: String, 
    defaultValue: 'admin'
  },
  pwd: { 
    type: String,
    defaultValue: 'C1sco12345'
  },
});