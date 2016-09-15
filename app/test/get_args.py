# This module is used to parse arguments.
import argparse

from discover.logger import Logger
from test.config.local_config import MONGODB_CONFIG, ENV_CONFIG, COLLECTION_CONFIG


class GetArgs(Logger):
    def __init__(self):
        pass

    def get_args(self):
        # try to read scan plan from command line parameters
        parser = argparse.ArgumentParser()
        default_env = ENV_CONFIG
        parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                            default=MONGODB_CONFIG,
                            help="name of config file with MongoDB servr access details")
        parser.add_argument("-e", "--env", nargs="?", type=str,
                            default=default_env,
                            help="name of environment to scan \n(default: " + default_env + ")")
        parser.add_argument("-y", "--inventory", nargs="?", type=str,
                            default=COLLECTION_CONFIG,
                            help="name of inventory collection \n(default: 'inventory')")
        parser.add_argument("-l", "--loglevel", nargs="?", type=str, default="INFO",
                            help="logging level \n(default: 'INFO')")
        args = parser.parse_args()
        return args
