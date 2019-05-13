import argparse
import json
import time
import traceback
try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus
from pymongo import MongoClient

DEFAULT_PORT = 27017
DEFAULT_USER = 'calipso'
AUTH_DB = 'calipso'

max_connection_attempts = 5
collection_names = ["inventory", "links", "messages", "scans", "scheduled_scans", "cliques"]


class MongoConnector(object):
    def __init__(self, host, port, user, pwd, db):
        # Create calipso db and user if they don't exist
        base_uri = "mongodb://%s:%s/" % (host, port)
        base_client = MongoClient(base_uri)
        base_client.close()

        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db

        self.uri = None
        self.client = None
        self.database = None
        self.connect()

    def connect(self):
        self.disconnect()
        self.uri = "mongodb://%s:%s@%s:%s/%s" % (quote_plus(self.user), quote_plus(self.pwd),
                                                 self.host, self.port, self.db)
        self.client = MongoClient(self.uri)
        self.database = self.client[self.db]

    def disconnect(self):
        if self.client:
            print("Disconnecting from DB...")
            self.client.close()
            self.client = None

    def clear_collection(self, collection):
        self.database[collection].remove()

    def find_all(self, collection, remove_mongo_ids=False):
        cursor = self.database[collection].find()
        docs = []
        for doc in cursor:
            if remove_mongo_ids is True:
                doc.pop('_id')
            docs.append(doc)
        return docs

    def insert_collection(self, collection, data):
        doc_ids = self.database[collection].insert(data)
        doc_count = len(doc_ids) if isinstance(doc_ids, list) else 1
        print("Inserted '%s' collection in central DB, Total docs inserted: %s"
              % (collection, doc_count))


def backoff(i):
    return 2 ** (i - 1)


def read_servers_from_cli():
    try:
        servers_count = int(input("How many Calipso Servers to replicate? "))
        if servers_count < 1:
            raise TypeError()
    except TypeError:
        print("Server count should be a positive integer")
        return 1

    servers = []
    for n in range(1, servers_count + 1):
        remote_name = raw_input("Remote Calipso Server #{} Hostname/IP\n".format(n))
        remote_secret = raw_input("Remote Calipso Server #{} Secret\n".format(n))
        servers.append({"name": remote_name, "secret": remote_secret, "attempt": 0, "imported": False})

    central_name = raw_input("Central Calipso Server Hostname/IP\n")
    central_secret = raw_input("Central Calipso Server Secret\n")

    central = {'name': central_name, 'secret': central_secret}
    return servers, central


def read_servers_from_file(filename):
    with open(filename) as f:
        config = json.load(f)

        servers = [
            {"name": r['name'], "secret": r['secret'], "attempt": 0, "imported": False}
            for r in config['remotes']
        ]

        return servers, config['central']


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",
                        help="Path to server configurations json file",
                        type=str,
                        required=False)

    args = parser.parse_args()
    servers, central = read_servers_from_file(args.config) if args.config else read_servers_from_cli()

    if not servers or all(s['imported'] is True for s in servers):
        print("Nothing to do. Exiting")
        return 0

    destination_connector = MongoConnector(central['name'], DEFAULT_PORT, DEFAULT_USER, central['secret'], AUTH_DB)
    for col in collection_names:
        print ("Clearing collection {} from {}...".format(col, central['name']))
        destination_connector.clear_collection(col)

    while all(s['imported'] is False for s in servers):
        source_connector = None
        for s in servers:
            s['attempt'] += 1
            if s['attempt'] > 1:
                print("Retrying import from remote {}... Attempt #{}".format(s['name'], s['attempt']))
                time.sleep(backoff(s['attempt']))

            try:
                source_connector = MongoConnector(s["name"], DEFAULT_PORT, DEFAULT_USER, s["secret"], AUTH_DB)
                for col in collection_names:
                    # read from remote DBs and export to local json files
                    print("Getting the {} Collection from {}...".format(col, s["name"]))

                    documents = source_connector.find_all(col, remove_mongo_ids=True)

                    # write all in-memory json docs into the central DB
                    print ("Pushing the {} Collection into {}...".format(col, central['name']))
                    destination_connector.insert_collection(col, documents)

                s['imported'] = True
                source_connector.disconnect()
                source_connector = None
            except Exception:
                if source_connector is not None:
                    source_connector.disconnect()
                traceback.print_exc()

                if s['attempt'] >= max_connection_attempts:
                    destination_connector.disconnect()
                    print("Failed to perform import from remote {}. Tried {} times".format(s['name'], s['attempt']))
                    return 1

    destination_connector.disconnect()
    print("Workload completed")
    return 0


if __name__ == "__main__":
    exit(run())
