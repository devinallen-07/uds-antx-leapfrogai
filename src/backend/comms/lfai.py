import requests
import pandas as pd
import numpy as np
import os
from logs import get_logger

log = get_logger()

def build_transcribe_request(file_path, response_type='json', segmentation=[]):
   raise NotImplementedError

def transcribe():
   raise NotImplementedError

def inference():
   raise NotImplementedError
