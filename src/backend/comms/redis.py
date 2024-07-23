import redis
import os
from logs import get_logger

log = get_logger()

REDIS_ENGINE = None

def create_redis_connection():
   host = os.environ.get('REDIS_HOST')
   pwd = os.environ.get('REDIS_PASSSWORD')
   port = os.environ.get('REDIS_PORT', '6379')
   r = redis.Redis(host=host, port=port, password=pwd)
   REDIS_ENGINE = r
   return r


def get_redis_connection():
   if REDIS_ENGINE is None:
      return create_redis_connection()
   else:
      try:
         REDIS_ENGINE.ping()
      except Exception as e:
         log.warn(f'Error connecting to redis: {e}')
         return create_redis_connection()
      return REDIS_ENGINE
   
def get_processed_files():
   return []
