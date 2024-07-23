import os
from datetime import datetime

PROJECT_ID = os.environ.get('PROJECT_ID')
REGION = os.environ.get('REGION')

METADATA_URL = 'http://metadata.google.internal/computeMetadata/v1'
METADATA_HEADERS = {'Metadata-Flavor': 'Google'}
SERVICE_ACCOUNT = 'default'

SPARK_SA = os.environ.get('SPARK_SA')

BASE_GCP_URL = "https://dataproc.googleapis.com"
CLUSTER_URL = f'{BASE_GCP_URL}/v1/projects/{PROJECT_ID}/regions/{REGION}/clusters'
SUBMMIT_JOB_URL = f'{BASE_GCP_URL}/v1/projects/{PROJECT_ID}/regions/{REGION}/jobs:submit/'
STATUS_JOB_URL = f'{BASE_GCP_URL}/v1/projects/{PROJECT_ID}/regions/{REGION}/jobs'
DATASET_NAME = "wordcount_dataset"
TABLE_NAME = "wordcount_output"
CLUSTER_NAME = "democluster-bd34"

CLUSTER_CFG = {
  "projectId": PROJECT_ID,
  "clusterName": CLUSTER_NAME ,
  "config": {
    "configBucket": "",
    "gceClusterConfig": {
      "networkUri": "default",
      "subnetworkUri": "",
      "internalIpOnly": "true",
      "serviceAccount": SPARK_SA,
      "zoneUri": "",
      "metadata": {},
      "tags": [],
    },
    "masterConfig": {
      "numInstances": 1,
      "machineTypeUri": "n1-standard-2",
      "diskConfig": {
        "bootDiskType": "pd-balanced",
        "bootDiskSizeGb": "50",
        "numLocalSsds": 0,
        "localSsdInterface": "SCSI"
      },
      "minCpuPlatform": "",
      "imageUri": ""
    },
    "softwareConfig": {
      "imageVersion": "2.2-debian12",
      "properties": {
        "dataproc:dataproc.allow.zero.workers": "true"
      },
      "optionalComponents": []
    },
    "lifecycleConfig": {
      "autoDeleteTtl": "600s"
    },
    "initializationActions": [],
    "encryptionConfig": {},
    "autoscalingConfig": {
      "policyUri": ""
    },
    "endpointConfig": {
      "enableHttpPortAccess": "false"
    },
    "securityConfig": {
      "kerberosConfig": {}
    }
  },
  "labels": {},
  "status": {},
  "statusHistory": [
    {}
  ],
  "metrics": {}
}
    
DEFAULT_JOB_CFG = {
  "projectId": PROJECT_ID,
  "job": {
    "placement": {
      "clusterName": CLUSTER_NAME
    },
    "statusHistory": [],
    "reference": {
      "jobId": f'workload-{datetime.now().strftime("%Y%m%d-%H%M%S")}',
      "projectId": PROJECT_ID
    },
    "pysparkJob": {
      "mainPythonFileUri": "gs://test_spk/spark_word_count.py", #TODO Verify this file
      "args": [PROJECT_ID],
      "properties": {}
    }
  }
}
