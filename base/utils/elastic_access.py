###############################################################################
# Copyright (c) 2017-2019 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import datetime

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from base.utils.data_access_base import DataAccessBase
from base.utils.inventory_mgr import InventoryMgr
from base.utils.string_utils import stringify_doc


class ElasticAccess(DataAccessBase):
    default_conf_file = '/local_dir/elastic_access.conf'

    REQUIRED_ENV_VARIABLES = {
        'host': 'ES_SERVICE_HOST',
        'port': 'ES_SERVICE_PORT'
    }
    OPTIONAL_ENV_VARIABLES = {}

    LOG_FILENAME = 'elastic_access.log'
    PROJECTIONS = {  # TODO
        'inventory': ['_id', 'id', 'type', 'environment'],
        'links': [],
        'cliques': []
    }
    TREE_ROOT_ID = 'root'

    def __init__(self, bulk_chunk_size=1000):
        super().__init__()
        self.inv = InventoryMgr()

        self.bulk_chunk_size = bulk_chunk_size
        self.connection_params = {}
        self.connection = None
        self.connect()

    @property
    def is_connected(self):
        return self.connection is not None

    def get_connection_parameters(self):
        try:
            return self._get_connection_parameters()
        except Exception as e:
            self.log.warning("Failed to connect to ElasticSearch. Error: {}".format(e))
            return {}

    def connect(self):
        connection_params = self.get_connection_parameters()
        if not connection_params or (connection_params == self.connection_params and self.connection):
            return

        self.connection_params = connection_params

        connection = Elasticsearch([self.connection_params])
        if connection.ping():
            self.log.info("Successfully connected to Elasticsearch at {}:{}".format(self.connection_params['host'],
                                                                                    self.connection_params['port']))
            self.connection = connection
        else:
            raise ConnectionError("Failed to connect to Elasticsearch at {}:{}".format(self.connection_params['host'],
                                                                                       self.connection_params['port']))
        self.connection = connection

    def create_index(self, index_name, settings=None):
        if settings is None:
            settings = {
                "settings": {
                    "number_of_shards": 1,
                    "number_of_replicas": 0,
                    "index.mapping.total_fields.limit": 2000
                }
            }
        if not self.connection.indices.exists(index_name):
            self.connection.indices.create(index=index_name, ignore=[400, 404], body=settings)
            self.log.info('Created Index {}'.format(index_name))
            return True
        return False

    def dump_collections(self, env, projections=None):
        if not projections:
            projections = ElasticAccess.PROJECTIONS

        actions = []
        for col, projection in projections.items():
            date = datetime.datetime.now().strftime("%Y.%m.%d")
            index_name = 'calipso-{}-{}'.format(col, date)
            self.create_index(index_name)

            for doc in self.inv.find({'environment': env}, collection=col):
                stringify_doc(doc)
                actions.append({
                    '_op_type': 'index',
                    '_index': index_name,
                    '_id': doc['_id'],
                    'doc': doc  # TODO: use projections
                })

        ok, errors = bulk(self.connection, actions, stats_only=True, raise_on_error=False, chunk_size=self.bulk_chunk_size)
        self.log.info("Successfully indexed {} documents to Elasticsearch, errors: {}".format(ok, errors))

    def dump_tree(self, env):
        data_list = [
            {
                'id': ElasticAccess.TREE_ROOT_ID,
                'name': 'environments'
            }, {
                'id': env,
                'name': env,
                'parent': ElasticAccess.TREE_ROOT_ID
            }
        ]

        for doc in self.inv.find({'environment': env}):
            data_list.append({
                'id': "{}:{}".format(env, doc['id']),
                'name': doc['name'],
                'parent': "{}:{}".format(env, doc['parent_id']),
                'type': doc['type']
            })

        index_name = 'calipso-tree-{}'.format(datetime.datetime.now().strftime("%Y.%m.%d"))
        # TODO: handle response
        # ok, errors = self.connection.index(index_name, {'doc': data_list})
        # self.log.info("Successfully indexed {} documents to Elasticsearch index '{}', errors: {}".format(
        #     ok, index_name, errors)
        # )
        env_doc = self.inv.find_one({'name': env}, collection='environments_config')
        print(self.connection.index(index_name, {'last_scanned': env_doc['last_scanned'], 'doc': data_list}, id='1'))
