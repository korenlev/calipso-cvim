#!/usr/bin/env python3

# handle monitoring events

import argparse
import json
import sys

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', nargs='?', type=str,
        default='',
        help="read input from the specifed file \n(default: from stdin)")
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
        raise InputError("No input provided on stdin")
        exit(1)

check_result = json.loads(input)
check_result = check_result['check']
name = check_result['name']
status = check_result['status']
object_type = name[:name.index('_')]
object_id = name[name.index('_')+1:]

handler = None
if object_type == 'otep':
    from monitoring.handlers.handle_otep import HandleOtep
    handler = HandleOtep()
if object_type == 'pnic':
    from monitoring.handlers.handle_pnic import HandlePnic
    handler = HandlePnic()
if handler:
    handler.handle(object_id, check_result)

