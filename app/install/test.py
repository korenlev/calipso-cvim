from pymongo import MongoClient, ReturnDocument
from pymongo.errors import ConnectionFailure
from urllib.parse import quote_plus
import docker
import argparse
import dockerpycreds
import time
import json


DockerClient = docker.from_env()

image = DockerClient.images.list(all=True, name="korenlev/calipso:ldap")

if image:
	print(image, "exists...not downloading...")
else:
	print("image korenlev/calipso:ldap missing, hold on while downloading first...\n")
