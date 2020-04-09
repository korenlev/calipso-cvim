from __future__ import print_function

try:
    from future import standard_library
    standard_library.install_aliases()
except ImportError:
    pass

import argparse
import json
import os
import ssl
try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus
from pymongo import MongoClient, IndexModel, ASCENDING
from pymongo.errors import OperationFailure, ConnectionFailure

DEFAULT_INITIAL_DATA_PATH = "/calipso/mongo/initial_data"
DEFAULT_DB = "calipso"
DEFAULT_USER = "calipso"
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 27017
ADMIN_USER = "admin"
ADMIN_DB = "admin"

SSL_ENABLED = os.environ.get("CALIPSO_MONGO_SSL_ENABLED", True)
HOST = os.environ.get("CALIPSO_MONGO_SERVICE_HOST", DEFAULT_HOST)
PORT = os.environ.get("CALIPSO_MONGO_SERVICE_PORT", DEFAULT_PORT)
CALIPSO_USER = os.environ.get("CALIPSO_MONGO_SERVICE_USER", DEFAULT_USER)
CALIPSO_PWD = os.environ.get("CALIPSO_MONGO_SERVICE_PWD")
CALIPSO_DB = os.environ.get("CALIPSO_MONGO_SERVICE_AUTH_DB", DEFAULT_DB)

STATUS_CODES = ["OK", "ERROR"]

max_connection_attempts = 3
initial_collections = {"api_tokens", "attributes_for_hover_on_data", "clique_constraints", "clique_types",
                       "cliques", "connection_tests", "constants", "environment_options", "environments_config",
                       "graphs", "inventory", "link_types", "links", "messages",
                       "meteor_accounts_loginServiceConfiguration", "monitoring_config", "monitoring_config_templates",
                       "network_agent_types", "roles", "scans", "scheduled_scans", "schemas", "statistics",
                       "supported_environments", "user_settings", "users", "validations"}


class MongoConnector(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.user = None
        self.pwd = None
        self.db = None

        self.client = None
        self.auth_enabled = False

    @property
    def is_connected(self):
        return self.client is not None

    @property
    def database(self):
        return self.client[self.db] if self.is_connected and self.db else None

    def connect(self, db=None, user=None, pwd=None):
        self.disconnect()
        self.db = db
        self.user = user
        self.pwd = pwd
        if user and pwd:
            self.auth_enabled = True
            uri = "mongodb://%s:%s@%s:%s/%s" % (quote_plus(self.user), quote_plus(self.pwd),
                                                self.host, self.port, self.db)
        else:
            self.auth_enabled = False
            uri = "mongodb://%s:%s/" % (self.host, self.port)

        if SSL_ENABLED:
            self.client = MongoClient(uri, ssl=True, ssl_cert_reqs=ssl.CERT_NONE, connect=True)
        else:
            self.client = MongoClient(uri, connect=True)

    def create_user(self, db=None, user=None, pwd=None, roles=None):
        if not self.auth_enabled:
            if not user or not pwd:
                raise ValueError("User and pwd need to be specified while auth is disabled")
        elif self.user != ADMIN_USER:
            raise ValueError("Only admin user can create other users while auth is enabled")

        if not roles:
            roles = ["readWrite"]

        return self.client[db if db else self.db].command("createUser",
                                                          user if user else self.user,
                                                          pwd=pwd if pwd else self.pwd,
                                                          roles=roles)

    def change_password(self, new_pwd, db=None, user=None):
        if not new_pwd:
            print("New password is empty")

        if not user:
            user = self.user
        if user == self.user and new_pwd == self.pwd:
            print("Passwords are identical")

        if self.auth_enabled and not self.user == ADMIN_USER and self.user != user:
            raise ValueError("Only admin user can change other users' passwords while auth is enabled")

        print("Changing password for user '%s'" % user)
        self.client[db if db else self.db].command("updateUser", user, pwd=new_pwd)
        if self.user == user:
            self.pwd = new_pwd
        print("Password for user '%s' successfully changed" % user)

    def collection_exists(self, name):
        return name in self.database.collection_names()

    def create_collection(self, name, recreate=False):
        if self.collection_exists(name):
            if recreate:
                self.drop_collection(name)
            else:
                return self.database[name]
        return self.database.create_collection(name)

    def create_indexes(self, collection, indexes):
        if not indexes:
            return

        index_models = []
        for index in indexes:
            if isinstance(index, dict):
                index_models.append(IndexModel([(k, v) for k, v in index.items()]))
            elif isinstance(index, list):
                index_models.append(IndexModel([(i, ASCENDING) for i in index]))
            else:
                index_models.append(IndexModel([(index, ASCENDING)]))

        return self.database[collection].create_indexes(index_models)

    def drop_collection(self, name):
        self.database[name].drop()

    def find(self, collection, query=None):
        return self.database[collection].find(query)

    def find_one(self, collection, query=None):
        return self.database[collection].find_one(query)

    def insert(self, collection, docs):
        return self.database[collection].insert(docs)

    def update(self, collection, spec, doc, upsert=False):
        return self.database[collection].update(spec, doc, upsert=upsert)

    def insert_collection_from_file(self, path, collection, indexes=None):
        with open(path) as f:
            data = json.load(f)
            self.create_collection(name=collection, recreate=True)

            if data:
                doc_ids = self.insert(collection, data)
                doc_count = len(doc_ids) if isinstance(doc_ids, list) else 1
                print("Inserted '%s' collection in db. Documents inserted: %s" % (collection, doc_count))

            if indexes:
                self.database[collection].create_indexes(indexes)

    def disconnect(self):
        if self.is_connected:
            print("Disconnecting from mongo...")
            self.client.close()
            self.client = None


# Exit with a pre-formatted message
def _exit(status_code, exit_code=None):
    # check STATUS_CODES for appropriate status texts
    print("Status code: %s" % STATUS_CODES[status_code])
    exit(exit_code if exit_code is not None else status_code)


def run():
    if not CALIPSO_PWD:
        print("CALIPSO_MONGO_SERVICE_PWD environment variable is not defined")
        _exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data_path",
                        help="Path to initial data collections (default={})".format(DEFAULT_INITIAL_DATA_PATH),
                        type=str,
                        default=DEFAULT_INITIAL_DATA_PATH,
                        required=False)
    args = parser.parse_args()

    mongo_connector = MongoConnector(HOST, PORT)
    attempt = 1
    while True:
        try:
            # Connect with no auth
            mongo_connector.connect()

            # Create admin user
            mongo_connector.create_user(db=ADMIN_DB, user=ADMIN_USER, pwd=CALIPSO_PWD,
                                        roles=[{"role": "userAdminAnyDatabase", "db": ADMIN_DB}])
            # Create calipso user
            mongo_connector.create_user(db=CALIPSO_DB, user=CALIPSO_USER, pwd=CALIPSO_PWD,
                                        roles=[{"role": "readWrite", "db": CALIPSO_DB}])
            break
        except OperationFailure as e:  # TODO!
            print(e)
            # print("Initial data already setup. Exiting")
            mongo_connector.disconnect()
            _exit(0)
        except ConnectionFailure:
            if attempt >= max_connection_attempts:
                mongo_connector.disconnect()
                raise ValueError("Failed to connect to mongod. Tried %s times" % attempt)
            attempt += 1
            print("Waiting for mongod to come online... Attempt #%s" % attempt)
            # No need to use backoff since Mongo client has built-in timeout handling

    try:
        # Try connecting to calipso db with newly created user
        mongo_connector.connect(db=CALIPSO_DB, user=CALIPSO_USER, pwd=CALIPSO_PWD)
    except OperationFailure:
        print("Failed to setup calipso user")
        mongo_connector.disconnect()
        _exit(1)

    indexes_file = None
    try:
        environments_collection = mongo_connector.database['environments_config']
        if environments_collection.count() > 0:
            print("Database and at least one environment already exist, skipping data setup...")
        else:
            indexes = {}
            try:
                indexes_file = open(os.path.join(args.data_path, "indexes.json"))
                indexes = json.load(indexes_file)
            except ValueError:
                print("Failed to parse indexes from indexes.json file")
            except IOError:
                print("Indexes file not found")

            for collection_name in initial_collections:
                filepath = os.path.join(args.data_path, "{}.json".format(collection_name))
                if os.path.exists(filepath):
                    mongo_connector.insert_collection_from_file(path=filepath, collection=collection_name,
                                                                indexes=indexes.get(collection_name))
                else:
                    mongo_connector.create_collection(name=collection_name, recreate=True)
                    if indexes:
                        mongo_connector.create_indexes(collection=collection_name,
                                                       indexes=indexes.get(collection_name))
                    print("Inserted empty '%s' collection in db" % (collection_name,))
    finally:
        mongo_connector.disconnect()
        if indexes_file:
            indexes_file.close()

    print("Initial data setup finished")
    _exit(0)


if __name__ == "__main__":
    run()
