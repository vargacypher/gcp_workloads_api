import json
import requests

from datetime import datetime
from settings import *
from .utils import *


# '''
# ***********************************************************************************************************************************************************
# Os jobs no Dataproc Serverless nao foram testado por completo devido a quotas de CPU elevadas para o servico e nao disponivel na minha conta.
# ***********************************************************************************************************************************************************
# '''

def dataproc_submit_batch(python_file_url:str) -> dict:
    timestamp = datetime.now()
    formatted_timestamp = timestamp.strftime("%Y%m%d-%H%M%S")
    dataproc_batch_url = f"https://dataproc.googleapis.com/v1/projects/{PROJECT_ID}/locations/{REGION}/batches?batch_id={formatted_timestamp}"

    payload = {
        "runtimeConfig": {
            "version": "2.0",
            "properties": {
                "spark.dynamicAllocation.executorAllocationRatio": "1.0",
                "spark.dynamicAllocation.initialExecutors": "2",
                "spark.dynamicAllocation.minExecutors": "2",
                "spark.dynamicAllocation.maxExecutors": "20"
            }
        },
        "environmentConfig": {
            "executionConfig": {
                "serviceAccount": SPARK_SA,
                # "ttl": '10m',
                # # "subnetworkUri": SUBNET,
                "stagingBucket": 'test_spk'

            }
        },
        "pysparkBatch": {
            "mainPythonFileUri": python_file_url
            # "args": [source_input, target_output]
        }
    }

    if get_access_token():
        bearer_token = get_access_token()
    else:
        bearer_token = get_default_access_token()

    headers = {'Authorization': f'Bearer {bearer_token}', 'Content-Type': 'application/json'}
    response = requests.post(url=dataproc_batch_url, headers=headers, json=payload)
    response_content = json.loads(response.content)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return response_content['error']['message']

    return {'dataproc_response':response_content,'workload_id':f'{formatted_timestamp}'}



def get_dataproc_batch_status(workload_id:str)-> dict:

    dataproc_batch_url = f"https://dataproc.googleapis.com/v1/projects/{PROJECT_ID}/locations/{REGION}/batches/{workload_id}"

    if get_access_token():
        bearer_token = get_access_token()
    else:
        bearer_token = get_default_access_token()

    headers = {'Authorization': f'Bearer {bearer_token}', 'Content-Type': 'application/json'}
    response = requests.get(url=dataproc_batch_url, headers=headers)
    response_content = json.loads(response.content)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return response_content['error']['message']

    return response_content
