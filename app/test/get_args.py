# This module use to parse arguments.
import argparse

from discover.logger import Logger


class GetArgs(Logger):
    def __init__(self):
        pass

    def get_args(self):
        # try to read scan plan from command line parameters
        parser = argparse.ArgumentParser()
        default_env = "Mirantis-Liberty"
        parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                            default="",
                            help="name of config file with MongoDB servr access details")
        parser.add_argument("-e", "--env", nargs="?", type=str,
                            default=default_env,
                            help="name of environment to scan \n(default: " + default_env + ")")
        parser.add_argument("-y", "--inventory", nargs="?", type=str,
                            default="inventory",
                            help="name of inventory collection \n(default: 'inventory')")
        parser.add_argument("-l", "--loglevel", nargs="?", type=str, default="INFO",
                            help="logging level \n(default: 'INFO')")
        args = parser.parse_args()
        return args
