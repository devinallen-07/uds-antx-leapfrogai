import boto3
import os
from logs import get_logger

log = get_logger()

def get_client(region='us-gov-west-1'):
   access_key = os.environ.get('S3_ACCESS_KEY', None)
   secret_key = os.environ.get('S3_SECRET_KEY', None)


def get_files(prefix=''):
   return None