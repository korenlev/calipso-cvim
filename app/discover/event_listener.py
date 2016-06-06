from kombu import Connection
import sys

def consume():
  with Connection('amqp://nova:btE6JPF9@10.56.20.83:5672//') as conn:
    simple_queue = conn.SimpleQueue('simple_queue')
    try:
      message = simple_queue.get(block=True, timeout=1)
    except Exception as e:
      if not e or not str(e).strip():
        print("No message")
      else:
        print(e)
      sys.exit(1)
    print("Received: %s" % message.payload)
    message.ack()
    simple_queue.close()

if __name__ == '__main__':
  consume()

