########################################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems) and others #
#                                                                                      #
# All rights reserved. This program and the accompanying materials                     #
# are made available under the terms of the Apache License, Version 2.0                #
# which accompanies this distribution, and is available at                             #
# http://www.apache.org/licenses/LICENSE-2.0                                           #
########################################################################################
from pymongo import MongoClient, ReturnDocument
from pymongo.errors import ConnectionFailure
from urllib.parse import quote_plus
import docker
import argparse
import dockerpycreds
# note : not used, useful for docker api security if used
import time
import json


class MongoComm:
    # deals with communication from host/installer server to mongoDB, includes methods for future use
    try:

        def __init__(self, host, user, password, port):
            self.uri = "mongodb://%s:%s@%s:%s/%s" % (
                quote_plus(user), quote_plus(password), host, port, "calipso")
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

        def remove_doc(self, coll, doc):
            collection = self.client.calipso[coll]
            collection.remove(doc)

        def remove_coll(self, coll):
            collection = self.client.calipso[coll]
            collection.remove()

        def find_update(self, coll, key, val, data):
            collection = self.client.calipso[coll]
            collection.find_one_and_update(
                {key: val},
                {"$set": data},
                upsert=True
            )

        def update(self, coll, doc, upsert=False):
            collection = self.client.calipso[coll]
            doc_id = collection.update_one({'_id': doc['_id']},{'$set': doc}, upsert=upsert)
            return doc_id

    except ConnectionFailure:
        print("MongoDB Server not available")


DockerClient = docker.from_env()   # using local host docker environment parameters


def copyfile(filename):
    c = MongoComm(args.hostname, args.dbuser, args.dbpassword, args.dbport)
    txt = open('db/'+filename+'.json')
    data = json.load(txt)
    c.remove_coll(filename)
    doc_id = c.insert(filename, data)
    print("Copied", filename, "mongo doc_ids:\n\n", doc_id, "\n\n")
    time.sleep(1)


# functions to check and start calipso containers:
def startmongo(dbport):
    if not DockerClient.containers.list(all=True, filters={"name": "calipso-mongo"}):
        print("\nstarting container calipso-mongo, please wait...\n")
        image = DockerClient.images.list(all=True, name="korenlev/calipso:mongo")
        if image:
            print(image, "exists...not downloading...")
        else:
            print("image korenlev/calipso:mongo missing, hold on while downloading first...\n")
            image = DockerClient.images.pull("korenlev/calipso:mongo")
            print("Downloaded", image, "\n\n")
        mongocontainer = DockerClient.containers.run('korenlev/calipso:mongo', detach=True, name="calipso-mongo",
                                                     ports={'27017/tcp': dbport, '28017/tcp': 28017},
                                                     restart_policy={"Name": "always"})
        # wait a bit till mongoDB is up before starting to copy the json files from 'db' folder:
        time.sleep(5)
        enable_copy = input("create initial calipso DB ? (copy json files from 'db' folder to mongoDB -"
                            " 'c' to copy, 'q' to skip):")
        if enable_copy == "c":
            print("\nstarting to copy json files to mongoDB...\n\n")
            print("-----------------------------------------\n\n")
            time.sleep(1)
            copyfile("attributes_for_hover_on_data")
            copyfile("clique_constraints")
            copyfile("clique_types")
            copyfile("cliques")
            copyfile("constants")
            copyfile("environments_config")
            copyfile("inventory")
            copyfile("link_types")
            copyfile("links")
            copyfile("messages")
            copyfile("meteor_accounts_loginServiceConfiguration")
            copyfile("users")
            copyfile("monitoring_config")
            copyfile("monitoring_config_templates")
            copyfile("network_agent_types")
            copyfile("roles")
            copyfile("scans")
            copyfile("scheduled_scans")
            copyfile("statistics")
            copyfile("supported_environments")

            # note : 'messages', 'roles', 'users' and some of the 'constants' are filled by calipso-ui at runtime
            # some other docs are filled later by scanning, logging and monitoring
        else:
            return
    else:
        print("container named calipso-mongo already exists, please deal with it using docker...\n")
        return


def startlisten():
    if not DockerClient.containers.list(all=True, filters={"name": "calipso-listen"}):
        print("\nstarting container calipso-listen...\n")
        image = DockerClient.images.list(all=True, name="korenlev/calipso:listen")
        if image:
            print(image, "exists...not downloading...")
        else:
            print("image korenlev/calipso:listen missing, hold on while downloading first...\n")
            image = DockerClient.images.pull("korenlev/calipso:listen")
            print("Downloaded", image, "\n\n")
        listencontainer = DockerClient.containers.run('korenlev/calipso:listen', detach=True, name="calipso-listen",
                                                      ports={'22/tcp': 50022},
                                                      restart_policy={"Name": "always"},
                                                      environment=["PYTHONPATH=/home/scan/calipso_prod/app",
                                                                   "MONGO_CONFIG=/local_dir/calipso_mongo_access.conf"],
                                                      volumes={'/home/calipso': {'bind': '/local_dir', 'mode': 'rw'}})
    else:
        print("container named calipso-listen already exists, please deal with it using docker...\n")
        return


def startldap():
    if not DockerClient.containers.list(all=True, filters={"name": "calipso-ldap"}):
        print("\nstarting container calipso-ldap...\n")
        image = DockerClient.images.list(all=True, name="korenlev/calipso:ldap")
        if image:
            print(image, "exists...not downloading...")
        else:
            print("image korenlev/calipso:ldap missing, hold on while downloading first...\n")
            image = DockerClient.images.pull("korenlev/calipso:ldap")
            print("Downloaded", image, "\n\n")
        ldapcontainer = DockerClient.containers.run('korenlev/calipso:ldap', detach=True, name="calipso-ldap",
                                                    ports={'389/tcp': 389, '389/udp': 389},
                                                    restart_policy={"Name": "always"},
                                                    volumes={'/home/calipso/': {'bind': '/local_dir/', 'mode': 'rw'}})
    else:
        print("container named calipso-ldap already exists, please deal with it using docker...\n")
        return


def startapi():
    if not DockerClient.containers.list(all=True, filters={"name": "calipso-api"}):
        print("\nstarting container calipso-api...\n")
        image = DockerClient.images.list(all=True, name="korenlev/calipso:api")
        if image:
            print(image, "exists...not downloading...")
        else:
            print("image korenlev/calipso:api missing, hold on while downloading first...\n")
            image = DockerClient.images.pull("korenlev/calipso:api")
            print("Downloaded", image, "\n\n")
        apicontainer = DockerClient.containers.run('korenlev/calipso:api', detach=True, name="calipso-api",
                                                   ports={'8000/tcp': 8000, '22/tcp': 40022},
                                                   restart_policy={"Name": "always"},
                                                   environment=["PYTHONPATH=/home/scan/calipso_prod/app",
                                                                "MONGO_CONFIG=/local_dir/calipso_mongo_access.conf",
                                                                "LDAP_CONFIG=/local_dir/ldap.conf",
                                                                "LOG_LEVEL=DEBUG"],
                                                   volumes={'/home/calipso/': {'bind': '/local_dir/', 'mode': 'rw'}})
    else:
        print("container named calipso-api already exists, please deal with it using docker...\n")
        return


def startscan():
    if not DockerClient.containers.list(all=True, filters={"name": "calipso-scan"}):
        print("\nstarting container calipso-scan...\n")
        image = DockerClient.images.list(all=True, name="korenlev/calipso:scan")
        if image:
            print(image, "exists...not downloading...")
        else:
            print("image korenlev/calipso:scan missing, hold on while downloading first...\n")
            image = DockerClient.images.pull("korenlev/calipso:scan")
            print("Downloaded", image, "\n\n")
        scancontainer = DockerClient.containers.run('korenlev/calipso:scan', detach=True, name="calipso-scan",
                                                    ports={'22/tcp': 30022},
                                                    restart_policy={"Name": "always"},
                                                    environment=["PYTHONPATH=/home/scan/calipso_prod/app",
                                                                 "MONGO_CONFIG=/local_dir/calipso_mongo_access.conf"],
                                                    volumes={'/home/calipso/': {'bind': '/local_dir/', 'mode': 'rw'}})
    else:
        print("container named calipso-scan already exists, please deal with it using docker...\n")
        return


def startsensu():
    if not DockerClient.containers.list(all=True, filters={"name": "calipso-sensu"}):
        print("\nstarting container calipso-sensu...\n")
        image = DockerClient.images.list(all=True, name="korenlev/calipso:sensu")
        if image:
            print(image, "exists...not downloading...")
        else:
            print("image korenlev/calipso:sensu missing, hold on while downloading first...\n")
            image = DockerClient.images.pull("korenlev/calipso:sensu")
            print("Downloaded", image, "\n\n")
        sensucontainer = DockerClient.containers.run('korenlev/calipso:sensu', detach=True, name="calipso-sensu",
                                                     ports={'22/tcp': 20022, '3000/tcp': 3000, '4567/tcp': 4567,
                                                            '5671/tcp': 5671, '15672/tcp': 15672},
                                                     restart_policy={"Name": "always"},
                                                     environment=["PYTHONPATH=/home/scan/calipso_prod/app"],
                                                     volumes={'/home/calipso/': {'bind': '/local_dir/', 'mode': 'rw'}})
    else:
        print("container named calipso-sensu already exists, please deal with it using docker...\n")
        return


def startui(host, dbuser, dbpassword, webport, dbport):
    if not DockerClient.containers.list(all=True, filters={"name": "calipso-ui"}):
        print("\nstarting container calipso-ui...\n")
        image = DockerClient.images.list(all=True, name="korenlev/calipso:ui")
        if image:
            print(image, "exists...not downloading...")
        else:
            print("image korenlev/calipso:ui missing, hold on while downloading first...\n")
            image = DockerClient.images.pull("korenlev/calipso:ui")
            print("Downloaded", image, "\n\n")
        uicontainer = DockerClient.containers.run('korenlev/calipso:ui', detach=True, name="calipso-ui",
                                                  ports={'3000/tcp': webport},
                                                  restart_policy={"Name": "always"},
                                                  environment=["ROOT_URL=http://" + host + ":" + str(webport),
                                                               "MONGO_URL=mongodb://" + dbuser + ":" + dbpassword
                                                               + "@" + host + ":" + str(dbport) + "/calipso",
                                                               "LDAP_CONFIG=/local_dir/ldap.conf"])
    else:
        print("container named calipso-ui already exists, please deal with it using docker...\n")
        return


# functions to check and stop calipso containers:
def stopmongo():
    if DockerClient.containers.list(all=True, filters={"name": "calipso-mongo"}):
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


def stoplisten():
    if DockerClient.containers.list(all=True, filters={"name": "calipso-listen"}):
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


def stopldap():
    if DockerClient.containers.list(all=True, filters={"name": "calipso-ldap"}):
        print("fetching container name calipso-ldap...\n")
        calipso_ldap = DockerClient.containers.get("calipso-ldap")
        if calipso_ldap.status != "running":
            print("calipso-ldap is not running...")
            time.sleep(1)
            print("removing container name", calipso_ldap.name, "...\n")
            calipso_ldap.remove()
        else:
            print("killing container name", calipso_ldap.name, "...\n")
            calipso_ldap.kill()
            time.sleep(1)
            print("removing container name", calipso_ldap.name, "...\n")
            calipso_ldap.remove()
    else:
        print("no container named 'calipso-ldap' found...")


def stopapi():
    if DockerClient.containers.list(all=True, filters={"name": "calipso-api"}):
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


def stopscan():
    if DockerClient.containers.list(all=True, filters={"name": "calipso-scan"}):
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


def stopsensu():
    if DockerClient.containers.list(all=True, filters={"name": "calipso-sensu"}):
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


def stopui():
    if DockerClient.containers.list(all=True, filters={"name": "calipso-ui"}):
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


# parser for getting optional command arguments:
parser = argparse.ArgumentParser()
parser.add_argument("--hostname", help="Hostname or IP address of the server (default=172.17.0.1)",type=str,
                    default="172.17.0.1", required=False)
parser.add_argument("--webport", help="Port for the Calipso WebUI (default=80)",type=int,
                    default="80", required=False)
parser.add_argument("--dbport", help="Port for the Calipso MongoDB (default=27017)",type=int,
                    default="27017", required=False)
parser.add_argument("--dbuser", help="User for the Calipso MongoDB (default=calipso)",type=str,
                    default="calipso", required=False)
parser.add_argument("--dbpassword", help="Password for the Calipso MongoDB (default=calipso_default)",type=str,
                    default="calipso_default", required=False)
args = parser.parse_args()

container = ""
action = ""
container_names = ["all", "calipso-mongo", "calipso-scan", "calipso-listen", "calipso-ldap", "calipso-api",
                     "calipso-sensu", "calipso-ui"]
container_actions = ["stop", "start"]
while action not in container_actions:
    action = input("Action? (stop, start, or 'q' to quit):\n")
    if action == "q":
        exit()
while container not in container_names:
    container = input("Container? (all, calipso-mongo, calipso-scan, calipso-listen, calipso-ldap, calipso-api, "
                      "calipso-sensu, calipso-ui or 'q' to quit):\n")
    if container == "q":
        exit()

# starting the containers per arguments:
if action == "start":
    # building /home/calipso/calipso_mongo_access.conf and /home/calipso/ldap.conf files, per the arguments:
    calipso_mongo_access_text = "server " + args.hostname + "\nuser " + args.dbuser + "\npassword " + \
                                args.dbpassword + "\nauth_db calipso"
    ldap_text = "user admin" + "\npassword password" + "\nurl ldap://" + args.hostname + ":389" + \
                "\nuser_id_attribute CN" + "\nuser_pass_attribute userpassword" + \
                "\nuser_objectclass inetOrgPerson" + \
                "\nuser_tree_dn OU=Users,DC=openstack,DC=org" + "\nquery_scope one" + \
                "\ntls_req_cert allow" + \
                "\ngroup_member_attribute member"
    print("creating default /home/calipso/calipso_mongo_access.conf file...\n")
    calipso_mongo_access_file = open("/home/calipso/calipso_mongo_access.conf", "w+")
    time.sleep(1)
    calipso_mongo_access_file.write(calipso_mongo_access_text)
    calipso_mongo_access_file.close()
    print("creating default /home/calipso/ldap.conf file...\n")
    ldap_file = open("/home/calipso/ldap.conf", "w+")
    time.sleep(1)
    ldap_file.write(ldap_text)
    ldap_file.close()

    if container == "calipso-mongo" or container == "all":
        startmongo(args.dbport)
        time.sleep(1)
    if container == "calipso-listen" or container == "all":
        startlisten()
        time.sleep(1)
    if container == "calipso-ldap" or container == "all":
        startldap()
        time.sleep(1)
    if container == "calipso-api" or container == "all":
        startapi()
        time.sleep(1)
    if container == "calipso-scan" or container == "all":
        startscan()
        time.sleep(1)
    if container == "calipso-sensu" or container == "all":
        startsensu()
        time.sleep(1)
    if container == "calipso-ui" or container == "all":
        startui(args.hostname, args.dbuser, args.dbpassword, args.webport, args.dbport)
        time.sleep(1)

# stopping the containers per arguments:
if action == "stop":
    if container == "calipso-mongo" or container == "all":
        stopmongo()
    if container == "calipso-listen" or container == "all":
        stoplisten()
    if container == "calipso-ldap" or container == "all":
        stopldap()
    if container == "calipso-api" or container == "all":
        stopapi()
    if container == "calipso-scan" or container == "all":
        stopscan()
    if container == "calipso-sensu" or container == "all":
        stopsensu()
    if container == "calipso-ui" or container == "all":
        stopui()


