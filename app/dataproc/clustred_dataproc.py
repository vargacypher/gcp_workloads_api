import json
import requests

from time import sleep
from .settings import *
from .utils import _create_bq_demo_db,get_access_token,get_default_access_token
from typing import List

def dataproc_submit_demo_job() -> List:
    _create_bq_demo_db()

    results = []
    
    reponse_create = _create_cluster()
    results.append(reponse_create)
    sleep(10)
    response_submmit = _submmit_job()
    results.append(response_submmit)
    
    return results


def get_job_status(workload_id:str) -> dict:
    """
    Get job result status

    :return: A dict with service response if job information and status
    """
    job_url = f'{STATUS_JOB_URL}/{workload_id}'

    if get_access_token():
        bearer_token = get_access_token()
    else:
        bearer_token = get_default_access_token()

    headers = {'Authorization': f'Bearer {bearer_token}', 'Content-Type': 'application/json'}
    response = requests.get(url=job_url, headers=headers)
    response_content = json.loads(response.content)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return response_content['error']['message']

    return response_content


def _create_cluster() -> dict:
    """
    Create dataproc cluster

    :return: A dict with service response
    """
    dataproc_batch_url = CLUSTER_URL

    payload = CLUSTER_CFG
    bearer_token = get_access_token()

    headers = {'Authorization': f'Bearer {bearer_token}', 'Content-Type': 'application/json'}
    response = requests.post(url=dataproc_batch_url, headers=headers, json=payload)
    response_content = json.loads(response.content)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return response_content['error']['message']

    return {'creating cluster':response_content}


def _submmit_job() -> dict:
    """
    Subimmit dataproc job

    :return: A dict with service response and workload_id
    """

    submmit_job_url = SUBMMIT_JOB_URL

    payload = DEFAULT_JOB_CFG
    bearer_token = get_access_token()

    headers = {'Authorization': f'Bearer {bearer_token}', 'Content-Type': 'application/json'}
    response = requests.post(url=submmit_job_url, headers=headers, json=payload)
    response_content = json.loads(response.content)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return response_content['error']['message']

    return {'created job':response_content,'workload_id':DEFAULT_JOB_CFG["job"]["reference"]["jobId"]}


