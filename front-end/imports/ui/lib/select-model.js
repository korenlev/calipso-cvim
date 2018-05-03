import * as R from 'ramda'; 

export const createSelectArgs = function (params) {
  let instance = Template.instance();
  let reset_fields = params.hash.reset_fields ? params.hash.reset_fields : [];

  return {
    values: params.hash.values,
    type: params.hash.type,
    placeholder: params.hash.placeholder,
    options: params.hash.options,
    multi: params.hash.multi ? params.hash.multi : false, 
    disabled: params.hash.disabled,
    reset_fields: reset_fields,
    setModel: params.hash.setModel ? params.hash.setModel.fn : 
      function (values) {
        let model = instance.data.model; 
        let newModel = R.assoc(params.hash.key, values, model);
        // Workaround for resetting independent model fields
        reset_fields.forEach(function(field) {
            // TODO: provide default value? Empty array may be fine though
            newModel = R.assoc(field, [], newModel);
        });
        if (instance.data.setModel) {
          instance.data.setModel(newModel); 
        }
      },
    showNullOption: R.isNil(params.hash.showNullOption) ? false : params.hash.showNullOption
  };
};
