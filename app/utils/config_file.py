import os


class ConfigFile:

    def get_config_file(self, config_file):
        # try to look in the current work directory
        # as defined by PYTHONPATH
        python_path = os.environ['PYTHONPATH']
        if os.pathsep in python_path:
            python_path = python_path.split(os.pathsep)[0]
        config_file = python_path + '/config/' + config_file
        return config_file

    # read config info from config file
    def read_config_from_config_file(self, config_file):
        params = {}
        try:
            with open(config_file) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("#") or " " not in line:
                        continue
                    index = line.index(" ")
                    key = line[: index].strip()
                    value = line[index + 1:].strip()
                    if value:
                        params[key] = value
        except Exception as e:
            raise e
        return params
