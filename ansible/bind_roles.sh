#!/bin/bash

function bind_roles {
    echo "=============================================================================================================================================="
    echo "============================Biding roles==========================================================================================="

    gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:api-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/storage.admin"

    gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:api-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/dataproc.admin"

    gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:api-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountTokenCreator"

    gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:api-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountUser"

    gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:api-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/bigquery.user"

    gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:api-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/bigquery.jobUser"

    echo "=============================================================================================================================================="
    echo "=============================================================================================================================================="

    gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:spark-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/storage.admin"

    gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:spark-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/bigquery.dataEditor"

    gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:spark-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/bigquery.user"

    gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:spark-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/dataproc.worker"

    echo "=============================================================================================================================================="
    echo "=============================================================================================================================================="

    echo "=============================================================================================================================================="
    echo "============================Enabling private ip google access======================================================================================="

    gcloud compute networks subnets update default  --region=$REGION --enable-private-ip-google-access

    echo "=============================================================================================================================================="
    echo "=============================================================================================================================================="
}

bind_roles