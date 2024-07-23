import redis
import pandas
import numpy
from comms.redis import get_redis_connection
from logs import get_logger, setup_logging
import os

log = get_logger()

class Listener:

   def __init__(self):
      self.r = get_redis_connection()
      self.sub_channel = os.environ.get('SUB_CHANNEL', 'events')

   #TODO: implement
   def process_message(self, data):
      raise NotImplementedError

   def run(self):
      r = self.r
      pubsub = r.pubsub()
      pubsub.subscribe(self.sub_channel)
      log.info(f'Subscribed to {self.sub_channel}, listening for messages')
      for message in pubsub.listen():
         if message['type'] == 'message':
            log.info(f"Recieved message: {message['data'].decode('utf-8')}")
            self.process_message(message['data'])


if __name__ == '__main__':
   setup_logging()
   listener = Listener()
   listener.run()
