#!/usr/bin/env python3

import argparse
import json
import time

from kafka import KafkaConsumer

from discover.configuration import Configuration
from discover.mongo_access import MongoAccess
from discover.inventory_mgr import InventoryMgr
from discover.logger import Logger


class StatsConsumer(MongoAccess, Logger):
    default_env = "WebEX-Mirantis@Cisco"

    def __init__(self):
        self.get_args()
        self.set_loglevel(self.args.loglevel)
        self.conf = Configuration(self.args.mongo_config)
        self.inv = InventoryMgr()
        self.inv.set_inventory_collection(self.args.inventory)
        stats_coll = self.inv.get_coll_name('statistics')
        self.stats = self.db[stats_coll]
        # consume messages from topic
        self.consumer = KafkaConsumer('VPP.stats',
                                      group_id='osdna_test',
                                      # debugging - read from first message
                                      auto_offset_reset='smallest',
                                      bootstrap_servers=['localhost:9092'])

    def get_args(self):
        # try to read scan plan from command line parameters
        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                            default="",
                            help="name of config file " +
                            "with MongoDB servr access details")
        parser.add_argument("-e", "--env", nargs="?", type=str,
                            default=self.default_env,
                            help="name of environment to scan \n" +
                            "(default: " + self.default_env + ")")
        parser.add_argument("-y", "--inventory", nargs="?", type=str,
                            default="inventory",
                            help="name of inventory collection \n" +
                            "(default: 'inventory')")
        parser.add_argument("-l", "--loglevel", nargs="?", type=str,
                            default="INFO",
                            help="logging level \n(default: 'INFO')")
        self.args = parser.parse_args()

    def read(self):
        for kafka_msg in self.consumer:
            msg = json.loads(kafka_msg.value.decode())
            self.add_stats(msg)

    def add_stats(self, msg):
        host_ip = msg['hostIp']
        search = {
            'environment': self.args.env,
            'type': 'host',
            'ip_address': host_ip
        }
        host = self.inv.find_items(search, get_single=True)
        if not host:
            self.log.error('could not find host with ip address=' + host_ip)
            return
        host_id = host['id']
        search = {
            'environment': self.args.env,
            'type': 'vedge',
            'host': host_id
        }
        vedge = self.inv.find_items(search, get_single=True)
        if not vedge:
            self.log.error('could not find vEdge for host: ' + host_id)
            return
        self.log.info('setting VPP stats for vEdge of host: ' + host_id)
        self.add_stats_for_object(vedge, msg)

    def add_stats_for_object(self, o, msg):
        msg['type'] = 'vedge_flows'
        msg['environment'] = self.args.env
        msg['object_type'] = o['type']
        msg['object_id'] = o['id']
        time_seconds = int(msg['averageArrivalNanoSeconds'] / 1000000000)
        sample_time = time.gmtime(time_seconds)
        msg['sample_time'] = time.strftime("%Y-%m-%dT%H:%M:%SZ", sample_time)
        # find instances between which the flow happens
        # to find the instance, find the related vNIC first
        msg['source'] = self.find_instance_for_stat('source', msg)
        msg['destination'] = self.find_instance_for_stat('destination', msg)
        self.stats.insert_one(msg)

    def find_instance_for_stat(self, direction, msg):
        search_by_mac_address = 'sourceMacAddress' in msg
        value_attr = 'MacAddress' if search_by_mac_address else 'IpAddress'
        value_to_search = msg[direction + value_attr]
        attr = 'mac_address' if search_by_mac_address else 'ip_address'
        search = {
            'environment': self.args.env,
            'type': 'vnic',
            attr: value_to_search
        }
        vnic = self.inv.find_items(search, get_single=True)
        if not vnic:
            self.log.error('failed to find vNIC for ' +
                           attr + '=' + value_to_search)
            return 'Unknown'
        # now find the instance name from the vnic name
        name_path = vnic['name_path'].split('/')
        instance_name = name_path[8]
        return instance_name

if __name__ == '__main__':
    stats_consumer = StatsConsumer()
    stats_consumer.read()
