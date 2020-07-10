import argparse
import json
import os
import ssl
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
REPLICA_SET = os.environ.get("CALIPSO_MONGO_SERVICE_RS_NAME", None)
CALIPSO_USER = os.environ.get("CALIPSO_MONGO_SERVICE_USER", DEFAULT_USER)
CALIPSO_PWD = os.environ.get("CALIPSO_MONGO_SERVICE_PWD")
CALIPSO_DB = os.environ.get("CALIPSO_MONGO_SERVICE_AUTH_DB", DEFAULT_DB)

STATUS_CODES = ["OK", "ERROR"]

max_connection_attempts = 3


# Lists of collections expected to exist in calipso DB
# Persistent collections will only be populated with initial data if they don't already exist in db
persistent_collections = {
    "api_tokens", "cliques", "connection_tests", "environments_config", "graphs",
    "inventory", "links", "messages", "scans", "scheduled_scans", "schemas", "validations"
}
# Predefined collections will always clear the existing data and repopulate the collections
predefined_collections = {
    "attributes_for_hover_on_data", "clique_constraints", "clique_types", "constants", "environment_options",
    "link_types", "supported_environments"
}


class MongoConnector(object):
    def __init__(self, host, port, rs=None):
        self.host = host
        self.port = port
        self.rs = rs

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
            uri = "mongodb://{}:{}@{}:{}/".format(quote_plus(self.user), quote_plus(self.pwd),
                                                  self.host, self.port)
        else:
            self.auth_enabled = False
            uri = "mongodb://{}:{}/".format(self.host, self.port)

        if self.db:
            uri += self.db
        if self.rs:
            uri += "?replicaSet={}".format(self.rs)

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

        print("Changing password for user '{}'".format(user))
        self.client[db if db else self.db].command("updateUser", user, pwd=new_pwd)
        if self.user == user:
            self.pwd = new_pwd
        print("Password for user '{}' successfully changed".format(user))

    def list_collections(self):
        # List all collections except for system ones
        return self.database.list_collection_names(filter={"name": {"$regex": r"^(?!system\\.)"}})

    def collection_exists(self, name):
        return name in self.list_collections()

    def create_collection(self, name, recreate=False):
        """
        :param name: collection name
        :param recreate: if True, drop the collection before creation
        :return: collection handle and the fact whether the collection was newly created
        """
        if self.collection_exists(name):
            if recreate:
                self.drop_collection(name)
            else:
                return self.database[name], False
        return self.database.create_collection(name), True

    def create_indexes(self, collection, indexes, recreate=True):
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

        if recreate:
            self.database[collection].drop_indexes()
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

    def insert_collection_from_file(self, path, collection, indexes=None, recreate=True):
        if self.collection_exists(collection) and not recreate:
            return

        with open(path) as f:
            data = json.load(f)
            self.create_collection(name=collection, recreate=True)

            if data:
                doc_ids = self.insert(collection, data)
                doc_count = len(doc_ids) if isinstance(doc_ids, list) else 1
                print("Inserted '{}' collection in db. Documents inserted: {}".format(collection, doc_count))

            if indexes:
                self.database[collection].create_indexes(indexes)

    def insert_collection(self, data_path, collection_name, indexes, recreate=True):
        filepath = os.path.join(data_path, "{}.json".format(collection_name))
        if os.path.exists(filepath):
            self.insert_collection_from_file(path=filepath, collection=collection_name,
                                             indexes=indexes, recreate=recreate)
        else:
            _, created = self.create_collection(name=collection_name, recreate=recreate)
            if indexes:
                self.create_indexes(collection=collection_name, indexes=indexes)

            if created:
                print("Inserted empty '{}' collection in db".format(collection_name))
            else:
                print("Persistent collection '{}' already exists in db".format(collection_name))

    def disconnect(self):
        if self.is_connected:
            print("Disconnecting from mongo...")
            self.client.close()
            self.client = None


# Exit with a pre-formatted message
def _exit(status_code, exit_code=None):
    # check STATUS_CODES for appropriate status texts
    print("Status code: {}".format(STATUS_CODES[status_code]))
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

    mongo_connector = MongoConnector(host=HOST, port=PORT, rs=REPLICA_SET)
    attempt = 1
    while True:
        try:
            # Connect with no auth
            mongo_connector.connect()

            # Create admin user
            mongo_connector.create_user(db=ADMIN_DB, user=ADMIN_USER, pwd=CALIPSO_PWD,
                                        roles=[{"role": "userAdminAnyDatabase", "db": ADMIN_DB},
                                               "clusterAdmin", "userAdmin"])
            # Create calipso user
            mongo_connector.create_user(db=CALIPSO_DB, user=CALIPSO_USER, pwd=CALIPSO_PWD,
                                        roles=[{"role": "readWrite", "db": CALIPSO_DB}])
            break
        except OperationFailure:
            print("Users are already configured")
            mongo_connector.disconnect()
            break
        except ConnectionFailure:
            if attempt >= max_connection_attempts:
                mongo_connector.disconnect()
                raise ValueError("Failed to connect to mongod. Tried {} times".format(attempt))
            attempt += 1
            print("Waiting for mongod to come online... Attempt #{}".format(attempt))
            # No need to use backoff since Mongo client has built-in timeout handling

    try:
        # Try connecting to calipso db with newly created user
        mongo_connector.connect(db=CALIPSO_DB, user=CALIPSO_USER, pwd=CALIPSO_PWD)
    except OperationFailure:
        print("Failed to connect as {} user".format(CALIPSO_USER))
        mongo_connector.disconnect()
        _exit(1)

    indexes_file = None
    try:
        indexes = {}
        try:
            indexes_file = open(os.path.join(args.data_path, "indexes.json"))
            indexes = json.load(indexes_file)
        except ValueError:
            print("Failed to parse indexes from indexes.json file")
        except IOError:
            print("Indexes file not found")

        existing_collections = mongo_connector.list_collections()
        # Go through all defined initial collections and them remove all deprecated ones
        for collection_name in persistent_collections:
            if collection_name in existing_collections:
                existing_collections.remove(collection_name)
            mongo_connector.insert_collection(data_path=args.data_path,
                                              collection_name=collection_name,
                                              indexes=indexes.get(collection_name),
                                              recreate=False)
        for collection_name in predefined_collections:
            if collection_name in existing_collections:
                existing_collections.remove(collection_name)
            mongo_connector.insert_collection(data_path=args.data_path,
                                              collection_name=collection_name,
                                              indexes=indexes.get(collection_name),
                                              recreate=True)

        for collection_name in existing_collections:
            print("Removing deprecated '{}' collection".format(collection_name))
            mongo_connector.drop_collection(collection_name)
    finally:
        mongo_connector.disconnect()
        if indexes_file:
            indexes_file.close()

    print("Initial data setup finished")
    _exit(0)


if __name__ == "__main__":
    run()
