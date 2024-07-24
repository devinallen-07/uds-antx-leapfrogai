from antx.src.backend.comms.valkey import get_valkey_connection
from logs import get_logger, setup_logging
import os
import json
import traceback

log = get_logger()

class Listener:
   def __init__(self):
      self.r = get_valkey_connection()
      self.sub_channel = os.environ.get('SUB_CHANNEL', 'events')
      self.processes = []

   def start_ingestion(self, data):
      raise NotImplementedError
   
   def end_ingestion(self, data):
      raise NotImplementedError

   def process_message(self, data):
      data = json.loads(data)
      msg_type = data['message_type']
      if msg_type == 'start':
         self.start_ingestion(data)
      elif msg_type == 'end':
         self.end_ingestion(data)
      else:
         log.warn(f'Could not process message: {data}')

   def run(self):
      r = self.r
      pubsub = r.pubsub()
      pubsub.subscribe(self.sub_channel)
      log.info(f'Subscribed to {self.sub_channel}, listening for messages')
      for message in pubsub.listen():
         if message['type'] == 'message':
            log.info(f"Recieved message: {message['data'].decode('utf-8')}")
            try:
               self.process_message(message['data'])
            except Exception as e:
               log.warn(f'Error processing message: {message}, {e}')
               log.warn(traceback.format_exc())
         else:
            log.info(f'Non-message received: {message}')


if __name__ == '__main__':
   setup_logging()
   listener = Listener()
   listener.run()
