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
import datetime
import math
from typing import Optional, List, Dict

from aiohttp import ClientResponse
from dateutil.relativedelta import relativedelta

from base.manager import AsyncManager
from base.utils.logging.logger import Logger
from manage.async_mongo_connector import AsyncMongoConnector
from manage.async_replication_client import AsyncReplicationClient
from manage.pod_data import PodData
from manage.pod_manager import PodManager
from manage.util import get_next_schedule, clean_scan_request


class ScheduleManager(AsyncManager):
    # Backoffs for different actions (in seconds)
    MAX_SCHEDULE_MANAGER_RESTART_BACKOFF = 3600
    DISCOVERY_RETRY_BACKOFF = 10
    REPLICATION_RETRY_BACKOFF = 30

    def __init__(self, mongo_host: str, mongo_pwd: str, mongo_port: int = AsyncMongoConnector.DEFAULT_PORT,
                 mongo_user: str = AsyncMongoConnector.DEFAULT_USER,
                 log_level: str = Logger.INFO, log_file: str = "", log_directory: Optional[str] = None,
                 skip_discovery: bool = False, skip_replication: bool = False):
        super().__init__(log_directory=log_directory,
                         log_level=log_level,
                         log_file=log_file, )

        # New PodData list usually populated by calling /set_remotes API endpoint
        self.new_pods: List[PodData] = []
        self.refresh_pods: bool = False

        # full_name: PodData mappings
        # full_name is expected to be unique
        self.pods: Dict[str, PodData] = {}

        self.central_mongo_connection: AsyncMongoConnector = (
            AsyncMongoConnector(host=mongo_host, port=mongo_port, user=mongo_user, pwd=mongo_pwd)
        )
        self.replication_client: AsyncReplicationClient = (
            AsyncReplicationClient(central_host=mongo_host, central_port=mongo_port,
                                   central_user=mongo_user, central_pwd=mongo_pwd)
        )
        self.pod_manager: PodManager = PodManager()
        self.current_op: str = "init"

        self.skip_discovery: bool = skip_discovery
        self.skip_replication: bool = skip_replication

        # Variable used to backoff schedule mgr restarts in case of consecutive failures
        self.failing_streak: int = 0
        self.latest_error: Optional[Exception] = None

    def set_op(self, name: str):
        self.current_op = name

    def _reset_error(self):
        self.failing_streak = 0
        self.latest_error = None

    def set_new_pods(self, pods: List[PodData]) -> None:
        self.new_pods = pods
        self.refresh_pods = True

    @staticmethod
    def setup_first_schedules(pod: PodData) -> None:
        """
            Set up first schedules if not already done
        :param pod: new PodData instance
        :return:
        """
        if pod.next_discovery or pod.next_replication:
            # First schedules are already set up
            return
        pod.next_discovery = datetime.datetime.utcnow()
        pod.next_replication = datetime.datetime.utcnow()

    async def load_environments(self) -> None:
        """
            Load all imported environments from central DB
            and parse the PodData objects from environment definitions.
            Set all valid environments as remotes to control.
        :return:
        """
        self.set_op("load_environments")
        environments_cursor = self.central_mongo_connection.find(
            collection=AsyncMongoConnector.environments_collection,
            query={"imported": True}
        )
        self.pods = {}
        async for env in environments_cursor:
            pod = PodData.from_env_config(env)
            if not pod:
                self.log.warning("Failed to parse pod data from environment config: {}".format(env["name"]))
                continue
            self.pods[pod.full_name] = pod

    async def save_environments(self, pods: List[PodData] = None, _all: bool = False) -> None:
        """
            Save environments from memory to central DB
        :param pods: list of PodData objects to save
        :param _all: save all remotes data from memory (takes priority over "pods" argument)
        :return:
        """
        self.set_op("save_environments")
        if _all:
            pods = self.pods.values()
        if not pods:
            return

        await self.central_mongo_connection.connect(force_reconnect=True)
        await self.central_mongo_connection.bulk_update(
            collection=AsyncMongoConnector.environments_collection,
            docs=[pod.to_env_config() for pod in pods],
            key="name",
            upsert=True,
        )
        self.central_mongo_connection.disconnect()

    async def clear_environments(self, pods: List[PodData] = None, _all: bool = False):
        """
            Clear collections in central DB for environments based on given list of pods
        :param pods: list of PodData objects to clear environments for
        :param _all: clear environments for all remotes in memory
        :return:
        """
        self.set_op("clear_environments")
        if _all:
            pods = self.pods.values()
        if not pods:
            return

        await self.replication_client.clear(remotes=pods, clear_env_config=True)

    async def connect_remotes(self, pods: List[PodData], force_reconnect: bool = False) -> None:
        """
            Try to connect to remote APIs, set a connection backoff if the attempt fails.
            Filter out the remotes that are under a backoff already.
        :param pods: list of PodData object in whatever connection state they're in
        :param force_reconnect: whether to reconnect to already connected remotes
        :return:
        """
        self.set_op("connect_remotes")
        # Filter out failing connections
        pods_to_connect = [pod for pod in pods if pod.is_available_to_connect]

        connection_results = await asyncio.gather(
            *[pod.connect_api(force_reconnect=force_reconnect) for pod in pods_to_connect],
            return_exceptions=True
        )
        for i, pod in enumerate(pods_to_connect):
            if connection_results[i] is True:
                pod.reset_connection_backoff()
            else:
                pod.backoff_connection_attempt()
                error_msg = (
                    " Error: {}".format(connection_results[i])
                    if isinstance(connection_results[i], Exception)
                    else ""
                )
                self.log.warning("Failed to connect to remote: {}.{}"
                                 .format(pods_to_connect[i].full_name, error_msg))

    async def update_remotes(self) -> None:
        """
            This method checks whether a new list of remotes was submitted via API.
            If self.new_pods is not empty and self.refresh_pods is set to True,
            it performs the diff between the new remotes list and existing one,
            after which all added pods are set up and connected using async API clients
            and removed pods are disconnected and cleaned up.
            Overlapping pods are left untouched.
        :return:
        """
        self.set_op("update_remotes")
        if not self.refresh_pods:
            return

        self.refresh_pods = False
        if not self.new_pods:
            return

        # To save processing time, new pods list is sorted before comparison loop
        added_pods = {}
        for new_pod in self.new_pods:
            old_pod = self.pods.get(new_pod.full_name)
            if old_pod and old_pod.is_same_pod(new_pod) and not old_pod.config_changed(new_pod):
                old_pod.is_kept = True
            else:
                added_pods[new_pod.full_name] = new_pod

        # Disconnect removed/reconfigured pods, clear the respective envs from central DB
        # and add what's left to the remaining pods list
        await self.clear_environments(
            pods=[pod for pod in self.pods.values() if not pod.is_kept]
        )

        remaining_pods = {}
        for pod in self.pods.values():
            if not pod.is_kept:
                pod.disconnect()
                continue
            pod.is_kept = False
            remaining_pods[pod.full_name] = pod

        await self.connect_remotes(pods=list(added_pods.values()))

        for pod in added_pods.values():
            self.setup_first_schedules(pod)
            remaining_pods[pod.full_name] = pod

        self.pods = remaining_pods
        self.new_pods = []
        await self.save_environments(_all=True)

    async def reconnect_remotes_with_pending_actions(self):
        """
            Reconnect remotes that are disconnected and have pending actions to perform.
            There is not much sense in reconnecting to remotes that are not due for discovery or replication
        :return:
        """
        self.set_op("reconnect_remotes")
        pods_to_reconnect = [
            pod for pod in self.pods.values()
            if not pod.is_connected and any(await self.get_pending_actions(pod, verify_health=False))
        ]

        await self.connect_remotes(pods=pods_to_reconnect, force_reconnect=True)

    async def _scan_pod(self, pod: PodData) -> None:
        """
            Send scan request to the remote pod if it is ready,
            then set next discovery schedule, otherwise try again after a backoff.
        :param pod: PodData instance
        :return:
        """

        if self.pod_manager.check_pod_available_for_action(pod=pod, action="discovery"):
            next_discovery = get_next_schedule(pod.next_discovery, pod.discovery_interval)
            try:
                if self.skip_discovery:
                    self.log.info("Simulating scan request to pod '{}'. Datetime: {}. "
                                  "Interval: {}. Next discovery: {}"
                                  .format(pod.name, datetime.datetime.utcnow(),
                                          pod.discovery_interval, next_discovery))
                else:
                    self.log.info("Sending scan request to pod '{}'. Datetime: {}. "
                                  "Interval: {}. Next discovery: {}"
                                  .format(pod.name, datetime.datetime.utcnow(),
                                          pod.discovery_interval, next_discovery))

                    await pod.calipso_client.scan_request(environment=pod.env_name)
                    # Set expected next discovery schedule only if scan request was sent successfully
                    pod.next_discovery = next_discovery
            except Exception:
                # In case of scan request error, try again later
                pod.next_discovery += relativedelta(seconds=self.DISCOVERY_RETRY_BACKOFF)
                raise
            finally:
                # Clear pod health so that replication doesn't happen mid-scan
                pod.health.reset()
        else:
            pod.next_discovery += relativedelta(seconds=self.DISCOVERY_RETRY_BACKOFF)

    async def scan_pods(self, pods: List[PodData]) -> None:
        self.set_op("scan_pods")
        results = await asyncio.gather(*[self._scan_pod(pod) for pod in pods], return_exceptions=True)
        for i, res in enumerate(results):
            if isinstance(res, Exception):
                self.log.warning("Failed to scan remote '{}'. "
                                 "Error: ({}) {}".format(pods[i].name, type(res), res))

    async def replicate_pods(self, pods: List[PodData]) -> None:
        """
            Replicate data from remotes that are due.
            If a pod is not available for replication (either disconnected, has a scan is in progress, etc),
            the replication is NOT skipped but rather postponed until next iteration of scheduler loop
        :param pods: list of remotes to replicate from
        :return:
        """
        self.set_op("replicate_pods")
        if not pods:
            return

        # TODO: disconnect pods on errors?
        pods_to_replicate = []
        for pod in pods:
            # If a scan is active, try again next time (don't skip next schedule)
            if self.pod_manager.check_pod_available_for_action(pod=pod, action="replication"):
                pod.next_replication = get_next_schedule(pod.next_replication, pod.replication_interval)
                self.log.info("{} from pod: '{}'. Datetime: {}. Interval: {}. Next replication: {}"
                              .format("Simulating replication" if self.skip_replication else "Replicating",
                                      pod.name, datetime.datetime.utcnow(), pod.replication_interval,
                                      pod.next_replication))
                pods_to_replicate.append(pod)
            else:
                pod.next_replication += relativedelta(seconds=self.REPLICATION_RETRY_BACKOFF)

        if self.skip_replication:
            return

        replications_results = await self.replication_client.run(remotes=pods_to_replicate)
        for i, replication_result in enumerate(replications_results):
            if isinstance(replication_result, Exception):
                self.log.error("Failed replication from remote {}. Error: {}".format(pods_to_replicate[i].name,
                                                                                     replication_result))
        return

    async def _send_manual_scan_request(self, pod: PodData, scan_doc: dict, coll: str = "scans") -> ClientResponse:
        """
            Send scan request to remote and reset pod health to prevent immediate replication
        :param pod: PodData instance
        :param scan_doc: API-valid scan request document
        :param coll: collection name (scans or scheduled_scans)
        :return: response from API client
        """
        self.log.info("Sending manual scan request to remote: {}".format(pod.name))
        # Reset remote health to avoid instant replication
        pod.health.reset()
        return await pod.calipso_client.send_post(endpoint=coll, payload=clean_scan_request(request=scan_doc,
                                                                                            coll=coll))

    async def send_manual_scan_requests(self) -> None:
        """
            Send all remote scan requests (with "scan_to_remote" flag set) to respective pods via API.
            After the requests are sent, unset the "scan_to_remote" flag in remote scan request documents
            and set "replicate" flag to trigger a replication later.
        :return:
        """
        self.set_op("send_manual_scan_requests")
        await self.central_mongo_connection.connect(force_reconnect=True)

        requests_to_send = []
        for coll in ("scans", "scheduled_scans"):
            pending_requests = self.central_mongo_connection.find(
                collection=coll,
                query={
                    "send_to_remote": True
                }
            )

            async for request in pending_requests:
                pod = self.pods.get(request.get("environment"))
                if not pod:
                    self.log.warning("Scan request for env '{}' is marked as remote, "
                                     "but no matching remote is found")
                    continue

                # Remote environment has a non-compound name
                request["env_name"] = pod.env_name
                requests_to_send.append({
                    "request_id": request["_id"],
                    "pod": pod,
                    "coll": coll,
                    "func": self._send_manual_scan_request(pod=pod, scan_doc=request, coll=coll)
                })

        if not requests_to_send:
            self.central_mongo_connection.disconnect()
            return

        await self.connect_remotes(pods=[r["pod"] for r in requests_to_send],
                                   force_reconnect=True)
        results = await asyncio.gather(*[req["func"] for req in requests_to_send], return_exceptions=True)

        successful_request_docs = []
        for i, res in enumerate(results):
            if res and isinstance(res, Exception):
                self.log.warning("Failed to send scan request to remote {}. Error: {}"
                                 .format(requests_to_send[i]["pod"].full_name, res))
            else:
                req_doc = {
                    "_id": requests_to_send[i]["request_id"],
                    "send_to_remote": False
                }
                if requests_to_send[i]["coll"] == "scans":
                    req_doc.update({
                        "replicate": True,
                        "status": "pending_replication"
                    })
                successful_request_docs.append(req_doc)

        for coll in ("scans", "scheduled_scans"):
            await self.central_mongo_connection.bulk_update(
                collection=coll,
                docs=successful_request_docs,
                key="_id",
                upsert=False,
            )
        self.central_mongo_connection.disconnect()

    async def perform_manual_replications(self) -> None:
        """
            Perform replications from all remotes that recently had been manually scanned
            based on "replicate" flag in scan request doc.
            After replication has finished successfully, unset the "replicate" flag.
        :return:
        """
        self.set_op("perform_manual_replications")
        await self.central_mongo_connection.connect(force_reconnect=True)

        pending_requests = self.central_mongo_connection.find(
            collection="scans",
            query={
                "replicate": True
            }
        )

        pods_to_replicate = []
        now = datetime.datetime.utcnow()
        async for request in pending_requests:
            pod = self.pods.get(request.get("environment"))
            if not pod:
                self.log.warning("Replication is requested for env '{}', "
                                 "but no matching remote is found")
                continue

            # This is needed to avoid premature replication without breaking everything else in the process
            if now < request["submit_timestamp"] + relativedelta(minutes=1):
                continue

            pods_to_replicate.append({"pod": pod, "request_id": request["_id"]})

        self.central_mongo_connection.disconnect()
        if not pods_to_replicate:
            return

        # Reconnect to remotes and check actual health statuses
        await self.connect_remotes(pods=[p["pod"] for p in pods_to_replicate],
                                   force_reconnect=True)

        # Filter only remotes that are ready
        pods_to_replicate = [
            p for p in pods_to_replicate
            if self.pod_manager.check_pod_available_for_action(pod=p["pod"], action="replication")
        ]

        # Replicate
        replication_errors = await self.replication_client.run(remotes=[p["pod"] for p in pods_to_replicate])

        # successful_replication_docs = []
        for i, replication_error in enumerate(replication_errors):
            if replication_error and isinstance(replication_error, Exception):
                self.log.error("Failed to replicate from remote {}. Error: {}"
                               .format(pods_to_replicate[i]["pod"].name, replication_error))

    async def get_pending_actions(self, pod: PodData, verify_health: bool) -> (bool, bool):
        """
            Checks pod health and pending action status
        :param pod: initialized PodData object with set first schedules
        :param verify_health: whether to check pod connection or simply return pending actions
        :return: two flags: whether pod is pending discovery and replication
        """
        self.set_op("get_pending_actions")

        # Setup first schedules for pod if missing
        if not pod.next_discovery or not pod.next_replication:
            self.setup_first_schedules(pod)
            return True, True

        pending_actions = (
            pod.next_discovery <= datetime.datetime.utcnow(),
            pod.next_replication <= datetime.datetime.utcnow()
        )

        # Return pending actions if health verification doesn't make sense
        if not any(pending_actions) or not verify_health:
            return pending_actions

        if not pod.is_connected:
            return False, False

        await self.pod_manager.set_pod_health(pod)
        if not self.pod_manager.is_pod_compatible(pod):
            self.log.warning("Remote {} is not ready".format(pod.name))
            return False, False

        return pending_actions

    async def idle(self) -> None:
        self.set_op("idle")
        await asyncio.sleep(1)

    async def _configure(self) -> None:
        # Set up connection to central MongoDB.
        # Schedule manager cannot proceed if this step fails.
        self.set_op("connect_to_central_db")
        await self.central_mongo_connection.connect()

        # Load environments documents for defined remotes
        await self.load_environments()
        self.central_mongo_connection.disconnect()

    async def configure(self) -> None:
        """
            Error-tolerant wrapper for configuration setup method.
            If configuration method is consistently unable to complete,
            the wrapper linearly backoffs further iterations.
        """
        self.set_op("configure")
        self.failing_streak = 0

        def connection_backoff() -> int:
            return min(self.MAX_SCHEDULE_MANAGER_RESTART_BACKOFF,
                       5 * self.failing_streak)

        while True:
            try:
                await self._configure()
                self._reset_error()
                break
            except Exception as e:
                self.log.error("Schedule manager configure() failed. Error: {}".format(e))
                self.failing_streak += 1
                self.latest_error = e
                self.central_mongo_connection.disconnect()
                await asyncio.sleep(connection_backoff())

    async def _do_action(self):
        while True:
            # Connect remotes with pending actions
            await self.reconnect_remotes_with_pending_actions()

            # Check if new remotes were added via API and update the list
            await self.update_remotes()

            # Send manual scan and scheduled scan requests to remotes
            await self.send_manual_scan_requests()

            # Perform replications for manually submitted scans
            await self.perform_manual_replications()

            # Find out pending actions (discovery, replication) for all remotes
            pods_list = list(self.pods.values())
            pod_actions = await asyncio.gather(
                *[self.get_pending_actions(pod, verify_health=True) for pod in pods_list]
            )

            discovery_requests = []
            replications = []
            for i, (discovery_pending, replication_pending) in enumerate(pod_actions):
                if discovery_pending:
                    discovery_requests.append(pods_list[i])
                if replication_pending:
                    replications.append(pods_list[i])

            # Send scan requests to all pending remotes
            # (skipping the disconnected remotes and those that have an action in progress)
            await self.scan_pods(sorted(discovery_requests, key=lambda p: p.next_discovery))

            # Replicate from all pending remotes
            # (skipping the disconnected remotes and those that have an action in progress)
            await self.replicate_pods(replications)

            if discovery_requests or replications:
                # Save environments that had discovery or replication performed to the central DB
                await self.save_environments(pods=discovery_requests + replications)
            else:
                # Sleep only if no action has been performed during the action loop
                if not discovery_requests and not replications:
                    await self.idle()

            self._reset_error()

    async def do_action(self):
        """
            Error-tolerant wrapper for main loop.
            If main loop is consistently unable to fully complete an iteration,
            the wrapper exponentially backoffs further iterations.
        """
        self.failing_streak = 0

        def connection_backoff() -> int:
            return min(self.MAX_SCHEDULE_MANAGER_RESTART_BACKOFF,
                       int(math.pow(2, min(self.failing_streak, 12))))

        while True:
            try:
                return await self._do_action()
            except Exception as e:
                self.log.error("Schedule manager failed. Error: {}".format(e))
                self.failing_streak += 1
                self.latest_error = e
                self.central_mongo_connection.disconnect()
                await asyncio.sleep(connection_backoff())

    def stop(self):
        # TODO: cleanup?
        super().stop()
        self.central_mongo_connection.disconnect()
