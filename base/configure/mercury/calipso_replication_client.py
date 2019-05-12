import json
import os
import time
import traceback
from bson import json_util
from bson import BSON
try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus
from pymongo import MongoClient

BACKUP_DATA_PATH = """C:\it_logs"""
DEFAULT_PORT = 27017
DEFAULT_USER = 'calipso'
AUTH_DB = 'calipso'

max_connection_attempts = 5


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
            print("Disconnecting from mongo...")
            self.client.close()
            self.client = None

    def remove_collection(self, collection):
        self.database[collection].remove()

    def insert(self, collection, docs):
        return self.database[collection].insert(docs)

    def get_collection(self, srv_name, collection):
        file_name = "%s-%s.json" % (srv_name, collection)
        cursor = self.database[collection].find()
        f = open(os.path.join(BACKUP_DATA_PATH, file_name), "w")
        f.write('[')
        qnt_cursor = 0
        for document in cursor:
            qnt_cursor += 1
            num_max = cursor.count()
            if num_max == 1:
                f.write(json.dumps(document, indent=4, sort_keys=False, default=json_util.default))
            elif num_max >= 1 and qnt_cursor <= num_max - 1:
                f.write(json.dumps(document, indent=4, sort_keys=False, default=json_util.default))
                f.write(',')
            elif qnt_cursor == num_max:
                f.write(json.dumps(document, indent=4, sort_keys=False, default=json_util.default))
        f.write(']')
        print ("exported data saved to {}/{}-{}.json".format(BACKUP_DATA_PATH, srv_name, collection))
        return f

    def insert_collection(self, srv_name, collection):
        file_name = "%s-%s.json" % (srv_name, collection)
        with open(os.path.join(BACKUP_DATA_PATH, file_name)) as f:
            j_data = json.load(f)
            data = BSON.encode(j_data)
            self.remove_collection(collection)
            doc_ids = self.insert(collection, data)
            doc_count = len(doc_ids) if isinstance(doc_ids, list) else 1
            print("Inserted '%s' collection in central db. Documents inserted: %s" % (collection, doc_count))


def backoff(i):
    return 2 ** (i - 1)


if __name__ == "__main__":
    SRVN = input("How many SRVs to replicate? ")
    SRV = {}
    SRVs = []
    n = 1
    while n < SRVN + 1:
        remote_name = raw_input("Remote Calipso Server {} Hostname/IP\n".format(n))
        remote_secret = raw_input("Remote Calipso Server {} Secret\n".format(n))
        SRV.update({"name": remote_name, "secret": remote_secret})
        SRVs.append(SRV)
        n += 1
    collection_names = ["inventory", "links", "messages", "scans", "scheduled_scans",
                        "statistics", "cliques"]
    central_name = raw_input("Central Calipso Server Hostname/IP\n")
    central_secret = raw_input("Central Calipso Server Secret\n")
    attempt = 2
    while True:
        try:
            # read from remote DBs and export to local json files
            for s in SRVs:
                mongo_connector = MongoConnector(s["name"], DEFAULT_PORT,
                                                 DEFAULT_USER, s["secret"], AUTH_DB)
                print ("Exporting collections from {}...".format(s["name"]))
                for col in collection_names:
                    print("Exporting Collection {}...".format(col))
                    mongo_connector.get_collection(s["name"], col)
                    mongo_connector.disconnect()
                    # write from all local json files into the central DB
                    mongo_connector = MongoConnector(central_name, DEFAULT_PORT,
                                                     DEFAULT_USER, central_secret, AUTH_DB)
                    print ("Importing data from {}-{}.json...".format(s["name"], col))
                    mongo_connector.insert_collection(s["name"], col)
            break
        except:
            traceback.print_exc()
            if attempt >= max_connection_attempts:
                raise ValueError("Failed to connect to mongodb. Tried %s times" % attempt)
            attempt += 1
            print("Waiting for mongodb to come online... Attempt #%s" % attempt)
            time.sleep(backoff(attempt))
        mongo_connector.disconnect()
        print("Workload completed")
        exit(0)
