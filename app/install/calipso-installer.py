from pymongo import MongoClient, ReturnDocument
from pymongo.errors import ConnectionFailure
from urllib.parse import quote_plus
import docker
import argparse
import dockerpycreds
import time

class MongoComm:
    # deals with communication from host/installer server to mongoDB

    try:

        def __init__(self, user, password, host, db, port):
            self.uri = "mongodb://%s:%s@%s:%s/%s" % (
                quote_plus(user), quote_plus(password), host, port, db)
            self.client = MongoClient(self.uri)

        def find(self, coll, key, val):
            collection = self.client.calipso[coll]
            doc = collection.find({key: val})
            return doc

        def get(self, coll, doc_name):
            collection = self.client.calipso[coll]
            doc = collection.find_one({"name": doc_name})
            return doc

        def insert(self, coll, doc):
            collection = self.client.calipso[coll]
            doc_id = collection.insert(doc)
            return doc_id

        def remove(self, coll, doc):
            collection = self.client.calipso[coll]
            collection.remove(doc)

        def update(self, coll, key, val, data):
            collection = self.client.calipso[coll]
            collection.find_one_and_update(
                {key: val},
                {"$set": data},
                upsert=True
            )

    except ConnectionFailure:
        print("MongoDB Server not available")

parser = argparse.ArgumentParser()
parser.add_argument("--Hostname", help="Hostname or IP address of the server (default=172.17.0.1)",type=str,
                    default="172.17.0.1", required=False)
parser.add_argument("--WebUI_port", help="Port for the Calipso WebUI (default=80)",type=int,
                    default="80", required=False)
parser.add_argument("--DB_name", help="DataBase name for the Calipso MongoDB (default=calipso)",type=str,
                    default="calipso", required=False)
parser.add_argument("--DB_port", help="Port for the Calipso MongoDB (default=27017)",type=int,
                    default="27017", required=False)
parser.add_argument("--DB_user", help="User for the Calipso MongoDB (default=calipso)",type=str,
                    default="calipso", required=False)
parser.add_argument("--DB_password", help="Password for the Calipso MongoDB (default=calipso_default)",type=str,
                    default="calipso_default", required=False)
args = parser.parse_args()

container = ""
action = ""
container_names = ["all", "calipso-mongo", "calipso-scan", "calipso-listen", "calipso-ldap", "calipso-api",
                     "calipso-sensu", "calipso-ui"]
while container not in container_names:
    container = input("Container? (all, calipso-mongo, calipso-scan, calipso-listen, calipso-ldap, calipso-api, "
                      "calipso-sensu, calipso-ui or 'q' to quit):\n")
    if container == "q":
        exit()
container_actions = ["stop", "start"]
while action not in container_actions:
    action = input("Action? (stop, start, or 'q' to quit):\n")
    if action == "q":
        exit()

DockerClient = docker.from_env()   # using local host docker environment parameters

if action == "start":
    if container == "all" or "calipso-mongo":
        print("starting container calipso-mongo...\n")
        MongoContainer = DockerClient.containers.run('korenlev/calipso:mongo',detach=True, name="calipso-mongo",
                                             ports={'27017/tcp': 27017, '28017/tcp': 28017},
                                             volumes={'/home/calipso/db': {'bind': '/data/db', 'mode': 'rw'}})
    if container == "all" or "calipso-listen":
        print("starting container calipso-listen...\n")
        ListenContainer = DockerClient.containers.run('korenlev/calipso:listen',detach=True, name="calipso-listen",
                                              ports={'22/tcp': 50022},
                                              environment=["PYTHONPATH=/home/scan/calipso_prod/app",
                                                          "MONGO_CONFIG=/local_dir/calipso_mongo_access.conf"],
                                              volumes={'/home/calipso': {'bind': '/local_dir', 'mode': 'rw'}})
    if container == "all" or "calipso-ldap":
        print("starting container calipso-ldap...\n")
        LDAPContainer = DockerClient.containers.run('korenlev/calipso:ldap',detach=True, name="calipso-ldap",
                                            ports={'389/tcp': 389, '389/udp': 389},
                                            volumes={'/home/calipso/': {'bind': '/local_dir/', 'mode': 'rw'}})
    if container == "all" or "calipso-api":
        print("starting container calipso-api...\n")
        APIContainer = DockerClient.containers.run('korenlev/calipso:api',detach=True, name="calipso-api",
                                           ports={'8000/tcp': 8000, '22/tcp': 40022},
                                           environment=["PYTHONPATH=/home/scan/calipso_prod/app",
                                                          "MONGO_CONFIG=/local_dir/calipso_mongo_access.conf",
                                                          "LDAP_CONFIG=/local_dir/ldap.conf",
                                                          "LOG_LEVEL=DEBUG"],
                                           volumes={'/home/calipso/': {'bind': '/local_dir/', 'mode': 'rw'}})
    if container == "all" or "calipso-scan":
        print("starting container calipso-scan...\n")
        ScanContainer = DockerClient.containers.run('korenlev/calipso:scan',detach=True, name="calipso-scan",
                                            ports={'22/tcp': 30022},
                                            environment=["PYTHONPATH=/home/scan/calipso_prod/app",
                                                         "MONGO_CONFIG=/local_dir/calipso_mongo_access.conf"],
                                            volumes={'/home/calipso/': {'bind': '/local_dir/', 'mode': 'rw'}})
    if container == "all" or "calipso-sensu":
        print("starting container calipso-sensu...\n")
        SensuContainer = DockerClient.containers.run('korenlev/calipso:sensu',detach=True, name="calipso-sensu",
                                             ports={'22/tcp': 20022, '3000/tcp': 3000, '4567/tcp': 4567,
                                                    '5671/tcp': 5671, '15672/tcp': 15672},
                                             environment=["PYTHONPATH=/home/scan/calipso_prod/app"],
                                             volumes={'/home/calipso/': {'bind': '/local_dir/', 'mode': 'rw'}})
    if container == "all" or "calipso-ui":
        print("starting container calipso-ui...\n")
        UIContainer = DockerClient.containers.run('korenlev/calipso:ui',detach=True, name="calipso-ui",
                                                  ports={'3000/tcp': 80},
                                                  environment=["ROOT_URL=http://korlev-calipso-dev.cisco.com:80",
                                                               "MONGO_URL=mongodb://calipso:calipso_default@"
                                                               "korlev-calipso-dev.cisco.com:27017/calipso",
                                                               "LDAP_CONFIG=/local_dir/ldap.conf"])

    c = MongoComm(args.DB_user, args.DB_password, args.Hostname, args.DB_name, args.DB_port)
    doc = dict(name="name", game_password="game_password")
    c.insert("coll", doc)

if action == "stop":
    if (container == "all" or container == "calipso-mongo") and \
            (DockerClient.containers.list(all=True, filters={"name": "calipso-mongo"})):
        print("fetching container name calipso-mongo...\n")
        calipso_mongo = DockerClient.containers.get("calipso-mongo")
        if calipso_mongo.status != "running":
            print("calipso-mongo is not running...")
            time.sleep(1)
            print("removing container name", calipso_mongo.name, "...\n")
            calipso_mongo.remove()
        else:
            print("killing container name", calipso_mongo.name, "...\n")
            calipso_mongo.kill()
            time.sleep(1)
            print("removing container name", calipso_mongo.name, "...\n")
            calipso_mongo.remove()
    else:
        print("no container named 'calipso-mongo' found...")

    if (container == "all" or container == "calipso-listen") and \
            (DockerClient.containers.list(all=True, filters={"name": "calipso-listen"})):
        print("fetching container name calipso-listen...\n")
        calipso_listen = DockerClient.containers.get("calipso-listen")
        if calipso_listen.status != "running":
            print("calipso-listen is not running...")
            time.sleep(1)
            print("removing container name", calipso_listen.name, "...\n")
            calipso_listen.remove()
        else:
            print("killing container name", calipso_listen.name, "...\n")
            calipso_listen.kill()
            time.sleep(1)
            print("removing container name", calipso_listen.name, "...\n")
            calipso_listen.remove()
    else:
        print("no container named 'calipso-listen' found...")

    if (container == "all" or container == "calipso-ldap") and \
            (DockerClient.containers.list(all=True, filters={"name": "calipso-ldap"})):
        print("fetching container name calipso-ldap...\n")
        calipso_ldap = DockerClient.containers.get("calipso-ldap")
        if calipso_ldap.status != "running":
            print("calipso-ldap is not running...")
            time.sleep(1)
            print("removing container name", calipso_ldap.name, "...\n")
            calipso_mongo.remove()
        else:
            print("killing container name", calipso_ldap.name, "...\n")
            calipso_ldap.kill()
            time.sleep(1)
            print("removing container name", calipso_ldap.name, "...\n")
            calipso_ldap.remove()
    else:
        print("no container named 'calipso-ldap' found...")

    if (container == "all" or container == "calipso-api") and \
            (DockerClient.containers.list(all=True, filters={"name": "calipso-api"})):
        print("fetching container name calipso-api...\n")
        calipso_api = DockerClient.containers.get("calipso-api")
        if calipso_api.status != "running":
            print("calipso-api is not running...")
            time.sleep(1)
            print("removing container name", calipso_api.name, "...\n")
            calipso_api.remove()
        else:
            print("killing container name", calipso_api.name, "...\n")
            calipso_api.kill()
            time.sleep(1)
            print("removing container name", calipso_api.name, "...\n")
            calipso_api.remove()
    else:
        print("no container named 'calipso-api' found...")

    if (container == "all" or container == "calipso-scan") and \
            (DockerClient.containers.list(all=True, filters={"name": "calipso-scan"})):
        print("fetching container name calipso-scan...\n")
        calipso_scan = DockerClient.containers.get("calipso-scan")
        if calipso_scan.status != "running":
            print("calipso-scan is not running...")
            time.sleep(1)
            print("removing container name", calipso_scan.name, "...\n")
            calipso_scan.remove()
        else:
            print("killing container name", calipso_scan.name, "...\n")
            calipso_scan.kill()
            time.sleep(1)
            print("removing container name", calipso_scan.name, "...\n")
            calipso_scan.remove()
    else:
        print("no container named 'calipso-scan' found...")

    if (container == "all" or container == "calipso-sensu") and \
            (DockerClient.containers.list(all=True, filters={"name": "calipso-sensu"})):
        print("fetching container name calipso-sensu...\n")
        calipso_sensu = DockerClient.containers.get("calipso-sensu")
        if calipso_sensu.status != "running":
            print("calipso-sensu is not running...")
            time.sleep(1)
            print("removing container name", calipso_sensu.name, "...\n")
            calipso_sensu.remove()
        else:
            print("killing container name", calipso_sensu.name, "...\n")
            calipso_sensu.kill()
            time.sleep(1)
            print("removing container name", calipso_sensu.name, "...\n")
            calipso_sensu.remove()
    else:
        print("no container named 'calipso-sensu' found...")

    if (container == "all" or container == "calipso-ui") and \
            (DockerClient.containers.list(all=True, filters={"name": "calipso-ui"})):
        print("fetching container name calipso-ui...\n")
        calipso_ui = DockerClient.containers.get("calipso-ui")
        if calipso_ui.status != "running":
            print("calipso-ui is not running...")
            time.sleep(1)
            print("removing container name", calipso_ui.name, "...\n")
            calipso_ui.remove()
        else:
            print("killing container name", calipso_ui.name, "...\n")
            calipso_ui.kill()
            time.sleep(1)
            print("removing container name", calipso_ui.name, "...\n")
            calipso_ui.remove()
    else:
        print("no container named 'calipso-ui' found...")

