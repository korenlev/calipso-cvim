import * as R from 'ramda'; 

export const createSelectArgs = function (params) {
  let instance = Template.instance();
  return {
    context: params.hash.context,
    key: params.hash.key,
    type: params.hash.type,
    placeholder: params.hash.placeholder,
    options: params.hash.options,
    multi: params.hash.multi ? params.hash.multi : false, 
    setModel: function (key, value) {
      let mainModel = instance.data.model; 
      let newMainModel = R.assoc(key, value, mainModel);
      instance.data.setModel(instance.data.key, newMainModel); 
    },
  };
};
