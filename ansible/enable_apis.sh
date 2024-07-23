#!/bin/bash

function enable_apis {
    echo "=============================================================================================================================================="
    echo "============================Enabling API's services==========================================================================================="

    gcloud services enable compute.googleapis.com 
    gcloud services enable iam.googleapis.com
    gcloud services enable dataproc.googleapis.com 
    gcloud services enable bigquerystorage.googleapis.com 
    gcloud services enable artifactregistry.googleapis.com 
    gcloud services enable run.googleapis.com 
    gcloud services enable containerregistry.googleapis.com 
    gcloud services enable cloudresourcemanager.googleapis.com 
    gcloud services enable cloudbuild.googleapis.com

    echo "=============================================================================================================================================="
    echo "=============================================================================================================================================="
}

enable_apis