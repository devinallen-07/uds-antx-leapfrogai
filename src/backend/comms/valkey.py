import redis
import json
import pandas as pd
import os
from io import StringIO
from logs import get_logger

log = get_logger()

REDIS_ENGINE = None

def create_valkey_connection():
   host = os.environ.get('REDIS_HOST')
   pwd = os.environ.get('REDIS_PASSSWORD')
   port = os.environ.get('REDIS_PORT', '6379')
   r = redis.Redis(host=host, port=port, password=pwd)
   REDIS_ENGINE = r
   return r

def get_valkey_connection():
   if REDIS_ENGINE is None:
      return create_valkey_connection()
   else:
      try:
         REDIS_ENGINE.ping()
      except Exception as e:
         log.warn(f'Error connecting to redis: {e}')
         return create_valkey_connection()
      return REDIS_ENGINE
   
def get_output_frame(key):
   r = get_valkey_connection()
   df = pd.read_json(StringIO(r.get(key).decode('utf-8')))
   return df

def put_output_frame(df, key):
   r = get_valkey_connection()
   r.set(key, df.to_json())


def get_processed_files(key):
   r = get_valkey_connection()
   files = list(json.loads(r.get(key)))
   return files

def set_processed_files(key, files):
   r = get_valkey_connection()
   r.set(key, json.dumps(files))
