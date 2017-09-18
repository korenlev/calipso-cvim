#!/usr/bin/env python3
from abc import ABC
import argparse
import distutils.version
import logging
import os.path
import re
import subprocess
import sys


def run_command(cmd, raise_on_error=False) -> str:
    try:
        output = subprocess.check_output([cmd], shell=True)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        error_msg = 'Error running command: {}, output: {}'\
            .format(cmd, e.output.decode('utf-8'))
        if raise_on_error:
            raise RuntimeError(error_msg)
        return msg


class Logger(ABC):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

    PROJECT_NAME = 'Calipso'

    levels = [DEBUG, INFO, WARNING, ERROR, CRITICAL]
    log_format = '%(asctime)s %(levelname)s: %(message)s'
    formatter = logging.Formatter(log_format)
    default_level = INFO

    def __init__(self, logger_name: str = PROJECT_NAME,
                 level: str = default_level):
        super().__init__()
        self.check_level(level)
        self.log = logging.getLogger(logger_name)
        logging.basicConfig(format=self.log_format,
                            level=level)
        self.log.propagate = False
        self.set_loglevel(level)
        self.env = None
        self.level = level

    def set_env(self, env):
        self.env = env

    @staticmethod
    def check_level(level):
        if level.upper() not in Logger.levels:
            raise ValueError('Invalid log level: {}. Supported levels: ({})'
                             .format(level, ", ".join(Logger.levels)))

    @staticmethod
    def get_numeric_level(loglevel):
        Logger.check_level(loglevel)
        numeric_level = getattr(logging, loglevel.upper(), Logger.default_level)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: {}'.format(loglevel))
        return numeric_level

    def set_loglevel(self, loglevel):
        # assuming loglevel is bound to the string value obtained from the
        # command line argument. Convert to upper case to allow the user to
        # specify --log=DEBUG or --log=debug
        numeric_level = self.get_numeric_level(loglevel)

        for handler in self.log.handlers:
            handler.setLevel(numeric_level)
        self.log.setLevel(numeric_level)
        self.level = loglevel

    def _log(self, level, message, *args, exc_info=False, **kwargs):
        self.log.log(level, message, *args, exc_info=exc_info, **kwargs)

    def debug(self, message, *args, **kwargs):
        self._log(logging.DEBUG, message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        self._log(logging.INFO, message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self._log(logging.WARNING, message, *args, **kwargs)

    def warn(self, message, *args, **kwargs):
        self.warning(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        self._log(logging.ERROR, message, *args, **kwargs)

    def exception(self, message, *args, **kwargs):
        self._log(logging.ERROR, message, exc_info=True, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        self._log(logging.CRITICAL, message, *args, **kwargs)

    def add_handler(self, handler):
        handler_defined = handler.__class__ in map(lambda h: h.__class__,
                                                   self.log.handlers)

        if not handler_defined:
            handler.setLevel(self.level)
            handler.setFormatter(self.formatter)
            self.log.addHandler(handler)


class FileLogger(Logger):

    def __init__(self, log_file: str, level: str = Logger.default_level):
        super().__init__(logger_name="{}-File".format(self.PROJECT_NAME),
                         level=level)
        self.add_handler(logging.handlers.WatchedFileHandler(log_file))


class ApexEnvironmentFetcher:

    DEFAULTS = {
        'logfile': '/home/calipso/log/apex_environment_fetch.log',
        'mongo_config': '/local_dir/calipso_mongo_access.conf',
        'config_dir': '/home/calipso/apex_configuration',
        'env': 'Apex-Euphrates',
        'loglevel': 'INFO',
        'git_repo': 'https://git.opnfv.org/calipso',
        'root': False
    }

    USER_NAME = 'calipso'
    USER_PWD = 'calipso_default'
    REPO_LOCAL_NAME = 'Calipso'
    INSTALLER = 'python3 app/install/calipso-installer.py --command start-all'
    CONFIG_FILE_NAME = 'apex-configuration.conf'
    SSH_DIR = '/home/calipso/.ssh'

    def __init__(self):
        self.args = self.get_args()
        self.log = None
        self.config_file = '{}/{}'.format(self.args.config_dir,
                                          self.CONFIG_FILE_NAME)

    def get_args(self):
        # try to read scan plan from command line parameters
        parser = argparse.ArgumentParser()
        parser.add_argument('-m', '--mongo_config', nargs='?', type=str,
                            default=self.DEFAULTS['mongo_config'],
                            help='name of config file ' +
                                 'with MongoDB server access details\n'
                                 '(Default: {})'
                                 .format(self.DEFAULTS['mongo_config']))
        parser.add_argument('-d', '--config_dir', nargs='?', type=str,
                            default=self.DEFAULTS['config_dir'],
                            help='path to directory with config data\n'
                                 '(Default: {})'
                                 .format(self.DEFAULTS['config_dir']))
        parser.add_argument('-a', '--apex', nargs='?', type=str,
                            help='name of environment to Apex host')
        parser.add_argument('-e', '--env', nargs='?', type=str,
                            help='name of environment to create')
        parser.add_argument('-l', '--loglevel', nargs='?', type=str,
                            default=self.DEFAULTS['loglevel'],
                            help='logging level \n(default: "{}")'
                            .format(self.DEFAULTS['loglevel']))
        parser.add_argument('-f', '--logfile', nargs='?', type=str,
                            default=self.DEFAULTS['logfile'],
                            help='log file \n(default: "{}")'
                            .format(self.DEFAULTS['logfile']))
        parser.add_argument('-g', '--git', nargs='?', type=str,
                            help='URL to clone Git repository\n(default: {})'
                            .format(self.DEFAULTS['git_repo']),
                            default=self.DEFAULTS['git_repo'])
        parser.add_argument('--root', dest='root', action='store_true')
        parser.add_argument('--no-root', dest='root', action='store_false')
        parser.set_defaults(root=False)
        return parser.parse_args()

    @staticmethod
    def run_cmd(cmd: str ='', use_sudo=True, as_user=None):
        sudo_prefix = '' if not use_sudo \
            else 'sudo {} '.format(as_user if as_user else '')
        command = '{}{}'.format(sudo_prefix, cmd)
        output = run_command(cmd=command, raise_on_error=True)
        return output

    def add_user(self):
        if not os.path.exists('/home/{}'.format(self.USER_NAME)):
            self.run_cmd('adduser -p {} {}'.format(self.USER_PWD,
                                                   self.USER_NAME))
        self.run_cmd('usermod -aG wheel {}'.format(self.USER_NAME))

    def add_log_dir(self):
        log_dir = os.path.dirname(self.args.logfile)
        self.run_cmd('mkdir -p {}'.format(log_dir), use_sudo=self.args.root)
        self.run_cmd('chmod a+w {}'.format(log_dir), use_sudo=self.args.root)

    def get_source_tree(self):
        self.run_cmd('git clone {} {}'.format(self.args['git_repo'],
                                              self.REPO_LOCAL_NAME),
                     as_user=self.USER_NAME)

    @staticmethod
    def version_greater_eq(v1, v2):
        return distutils.version.StrictVersion(v1) >= \
               distutils.version.StrictVersion(v2)

    def has_prerequisite(self, package: str, version: str=None):
        try:
            info = self.run_cmd('yum info {}'.format(package))
            if not info or re.match('Error: No matching Packages', info):
                return False
            if not version:
                return True
            # check version
            lines = info.splitlines()
            matches = [l for l in lines if re.match('version *:', l)]
            if not matches:
                raise ValueError('version data missing in "yum info" output '
                                 '(package {})'
                                 .format(package))
            actual_version = matches[0]
            if not self.version_greater_eq(actual_version, version):
                print('package {}: version required={}, actual={}'
                      .format(package, version, actual_version))
        except RuntimeError as e:
            err_number, err_text = e.args
            if 'not found' in err_text:
                return False
            else:
                raise e

    def install_prerequisite(self, package: str, version: str=None):
        if self.has_prerequisite(package, version):
            return
        self.run_cmd('yum install {}'.format(package))
        self.run_cmd('')

    def run_installer(self):
        if self.args.root:
            self.install_prerequisite('python', '3.5')
            self.install_prerequisite('docker', '17.03')
            # XXX need to find name of docker lib
            self.install_prerequisite('python docker lib')
        self.run_cmd('cd {} && {}'
                     .format(self.REPO_LOCAL_NAME, self.INSTALLER),
                     as_user=self.USER_NAME)

    def get_inet(self):
        output = self.run_cmd('ifconfig br-admin')
        lines = output.splitlines()
        if not lines or len(lines) < 2:
            self.log.error('Unable to feth inet address, output: {}'
                           .format(output))
            return
        inet_parts = lines[1].split()
        inet_address = inet_parts[1]
        return inet_address

    def set_ssh_dir(self):
        self.run_cmd('mkdir -p {}'.format(self.SSH_DIR))
        # will be used to access undercloud VM
        self.run_cmd('cp /root/.ssh/id_rsa {}/uc-id_rsa'.format(self.SSH_DIR))
        self.run_cmd('cp /root/.ssh/id_rsa.pub {}/uc-id_rsa.pub'
                     .format(self.SSH_DIR))
        self.run_cmd('chown calipso.calipso {}/uc-id_rsa*'.format(self.SSH_DIR))

    def setup_environment_config(self, config_file):
        self.run_cmd('mkdir -p {}'.format(self.args.config_dir))
        env_config = {
            'name': self.args.env,
            'configuration': []
        }
        inet = self.get_inet()
        config_file.write('inet {}\n'.format(inet))
        self.set_ssh_dir()

    def setup_environment(self):
        print('Fetching Apex environment settings')
        if False:  # XXX currently disabled
            if self.args.root:
                self.add_user()
            self.add_log_dir()
            self.log = FileLogger(self.args.logfile)
            if self.args.root:
                self.get_source_tree()
            self.run_installer()
        with open(self.config_file, 'w') as config_file:
            self.setup_environment_config(config_file)
        print('Finished fetching Apex environment settings')

    def get(self):
        try:
            self.setup_environment()
            return True, 'Environment setup finished successfully'
        except RuntimeError as e:
            return False, str(e)

if __name__ == '__main__':
    fetcher = ApexEnvironmentFetcher()
    ret, msg = fetcher.get()
    if not ret:
        if fetcher.log:
            fetcher.log.error(msg)
        else:
            print(msg)
    sys.exit(0 if ret else 1)
