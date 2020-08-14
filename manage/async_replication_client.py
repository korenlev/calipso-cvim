###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import asyncio
import traceback
from typing import List, Union, Optional

from pymongo.errors import ConnectionFailure, OperationFailure

from base.utils.logging.full_logger import FullLogger
from base.utils.logging.logger import Logger
from base.utils.util import async_measure_perf_time
from manage.async_mongo_connector import AsyncMongoConnector
from manage.pod_data import PodData


class AsyncReplicationClient:
    LOG_FILE = "async_replication_client.log"
    LOG_LEVEL = Logger.INFO

    reconstructable_collections = ["inventory", "links", "cliques"]
    collection_names = ["cliques", "graphs", "inventory", "links", "scans", "scheduled_scans"]

    def __init__(self, central_host: str, central_pwd: str,
                 central_port: int = AsyncMongoConnector.DEFAULT_PORT,
                 central_user: str = AsyncMongoConnector.DEFAULT_USER,
                 max_concurrent_replications: int = 10):
        # TODO: revise logging levels
        self.max_concurrent_replications = max(1, max_concurrent_replications)
        self.central_host = central_host
        self.central_port = central_port
        self.central_pwd = central_pwd
        self.central_user = central_user
        self.log = FullLogger(name="Async Replication Client", log_file=self.LOG_FILE, level=self.LOG_LEVEL)

    async def _replicate(self, remote_config: PodData, jobs_queue: asyncio.Queue,
                         source_conn: AsyncMongoConnector, destination_conn: AsyncMongoConnector):
        env_doc = await source_conn.find_one(collection=AsyncMongoConnector.environments_collection,
                                             env=remote_config.env_name)
        if not env_doc:
            self.log.warning("Environment {} is missing from remote {}".format(remote_config.env_name,
                                                                               remote_config.name))
            return

        del env_doc["_id"]
        env_doc["imported"] = True
        env_doc.update(remote_config.to_env_config())

        await destination_conn.update_one(collection=AsyncMongoConnector.environments_collection,
                                          doc=env_doc,
                                          key="name",
                                          upsert=True)

        for col in self.collection_names:
            # read from remote DBs and export to local json files
            self.log.info("Getting the {} Collection from {}...".format(col, remote_config.name))

            cursor = source_conn.find(collection=col, env=remote_config.env_name)

            documents = []
            async for doc in cursor:
                doc["imported"] = True
                doc["environment"] = remote_config.full_name

                original_id = doc.pop('_id')
                if col in self.reconstructable_collections:
                    doc['original_id'] = original_id

                documents.append(doc)

            # write all in-memory json docs into the central DB
            self.log.info("Pushing the {} Collection from {} into central...".format(col, remote_config.name))
            await destination_conn.insert_collection(col, documents)

        await jobs_queue.put((destination_conn, remote_config.full_name))

    @async_measure_perf_time()
    async def replicate(self, remote_config: PodData, jobs_queue: asyncio.Queue) -> None:
        self.log.info("Connecting to remote {}".format(remote_config.name))
        source_conn, destination_conn = None, None
        try:
            source_conn = await AsyncMongoConnector.create(
                host=remote_config.host, pwd=remote_config.calipso_mongo_password,
                db_label=remote_config.full_name, logger=self.log, connect=True
            )
            destination_conn = await AsyncMongoConnector.create(
                host=self.central_host, port=self.central_port, pwd=self.central_pwd,
                logger=self.log, connect=True
            )

            return await self._replicate(remote_config=remote_config, jobs_queue=jobs_queue,
                                         source_conn=source_conn, destination_conn=destination_conn)
        except Exception:
            if destination_conn:
                destination_conn.disconnect()
            raise
        finally:
            if source_conn:
                source_conn.disconnect()

    @async_measure_perf_time()
    async def reconstruct_ids(self, destination_conn: AsyncMongoConnector, env_name: str) -> None:
        self.log.info("Fixing ids for links and cliques for env: {}".format(env_name))
        rc = {}
        for col in self.reconstructable_collections:
            rc[col] = {}
            cursor = destination_conn.find(col, env=env_name)
            async for obj in cursor:
                original_id = obj.pop("original_id")
                rc[col][original_id] = obj

        for link_orig_id, link in rc["links"].items():
            if 'source' not in link or 'target' not in link:
                self.log.info("Malformed link: {}".format(link))
                continue
            link["source"] = rc["inventory"][link["source"]]["_id"]
            link["target"] = rc["inventory"][link["target"]]["_id"]

        for clique_orig_id, clique in rc["cliques"].items():
            if any(req_field not in clique for req_field in ('links', 'links_detailed')):
                self.log.info("Malformed clique: {}".format(clique))
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

        for col in self.reconstructable_collections:
            await destination_conn.clear_collection(col, envs=[env_name])
            await destination_conn.insert_collection(col, list(rc[col].values()))

    async def reconstruct(self, jobs_queue: asyncio.Queue) -> None:
        while True:
            destination_conn, env_name = await jobs_queue.get()
            try:
                await self.reconstruct_ids(destination_conn=destination_conn, env_name=env_name)
            except Exception as e:
                self.log.error("Failed to reconstruct ids for environment: {}. Error: {}".format(env_name, e))
                traceback.print_exc()  # TODO: remove traceback!
            finally:
                destination_conn.disconnect()
            jobs_queue.task_done()

    async def clear(self, remotes: List[PodData]) -> None:
        # Clear central collections for replication purposes
        central_conn = None
        try:
            central_conn = await AsyncMongoConnector.create(
                host=self.central_host, port=self.central_port, pwd=self.central_pwd, logger=self.log,
                connect=True
            )
            for col in self.collection_names:
                self.log.info("Clearing collection {} from central...".format(col))
                await central_conn.clear_collection(col, [r.full_name for r in remotes])
        finally:
            if central_conn:
                central_conn.disconnect()

    async def _run(self, remotes: List[PodData]) -> List[Optional[Exception]]:
        """
            Runs replications + ids reconstructions
        :param remotes: list of remote pods configurations
        :return: list of results from replicator tasks (reconstuctor tasks logs tbd)
        """
        self.log.info("Replicating from remotes: {}".format([r.env_name for r in remotes]))
        jobs_queue = asyncio.Queue(maxsize=len(remotes))

        replicators = [
            asyncio.ensure_future(self.replicate(remote_config=remote, jobs_queue=jobs_queue))
            for remote in remotes
        ]
        reconstructors = [
            asyncio.ensure_future(self.reconstruct(jobs_queue=jobs_queue))
            for _ in remotes
        ]
        replicators_results = await asyncio.gather(*replicators, return_exceptions=True)

        await jobs_queue.join()
        for c in reconstructors:
            c.cancel()
        return replicators_results

    async def run(self, remotes: List[PodData]) -> List[Union[None, Exception]]:
        """

        :param remotes: list of remote pods configurations
        :return: whether replication was overall successful (details tbd)
        """
        if not remotes:
            return []

        try:
            await self.clear(remotes=remotes)
        except (ConnectionFailure, OperationFailure) as e:
            self.log.error("Failed to clear central db for replication. Error: {}".format(e))
            return []

        results = []
        for i in range(0, len(remotes), self.max_concurrent_replications):
            results.extend(await self._run(remotes[i:i + self.max_concurrent_replications]))
        return results
