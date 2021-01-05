# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from azure.cosmos import CosmosClient
import azure.functions as func
import time


def add_date(string=None):
    '''Generate today's timestamp'''

    today = time.strftime("%Y-%m-%d, %H:%M:%S")

    return today


def main(F2activitytrigger, outputDocument: func.Out[func.Document]) -> str:

    result3 = F2activitytrigger.copy()

    result3['timestamp'] = add_date()

    outputDocument.set(func.Document.from_dict(result3))

    return ""
