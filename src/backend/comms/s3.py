import boto3
import os
from logs import get_logger
from comms.redis import get_processed_files

log = get_logger()

REGION = os.environ.get('S3_REGION', None)
ENDPOINT = os.environ.get('S3_ENDPOINT', 'http://localhost:9000')
BUCKET = os.environ.get('S3_BUCKET', 'antx')

def get_s3_client():
   access_key = os.environ.get('S3_ACCESS_KEY', "test-user")
   secret_key = os.environ.get('S3_SECRET_KEY', "test-secret")
   return boto3.client('s3', endpoint_url=ENDPOINT,
                       access_key=access_key, secret_key=secret_key)

def get_files(prefix=''):
   processed_files = get_processed_files()
   s3 = get_s3_client()
   s3_objects = s3.list_objects_v2(Bucket=BUCKET, Prefix=prefix)
   to_process = []
   for object in s3_objects['Contents']:
      if object['Key'] not in processed_files:
         to_process.append(object['Key'])
   return to_process
