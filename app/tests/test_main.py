from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch
# from typing import Callable
# import httpx

client = TestClient(app)

'''
WIP

'''

def test_status():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    res = response.json()
    assert res['success'] is True
    assert res['requestId'] is not None
    assert res['response'] is not None


# def get_client() -> Callable[[str], httpx.Response]:
#     return httpx.get
# # Override the dependency
# app.dependency_overrides[get_client] = lambda: mock_get

# def test_result_demo():
#     # Make a request to the FastAPI endpoint
#     response = client.get("/workloads/batch-cluster/get-demo-result")
#     print(response)
#     # Assert the response
#     assert response.status_code == 200
#     assert response.json() == {"key": "value"}