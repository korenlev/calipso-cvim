import argparse

from kombu import Queue, Exchange
from kombu.log import get_logger
from kombu.mixins import ConsumerMixin

from discover.configuration import Configuration
from discover.event_handler import EventHandler
from discover.inventory_mgr import InventoryMgr

logger = get_logger(__name__)


class Worker(ConsumerMixin):
    event_queues = [
        Queue('notification.nova',
              Exchange('nova', 'topic', durable=False),
              durable=False, routing_key='#'),
        Queue('notifications.neutron',
              Exchange('neutron', 'topic', durable=False),
              durable=False, routing_key='#'),
        Queue('notifications.neutron',
              Exchange('openstack', 'topic', durable=False),
              durable=False, routing_key='notification.info')
    ]

    def __init__(self, connection):
        self.connection = connection

    def set_env(self, env, inventory_collection):
        inv = InventoryMgr()
        inv.set_inventory_collection(inventory_collection)
        self.handler = EventHandler(env, inventory_collection)
        self.notification_responses = {
            "compute.instance.create.end": self.handler.instance_add,
            "compute.instance.delete.end": self.handler.instance_delete,
            "compute.instance.rebuild.end": self.handler.instance_update,
            "compute.instance.update": self.handler.instance_update,

            "servergroup.create": self.handler.region_add,
            "servergroup.delete": self.handler.region_delete,
            "servergroup.update": self.handler.region_update,
            "servergroup.addmember": self.handler.region_update,

            "compute.instance.shutdown.start": self.handler.instance_down,
            "compute.instance.power_off.start": self.handler.instance_down,
            "compute.instance.power_on.end": self.handler.instance_up,
            "compute.instance.suspend.start": self.handler.instance_down,
            "compute.instance.suspend.end": self.handler.instance_up,

            "network.create.end": self.handler.network_create,
            "network.delete.end": self.handler.network_delete,

            "subnet.create.end": self.handler.subnet_create,
            "subnet.delete.end": self.handler.subnet_delete,

            "port.create.end": self.handler.port_create,
            "port.delete.end": self.handler.port_delete,

            "router.create.end": self.handler.router_create,

            "router.update.end": self.handler.router_update,

            "router.delete.end": self.handler.router_delete,

            "router.interface.create": self.handler.router_interface_create,
            "router.interface.delete": self.handler.router_interface_delete,
        }

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=self.event_queues,
                         accept=['json'],
                         callbacks=[self.process_task])]

    def process_task(self, body, message):
        if "event_type" in body:
            self.handle_event(body["event_type"], body)
        message.ack()

    def handle_event(self, type, notification):
        print("got notification, event_type: " + type + '\n' + str(notification))
        if type not in self.notification_responses.keys():
            return ""
        return self.notification_responses[type](notification)


def get_args():
    # try to read scan plan from command line parameters
    parser = argparse.ArgumentParser()
    default_env = "Mirantis-Liberty"
    parser.add_argument("-m", "--mongo_config", nargs="?", type=str,
                        default="",
                        help="name of config file with MongoDB servr access details")
    parser.add_argument("-e", "--env", nargs="?", type=str,
                        default=default_env,
                        help="name of environment to scan \n(default: " + default_env + ")")
    parser.add_argument("-y", "--inventory", nargs="?", type=str,
                        default="inventory",
                        help="name of inventory collection \n(default: 'inventory')")
    parser.add_argument("-l", "--loglevel", nargs="?", type=str, default="INFO",
                        help="logging level \n(default: 'INFO')")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    from kombu import Connection
    from kombu.utils.debug import setup_logging

    # setup root logger
    setup_logging(loglevel='DEBUG', loggers=[''])

    args = get_args()
    conf = Configuration(args.mongo_config)
    env = args.env
    conf.use_env(env)
    amqp_config = conf.get("AMQP")
    host = amqp_config["host"]
    port = amqp_config["port"]
    user = amqp_config["user"]
    pwd = amqp_config["password"]
    connect_url = 'amqp://' + user + ':' + pwd + '@' + host + ':' + port + '//'
    with Connection(connect_url) as conn:
        try:
            print(conn)
            worker = Worker(conn)
            worker.set_env(env, args.inventory)
            worker.run()
        except KeyboardInterrupt:
            print('Stopped')
