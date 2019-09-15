###############################################################################
# Copyright (c) 2017-2019 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from datetime import datetime
import time
import argparse
from bson import ObjectId

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from calipso_replication_client import MongoConnector


class ElasticClient(object):

    LOG_FILENAME = 'es_access.log'
    PROJECTIONS = {  # TODO
        'inventory': ['_id', 'id', 'type', 'environment'],
        'links': [],
        'cliques': []
    }
    TREE_ROOT_ID = 'root'
    CONNECTION_RETRIES = 10

    def __init__(self, host, port, user, pwd, db, bulk_chunk_size=1000, db_label="central DB"):
        self.bulk_chunk_size = bulk_chunk_size
        self.connection = None
        self.inventory_collection = None
        self.inventory_collection_name = None
        self.collections = {}
        self.mongo = MongoConnector(host, port, user, pwd, db, db_label)
        self.stringify_map = {
            ObjectId: self.stringify_object_id,
            datetime: self.stringify_datetime
        }

    @staticmethod
    def stringify_datetime(dt):
        return dt.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

    @staticmethod
    def stringify_object_id(object_id):
        return str(object_id)

    def stringify_object_values_by_type(self, obj, object_type):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, object_type):
                    obj[key] = self.stringify_map[object_type](value)
                else:
                    self.stringify_object_values_by_type(value, object_type)
        elif isinstance(obj, list):
            for index, value in enumerate(obj):
                if isinstance(value, object_type):
                    obj[index] = self.stringify_map[object_type](value)
                else:
                    self.stringify_object_values_by_type(value, object_type)

    def stringify_object_values_by_types(self, obj, object_types):
        for object_type in object_types:
            self.stringify_object_values_by_type(obj, object_type)

    def stringify_doc(self, doc):
        self.stringify_object_values_by_types(doc, self.stringify_map.keys())

    @staticmethod
    def connection_backoff(i):
        return i  # Linear backoff

    @property
    def is_connected(self):
        return self.connection is not None

    def connect(self, conn_params):
        connection = Elasticsearch([conn_params])
        attempt = 1
        while True:
            if connection.ping():
                print("Successfully connected to Elasticsearch at {}:{}".format(conn_params['host'],
                                                                                        conn_params['port']))
                self.connection = connection
                break
            else:
                fail_msg = "Failed to connect to Elasticsearch at {}:{}".format(conn_params['host'],
                                                                                conn_params['port'])
                if attempt <= self.CONNECTION_RETRIES:
                    backoff = self.connection_backoff(attempt)
                    print("{}. Retrying after {} seconds".format(fail_msg, backoff))
                    time.sleep(backoff)
                    attempt += 1
                    continue
                raise ConnectionError(fail_msg)
        self.connection = connection

    def create_index(self, index_name, settings=None, delete_if_exists=False):
        if settings is None:
            settings = {
                "settings": {
                    "number_of_shards": 1,
                    "number_of_replicas": 1,
                    "index.mapping.total_fields.limit": 2000
                }
            }

        if self.connection.indices.exists(index_name):
            if not delete_if_exists:
                return False
            self.connection.indices.delete(index=index_name, ignore=[400, 404])

        self.connection.indices.create(index=index_name, ignore=[400, 404], body=settings)
        print('Created Index {}'.format(index_name))
        return True

    def delete_documents_by_env(self, index, env):
        query = {
          "query": {
            "match": {
              "environment": env
            }
          }
        }
        self.connection.delete_by_query(index, query)

    def dump_collections(self, env=None, projections=None):
        if not projections:
            projections = ElasticClient.PROJECTIONS
        actions = []
        for col, projection in projections.items():
            date = datetime.now().strftime("%Y.%m.%d")
            index_name = 'calipso-{}-{}'.format(col, date)
            self.create_index(index_name)
            if env:
                self.delete_documents_by_env(index_name, env)
            for doc in self.mongo.find_all(collection=col, env=env):
                self.stringify_doc(doc)
                actions.append({
                    '_op_type': 'index',
                    '_index': index_name,
                    '_id': doc['_id'],
                    'doc': doc  # TODO: use projections
                })

        ok, errors = bulk(self.connection, actions, stats_only=True, raise_on_error=False, chunk_size=self.bulk_chunk_size)
        print("Successfully indexed {} documents to Elasticsearch, errors: {}".format(ok, errors))

    def dump_tree(self, env):
        data_list = [
            {
                'id': ElasticClient.TREE_ROOT_ID,
                'name': 'environments'
            }, {
                'id': "{}:{}".format(env, env),
                'name': env,
                'environment': env,
                'parent': ElasticClient.TREE_ROOT_ID
            }
        ]

        for doc in self.mongo.find_all(collection="inventory", env=env):
            data_list.append({
                'id': "{}:{}".format(env, doc['id']),
                'name': doc['name'],
                'parent': "{}:{}".format(env, doc['parent_id']),
                'type': doc['type'],
                'environment': env
            })

        index_name = 'calipso-tree-{}'.format(datetime.datetime.now().strftime("%Y.%m.%d"))
        doc_id = '1'

        doc = self.connection.get(index_name, doc_id, ignore=[400, 404])
        if doc and doc.get('found', False) is True:
            for item in doc.get('_source', {}).get('doc', []):
                item_env = item.get('environment')
                if item_env and item_env != env:
                    data_list.append(item)

        # TODO: handle response
        # ok, errors = self.connection.index(index_name, {'doc': data_list})
        # self.log.info("Successfully indexed {} documents to Elasticsearch index '{}', errors: {}".format(
        #     ok, index_name, errors)
        # )
        env_doc = self.mongo.find_all(env=env, collection='environments_config')
        self.connection.index(index_name, {'last_scanned': env_doc['last_scanned'], 'doc': data_list}, id=doc_id)


def fatal(err):
    print(err)
    exit(1)


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--es_server",
                        help="FQDN or IP address of the ElasticSearch Server"
                             " (default=localhost)",
                        type=str,
                        default="localhost",
                        required=False)
    parser.add_argument("--m_server",
                        help="FQDN or IP address of the MongoDB Server"
                             " (default=localhost)",
                        type=str,
                        default="localhost",
                        required=False)
    parser.add_argument("--es_port",
                        help="TCP Port exposed on the ElasticSearch Server "
                             " (default=9200)",
                        type=int,
                        default=9200,
                        required=False)
    parser.add_argument("--m_port",
                        help="TCP Port exposed on the MongoDB Server "
                             " (default=27017)",
                        type=int,
                        default=27017,
                        required=False)
    parser.add_argument("--environment",
                        help="specify environment(pod) name configured in MongoDB"
                             " (default=None)",
                        type=str,
                        default=None,
                        required=False)
    parser.add_argument("--m_user",
                        help="specify username with calipso access privileges on MongoDB"
                             " (default=calipso)",
                        type=str,
                        default="calipso",
                        required=False)
    parser.add_argument("--m_pwd",
                        help="specify password for m_user on MongoDB"
                             " (default=calipso_default)",
                        type=str,
                        default="calipso_default",
                        required=False)
    parser.add_argument("--version",
                        help="get a reply back with calipso_elastic_client version",
                        action='version',
                        default=None,
                        version='%(prog)s version: 0.4.18')

    args = parser.parse_args()
    es = ElasticClient(args.m_server, args.m_port, args.m_user, args.m_pwd, "calipso")
    es_conn_params = {"host": args.es_server, "port": args.es_port}
    es.connect(es_conn_params)
    es.dump_collections(args.environment)
    es.dump_tree(args.environment)
    exit(0)


if __name__ == "__main__":
    run()
