from kombu.mixins import ConsumerMixin
from kombu.log import get_logger
from kombu import Queue, Exchange

logger = get_logger(__name__)


class Worker(ConsumerMixin):
  event_queues = [
    Queue('notifications.info', Exchange('nova', 'topic', durable=False), durable=False),
    Queue('notifications.info', Exchange('neutron', 'topic', durable=False), durable=False)
  ]

  def __init__(self, connection):
    self.connection = connection

  def get_consumers(self, Consumer, channel):
    return [Consumer(queues=self.event_queues,
      accept=['json'],
      callbacks=[self.process_task])]

  def process_task(self, body, message):
    print("RECEIVED MESSAGE: %r" % (body, ))
    message.ack()

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
