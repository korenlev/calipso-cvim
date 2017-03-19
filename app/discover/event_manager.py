import argparse

import time

from multiprocessing import Process, Manager as SharedManager

from discover.manager import Manager
from discover.environment_listener import listen
from utils.mongo_access import MongoAccess


class EventManager(Manager):
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
                            help="Name of config file " +
                                 "with MongoDB server access details")
        parser.add_argument("-c", "--collection", nargs="?", type=str,
                            default=EventManager.DEFAULTS["collection"],
                            help="Environments collection to read from")
        parser.add_argument("-y", "--inventory", nargs="?", type=str,
                            default=EventManager.DEFAULTS["inventory"],
                            help="name of inventory collection \n" +
                                 "(default: '{}')".format(EventManager.DEFAULTS["inventory"]))
        parser.add_argument("-i", "--interval", nargs="?", type=float,
                            default=EventManager.DEFAULTS["interval"],
                            help="Interval between collection polls"
                                 "(must be more than {} seconds)"
                            .format(EventManager.MIN_INTERVAL))
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

        self.log.info("Started EventManager with following configuration:\n"
                      "Mongo config file path: {0}\n"
                      "Collection: {1}\n"
                      "Polling interval: {2} second(s)"
                      .format(self.args.mongo_config, self.collection.name, self.interval))

    def listen_to_events(self, env_name, process_vars):
        listen({
            'env': env_name,
            'mongo_config': self.args.mongo_config,
            'inventory': self.args.inventory,
            'loglevel': self.args.loglevel,
            'environments_collection': self.args.collection,
            'process_vars': process_vars
        })

    def update_operational_statuses(self):
        self.collection.update_many(
            {"name": {"$in": [p.get("name")
                              for p in self.processes
                              if p.get("vars").get("operational", "").lower() == "running"]}},
            {"$set": {"operational": "running"}}
        )
        self.collection.update_many(
            {"name": {"$in": [p.get("name")
                              for p in self.processes
                              if p.get("vars").get("operational", "").lower() == "error"]}},
            {"$set": {"operational": "error"}}
        )

    def do_action(self):
        try:
            while True:
                # Update "operational" field in db before removing dead processes
                # so that we keep last statuses of env listeners before they were terminated
                self.update_operational_statuses()

                # Remove dead processes from memory so that they are fetched freshly from db later
                self.processes = [process for process in self.processes
                                  if process.get("process").is_alive()]

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
                time.sleep(self.interval)
        finally:
            # Gracefully stop processes
            for p in self.processes:
                self.log.info("Stopping '{0}' event listener".format(p.get("name")))
                p.get("process").terminate()


if __name__ == "__main__":
    EventManager().run()
