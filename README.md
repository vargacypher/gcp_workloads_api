
# Workloads-Api
![alt text](demo_api.png)


Em um novo projeto na GCP com **billing ativado**, **utilizando o cloud shell**

**Autorizar a CLI gcloud**: https://cloud.google.com/sdk/docs/authorizing?hl=pt-br
**Necessario conta com privilegios"

### First step
**clonar o repo e definir o projeto**
#### Provisionar o ambiente e permissoes
```shell
python3 -m venv env 
source env/bin/activate
pip3 install ansible requests google-auth

export PROJECT_ID=$(gcloud config get-value project)
export REGION=us-central1
ansible-galaxy collection install google.cloud
ansible-playbook ./ansible/playbook.yaml
```


#### Buildar app
```shell
deactivate && rm -rf env
gcloud builds submit --config cloudbuild.yaml --substitutions _PROJECT_ID=$PROJECT_ID,_COMMIT_SHA=latest,_REGION=$REGION,_API_SA=api-sa@$PROJECT_ID.iam.gserviceaccount.com,_SPARK_SA=spark-sa@$PROJECT_ID.iam.gserviceaccount.com

gcloud compute networks subnets update default  --region=$REGION --enable-private-ip-google-access

```


#### Testes (Demo spark word-count)

```shell

#Exporta a URL do servico cloud run
export URL=$(gcloud run services describe workloads-api --format='value(status.url)')
#Seleciona a regiao
32 us-central1 OU SUA $REGIAO

export STS_TOKEN=$(gcloud auth print-identity-token)

curl $URL/healthcheck -H "Authorization: Bearer $STS_TOKEN"

curl -X 'POST' $URL/v1/workloads/batch-cluster/submit-demo?python_file_url=gs%3A%2F%2Ftest_spk%2Fspark_word_count.py -H "Authorization: Bearer $STS_TOKEN"

#Utilizar o workload_id retornado no step anterior para resgatar o status
curl $URL/v1/workloads/batch-cluster/get-demo-status/$WORKLOAD_ID_RETORNADO_NO_CURL_ANTERIOR -H "Authorization: Bearer $STS_TOKEN"  

curl $URL/v1/workloads/batch-cluster/get-demo-result -H "Authorization: Bearer $STS_TOKEN"
```


ADC`S
ACLS
ROLES
