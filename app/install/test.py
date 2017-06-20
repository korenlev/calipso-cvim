import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--Hostname", help="Hostname or IP address of the server (default=localhost)",
                    type=str)
parser.add_argument("WebUI_port", help="Port for the Calipso WebUI (default=80)", nargs='*',
                    type=str)
parser.add_argument("DB_port", help="Port for the Calipso MongoDB (default=27017)",
                    type=str)
args = parser.parse_args()
if args.Hostname:
    print ("verbosity turned on")
print(args.Hostname, args.WebUI_port, args.DB_port)
