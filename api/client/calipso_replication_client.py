import argparse
import copy
import json
import subprocess
import time
import ssl
from pymongo import MongoClient
from sys import exit
from six.moves import input
from six.moves.urllib.parse import quote_plus

from yaml import safe_load as yaml_load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


DEFAULT_PORT = 27017
DEFAULT_USER = 'calipso'
AUTH_DB = 'calipso'
DEBUG = False
QUIET = False

K8S = "k8s"
DEFAULT_K8S_NAMESPACE = "calipso"
DISCOVERABLE_DEPLOYMENT_TYPES = [K8S]

max_connection_attempts = 5
collection_names = ["environments_config", "inventory", "links", "messages", "scans", "scheduled_scans", "cliques"]
reconstructable_collections = ["inventory", "links", "cliques"]


def debug(msg):
    if DEBUG is True:
        print(msg)


def info(msg):
    if QUIET is not True:
        print(msg)


class MongoConnector(object):
    def __init__(self, host, port, user, pwd, db, db_label="central DB"):

        self.host = "[{}]".format(host) if ":" in host and "[" not in host else host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db
        self.db_label = db_label

        self.uri = None
        self.client = None
        self.database = None
        self.connect()

    def connect(self):
        self.disconnect()
        if self.user and self.pwd:
            self.uri = "mongodb://%s:%s@%s:%s/%s" % (quote_plus(self.user), quote_plus(self.pwd),
                                                     self.host, self.port, self.db)
        else:
            self.uri = "mongodb://%s:%s/%s" % (self.host, self.port, self.db)
        self.client = MongoClient(self.uri, connectTimeoutMS=10000, serverSelectionTimeoutMS=10000, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
        self.database = self.client[self.db]

    def disconnect(self):
        if self.client:
            info("Disconnecting from {}...".format(self.db_label))
            self.client.close()
            self.client = None

    def clear_collection(self, collection):
        self.database[collection].remove()

    def find_all(self, collection, remove_mongo_ids=False, env=None):
        if not env:
            env = {"$exists": True}
        if collection == "environments_config":
            if env:
                cursor = self.database[collection].find({"name": env})
            else:
                cursor = self.database[collection].find()
        else:
            mongo_filter = {"environment": env}
            cursor = self.database[collection].find(mongo_filter)
        docs = []
        for doc in cursor:
            if remove_mongo_ids is True:
                original_id = doc.pop('_id')
                if collection in reconstructable_collections:
                    doc['original_id'] = original_id
            docs.append(doc)
        return docs

    def collection_exists(self, name):
        return name in self.database.collection_names()

    def create_collection(self, name):
        return self.database.create_collection(name)

    def insert_collection(self, collection, data):
        if data:
            doc_ids = self.database[collection].insert(data)
            doc_count = len(doc_ids) if isinstance(doc_ids, list) else 1
            info("Inserted '{}' collection in {}, Total docs inserted: {}".format(collection, self.db_label, doc_count))
        elif not self.collection_exists(collection):
            self.create_collection(collection)
            info("Inserted empty '{}' collection in {}".format(collection, self.db_label))
        else:
            info("Skipping empty '{}' collection".format(collection,))


def backoff(i):
    return 2 ** (i - 1)


def read_servers_from_cli():
    try:
        servers_count = int(input("How many Calipso Servers to replicate? "))
        if servers_count < 1:
            raise TypeError()
    except TypeError:
        info("Server count should be a positive integer")
        return 1

    servers = []

    for n in range(1, servers_count + 1):
        remote_host = input("Remote Calipso Server #{} Hostname/IP\n".format(n))
        remote_secret = input("Remote Calipso Server #{} Secret\n".format(n))
        servers.append({"host": remote_host, "mongo_pwd": remote_secret, "attempt": 0, "imported": False})

    central_host = input("Central Calipso Server Hostname/IP\n")
    central_port = input("Central Calipso Server Port (default: {})\n".format(DEFAULT_PORT))
    central_secret = input("Central Calipso Server Secret\n")

    central = {'host': central_host, 'port': central_port if central_port else DEFAULT_PORT, 'mongo_pwd': central_secret}
    return servers, central


def read_servers_from_file(filename):
    with open(filename) as f:
        if filename.endswith(".yaml"):
            config = yaml_load(f)
        elif filename.endswith(".json"):
            config = json.load(f)

        for remote in config.get("remotes", []):
            remote.update({"attempt": 0, "imported": False})

        return config["remotes"], config.get("central")


def discover_k8s_mongo(namespace="calipso", kubectl_cmd=""):
    ns_arg = " -n {}".format(namespace) if namespace else ""
    if not kubectl_cmd:
        kubectl_cmd = "/usr/bin/kubectl"
    pod_cmd = subprocess.Popen('{} get pods{} -o json'.format(kubectl_cmd, ns_arg), shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)

    output, stderr = pod_cmd.communicate()
    if pod_cmd.returncode != 0 or stderr or len(output) < 1:
        raise Exception("Failed to discover location of central mongo server. Error: %s" % stderr)

    json_output = json.loads(output)
    central_config = None
    for pod in json_output["items"]:
        if pod["metadata"]["name"].startswith("calipso-mongo"):
            containers = pod["spec"]["containers"]
            if len(containers) == 0:
                raise ValueError("No running containers in mongo pod")
            env = containers[0]["env"]
            mongo_pwd = None
            for entry in env:
                if entry["name"] == "CALIPSO_MONGO_SERVICE_PWD":
                    mongo_pwd = entry["value"]
            if not mongo_pwd:
                raise ValueError("Mongo password not found in container env")
            central_config = {"host": pod["status"]["hostIP"], "mongo_pwd": mongo_pwd}
            break

    if not central_config:
        raise ValueError("Central mongo pod not found")

    # Assuming mongo pod uses NodePort service
    svc_cmd = subprocess.Popen('{} get service calipso-mongo{} -o json'.format(kubectl_cmd, ns_arg), shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, stderr = svc_cmd.communicate()
    if svc_cmd.returncode != 0 or stderr or len(output) < 1:
        raise Exception("Failed to get calipso-mongo service. Error: %s" % stderr)

    json_output = json.loads(output)
    ports = json_output['spec'].get('ports')
    if len(ports) < 1 or not ports[0].get("nodePort"):
        raise ValueError("Missing nodePort from mongo service spec")
    central_config['port'] = ports[0]['nodePort']
    return central_config


def discover_mongo_active_node(deployment_type, *args, **kwargs):
    if deployment_type == K8S:
        return discover_k8s_mongo(namespace=kwargs.get("namespace"), kubectl_cmd=kwargs.get("kubectl_cmd"))
    # TODO: support more deployment types
    raise ValueError("Central credentials not specified in config and no discoverable deployment type is chosen")


def add_duplicate_remotes(servers, scale):
    all_servers = copy.deepcopy(servers)
    for i in range(scale - len(servers)):
        dup_number = (i // len(servers)) + 1
        server = copy.deepcopy(servers[i % len(servers)])
        server['name'] = "{}-{}".format(server["name"], dup_number)
        all_servers.append(server)
    return all_servers


def reconstruct_ids(destination_connector):
    info("\nFixing ids for links and cliques")
    rc = {}
    for col in reconstructable_collections:
        rc[col] = {}
        objects = destination_connector.find_all(col)
        for obj in objects:
            original_id = obj.pop("original_id")
            rc[col][original_id] = obj

    for link_orig_id, link in rc["links"].items():
        if 'source' not in link or 'target' not in link:
            debug("Malformed link: {}".format(link))
            continue
        link["source"] = rc["inventory"][link["source"]]["_id"]
        link["target"] = rc["inventory"][link["target"]]["_id"]

    for clique_orig_id, clique in rc["cliques"].items():
        if any(req_field not in clique for req_field in ('links', 'links_detailed')):
            debug("Malformed clique: {}".format(clique))
            continue

        clique["focal_point"] = rc["inventory"][clique["focal_point"]]["_id"]

        if 'nodes' in clique:
            clique["nodes"] = [rc["inventory"][node_id]["_id"] for node_id in clique["nodes"]]

        clique_new_links, clique_new_links_detailed = [], []
        for link_id in clique["links"]:
            new_link = rc["links"][link_id]
            clique_new_links.append(new_link["_id"])
            clique_new_links_detailed.append(new_link)

        clique["links"] = clique_new_links
        clique["links_detailed"] = clique_new_links_detailed

    for col in reconstructable_collections:
        # TODO: scale - don't clear collection and split insertions
        destination_connector.clear_collection(col)
        destination_connector.insert_collection(col, list(rc[col].values()))


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",
                        help="Path to server configurations json file",
                        type=str,
                        required=False)
    parser.add_argument("--debug",
                        help="Print debug messages",
                        action="store_true",
                        required=False)
    parser.add_argument("--deployment_type",
                        type=str.lower,
                        help="Deployment type (for central config discovery)",
                        choices=DISCOVERABLE_DEPLOYMENT_TYPES)
    parser.add_argument("--namespace",
                        type=str,
                        help="K8s namespace with central mongo pod (deployment type: {}). Default: {}".format(K8S, DEFAULT_K8S_NAMESPACE),
                        default="calipso")
    parser.add_argument("--scale",
                        type=int,
                        default=1,
                        help="Target number of remote pods for scale testing. Must be greater than or equal to "
                             "the number of remote pods in the configuration. Other pods configurations will be "
                             "copied from supplied remotes data and have names with appended sequential numbers",
                        required=False)
    parser.add_argument("--quiet",
                        help="Silence all output",
                        action="store_true",
                        required=False)
    parser.add_argument("--version",
                        help="get a reply back with replication_client version",
                        action='version',
                        default=None,
                        version='%(prog)s version: 0.7.6')

    args = parser.parse_args()

    global DEBUG, QUIET
    DEBUG, QUIET = args.debug, args.quiet

    servers, central = read_servers_from_file(args.config) if args.config else read_servers_from_cli()
    if not central:
        central = discover_mongo_active_node(args.deployment_type, namespace=args.namespace)
    if len(servers) == 0:
        info("No remote servers defined. Nothing to replicate")
        return 0
    if len(servers) < args.scale:
        servers = add_duplicate_remotes(servers, args.scale)

    if not servers or all(s['imported'] is True for s in servers):
        info("Nothing to do. Exiting")
        return 0

    init_time = time.time()
    destination_connector = MongoConnector(host=central['host'], port=central.get('port', DEFAULT_PORT),
                                           user=DEFAULT_USER, pwd=central['mongo_pwd'], db=AUTH_DB)
    for col in collection_names:
        info("Clearing collection {} from central...".format(col))
        destination_connector.clear_collection(col)

    upload_time = time.time()
    while all(s['imported'] is False for s in servers):
        source_connector = None
        for s in servers:
            s['attempt'] += 1
            if s['attempt'] > 1:
                info("Retrying import from remote {}... Attempt #{}".format(s['name'], s['attempt']))
                time.sleep(backoff(s['attempt']))

            try:
                source_connector = MongoConnector(host=s["host"], port=s.get("port", DEFAULT_PORT),
                                                  user=DEFAULT_USER, pwd=s["mongo_pwd"], db=AUTH_DB,
                                                  db_label=s.get("name", "remote"))
                info("")
                for col in collection_names:
                    # read from remote DBs and export to local json files
                    info("Getting the {} Collection from {}...".format(col, s["name"]))

                    documents = source_connector.find_all(col, remove_mongo_ids=True)

                    # write all in-memory json docs into the central DB
                    info("Pushing the {} Collection into central...".format(col))
                    destination_connector.insert_collection(col, documents)

                s['imported'] = True
                source_connector.disconnect()
                source_connector = None
            except Exception as e:
                info("Failed to connect to {}, error: {}".format(s["name"], e.args))
                if source_connector is not None:
                    source_connector.disconnect()

                if s['attempt'] >= max_connection_attempts:
                    destination_connector.disconnect()
                    info("Failed to perform import from remote {}. Tried {} times".format(s['name'], s['attempt']))
                    return 1
                break

    # reconstruct source-target ids for links and cliques
    reconstruct_time = time.time()
    reconstruct_ids(destination_connector)
    destination_connector.disconnect()
    info("\nWorkload completed")
    finish_time = time.time()
    debug("Total time: {}\nUpload time: {}\nReconstruct time: {}".format(finish_time - init_time, reconstruct_time - upload_time, finish_time - reconstruct_time))
    return 0


if __name__ == "__main__":
    exit(run())
