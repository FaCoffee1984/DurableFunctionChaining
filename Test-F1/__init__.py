# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import hashlib
import time
import datetime
from azure.cosmos import CosmosClient
import azure.functions as func

def generate_id(string=None, length=10):
    '''This function generates a hash id to be attached to each new row'''

    ts = time.time()
    guid = hashlib.shake_128((str(string) + str(ts)).encode()).hexdigest(10)
    return guid

def main(orchestratorActivityTrigger, outputDocument: func.Out[func.Document]) -> None:

    '''
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due')

    logging.info('Python timer trigger function ran at %s', utc_timestamp) 
    '''

    result1 = {
    "first_letter": "A",
    "second_letter": "B",
    "third_letter": "C",
    "score": 0.001,
    }

    result1['id'] = generate_id()

    outputDocument.set(func.Document.from_dict(result1))

    return ""
