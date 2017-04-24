import { SimpleSchema } from 'meteor/aldeed:simple-schema';

export let _idFieldDef = {
  type: { 
    _str: { type: String, regEx: SimpleSchema.RegEx.Id } 
  } 
};
