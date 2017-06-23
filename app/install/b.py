from pymongo import MongoClient, ReturnDocument
from pymongo.errors import ConnectionFailure
from urllib.parse import quote_plus
import docker
import argparse
import dockerpycreds
import time
import json


DockerClient = docker.from_env()

images = DockerClient.images.list(filters={"name": "korenlev/calipso"})
print(images)
if "korenlev/calipso:ldap" in images:
	print("image korenlev/calipso:mongo missing, downloading...this might take a while")
else:
	print("it's there")
