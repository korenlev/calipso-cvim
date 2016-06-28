from kombu.mixins import ConsumerMixin
from kombu.log import get_logger
from kombu import Queue, Exchange

from event_handler import EventHandler

logger = get_logger(__name__)


class Worker(ConsumerMixin):
  event_queues = [
    Queue('notifications.info', Exchange('nova', 'topic', durable=False), durable=False),
    Queue('notifications.info', Exchange('neutron', 'topic', durable=False), durable=False)
  ]

  def __init__(self, connection):
    self.connection = connection
    self.handler = EventHandler()
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
      "compute.instance.suspend.end": self.handler.instance_up
    }

  def get_consumers(self, Consumer, channel):
    return [Consumer(queues=self.event_queues,
      accept=['json'],
      callbacks=[self.process_task])]

  def process_task(self, body, message):
    self.handle_event(body["event_type"], body)
    message.ack()

  def handle_event(self, type, notification):
    if type not in self.notifications_to_catch:
      return ""
    return self.notification_responses[type](notification)

if __name__ == '__main__':
  from kombu import Connection
  from kombu.utils.debug import setup_logging
  # setup root logger
  setup_logging(loglevel='DEBUG', loggers=[''])

  with Connection('amqp://nova:btE6JPF9@10.56.20.83:5672//') as conn:
    try:
      print(conn)
      worker = Worker(conn)
      worker.run()
    except KeyboardInterrupt:
      print('Stopped')
