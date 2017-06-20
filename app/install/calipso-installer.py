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
                    default="172.17.0.1", required=True)
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

DockerClient = docker.from_env()   # using local host docker environment parameters

MongoContainer = DockerClient.containers.run('korenlev/calipso:mongo',detach=True, name="calipso-mongo",
                                             ports={'27017/tcp': 27017, '28017/tcp': 28017},
                                             volumes={'/home/calipso/db': {'bind': '/data/db', 'mode': 'rw'}})

ListenContainer = DockerClient.containers.run('korenlev/calipso:listen',detach=True, name="calipso-listen",
                                             ports={'22/tcp': 50022},
                                             environment=["PYTHONPATH=/home/scan/calipso_prod/app",
                                                          "MONGO_CONFIG=/local_dir/calipso_mongo_access.conf"],
                                             volumes={'/home/calipso': {'bind': '/local_dir', 'mode': 'rw'}})

LDAPContainer = DockerClient.containers.run('korenlev/calipso:ldap',detach=True, name="calipso-ldap",
                                             ports={'389/tcp': 389, '389/udp': 389},
                                             volumes={'/home/calipso/': {'bind': '/local_dir/', 'mode': 'rw'}})

APIContainer = DockerClient.containers.run('korenlev/calipso:api',detach=True, name="calipso-api",
                                             ports={'8000/tcp': 8000, '22/tcp': 40022},
                                             environment=["PYTHONPATH=/home/scan/calipso_prod/app",
                                                          "MONGO_CONFIG=/local_dir/calipso_mongo_access.conf",
                                                          "LDAP_CONFIG=/local_dir/ldap.conf",
                                                          "LOG_LEVEL=DEBUG"],
                                             volumes={'/home/calipso/': {'bind': '/local_dir/', 'mode': 'rw'}})

ScanContainer = DockerClient.containers.run('korenlev/calipso:scan',detach=True, name="calipso-scan",
                                             ports={'22/tcp': 30022},
                                             environment=["PYTHONPATH=/home/scan/calipso_prod/app",
                                                          "MONGO_CONFIG=/local_dir/calipso_mongo_access.conf"],
                                             volumes={'/home/calipso/': {'bind': '/local_dir/', 'mode': 'rw'}})

SensuContainer = DockerClient.containers.run('korenlev/calipso:sensu',detach=True, name="calipso-sensu",
                                             ports={'22/tcp': 20022, '3000/tcp': 3000, '4567/tcp': 4567,
                                                    '5671/tcp': 5671, '15672/tcp': 15672},
                                             environment=["PYTHONPATH=/home/scan/calipso_prod/app"],
                                             volumes={'/home/calipso/': {'bind': '/local_dir/', 'mode': 'rw'}})

UIContainer = DockerClient.containers.run('korenlev/calipso:ui',detach=True, name="calipso-ui",
                                             ports={'3000/tcp': 80},
                                             environment=["ROOT_URL=http://korlev-calipso-dev.cisco.com:80",
                                                          "MONGO_URL=mongodb://calipso:calipso_default@korlev-calipso-dev.cisco.com:27017/calipso",
                                                          "LDAP_CONFIG=/local_dir/ldap.conf"])

# creating objects from each running container:
time.sleep(1)
calipso_sensu = DockerClient.containers.get("calipso-sensu")
time.sleep(1)
calipso_api = DockerClient.containers.get("calipso-api")
time.sleep(1)
calipso_listen = DockerClient.containers.get("calipso-listen")
time.sleep(1)
calipso_mongo = DockerClient.containers.get("calipso-mongo")
time.sleep(1)
calipso_ui = DockerClient.containers.get("calipso-ui")
time.sleep(1)
calipso_scan = DockerClient.containers.get("calipso-scan")
time.sleep(1)
calipso_ldap = DockerClient.containers.get("calipso-ldap")

# running actions against the containers:
print(calipso_ldap.name)
time.sleep(10)
calipso_ldap.kill()
time.sleep(10)
calipso_ldap.remove()

c = MongoComm(args.DB_user, args.DB_password, args.Hostname, args.DB_name, args.DB_port)
doc = dict(name="name", game_password="game_password")
c.insert("coll", doc)
