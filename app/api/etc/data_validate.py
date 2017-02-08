class DataValidate:

    LIST = "list"

    def __init__(self):
        self.bool_table = {
            True: ["true", "1", 1],
            False: ["false", "0", 0]
        }
        self.types_customized_names = {
            'str': 'string',
            'bool': 'boolean',
            'int': 'integer',
            'ObjectId': 'MonoDB ObjectId'
        }

    def validate_and_convert_to_type(self, obj, t, converted):
        if converted:
            # user may input different values for the boolean True or False
            # convert the number or the string to corresponding python bool values
            if t == bool:
                if isinstance(obj, str):
                    obj = obj.lower()
                for b, values in self.bool_table.items():
                    if obj in values:
                        return b
                return None
            try:
                obj = t(obj)
            except Exception:
                return None
            return obj
        else:
            return obj if isinstance(obj, t) else None

    # get the requirement for validation
    # this requirement object will be used in validate_data method
    def get_validate_requirement(self, t, type_converted=False, validate=None, requirement=None,
                                 mandatory=False, error_messages={}):
        return {
            "type": t,
            "type_converted": type_converted,
            "validate": validate,
            "requirement": requirement,
            "mandatory": mandatory,
            "error_messages": error_messages
        }

    def validate_data(self, data, requirements):
        passed = True
        error_message = ""

        for key, requirement in requirements.items():
            # filters must contain mandatory keys
            value = data.get(key)
            error_messages = requirement['error_messages']
            type_converted = requirement['type_converted']
            if not value:
                if requirement["mandatory"]:
                    passed = False
                    error_message = error_messages['mandatory'] if "mandatory" in error_messages \
                        else "{} must be specified".format(key)
                    break
                else:
                    continue

            # check the type
            requirement_types = requirement['type']
            if not isinstance(requirement_types, list):
                requirement_types = [requirement_types]
            type_validated = False
            for requirement_type in requirement_types:
                converted_val = self.validate_and_convert_to_type(value, requirement_type, type_converted)
                if converted_val is not None:
                    if type_converted:
                        # value has been converted, update the data
                        data[key] = converted_val
                        value = converted_val
                    type_validated = True
                    break
            if not type_validated:
                passed = False
                print(type(value))
                required_types_string = self.prettify_string(
                    self.get_type_names(requirement_types), "or"
                )
                error_message = error_messages['type'] if 'type' in error_messages else \
                    "{0} should be {1}".format(key, required_types_string)
                break

            # validate the data against the requirement
            validate = requirement.get('validate')
            if not validate:
                continue
            requirement_value = requirement.get('requirement')
            if not isinstance(value, list):
                value = [value]
            # the data should be one of the values of the list
            if validate == DataValidate.LIST:
                for v in value:
                    if v not in requirement_value:
                        passed = False
                        error_message = error_messages['validate'] if 'validate' in error_messages else \
                            "The possible values of {0} are {1}" .format(key, self.prettify_string(requirement_value))
                        break
        return {"passed": passed, "error_message": error_message}

    # get customized type names from type names array
    def get_type_names(self, types):
        return [self.get_type_name(t) for t in types]

    # get customized type name from string <class 'type'>
    def get_type_name(self, t):
        t = str(t)
        a = t.split(" ")[1]
        type_name = a.rstrip(">").strip("'")
        # strip the former module names
        type_name = type_name.split('.')[-1]
        if type_name in self.types_customized_names.keys():
            type_name = self.types_customized_names[type_name]
        return type_name

    def prettify_string(self, arr, conj="and"):
        pretty_str = ""
        length = len(arr)
        if length == 0:
            return pretty_str
        if length == 1:
            return arr[0]
        for i, val in enumerate(arr):
            if i == 0:
                pretty_str += val
            elif i == length - 1:
                pretty_str += " {0} {1}".format(conj, val)
            else:
                pretty_str += ", " + val
        return pretty_str