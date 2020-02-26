import argparse
import datetime
import re
import time
from typing import Collection

from dateutil.relativedelta import relativedelta

from base.utils.logging.file_logger import FileLogger
from scan.manager import Manager
from schedule.pod_manager import PodManager
from schedule.pods_config_parser import get_pods_config, PodData


class ScheduleManager(Manager):

    DEFAULTS = {
        "setup_data": "/root/openstack-configs/setup_data.yaml",
        "mongo_config": "",
        "loglevel": "INFO"
    }

    schedule_regex = re.compile("(\d+)([ymwdhMS])")

    def __init__(self):
        self.args = self.get_args()
        super().__init__(log_directory=self.args.log_directory,
                         log_level=self.args.loglevel,
                         mongo_config_file=self.args.mongo_config)

        self.pods_config = None
        self.pod_manager = PodManager(log_level=self.args.loglevel)

    def get_next_schedule(self, last_schedule: datetime.datetime, interval: str, align_time: bool = True):
        regex_match = re.match(self.schedule_regex, interval)
        if not regex_match:
            self.log.error("Invalid schedule interval: {}".format(interval))
            return None

        number = int(regex_match.group(1))
        unit = regex_match.group(2)

        delta = relativedelta(years=number if unit == "y" else 0,
                              months=number if unit == "m" else 0,
                              weeks=number if unit == "w" else 0,
                              days=number if unit == "d" else 0,
                              hours=number if unit == "h" else 0,
                              minutes=number if unit == "M" else 0,
                              seconds=number if unit == "S" else 0)

        next_schedule = (last_schedule + delta).replace(microsecond=0)

        if align_time and unit != "S":
            next_schedule = next_schedule.replace(second=0)
            if unit != "M":
                next_schedule = next_schedule.replace(minute=0)
                if unit != "h":
                    next_schedule = next_schedule.replace(hour=0)
                    if unit == "w":
                        next_schedule -= relativedelta(days=next_schedule.isoweekday() - 1)
                    elif unit != "d":
                        next_schedule = next_schedule.replace(day=1)
                        if unit != "m":
                            next_schedule = next_schedule.replace(month=1)

        # TODO: figure out first schedule
        return next_schedule

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("-s", "--setup_data", nargs="?", type=str,
                            default=ScheduleManager.DEFAULTS.get("setup_data"),
                            help="File logger directory \n(default: '{}')"
                            .format(ScheduleManager.DEFAULTS.get("setup_data")))
        parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                            default=ScheduleManager.DEFAULTS["mongo_config"],
                            help="Path to config file " +
                                 "with MongoDB server access details")
        parser.add_argument("-d", "--log_directory", nargs="?", type=str,
                            default=FileLogger.LOG_DIRECTORY,
                            help="File logger directory \n(default: '{}')"
                                 .format(FileLogger.LOG_DIRECTORY))
        parser.add_argument("-l", "--loglevel", nargs="?", type=str,
                            default=ScheduleManager.DEFAULTS["loglevel"],
                            help="Logging level \n(default: '{}')"
                                 .format(ScheduleManager.DEFAULTS["loglevel"]))
        args = parser.parse_args()
        return args

    def configure(self):
        self.pods_config = get_pods_config(self.args.setup_data)
        for pod in self.pods_config:
            pod.env_name = "cvim-{}".format(pod.name)  # TODO: generalize?
            pod.name = "{}:{}:{}".format(pod.region, pod.metro, pod.env_name)  # TODO: generalize?
            pod.next_discovery = datetime.datetime.now()  # TODO: configurable first schedule
            pod.next_replication = datetime.datetime.now() # TODO: configurable discovery-replication delta??

    def scan_pods(self, pods: Collection[PodData]):
        for pod in pods:
            pod.next_discovery = self.get_next_schedule(pod.next_discovery, pod.discovery_interval)

            # If a scan is active, skip this schedule
            if self.pod_manager.check_pod_available_for_action(pod=pod, env_name=pod.env_name):
                print("Sending scan request to pod '{}'. Datetime: {}. Interval: {}. Next discovery: {}"
                      .format(pod.name, datetime.datetime.now(), pod.discovery_interval, pod.next_discovery))
                self.pod_manager.send_scan_request(pod=pod, env_name=pod.env_name)
                # Clear pod health so that replication doesn't happen mid-scan
                pod.health = {}

    def replicate_pods(self, pods: Collection[PodData]):
        if not pods:
            return

        for pod in pods:
            # If a scan is active, try again next time (don't skip next schedule)
            if self.pod_manager.check_pod_available_for_action(pod=pod, env_name=pod.env_name):
                # TODO: replicate!
                pod.next_replication = self.get_next_schedule(pod.next_replication, pod.replication_interval)
                print("Replicating from pod: '{}'. Datetime: {}. Interval: {}. Next replication: {}"
                      .format(pod.name, datetime.datetime.now(), pod.replication_interval, pod.next_replication))

    def do_action(self):
        # TODO: make async?
        while True:
            discovery_requests = []
            replications = []
            for pod in self.pods_config:
                self.pod_manager.set_pod_health(pod)
                if not self.pod_manager.check_pod_status(pod):
                    self.log.warning("Pod {} is not ready".format(pod.name))
                    continue

                if pod.next_discovery and pod.next_discovery <= datetime.datetime.now():
                    discovery_requests.append(pod)
                if pod.next_replication and pod.next_replication <= datetime.datetime.now():
                    replications.append(pod)

            self.scan_pods(sorted(discovery_requests, key=lambda p: p.next_discovery))
            self.replicate_pods(replications)

            time.sleep(1)


if __name__ == "__main__":
    ScheduleManager().run()

