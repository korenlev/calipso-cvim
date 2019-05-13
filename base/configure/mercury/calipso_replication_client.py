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

    def remove_collection(self, collection):
        self.database[collection].remove()

    def get_collection(self, collection):
        cursor = self.database[collection].find()
        docs = []
        for doc in cursor:
            docs.append(doc)
        return docs

    def insert_collection(self, collection, data):
        doc_ids = self.database[collection].insert(data)
        doc_count = len(doc_ids) if isinstance(doc_ids, list) else 1
        print("Inserted '%s' collection in central DB, Total docs inserted: %s"
              % (collection, doc_count))


def backoff(i):
    return 2 ** (i - 1)


if __name__ == "__main__":
    SRVn = input("How many Calipso Servers to replicate? ")
    SRVs = []
    n = 1
    while n < SRVn + 1:
        SRV = {}
        remote_name = raw_input("Remote Calipso Server {} Hostname/IP\n".format(n))
        remote_secret = raw_input("Remote Calipso Server {} Secret\n".format(n))
        SRV.update({"name": remote_name, "secret": remote_secret})
        SRVs.append(SRV)
        n += 1
    collection_names = ["inventory", "links", "messages", "scans",
                        "scheduled_scans", "cliques"]
    central_name = raw_input("Central Calipso Server Hostname/IP\n")
    central_secret = raw_input("Central Calipso Server Secret\n")
    attempt = 2
    while True:
        mc2 = MongoConnector(central_name, DEFAULT_PORT, DEFAULT_USER,
                             central_secret, AUTH_DB)
        for col in collection_names:
            print ("Clearing collection {} from {}...".format(col,central_name))
            mc2.remove_collection(col)
        try:
            for s in SRVs:
                for col in collection_names:
                    # read from remote DBs and export to local json files
                    mc1 = MongoConnector(s["name"], DEFAULT_PORT, DEFAULT_USER,
                                         s["secret"], AUTH_DB)
                    print("Getting the {} Collection from {}...".format(col, s["name"]))
                    documents = mc1.get_collection(col)
                    time.sleep(1)
                    mc1.disconnect()
                    # write all in-memory json docs into the central DB
                    print ("Pushing the {} Collection into {}...".format(col, central_name))
                    mc2.insert_collection(col, documents)
                    time.sleep(1)
                    mc2.disconnect()
            break
        except:
            traceback.print_exc()
            if attempt >= max_connection_attempts:
                raise ValueError("Failed to connect to mongodb. Tried %s times" % attempt)
            attempt += 1
            print("Waiting for mongodb to come online... Attempt #%s" % attempt)
            time.sleep(backoff(attempt))
        mc1.disconnect()
        mc2.disconnect()
        print("Workload completed")
        exit(0)
