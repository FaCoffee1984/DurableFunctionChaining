# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    yield context.call_activity('Test-F1')
    result2 = yield context.call_activity('Test-F2')
    yield context.call_activity('Test-F3', result2)
    

main = df.Orchestrator.create(orchestrator_function)

'''
def orchestrator_function(context: df.DurableOrchestrationContext, f: str):

    result = yield context.call_activity(f)

    return result

def main():

    result1 = df.Orchestrator.create(orchestrator_function('Test-F1', None))

    result2 = df.Orchestrator.create(orchestrator_function('Test-F2', None))

    result3 = df.Orchestrator.create(orchestrator_function('Test-F1', result2))
'''

