from models import SuccessResponse
from uuid import uuid4
from fastapi import APIRouter
from dataproc.clustred_dataproc import get_job_status,dataproc_submit_demo_job
from dataproc.utils import run_demojob_query
from dataproc.settings import DATASET_NAME,TABLE_NAME,PROJECT_ID
from typing import List

router = APIRouter()


@router.post("/workloads/batch-cluster/submit-demo", response_model=SuccessResponse)
async def submit(
            python_file_url: str = 'gs://test_spk/spark_word_count.py'
            ) -> SuccessResponse :
    response = dataproc_submit_demo_job()
    return {"success": True,'response': response, "requestId": uuid4()}


@router.get("/workloads/batch-cluster/get-demo-status/{workload_id}", response_model=SuccessResponse)
async def status(
            workload_id:str
            ) -> SuccessResponse :
    response = get_job_status(workload_id)
    return {"success": True,'response': response, "requestId": uuid4()}


@router.get("/workloads/batch-cluster/get-demo-result")
async def result_demo() -> List[dict]:
    response = run_demojob_query(PROJECT_ID,DATASET_NAME,TABLE_NAME)
    return response


# @router.post("/workloads/batch/submit-demo")
# async def submit(
#             python_file_url: str = 'gs://test_spk/spark_word_count.py'
#             ):
#     response = dataproc_submit_batch(
#         python_file_url=python_file_url,
#         source_input='SOURCE_INPUT_LOCATION',
#         target_output='TARGET_OUTPUT_LOCATION'
#     )
#     return response

# @router.get("/workloads/batch/get-demo-status")
# async def status(
#             workload_id:str
#             ):
#     response = get_dataproc_batch_status(workload_id)
#     return response

