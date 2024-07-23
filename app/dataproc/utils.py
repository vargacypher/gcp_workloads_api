import requests
from google.auth import default
from google.auth.transport.requests import Request
from google.cloud import bigquery

from .settings import *


def get_access_token():
    """
    This works on any GCP service, i.e. cloud run
    :return: access_token
    """
    try:
        url = f'{METADATA_URL}/instance/service-accounts/{SERVICE_ACCOUNT}/token'

        response = requests.get(url, headers=METADATA_HEADERS)
        response.raise_for_status()

        access_token = response.json()['access_token']
    except requests.exceptions.ConnectionError:
        return None

    return access_token


def get_default_access_token():
    """
    This works only locally for development
    Obtain the default credentials
    :return: access_token
    """
    credentials, project_id = default()

    if credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())

    return credentials.token


def _create_bq_demo_db():
    """
    Runs a BigQuery to create demo db

    :return: None
    """

    client = bigquery.Client()
    dataset_id = f"{PROJECT_ID}.{DATASET_NAME}" 

    try:
        client.get_dataset(dataset_id)
        print(f"Dataset '{dataset_id}' already exists. Skipping creation.")
    except:
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = "US"
        dataset = client.create_dataset(dataset, timeout=15)
        print(f"Created dataset '{PROJECT_ID}.{dataset.dataset_id}'.")


def run_demojob_query(project_id: str, dataset_name: str, table_name:str) -> list:
    """
    Runs a BigQuery query and returns the results as a list of dictionaries.

    Args:
        project_id (str): The ID of your Google Cloud project.
        dataset_name (str): The name of the dataset containing the table to query.
        query (str): The SQL query to execute.

    :return: A list of dictionaries representing the query results.
    """

    client = bigquery.Client(project_id)

    query_job = client.query(f"SELECT * FROM `{dataset_name}.{table_name}` LIMIT 100")

    # Get query results as a list of dictionaries
    results = query_job.result() 
    rows = [dict(row) for row in results]

    return rows
