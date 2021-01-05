# This function is not intended to be invoked directly. Instead it will be
# triggered by a starter function.


import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    yield context.call_activity('Test-F1')
    result2 = yield context.call_activity('Test-F2')
    yield context.call_activity('Test-F3', result2)
    

main = df.Orchestrator.create(orchestrator_function)

