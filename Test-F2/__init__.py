# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import azure.functions as func
from azure.cosmos import CosmosClient

def add_username(string=None):
    '''Generate username'''

    name = "Michael"
    surname = "Jackson"
    username = name+" "+surname

    return username


def main(F1activitytrigger, inputDocument: func.DocumentList) -> str:

    if inputDocument:
        logging.info('Document id: %s', inputDocument[0]['id'])

    result2 = inputDocument[0].data

    result2['username'] = add_username() 

    return result2
