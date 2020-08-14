###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import ssl
from typing import Optional, List, Union
from urllib.parse import quote_plus

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient, AsyncIOMotorCursor as Cursor
from pymongo import UpdateOne
from pymongo.collection import Collection
from pymongo.results import BulkWriteResult, UpdateResult

from base.utils.logging.full_logger import FullLogger
from base.utils.logging.logger import Logger
from base.utils.mongo_access import MongoAccess


class AsyncMongoConnector(object):
    LOG_FILE = "async_mongo_connector.log"
    LOG_LEVEL = Logger.INFO

    DEFAULT_PORT = 27017
    DEFAULT_USER = "calipso"
    DEFAULT_DB = "calipso"

    environments_collection = "environments_config"

    def __init__(self, host: str, pwd: str, port: int = DEFAULT_PORT, user: str = DEFAULT_USER,
                 db: str = DEFAULT_DB, db_label: str = "central DB",
                 logger: Optional[Logger] = None):

        self.host: str = "[{}]".format(host) if ":" in host and "[" not in host else host
        self.port: int = port
        self.user: str = user
        self.pwd: str = pwd
        self.db: str = db
        self.db_label: str = db_label
        self.log: Logger = (
            logger if logger
            else FullLogger(name="Async Mongo Connector", log_file=self.LOG_FILE, level=self.LOG_LEVEL)
        )

        self.uri: Optional[str] = None
        self.client: Optional[MongoClient] = None
        self.database: Optional[Collection] = None

    @classmethod
    async def create(cls, host: str, pwd: str, port: int = DEFAULT_PORT,
                     user: str = DEFAULT_USER, db: str = DEFAULT_DB, db_label: str = "central DB",
                     logger: Optional[Logger] = None, connect: bool = False) -> 'AsyncMongoConnector':
        instance = cls(host=host, port=port, user=user, pwd=pwd, db=db, db_label=db_label, logger=logger)
        if connect:
            await instance.connect()
        return instance

    async def connect(self, force_reconnect: bool = False) -> None:
        if self.client:
            if force_reconnect:
                self.disconnect()
            return

        if self.user and self.pwd:
            self.uri = "mongodb://%s:%s@%s:%s/%s" % (quote_plus(self.user), quote_plus(self.pwd),
                                                     self.host, self.port, self.db)
        else:
            self.uri = "mongodb://%s:%s/%s" % (self.host, self.port, self.db)
        self.client = MongoClient(self.uri, connectTimeoutMS=10000, serverSelectionTimeoutMS=10000,
                                  ssl=True, ssl_cert_reqs=ssl.CERT_NONE, connect=True)
        self.database = self.client[self.db]

    def disconnect(self) -> None:
        if self.client:
            self.log.debug("Disconnecting from {}...".format(self.db_label))
            self.client.close()
            self.client = None

    async def clear_collection(self, collection: str, envs: List[str] = None) -> None:
        if envs:
            return await self.database[collection].delete_many({"environment": {"$in": envs}})
        else:
            return await self.database[collection].clear()

    def _build_find_query(self, collection: str, query: dict = None, env: str = None) -> dict:
        if not query:
            query = {}
        if not env:
            env = {"$exists": True}
        query.update({"name": env} if collection == self.environments_collection else {"environment": env})
        return query

    def find(self, collection: str, query: dict = None, env: str = None) -> Cursor:
        return self.database[collection].find(
            self._build_find_query(collection=collection, query=query, env=env)
        )

    async def find_one(self, collection: str, query: dict = None, env: str = None) -> Optional[dict]:
        return await self.database[collection].find_one(
            self._build_find_query(collection=collection, query=query, env=env)
        )

    async def collection_exists(self, name: str) -> bool:
        return name in await self.database.list_collection_names()

    async def create_collection(self, name: str) -> Collection:
        return await self.database.create_collection(name)

    async def insert_collection(self, collection: str, data: Union[list, dict]) -> None:
        if data:
            result = await self.database[collection].insert_many(data if isinstance(data, list) else [data])
            self.log.debug("Inserted '{}' collection in {}, Total docs inserted: {}".format(collection, self.db_label,
                                                                                            len(result.inserted_ids)))
        elif not await self.collection_exists(collection):
            await self.create_collection(collection)
            self.log.debug("Inserted empty '{}' collection in {}".format(collection, self.db_label))
        else:
            self.log.debug("Skipping empty '{}' collection".format(collection, ))

    async def update_one(self, collection: str, doc: dict, key: str = None, upsert: bool = True) -> UpdateResult:
        return await self.database[collection].update_one(
            filter={key: doc[key]} if key else {},
            update={"$set": MongoAccess.encode_mongo_keys(doc)},
            upsert=upsert
        )

    async def update_many(self, collection: str, doc: dict, key: str = None) -> UpdateResult:
        return await self.database[collection].update_many(
            filter={key: doc[key]} if key else {},
            update={"$set": MongoAccess.encode_mongo_keys(doc)},
        )

    async def bulk_update(self, collection: str, docs: list, key: str,
                          upsert: bool = True, ordered: bool = False) -> BulkWriteResult:
        """
            Update multiple docs in *collection* based on the *key* field.
        :param collection: collection name
        :param docs: list of dicts with data to update in db
        :param key: field used to find the document to update for each doc in docs list
        :param upsert: if True, insert each doc in docs list that doesn't match any document in db
        :param ordered: whether the docs should updated in strict order of docs list
        :return:
        """

        ops = [
            UpdateOne(
                filter={key: doc[key]},
                update={"$set": MongoAccess.encode_mongo_keys(doc)},
                upsert=upsert
            )
            for doc in docs
        ]
        return await self.database[collection].bulk_write(ops, ordered=ordered)
