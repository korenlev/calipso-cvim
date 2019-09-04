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

from base.utils.inventory_mgr import InventoryMgr
from base.utils.logging.console_logger import ConsoleLogger
from base.utils.string_utils import stringify_doc


class ElasticAccess:
    PROJECTIONS = {  # TODO
        'inventory': ['_id', 'id', 'type', 'environment'],
        'links': [],
        'cliques': []
    }

    def __init__(self, host="localhost", port="9200", bulk_chunk_size=1000):
        self.log = ConsoleLogger()
        self.inv = InventoryMgr()

        self.host = host
        self.port = port
        self.bulk_chunk_size = bulk_chunk_size
        self.connection = None
        self.connect()

    def connect(self):
        connection = Elasticsearch([{'host': self.host, 'port': self.port}])
        if connection.ping():
            self.log.info("Successfully connected to Elasticsearch at {}:{}".format(self.host, self.port))
            self.connection = connection
        else:
            raise ConnectionError("Failed to connect to Elasticsearch at {}:{}".format(self.host, self.port))
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



