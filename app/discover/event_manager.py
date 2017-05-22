import argparse
import os
import signal

import time

from multiprocessing import Process, Manager as SharedManager

from discover.manager import Manager
from discover.environment_listener import listen
from utils.constants import OperationalStatus
from utils.mongo_access import MongoAccess


class EventManager(Manager):

    # After EventManager receives a SIGTERM,
    # it will try to terminate all listeners.
    # After this delay, a SIGKILL will be sent
    # to each listener that is still alive.
    SIGKILL_DELAY = 5  # in seconds

    DEFAULTS = {
        "mongo_config": "",
        "collection": "environments_config",
        "inventory": "inventory",
        "interval": 5,
        "loglevel": "INFO"
    }

    def __init__(self):
        super().__init__()
        self.args = None
        self.db_client = None
        self.interval = None
        self.processes = []

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                            default=EventManager.DEFAULTS["mongo_config"],
                            help="Name of config file with MongoDB server access details"
                                 .format(EventManager.DEFAULTS["mongo_config"]))
        parser.add_argument("-c", "--collection", nargs="?", type=str,
                            default=EventManager.DEFAULTS["collection"],
                            help="Environments collection to read from "
                                 "(default: '{}')"
                            .format(EventManager.DEFAULTS["collection"]))
        parser.add_argument("-y", "--inventory", nargs="?", type=str,
                            default=EventManager.DEFAULTS["inventory"],
                            help="name of inventory collection "
                                 "(default: '{}')"
                            .format(EventManager.DEFAULTS["inventory"]))
        parser.add_argument("-i", "--interval", nargs="?", type=float,
                            default=EventManager.DEFAULTS["interval"],
                            help="Interval between collection polls "
                                 "(must be more than {} seconds. Default: {})"
                            .format(EventManager.MIN_INTERVAL,
                                    EventManager.DEFAULTS["interval"]))
        parser.add_argument("-l", "--loglevel", nargs="?", type=str,
                            default=EventManager.DEFAULTS["loglevel"],
                            help="Logging level \n(default: 'INFO')")
        args = parser.parse_args()
        return args

    def configure(self):
        self.args = self.get_args()
        self.db_client = MongoAccess(self.args.mongo_config)
        self.collection = self.db_client.db[self.args.collection]
        self.interval = max(self.MIN_INTERVAL, self.args.interval)
        self.set_loglevel(self.args.loglevel)

        self.log.info("Started EventManager with following configuration:\n"
                      "Mongo config file path: {0}\n"
                      "Collection: {1}\n"
                      "Polling interval: {2} second(s)"
                      .format(self.args.mongo_config, self.collection.name, self.interval))

    def listen_to_events(self, env_name: str, process_vars: dict):
        listen({
            'env': env_name,
            'mongo_config': self.args.mongo_config,
            'inventory': self.args.inventory,
            'loglevel': self.args.loglevel,
            'environments_collection': self.args.collection,
            'process_vars': process_vars
        })

    def _get_alive_processes(self):
        return [p for p in self.processes if p['process'].is_alive()]

    def _get_operational(self, process: dict) -> OperationalStatus:
        try:
            return process.get("vars", {})\
                          .get("operational")
        except:
            self.log.error("Listener '{}' is unreachable".format(process.get("name")))
            return OperationalStatus.STOPPED

    def _update_operational_status(self, status: OperationalStatus):
        self.collection.update_many(
            {"name": {"$in": [process.get("name")
                              for process
                              in self.processes
                              if self._get_operational(process) == status]}},
            {"$set": {"operational": status.value}}
        )

    def update_operational_statuses(self):
        self._update_operational_status(OperationalStatus.RUNNING)
        self._update_operational_status(OperationalStatus.ERROR)
        self._update_operational_status(OperationalStatus.STOPPED)

    def cleanup_processes(self):
        # Query for envs that are no longer eligible for listening
        # (scanned == false and/or listen == false)
        dropped_envs = [env['name']
                        for env
                        in self.collection
                               .find(filter={'$or': [{'scanned': False},
                                                     {'listen': False}]},
                                     projection=['name'])]

        live_processes = []
        stopped_processes = []
        # Drop already terminated processes
        # and for all others perform filtering
        for process in [p for p in self.processes if p['process'].is_alive()]:
            # If env no longer qualifies for listening,
            # stop the listener.
            # Otherwise, keep the process
            if process['name'] in dropped_envs:
                process['process'].terminate()
                stopped_processes.append(process)
            else:
                live_processes.append(process)

        # Update all 'operational' statuses
        # for processes stopped on the previous step
        self.collection.update_many(
            {"name": {"$in": [process.get("name")
                              for process
                              in stopped_processes]}},
            {"$set": {"operational": OperationalStatus.STOPPED.value}}
        )

        # Keep the living processes
        self.processes = live_processes

    def do_action(self):
        try:
            while True:
                # Update "operational" field in db before removing dead processes
                # so that we keep last statuses of env listeners before they were terminated
                self.update_operational_statuses()

                # Perform a cleanup that filters out all processes
                # that are no longer eligible for listening
                self.cleanup_processes()

                envs = self.collection.find({'scanned': True, 'listen': True})

                # Iterate over environments that don't have an event listener attached
                for env in filter(lambda e: e['name'] not in
                                  map(lambda process: process["name"], self.processes),
                                  envs):
                    name = env['name']

                    # A dict that is shared between event manager and newly created env listener
                    process_vars = SharedManager().dict()
                    p = Process(target=self.listen_to_events,
                                args=(name, process_vars,),
                                name=name)
                    self.processes.append({"process": p, "name": name, "vars": process_vars})
                    self.log.info("Starting event listener for '{0}' env".format(name))
                    p.start()

                # Make sure statuses are up-to-date before event manager goes to sleep
                self.update_operational_statuses()
                time.sleep(self.interval)
        finally:
            # Fetch operational statuses before terminating listeners.
            # Shared variables won't be available after termination.
            stopping_processes = [process.get("name")
                                  for process
                                  in self.processes
                                  if self._get_operational(process) != OperationalStatus.ERROR]
            self._update_operational_status(OperationalStatus.ERROR)

            # Gracefully stop processes
            for process in self._get_alive_processes():
                self.log.info("Stopping '{0}' event listener".format(process.get("name")))
                process.get("process").terminate()

            # Give processes time to finish and kill them if they are stuck
            time.sleep(self.SIGKILL_DELAY)
            for process in self._get_alive_processes():
                self.log.info("Killing '{0}' event listener".format(process.get("name")))
                os.kill(process.get("process").pid, signal.SIGKILL)

            # Updating operational statuses for stopped processes
            self.collection.update_many(
                {"name": {"$in": stopping_processes}},
                {"$set": {"operational": OperationalStatus.STOPPED.value}}
            )

if __name__ == "__main__":
    EventManager().run()
