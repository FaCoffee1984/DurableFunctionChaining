import datetime
import logging

import azure.functions as func
import azure.durable_functions as df
from azure.durable_functions import DurableOrchestrationClient


async def main(mytimer: func.TimerRequest, starter: str) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    client = DurableOrchestrationClient(starter)
    instance_id = await client.start_new('TestOrchestrator')


