#!/usr/bin/env python3

# handle monitoring events

import argparse
import json
import sys

DEFAULT_ENV = "WebEX-Mirantis@Cisco"


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                        default="",
                        help="name of config file with MongoDB server " +
                        "access details")
    parser.add_argument("-e", "--env", nargs="?", type=str,
                        default=DEFAULT_ENV,
                        help="name of environment to scan \n" +
                        "(default: " + DEFAULT_ENV + ")")
    parser.add_argument("-y", "--inventory", nargs="?", type=str,
                        default="inventory",
                        help="name of inventory collection \n" +
                        "(default: 'inventory')")
    parser.add_argument('-i', '--inputfile', nargs='?', type=str,
                        default='',
                        help="read input from the specifed file \n" +
                        "(default: from stdin)")
    args = parser.parse_args()
    return args

input = None
args = get_args()
if args.inputfile:
    try:
        with open(args.inputfile, 'r') as input_file:
            input = input_file.read()
    except Exception as e:
        raise FileNotFoundError("failed to open input file: " + args.inputfile)
        exit(1)
else:
    input = sys.stdin.read()
    if not input:
        raise ValueError("No input provided on stdin")
        exit(1)

check_result = json.loads(input)
check_client = check_result['client']
check_result = check_result['check']
name = check_result['name']
status = check_result['status']
object_type = name[:name.index('_')]
object_id = name[name.index('_')+1:]
if 'environment' in check_client:
    args.env = check_client['environment']

handler = None
if object_type == 'otep':
    from monitoring.handlers.handle_otep import HandleOtep
    handler = HandleOtep(args)
if object_type == 'pnic':
    from monitoring.handlers.handle_pnic import HandlePnic
    handler = HandlePnic(args)
if object_type == 'vedge':
    from monitoring.handlers.handle_vedge_vpp import HandleVedgeVpp
    handler = HandleVedgeVpp(args)
if object_type == 'vnic':
    from monitoring.handlers.handle_vnic_vpp import HandleVnicVpp
    handler = HandleVnicVpp(args)
if object_type == 'link':
    from monitoring.handlers.handle_link import HandleLink
    handler = HandleLink(args)
if handler:
    handler.handle(object_id, check_result)
