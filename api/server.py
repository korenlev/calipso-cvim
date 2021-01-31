###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import argparse
import os

from gunicorn.app.base import BaseApplication
from gunicorn.six import iteritems

from api.app import App
from api.client.version import VERSION


# This class is used to integrate Gunicorn with falcon application
from base.utils.logging.logger import Logger


class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options
        self.application = app
        super().__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


_DEFAULTS = {
    "bind": "127.0.0.1:8000",
    "gunicorn_config": "/var/lib/calipso/gunicorn_logging.conf",
    "inventory": "inventory",
    "logfile": "api.log",
    "loglevel": Logger.INFO,
    "token-lifetime": 86400
}


def get_args():
    # TODO: defaults
    parser = argparse.ArgumentParser(description="Parameters for Calipso API")
    parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                        default=_DEFAULTS.get("mongo_config", ""),
                        help="name of config file with mongo access "
                             "details")
    parser.add_argument("--auth_config", nargs="?", type=str,
                        default=_DEFAULTS.get("auth_config", ""),
                        help="name of config file with "
                             "plaintext auth credentials")
    parser.add_argument("--cert_file", nargs="?", type=str,
                        default=_DEFAULTS.get("cert_file", ""),
                        help="path to SSL certificate")
    parser.add_argument("--key_file", nargs="?", type=str,
                        default=_DEFAULTS.get("key_file", ""),
                        help="path to SSL key")
    parser.add_argument("--no_ldap", action='store_true',
                        help="skip LDAP authentication")
    parser.add_argument("--ldap_config", nargs="?", type=str,
                        default=_DEFAULTS.get("ldap_config", ""),
                        help="name of the config file with ldap server "
                             "config details")
    parser.add_argument("-f", "--logfile", nargs="?", type=str,
                        default=_DEFAULTS["logfile"],
                        help="API log file name \n(default: {})".format(_DEFAULTS["logfile"]))
    parser.add_argument("-l", "--loglevel", nargs="?", type=str,
                        default=_DEFAULTS["loglevel"],
                        help="logging level \n(default: '{}')".format(_DEFAULTS["loglevel"]))
    parser.add_argument("--gunicorn_config", nargs="?", type=str,
                        default=_DEFAULTS["gunicorn_config"],
                        help="Gunicorn config file location")
    parser.add_argument("-b", "--bind", nargs="?", type=str,
                        default=_DEFAULTS["bind"],
                        help="binding address of the API server."
                             "Multiple comma-separated IPs are allowed\n"
                             "(default: {})".format(_DEFAULTS["bind"]))
    parser.add_argument("-y", "--inventory", nargs="?", type=str,
                        default=_DEFAULTS["inventory"],
                        help="name of inventory collection \n" +
                             "(default: '{}')".format(_DEFAULTS["inventory"]))
    parser.add_argument("-t", "--token-lifetime", nargs="?", type=int,
                        default=_DEFAULTS["token-lifetime"],
                        help="lifetime of the token")
    parser.add_argument("--version",
                        help="get Calipso API version",
                        action='version',
                        default=None,
                        version='Calipso API version: {}'.format(VERSION))
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()
    # Gunicorn configuration
    options = {
        "bind": args.bind.split(",") if "," in args.bind else args.bind,
        "certfile": args.cert_file,
        "keyfile": args.key_file,
        "workers": 4,
    }
    if os.path.isfile(args.gunicorn_config):
        options["logconfig"] = args.gunicorn_config

    app = App(mongo_config=args.mongo_config,
              ldap_enabled=not args.no_ldap,
              ldap_config=args.ldap_config,
              auth_config=args.auth_config,
              log_file=args.logfile,
              log_level=args.loglevel,
              inventory=args.inventory,
              token_lifetime=args.token_lifetime).get_app()
    StandaloneApplication(app, options).run()
